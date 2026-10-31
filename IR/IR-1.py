import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

choice = input("Enter 1 for text or 2 for file: ")

if choice == '1':
    text = input("Enter text: ")
else:
    file = input("Enter file name: ")
    with open(file, 'r') as f:
        text = f.read()

words = word_tokenize(text.lower())

stop_words = set(stopwords.words('english'))
filtered = [w for w in words if w.isalpha() and w not in stop_words]

ps = PorterStemmer()
stemmed = [ps.stem(w) for w in filtered]

print("Original Words:", words)
print("After Stop Word Removal:", filtered)
print("After Stemming:", stemmed)