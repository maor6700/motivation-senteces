import random

# List of motivational words and phrases
words = ["believe", "hope", "inspire", "motivate", "dream", "aspire", "encourage", "persist", "dare", "strive"]

# Generate a random index for the list of words
index = random.randint(0, len(words)-1)

# Get the word at the random index
word = words[index]

# Generate the motivational sentence
sentence = "You have the power to " + word + " and achieve your goals."

# Print the sentence
print(sentence)
