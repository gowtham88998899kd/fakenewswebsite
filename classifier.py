from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "news_samples.csv"
MODEL_FILE = BASE_DIR / "model" / "fake_news_model.joblib"


class FakeNewsClassifier:
    def __init__(self):
        self.pipeline = self._load_or_train_model()

    def _load_or_train_model(self):
        MODEL_FILE.parent.mkdir(parents=True, exist_ok=True)

        if MODEL_FILE.exists():
            return joblib.load(MODEL_FILE)

        dataset = pd.read_csv(DATA_FILE)
        X = dataset["text"]
        y = dataset["label"]

        pipeline = Pipeline(
            [
                ("tfidf", TfidfVectorizer(stop_words="english", ngram_range=(1, 2))),
                ("model", LogisticRegression(max_iter=1000, random_state=42)),
            ]
        )

        pipeline.fit(X, y)
        joblib.dump(pipeline, MODEL_FILE)
        return pipeline

    def predict(self, text):
        prediction = self.pipeline.predict([text])[0]
        probabilities = self.pipeline.predict_proba([text])[0]
        confidence = max(probabilities) * 100
        return prediction.upper(), round(float(confidence), 2)
