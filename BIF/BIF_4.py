import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv("METABRIC_RNA_Mutation.csv", low_memory=False)

# Separate input and output
data = data.dropna(subset=["overall_survival"])

X = data.select_dtypes(include="number").drop(
    columns=["patient_id", "overall_survival_months", "death_from_cancer"],
    errors="ignore"
)
y = data["overall_survival"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Handle missing values
X_train = X_train.fillna(X_train.median())
X_test = X_test.fillna(X_train.median())

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict results
prediction = model.predict(X_test)

# Check performance
print("Accuracy:", accuracy_score(y_test, prediction))
print("Confusion Matrix:\n", confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction, zero_division=0))

# Important features
print("Feature Importance:")
print(pd.Series(model.feature_importances_, index=X.columns)
      .sort_values(ascending=False).head(10))