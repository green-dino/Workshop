import streamlit as st
from pdfminer.high_level import extract_text
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk import FreqDist
from nltk.corpus import stopwords

# Define the TextAnalyzer class
class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.tokenized_sentences = [word_tokenize(sentence) for sentence in sent_tokenize(text)]
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

# Define the function to generate a word cloud
def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, max_words=150, background_color='white').generate(text)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Word Cloud from PDF Text')
    st.pyplot(fig)

# Define the function for interactive sentiment analysis
def interactive_sentiment_analysis(analyzer, selected_text):
    if st.checkbox("Interactive Sentiment Analysis"):
        sentiment_score = analyzer.sentiment_analyzer.polarity_scores(selected_text)['compound']
        st.write("Sentiment Score:", sentiment_score)

# Define the function for keyword extraction
def extract_keywords(text, num_keywords=5):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    word_freq = FreqDist(filtered_words)
    keywords = word_freq.most_common(num_keywords)
    return keywords

# Define the function for metrics calculation and visualization
def calculate_and_visualize_metrics(text):
    words = word_tokenize(text)
    word_count = len(words)

    sentences = sent_tokenize(text)
    sentence_lengths = [len(word_tokenize(sentence)) for sentence in sentences]

    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    paragraph_lengths = [len(word_tokenize(paragraph)) for paragraph in paragraphs]

    # Plotting
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

    ax1.bar(["Word Count"], [word_count], color='blue')
    ax1.set_ylabel("Count")

    ax2.hist(sentence_lengths, bins=20, color='green', edgecolor='black')
    ax2.set_xlabel("Sentence Length")
    ax2.set_ylabel("Frequency")

    ax3.hist(paragraph_lengths, bins=20, color='orange', edgecolor='black')
    ax3.set_xlabel("Paragraph Length")
    ax3.set_ylabel("Frequency")

    plt.tight_layout()
    st.pyplot(fig)

# Streamlit app
def main():
    st.title("PDF Word Cloud Generator")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        pdf_text = extract_text(uploaded_file)
        analyzer = TextAnalyzer(pdf_text)

        st.subheader("Sentiment Analysis Results:")
        st.write("Sentiment Score:", analyzer.sentiment_analyzer.polarity_scores(pdf_text)['compound'])

        interactive_sentiment_analysis(analyzer, st.text_area("Enter text for sentiment analysis:", value=""))

        st.subheader("Metrics:")
        calculate_and_visualize_metrics(pdf_text)

        st.subheader("Keywords:")
        keywords = extract_keywords(pdf_text)
        st.write("Top Keywords:", keywords)

        st.subheader("Word Cloud:")
        generate_word_cloud(pdf_text)

if __name__ == "__main__":
    main()
