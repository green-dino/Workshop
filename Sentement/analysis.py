import streamlit as st
import nltk
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
from PyPDF2 import PdfReader
import os, sys

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.tokenized_sentences = [word_tokenize(sentence) for sentence in sent_tokenize(text)]
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    def analyze_charting_method(self):
        relationships = []
        sentiments = []
        for i, sentence_tokens in enumerate(self.tokenized_sentences):
            if i < len(self.tokenized_sentences) - 1:
                relationships.append((sentence_tokens[-1], self.tokenized_sentences[i + 1][0]))
                sentiments.append(self.sentiment_analyzer.polarity_scores(' '.join(sentence_tokens))['compound'])

        if relationships:
            df = pd.DataFrame(list(zip(relationships, sentiments)), columns=['Relationships', 'Sentiment'])
            df[['Current Word', 'Next Word']] = pd.DataFrame(df['Relationships'].tolist(), index=df.index)
            df = df.drop(columns=['Relationships'])

            plt.figure(figsize=(12, 8))
            heatmap = sns.heatmap(pd.crosstab(df['Current Word'], df['Next Word'], values=df['Sentiment'], aggfunc='mean'),
                                  cmap="YlGnBu", annot=True, fmt='.2f')
            st.pyplot(heatmap)

    def analyze_feature_matrix_method(self, entity_number):
        try:
            if entity_number is not None and 0 < entity_number <= len(self.tokenized_sentences):
                while True:
                    # Print features and sentiment of the selected entity
                    selected_entity_features = self.tokenized_sentences[entity_number - 1]
                    entity_sentiment = self.sentiment_analyzer.polarity_scores(' '.join(selected_entity_features))[
                        'compound']
                    st.write(f"\nFeatures of Entity {entity_number}: {selected_entity_features}")
                    st.write(f"Sentiment of Entity {entity_number}: {entity_sentiment}")

                    # Ask the user for additional options
                    st.write("\nAdditional options:")
                    st.write("1. Analyze another entity")
                    st.write("2. Return to the main menu")
                    
                    # Use a unique key for each st.text_input
                    choice = st.text_input("Enter the number of your choice:", key=f"choice_{entity_number}")

                    if choice == '1':
                        # Let the user choose another entity
                        entity_number = int(st.text_input("Enter the number of the entity to examine:",
                                                        key=f"entity_number_{entity_number}"))
                    elif choice == '2':
                        break
                    else:
                        st.write("Invalid choice. Please enter '1' or '2'.")
            else:
                st.write("Invalid entity number. Please choose a valid entity number.")
        except IndexError:
            st.write("Error: Index out of range. Please choose a valid entity number.")


    def analyze_flow_method(self):
        # Identify key connectors or transition words indicating flow
        connectors = ['next', 'then', 'after', 'finally', 'in conclusion', 'first', 'second', 'third']

        # Extract relationships based on connectors
        relationships = []
        sentiments = []
        for i, sentence_tokens in enumerate(self.tokenized_sentences):
            for connector in connectors:
                if connector in sentence_tokens:
                    if i < len(self.tokenized_sentences) - 1:
                        relationships.append((connector, self.tokenized_sentences[i + 1][0]))
                        sentiments.append(
                            self.sentiment_analyzer.polarity_scores(' '.join(sentence_tokens))['compound'])

        if relationships:
            df = pd.DataFrame(list(zip(relationships, sentiments)), columns=['Relationships', 'Sentiment'])
            df[['Connector', 'Next Word']] = pd.DataFrame(df['Relationships'].tolist(), index=df.index)
            df = df.drop(columns=['Relationships'])

            plt.figure(figsize=(12, 8))
            heatmap = sns.heatmap(pd.crosstab(df['Connector'], df['Next Word'], values=df['Sentiment'], aggfunc='mean'),
                                  cmap="YlGnBu", annot=True, fmt='.2f')
            st.pyplot(heatmap)

def main():
    st.title("PDF Sentiment Analysis App")

    file_path = st.file_uploader("Upload a PDF file", type=["pdf"])
    if file_path:
        pdf_reader = PdfReader(file_path)
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
        text_analyzer = TextAnalyzer(pdf_text)

        analysis_method = st.selectbox("Choose an analysis method:", ["Charting Method", "Feature Matrix Method", "Flow Method"])

        if analysis_method == "Charting Method":
            text_analyzer.analyze_charting_method()
        elif analysis_method == "Feature Matrix Method":
            entity_number = st.number_input("Enter the number of the entity to examine:", min_value=1,
                                            max_value=len(text_analyzer.tokenized_sentences), step=1)
            text_analyzer.analyze_feature_matrix_method(int(entity_number))
        elif analysis_method == "Flow Method":
            text_analyzer.analyze_flow_method()

if __name__ == "__main__":
    main()
