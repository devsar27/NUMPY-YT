# Overfitting vs. Underfitting: Finding the "Sweet Spot"

# In Deep Learning, we don't just want a model that performs well on data it has SEEN.
# We want it to perform well on data it has NEVER seen before.

# --- ANALOGY: STUDYING FOR AN EXAM ---

# 1. UNDERFITTING (The "Too Lazy" Student)
# The student barely studies. They don't even learn the basic concepts.
# - Test on studied material: FAILS.
# - Final Exam (new questions): FAILS.
# In DL: The model is too simple (not enough layers or neurons) to find the pattern.

# 2. OVERFITTING (The "Memorizer" Student)
# The student memorizes every single word of the textbook instead of understanding the concepts.
# If a question has a typo, they memorize the typo too.
# - Test on studied material: PERFECT SCORE (100%).
# - Final Exam (new questions phrased differently): FAILS.
# In DL: The model is too complex and "remembers" the noise/randomness in the training data.

# 3. JUST RIGHT (The "Generalizer" Student)
# The student understands the core logic and concepts.
# - Test on studied material: Good Score.
# - Final Exam (new questions): Good Score.

# --- SIMULATING OVERFITTING IN CODE ---

import random

# Imagine a simple rule: Output = Input * 2
# But our training data has "noise" (like mistakes in the data)
training_data = [
    (1, 2),  # Correct
    (2, 4),  # Correct
    (3, 10), # NOISE! (Should be 6, but recorded as 10)
    (4, 8)   # Correct
]

# An OVERFITTING neuron would change its weight to try and get that "10" right.
# It might end up with a weird weight like 2.5 instead of 2.0.

print("--- OVERFITTING SIMULATION ---")
weight = 2.5 # The neuron "memorized" the mistake in the training data
print(f"Model thinks the rule is: Output = Input * {weight}")

# Now we give it UNSEEN data (the Final Exam)
unseen_input = 5
true_answer = 10 # 5 * 2
prediction = unseen_input * weight

print(f"\nFinal Exam Question: What is 5 * 2?")
print(f"Model Guess: {prediction}")
print(f"Real Answer: {true_answer}")
print(f"Error: {abs(prediction - true_answer)}")

print("\nConclusion: Because the model overfitted to the 'noise' (the mistake), it failed the final exam.")
