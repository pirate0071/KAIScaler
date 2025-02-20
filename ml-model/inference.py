import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import joblib

def load_trained_model():
    return load_model("lstm_autoscaler.h5")

def predict_cpu_usage(input_data):
    model = load_trained_model()
    input_data = np.array(input_data).reshape(1, 10, 1)
    prediction = model.predict(input_data)[0][0]
    return prediction

if __name__ == "__main__":
    test_data = joblib.load("train_data.pkl")[:1]  # Use first training sample
    prediction = predict_cpu_usage(test_data)
    print(f"Predicted CPU usage: {prediction}")