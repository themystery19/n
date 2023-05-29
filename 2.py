print("Stop Word finding")

import nltk
nltk.download('stopwords')
text="""Welcome you to programming knowldge. Lets start with our first tutorial in NLTK. We shall learn basic Nltk here"""

from nltk.corpus import stopwords

stop_words = stopwords.words('english')

from nltk.tokenize import word_tokenize,sent_tokenize

token = word_tokenize(text)

cleaned_token =[]
for word in token:
    if word not in stop_words:
        cleaned_token.append(word)

print("This is unclean",token)
print("this is clean",cleaned_token)