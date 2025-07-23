from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def get_count_vectorizer(texts, max_features=5000):
    vectorizer = CountVectorizer(max_features=max_features)
    return vectorizer.fit_transform(texts), vectorizer

def get_tfidf_vectorizer(texts, max_features=5000):
    vectorizer = TfidfVectorizer(max_features=max_features)
    return vectorizer.fit_transform(texts), vectorizer
