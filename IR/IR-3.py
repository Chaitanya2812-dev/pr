import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset

data = pd.read_csv("spam_ham_dataset.csv")

# Remove missing values

daa = data.dropna(subset=["text", "label"])

# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
data["text"], data["label"], test_size=0.2, random_state=42
)

# Convert text into numbers

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train model

model = MultinomialNB()
model.fit(X_train, y_train)

# Test model

prediction = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, prediction))

# Predict a new email

email = input("Enter email message: ")
result = model.predict(vectorizer.transform([email]))[0]
print("Email classification:", result.upper())
