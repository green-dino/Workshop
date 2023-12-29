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
def interactive_sentiment_analysis(analyzer):
    if st.checkbox("Interactive Sentiment Analysis"):
        # Allow users to select a sentence or paragraph for analysis
        selected_text = st.text_area("Enter text for sentiment analysis:", value="")
        sentiment_score = analyzer.sentiment_analyzer.polarity_scores(selected_text)['compound']
        st.write("Sentiment Score:", sentiment_score)

# Define the function for keyword extraction
def extract_keywords(text, num_keywords=5):
    # Tokenize the text
    words = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Calculate word frequencies
    word_freq = FreqDist(filtered_words)

    # Get the most common keywords
    keywords = word_freq.most_common(num_keywords)

    return keywords

# Streamlit app
def main():
    st.title("PDF Word Cloud Generator")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Extract text from the PDF
        pdf_text = extract_text(uploaded_file)

        # Analyze the text
        analyzer = TextAnalyzer(pdf_text)

        # Display sentiment analysis results (optional)
        st.subheader("Sentiment Analysis Results:")
        st.write("Sentiment Score:", analyzer.sentiment_analyzer.polarity_scores(pdf_text)['compound'])

        # Additional options
        interactive_sentiment_analysis(analyzer)
        extract_keywords(pdf_text)  # Corrected this line

        # Generate and display the word cloud
        st.subheader("Word Cloud:")
        generate_word_cloud(pdf_text)

if __name__ == "__main__":
    main()
