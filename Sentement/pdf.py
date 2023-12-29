import streamlit as st
from pdfminer.high_level import extract_text
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from nltk import FreqDist
from nltk.corpus import stopwords
import heapq

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
def calculate_and_visualize_metrics(text, metric_filter):
    if metric_filter == "Word Count":
        words = word_tokenize(text)
        count = len(words)
        st.write(f"{metric_filter}: {count}")

    elif metric_filter == "Sentence Length":
        sentences = sent_tokenize(text)
        sentence_lengths = [len(word_tokenize(sentence)) for sentence in sentences]
        st.bar_chart(sentence_lengths)
        st.write(f"{metric_filter} Distribution")

    elif metric_filter == "Paragraph Length":
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        paragraph_lengths = [len(word_tokenize(paragraph)) for paragraph in paragraphs]
        st.bar_chart(paragraph_lengths)
        st.write(f"{metric_filter} Distribution")

# Define the function to analyze paragraph structure and display heatmap
def analyze_paragraph_structure(paragraph):
    sentences = sent_tokenize(paragraph)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

    relationships = []
    for i, sentence_tokens in enumerate(tokenized_sentences):
        if i < len(tokenized_sentences) - 1:
            relationships.append((sentence_tokens[-1], tokenized_sentences[i + 1][0]))

    if relationships:
        df = pd.DataFrame(relationships, columns=['Current Word', 'Next Word'])
        plt.figure(figsize=(8, 6))
        heatmap = sns.heatmap(pd.crosstab(df['Current Word'], df['Next Word']), cmap="YlGnBu", annot=True, fmt='g')
        plt.title('Relationships Between Tokens')
        st.pyplot(heatmap.figure)

# Define the function to get themes from paragraphs
def get_themes(text):
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]

    themes = []
    for paragraph in paragraphs:
        words = [word.lower() for word in word_tokenize(paragraph) if word.isalnum()]
        stop_words = set(stopwords.words("english"))
        words = [word for word in words if word not in stop_words]

        freq_dist = FreqDist(words)

        if freq_dist:
            main_idea = max(freq_dist, key=freq_dist.get)
            themes.append(main_idea)

    return themes

# Define the function for sentence summarization
def sentence_summarization(text, num_sentences=5):
    sentences = sent_tokenize(text)

    stop_words = set(stopwords.words("english"))
    words = [word.lower() for word in sentences if word.lower() not in stop_words]

    word_freq = FreqDist(words)

    sentence_scores = {}
    for sentence in sentences:
        for word, freq in word_freq.items():
            if word in sentence.lower():
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq
                else:
                    sentence_scores[sentence] += freq

    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    return summary_sentences

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

        metric_filter = st.selectbox("Choose Metric", ["Word Count", "Sentence Length", "Paragraph Length"])

        st.subheader(f"{metric_filter} Metrics:")
        calculate_and_visualize_metrics(pdf_text, metric_filter)

        st.subheader("Keywords:")
        keywords = extract_keywords(pdf_text)
        st.write("Top Keywords:", keywords)

        st.subheader("Word Cloud:")
        generate_word_cloud(pdf_text)

        st.subheader("Sentence Analysis:")
        analysis_choice = st.radio("Choose Analysis", ["Themes", "Summarization"])
        
        if analysis_choice == "Themes":
            themes = get_themes(pdf_text)
            st.write("Themes:", themes)

        elif analysis_choice == "Summarization":
            num_summary_sentences = st.slider("Number of Sentences for Summarization", 1, 10, 5)
            summary_sentences = sentence_summarization(pdf_text, num_summary_sentences)
            st.write("Summary Sentences:")
            for sentence in summary_sentences:
                st.write("- ", sentence)

if __name__ == "__main__":
    main()
