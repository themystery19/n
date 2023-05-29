print(" Speech Tagging")

import nltk

nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag

text = "Welcome you to programming knowldge. Lets start with our first tutorial in NLTK. We shall learn basic Nltk here"

print("After Split",text)

tokens_tag = pos_tag(text)
print("After Tokenization",tokens_tag)
