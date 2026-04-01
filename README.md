# Fake News Classifier Project

This project is a simple **Diploma AI & ML mini project**. It takes a news paragraph as input and predicts whether the content looks **REAL** or **FAKE**.

## Project Title

Fake News Classifier Using Machine Learning

## Project Objective

To build a web application that can classify news content as real or fake using a machine learning model.

## Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSS

## Folder Structure

```text
New project/
|-- app.py
|-- classifier.py
|-- requirements.txt
|-- README.md
|-- data/
|   |-- news_samples.csv
|-- model/
|   |-- fake_news_model.joblib  (created automatically)
|-- static/
|   |-- style.css
|-- templates/
|   |-- index.html
```

## Step-by-Step Setup

### Step 1: Open the project folder

Open terminal in:

```powershell
C:\Users\gowth\Documents\New project
```

### Step 2: Install required packages

If needed, run:

```powershell
pip install -r requirements.txt
```

### Step 3: Run the project

```powershell
python app.py
```

### Step 4: Open in browser

Open this address:

```text
http://127.0.0.1:5000
```

### Step 5: Test the model

1. Paste a news paragraph.
2. Click **Analyze News**.
3. See the result as **REAL** or **FAKE**.

## How the Model Works

1. The user enters news text.
2. The TF-IDF method converts the text into numbers.
3. Logistic Regression checks patterns in the text.
4. The website shows the prediction with confidence.

## Sample Viva / Presentation Points

### Simple Introduction

"My project title is Fake News Classifier Using Machine Learning. This system accepts news content as input and predicts whether it is real or fake. I used Python, Flask, TF-IDF, and Logistic Regression to build the system."

### Problem Statement

There is a lot of false information on the internet and social media. People may believe fake news very easily. So this project helps identify suspicious content using machine learning.

### Why This Project

- Useful in the digital world
- Good AI & ML application
- Easy to explain in project review
- Combines machine learning and web development

### Algorithm Explanation

- **TF-IDF** converts words into feature values.
- **Logistic Regression** predicts the correct class from those features.

### Output Explanation

- If the text pattern looks trustworthy, the model predicts **REAL**.
- If the text pattern looks suspicious or similar to false samples, the model predicts **FAKE**.

## Important Note

This is a **student project**. It is useful for learning and demonstration. It is not a professional fact-checking system.

## Future Improvements

- Use a larger real dataset
- Add user login
- Save prediction history
- Improve model accuracy
- Deploy online
