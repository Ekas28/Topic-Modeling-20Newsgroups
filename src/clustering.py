from sklearn.cluster import KMeans

def apply_kmeans(tfidf_matrix, num_clusters=10):
    model = KMeans(n_clusters=num_clusters, random_state=42)
    model.fit(tfidf_matrix)
    return model
