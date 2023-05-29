print("Count Word")
import nltk
from nltk.corpus import webtext
from nltk.probability import FreqDist

nltk.download('webtext')
wt_words = webtext.words('testing.txt')
data_analysis = nltk.FreqDist(wt_words)
filter_word = dict([(m,n) for m,n in data_analysis.items() if len(m)>3])
for key in sorted(filter_word):
    print("%s %s" % (key,filter_word[key]))
data_analysis = nltk.FreqDist(filter_word)
