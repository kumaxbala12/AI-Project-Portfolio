"""
Clustering Reddit Posts

This script uses simulated Reddit post data, vectorizes it with TF-IDF, and clusters posts using KMeans.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def get_sample_data():
    posts = [
        "The new iPhone release was underwhelming.",
        "I love using Python for data science.",
        "What's the best GPU for gaming in 2025?",
        "Mental health awareness is rising on campus.",
        "Should I buy Tesla stock now?",
        "How to start investing in crypto safely?",
        "Quantum computing will change the world.",
        "The future of AI is both exciting and scary.",
        "Vaccines are crucial in modern medicine.",
        "I just built my first PC!"
    ]
    return pd.DataFrame({'text': posts})

def vectorize_and_cluster(df, n_clusters=3):
    tfidf = TfidfVectorizer(stop_words='english')
    X = tfidf.fit_transform(df['text'])

    km = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = km.fit_predict(X)

    # Visualization
    pca = PCA(n_components=2)
    coords = pca.fit_transform(X.toarray())
    plt.scatter(coords[:, 0], coords[:, 1], c=df['cluster'])
    plt.title("Reddit Post Clusters")
    plt.show()

    print(df)

def main():
    df = get_sample_data()
    vectorize_and_cluster(df)

if __name__ == "__main__":
    main()
