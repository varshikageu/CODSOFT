import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, data_path):
        # Load movie data
        self.movies = pd.read_csv(data_path)
        self.movies['genre'] = self.movies['genre'].fillna('')
        self.tfidf_matrix = None
        self.similarity_matrix = None
        self._prepare()

    def _prepare(self):
        # Convert genres to TF-IDF vectors
        vectorizer = TfidfVectorizer(token_pattern=r'[^|]+')
        self.tfidf_matrix = vectorizer.fit_transform(self.movies['genre'])
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def recommend(self, movie_title, top_n=5):
        if movie_title not in self.movies['title'].values:
            return f"Movie '{movie_title}' not found in database."

        idx = self.movies[self.movies['title'] == movie_title].index[0]
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]  # Exclude the movie itself

        recommendations = [self.movies['title'][i[0]] for i in sim_scores]
        return recommendations
