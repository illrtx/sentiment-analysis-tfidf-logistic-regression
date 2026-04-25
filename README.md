# sentiment-analysis-tfidf-logistic-regression

This project is a Machine Learning model that classifies movie reviews as Positive or Negative using Natural Language Processing (NLP).

---

#**Project Overview:**

The goal of this project is to build a sentiment analysis system that can understand the emotional tone of text reviews.

The model was trained on the IMDB dataset and can also predict sentiment for custom user inputs.

---

#**Technologies Used:**

- Python
- Scikit-learn
- TF-IDF (Text Feature Extraction)
- Logistic Regression
- Matplotlib

---

#**How It Works:**

1. Text data is converted into numerical features using TF-IDF
2. A Logistic Regression model is trained on the dataset
3. The model predicts whether a review is positive or negative
4. The output includes prediction and confidence scores

---

#**Model Performance:**

- Test Accuracy: 88%
- Balanced performance across both classes (Positive & Negative)

--

#**Example Predictions:**

| Review | Prediction |
|--------|-----------|
| the new phone is amazing | Positive 👍 |
| this movie is terrible and boring | Negative 👎 |
| the game was too slow and disappointing | Negative 👎 |

---

#**How to Run:**

1. Open the notebook: `sentiment_analysis.ipynb`
2. Run all cells
3. Use the function:

```python
predict_sentiment("your text here")
```
---
#**Author**

**Heba Alsulami**  
Artificial Intelligence Student  
