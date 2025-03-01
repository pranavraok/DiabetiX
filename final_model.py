import joblib  
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

dataSet = pd.read_csv("diabetes.csv")

# Replace 0 with median for required columns
columns_to_replace = ["Pregnancies", "Glucose", "BMI", "Age", "DiabetesPedigreeFunction"]
for col in columns_to_replace:
    dataSet[col] = dataSet[col].replace(0, dataSet[col].median())

# Only select the 5 columns you're using in HTML form
X = dataSet[["Pregnancies", "Glucose", "BMI", "Age", "DiabetesPedigreeFunction"]]
y = dataSet["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale only these selected columns
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=21)
knn.fit(X_train_scaled, y_train)

# Save model and scaler
joblib.dump(knn, "diabetes_model.pkl")
joblib.dump(sc, "scaler.pkl")

print("Model and Scaler saved successfully 🚀🔥")

