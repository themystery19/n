print ("Implemention of Tokenization")
import nltk
nltk.download('punkt')

text ="""Welcome you to programming knowldge. Lets start with our first tutorial in NLTK. We shall learn basic Nltk here"""

#from nltk.tokenize import word_tokenize
#print(word_tokenize(text))
 
from nltk.tokenize import sent_tokenize
print(sent_tokenize(text))