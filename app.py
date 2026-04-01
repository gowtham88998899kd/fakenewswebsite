import os

from flask import Flask, render_template, request

from classifier import FakeNewsClassifier


app = Flask(__name__)
classifier = FakeNewsClassifier()


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    confidence = None
    submitted_text = ""

    if request.method == "POST":
        submitted_text = request.form.get("news_text", "").strip()
        if submitted_text:
            prediction, confidence = classifier.predict(submitted_text)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        submitted_text=submitted_text,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
