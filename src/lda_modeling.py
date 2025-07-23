from sklearn.decomposition import LatentDirichletAllocation

def apply_lda(count_matrix, num_topics=10):
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(count_matrix)
    return lda
