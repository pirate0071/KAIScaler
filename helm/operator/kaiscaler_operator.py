import os
import numpy as np
import tensorflow as tf
from kubernetes import client, config, watch
import prometheus_api_client

# Load Kubernetes configuration
config.load_kube_config()
v1 = client.CoreV1Api()
custom_api = client.CustomObjectsApi()

# Connect to Prometheus
prom = prometheus_api_client.PrometheusConnect(url="http://prometheus-server", disable_ssl=True)

# Load AI model (Pre-trained LSTM for autoscaling predictions)
model = tf.keras.models.load_model("lstm_autoscaler.h5")

def get_metrics():
    """Fetch real-time CPU utilization from Prometheus"""
    query = "sum(rate(container_cpu_usage_seconds_total[5m]))"
    metrics = prom.custom_query(query)
    return [float(metric['value'][1]) for metric in metrics]

def predict_scaling():
    """Use AI model to predict the next CPU utilization trend"""
    metrics = get_metrics()
    if not metrics:
        return None

    x_input = np.array([metrics[-10:]])  # Last 10 readings
    x_input = np.expand_dims(x_input, axis=0)
    predicted_cpu = model.predict(x_input)[0][0]
    return predicted_cpu

def scale_deployment(deployment_name, namespace, replicas):
    """Trigger Kubernetes Horizontal Pod Autoscaler"""
    apps_v1 = client.AppsV1Api()
    body = {'spec': {'replicas': replicas}}
    apps_v1.patch_namespaced_deployment_scale(name=deployment_name, namespace=namespace, body=body)
    print(f"Scaled {deployment_name} to {replicas} replicas")

def watch_crd():
    """Watch for AIHorizontalScaler CRD changes"""
    w = watch.Watch()
    for event in w.stream(custom_api.list_cluster_custom_object, group="kaiscaler.io", version="v1alpha1", plural="aihorizontalscalers"):
        crd = event["object"]
        spec = crd["spec"]
        deployment_name = crd["metadata"]["name"]
        namespace = crd["metadata"]["namespace"]

        predicted_cpu = predict_scaling()
        if predicted_cpu:
            print(f"Predicted CPU Load: {predicted_cpu}")
            if predicted_cpu > spec["targetCPUUtilization"]:
                scale_deployment(deployment_name, namespace, spec["maxReplicas"])
            elif predicted_cpu < (spec["targetCPUUtilization"] * 0.5):  # Scale down threshold
                scale_deployment(deployment_name, namespace, spec["minReplicas"])

if __name__ == "__main__":
    watch_crd()