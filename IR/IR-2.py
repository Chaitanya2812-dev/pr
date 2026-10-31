# Retrieve documents using inverted index

documents = {
    "D1": "Machine Learning is useful",
    "D2": "Machine Learning uses data",
    "D3": "Data Science is useful"
}

index = {}

for doc, text in documents.items():
    for word in text.lower().split():
        if word not in index:
            index[word] = []
        index[word].append(doc)

print("Inverted Index:")
print(index)

query = input("Enter search word: ").lower()

print("Matching Documents:", index.get(query, "No documents found"))