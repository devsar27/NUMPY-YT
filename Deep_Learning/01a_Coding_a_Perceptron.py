# A simple Perceptron implementation from scratch in Python

# 1. Inputs (These are like the signals a biological neuron receives from dendrites)
inputs = [1.2, 2.0, -0.5]

# 2. Weights (These determine how 'important' each input is)
# For example, if you're deciding whether to go outside, 
# input[0] could be 'Is it sunny?', weight[0] could be high because you love the sun.
weights = [0.8, -0.3, 0.5]

# 3. Bias (This is a base offset. Are you generally prejudiced to go outside anyway?)
bias = 1.0

# 4. The Summation (The neuron adds up all inputs multiplied by their weights, plus the bias)
# Equation: (input_1 * weight_1) + (input_2 * weight_2) + (input_3 * weight_3) + bias
summation = (inputs[0] * weights[0]) + (inputs[1] * weights[1]) + (inputs[2] * weights[2]) + bias

print(f"The raw summation value is: {summation}")

# 5. The Activation Function (Decides whether this neuron 'fires' based on the summation)
# We will use a simple "Step Function": If summation > 0, it fires (outputs 1). Otherwise, it doesn't (outputs 0).
def step_activation(x):
    if x > 0:
        return 1
    else:
        return 0

output = step_activation(summation)

print(f"The Perceptron's final output is: {output}")

# Try changing the inputs, weights, or bias and run it again to see how the output changes!
