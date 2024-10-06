import tensorflow as tf
from tensorflow.keras import layers

def build_model(input_shape, num_actions):
    model = tf.keras.Sequential([
        layers.InputLayer(input_shape=input_shape),  # Define the input shape of the model
        layers.Dense(64, activation='relu'),         # First hidden layer with 64 neurons
        layers.Dense(64, activation='relu'),         # Second hidden layer with 64 neurons
        layers.Dense(num_actions, activation='linear')  # Output layer with 'num_actions' neurons
    ])
    
    # Compile the model with optimizer and loss function
    model.compile(optimizer='adam', loss='mse')  # Mean Squared Error loss for regression tasks
    return model
