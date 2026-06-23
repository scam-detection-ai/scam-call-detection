import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and Label
X = data[["call_duration", "frequency", "complaints"]]
y = data["label"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")
