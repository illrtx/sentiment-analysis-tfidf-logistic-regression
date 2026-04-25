import streamlit as st
import joblib

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("Movie Review Sentiment Analysis ")
st.write("This app predicts whether a review is Positive or Negative using TF-IDF and Logistic Regression.")

review = st.text_area("Enter a movie review:")

if st.button("Predict"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        review_vec = vectorizer.transform([review])
        prediction = model.predict(review_vec)[0]
        probability = model.predict_proba(review_vec)[0]

        if prediction == 1:
            st.success("Prediction: Positive ")
        else:
            st.error("Prediction: Negative ")

        st.write("Negative probability:", round(probability[0], 3))
        st.write("Positive probability:", round(probability[1], 3))
