# 1. Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

# 2. Load dataset
columns = ["buying", "maint", "doors", "persons",
           "lug_boot", "safety", "class"]

df = pd.read_csv("car_evaluation.csv", header=None, names=columns)

print("First 5 rows:")
print(df.head())

# 3. Separate input and output
X = df.drop("class", axis=1)
y = df["class"]

# 4. Convert categorical data into numbers
X = pd.get_dummies(X)

# 5. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Create Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 7. Train the model
model.fit(X_train, y_train)

# 8. Predict the results
y_pred = model.predict(X_test)

# 9. Evaluate the model
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 10. Confusion Matrix Visualization
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Random Forest Confusion Matrix")
plt.show()