# How a Neural Network Learns: Forward & Backpropagation

# In previous files, we magically provided the "right" weights. 
# But in real life, a Neural Network starts with RANDOM weights and has to "learn" them.
# How? By making mistakes and correcting itself!

import random

# 1. The Goal (The Training Data)
# Let's teach a single neuron a simple rule: 
# If input > 5, output 1 (Pass). If input <= 5, output 0 (Fail).
input_data = 7.0
true_answer = 1.0 # Because 7.0 > 5

# 2. Start with a completely RANDOM, terrible weight and bias
weight = random.uniform(-1, 1) # e.g., 0.3
bias = random.uniform(-1, 1)   # e.g., -0.5
learning_rate = 0.01           # How big of a step we take to fix our mistakes

print(f"--- STARTING OUT ---")
print(f"Initial Random Weight: {weight:.4f}, Bias: {bias:.4f}\n")

# 3. The Learning Loop (Epochs)
# We will show the neuron the data 20 times and force it to learn
epochs = 20

for epoch in range(epochs):
    
    # --- STEP A: FORWARD PROPAGATION (Make a Guess) ---
    # The neuron makes a prediction using its current (terrible) weight
    prediction = (input_data * weight) + bias
    
    # --- STEP B: CALCULATE THE ERROR (Loss) ---
    # How wrong was the guess compared to the real answer?
    # Simple Error = (Prediction - True Answer)
    error = prediction - true_answer
    
    # --- STEP C: BACKPROPAGATION (Learn from the mistake) ---
    # We update the weight and bias in the *opposite* direction of the error.
    # If we guessed too high (positive error), we reduce the weight.
    # If we guessed too low (negative error), we increase the weight.
    
    # (Note: This is a simplified version of Gradient Descent mathematics)
    weight_update = error * input_data * learning_rate
    bias_update = error * learning_rate
    
    # Update the actual weights!
    weight = weight - weight_update
    bias = bias - bias_update
    
    # Print the progress every few steps
    if epoch % 4 == 0 or epoch == epochs - 1:
        print(f"Epoch {epoch}: Prediction: {prediction:.4f} | Error: {error:.4f}")
        print(f"          -> Updated Weight: {weight:.4f}, Bias: {bias:.4f}")

print("\n--- TRAINING COMPLETE ---")
print("Notice how the Error gets smaller and smaller?")
print(f"Final Prediction: {(input_data * weight) + bias:.4f} (Very close to the true answer of {true_answer}!)")

# If you run this script multiple times, it starts with different random numbers,
# but it always figures out how to reach the right answer!
