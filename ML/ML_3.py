```python
# 1. Import libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

# 2. Load handwritten digits dataset
digits = load_digits()
X = digits.data
y = digits.target

print("Dataset shape:", X.shape)
print("Digit classes:", digits.target_names)

# 3. Display a sample digit
plt.imshow(digits.images[0], cmap='gray')
plt.title("Handwritten Digit: " + str(y[0]))
plt.show()

# 4. Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Create and train SVM model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# 6. Predict digit classes
y_pred = model.predict(X_test)

# 7. Calculate accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# 8. Display confusion matrix
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("SVM Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.show()

# 9. Display actual and predicted digit
print("Actual digit:", y_test[0])
print("Predicted digit:", y_pred[0])
```