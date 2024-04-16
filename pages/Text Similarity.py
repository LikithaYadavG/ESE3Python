import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

df = pd.read_csv("WomensClothingE-CommerceReviews.csv")  

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if isinstance(text, str):
        tokens = word_tokenize(text)
        
        tokens = [word.lower() for word in tokens]
        
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]
        
        tokens = [word.translate(str.maketrans('', '', string.punctuation)) for word in tokens]
        
        tokens = [word for word in tokens if word.strip() and not word.isdigit()]  # Remove numbers
        
        stemmed_tokens = [stemmer.stem(word) for word in tokens]
        
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]
        
        return lemmatized_tokens
    else:
        return []

# Handling NaN values
df['Review Text'].fillna('', inplace=True)

df['Review Text'] = df['Review Text'].apply(preprocess_text)

print(df['Review Text'])

filtered_df = df[df['Division Name'].isin(['General Petite', 'Intimates'])]

tokenized_texts = filtered_df['Review Text'].apply(lambda x: ' '.join(x))

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(tokenized_texts)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def identify_similar_reviews(similarity_matrix, threshold=0.7):
    similar_reviews = {}
    for i in range(len(similarity_matrix)):
        similar_reviews[i] = [j for j, score in enumerate(similarity_matrix[i]) if score > threshold and j != i]
    return similar_reviews

similar_reviews = identify_similar_reviews(cosine_sim)

for i, similar_list in similar_reviews.items():
    if similar_list:
        print(f"Review {i}: Similar to {similar_list}")
