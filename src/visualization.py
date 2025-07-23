import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def plot_bar_chart(words, scores, title='Top Words'):
    plt.figure(figsize=(8,6))
    sns.barplot(x=scores, y=words)
    plt.title(title)
    plt.show()

def plot_heatmap(matrix, title='Topic-Word Heatmap'):
    plt.figure(figsize=(10,6))
    sns.heatmap(matrix, cmap='Blues')
    plt.title(title)
    plt.show()

def plot_wordcloud(words, title='WordCloud'):
    wc = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()
