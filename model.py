import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

# Load data
df = pd.read_csv("dataset.csv")

# Features and labels
X = df["text"]
y = df["label"]

# Build pipeline: TF-IDF + Naive Bayes
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
   ("clf", MultinomialNB())
])

# Train
model.fit(X, y)

# Save model
with open("stress_model.pkl", "wb") as f:
   pickle.dump(model, f)

print("Model trained and saved!")