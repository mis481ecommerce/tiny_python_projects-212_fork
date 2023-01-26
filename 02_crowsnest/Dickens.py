#!/usr/bin/env python3
import random
import requests
from bs4 import BeautifulSoup

def get_text(url):
    """Get the text of a webpage"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

# URL of the webpage containing the text of the novel
url = 'http://www.gutenberg.org/files/1400/1400-h/1400-h.htm'

# Get the text of the novel
text = get_text(url)

def get_random_sentence(text):
    """Select a random sentence from the text"""

    # Split the text into sentences
    sentences = text.split('.')

    # Remove empty sentences
    sentences = [s for s in sentences if s.strip()]

    # Select a random sentence
    return random.choice(sentences)

# # Print a random sentence from the novel
# for i in range(10):
#     print(get_random_sentence(text))

# from googletrans import Translator
from translate import Translator

# Generate a random sentence
sentence = get_random_sentence(text)

# Translate the sentence into Chinese
translator = Translator(to_lang='zh')
translated = translator.translate(sentence)

# Print the original sentence and the translation
print(f'Original: {sentence}')
print(f'Translation: {translated}')
