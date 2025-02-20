import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib

# Generate synthetic training data
X_train = np.random.rand(1000, 10, 1)  # 1000 samples, 10 time steps, 1 feature
Y_train = np.random.rand(1000, 1)  # 1000 targets

# Build LSTM model
model = Sequential([
    LSTM(50, activation='relu', input_shape=(10, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(X_train, Y_train, epochs=20, verbose=1)

# Save model
model.save("lstm_autoscaler.h5")
joblib.dump(X_train, "train_data.pkl")

print("Model training complete and saved.")