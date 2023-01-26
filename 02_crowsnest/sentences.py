import random

# Read the text file containing the novel
with open('dickens_novel.txt', 'r') as file:
    text = file.read()

# Split the text into sentences
sentences = text.split('. ')

# Generate a random number of sentences to print
num_sentences = random.randint(5, 10)

# Choose random sentences from the list and print them
for i in range(num_sentences):
    random_sentence = random.choice(sentences)
    print(random_sentence)
