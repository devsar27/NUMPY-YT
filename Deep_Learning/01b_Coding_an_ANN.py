# Coding a Simple Artificial Neural Network (ANN) from Scratch
# We are connecting 3 Perceptrons together!

# Imagine we are trying to predict if a student will pass an exam.
# Inputs:
# 1. Hours studied (e.g., 5 hours)
# 2. Hours slept (e.g., 8 hours)
inputs = [5.0, 8.0]

# --- HIDDEN LAYER ---
# A Neural Network has "Hidden Layers" which are just groups of Perceptrons.
# Let's say our hidden layer has 2 Perceptrons (Neuron A and Neuron B).

# Neuron A (Maybe this neuron accidentally learns to care more about studying)
weights_A = [0.8, 0.2] 
bias_A = -2.0

# Neuron B (Maybe this neuron accidentally learns to care more about sleeping)
weights_B = [0.1, 0.9] 
bias_B = -4.0

# Calculate summation for Neuron A and Neuron B
sum_A = (inputs[0] * weights_A[0]) + (inputs[1] * weights_A[1]) + bias_A
sum_B = (inputs[0] * weights_B[0]) + (inputs[1] * weights_B[1]) + bias_B

# Activation Function (ReLU: Rectified Linear Unit)
# ReLU is very common. If sum > 0, output sum. If sum <= 0, output 0.
def relu_activation(x):
    return max(0, x)

# Get the outputs of the hidden layer neurons
output_A = relu_activation(sum_A)
output_B = relu_activation(sum_B)

print(f"Hidden Neuron A output: {output_A}")
print(f"Hidden Neuron B output: {output_B}")

# --- OUTPUT LAYER ---
# Now, the outputs of Neuron A and Neuron B become the *INPUTS* to our final Output Neuron.
# This final neuron decides the final prediction: Pass (1) or Fail (0).

hidden_layer_outputs = [output_A, output_B]

# Weights and bias for the output neuron
weights_Output = [0.6, 0.4]
bias_Output = -1.5

# Summation for the output neuron
sum_Output = (hidden_layer_outputs[0] * weights_Output[0]) + (hidden_layer_outputs[1] * weights_Output[1]) + bias_Output

# Activation for output (Step function like before)
def step_activation(x):
    if x > 0: return 1
    else: return 0

final_prediction = step_activation(sum_Output)

print(f"Final Prediction of the Neural Network (1=Pass, 0=Fail): {final_prediction}")

# Try changing the inputs (hours studied, hours slept) to see if you can make the student fail!
