from curses import nl
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import nltk
import sys
import time
import os

print('Loading Script:')
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

filename = input('Enter a filename: ')
path = r'hasil/'
f = open(os.path.join(path, filename))

comment = f.read()

word_tokens = word_tokenize(comment)

stop_words = set(stopwords.words('mode1'))
stop_words1 = ['bagus', 'sekali', 'enak', 'banget', 'tidak', 'suka', 'recomen'] #tambah di sini

word_tokens_no_stopwords1 = dict([(match, len([w for w in word_tokens if match in w])) for match in stop_words1])
word_tokens_no_stopwords = [w for w in word_tokens if not w in stop_words]

freq_kata_1 = nltk.FreqDist(word_tokens_no_stopwords1)
freq_kata_2 = nltk.FreqDist(word_tokens_no_stopwords)

print(freq_kata_2.most_common(20))
print(freq_kata_1.most_common())
freq_kata_2.plot(20)
freq_kata_1.plot()

plt.show()