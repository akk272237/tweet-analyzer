import streamlit as st 
import pandas as pd

st.title("Tweet analyzer")

uploaded_file = st.file_uploader("upload a csv of tweets" , type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### raw data")
    st.write(df.head())

    #basic stats
    st.write("### Tweet Statistics")
    st.write("Total Tweets:", len(df))
    st.write("Unique Users:", df["user"].nunique())

    #word count
    df["word_count"] = df["text"].apply(lambda x: len(str(x).split()))
    st.write("Average Words per Tweet:", df["word_count"].mean())

    #simple sentiment check 
    positive_words = ["love", "happy", "great", "awesome", "fun"]
    df["positive_score"] = df["text"].apply(
        lambda x: sum(word in str(x).lower() for word in positive_words)
    )

    st.write("### Positive Tweets")
    st.write(df[df["positive_score"] > 0][["user", "text"]])
    st.write("### Positivity Score")
    st.write("Average Positive Score:", df["positive_score"].mean())
    st.write("Total Positive Tweets:", (df["positive_score"] > 0).sum())


 









