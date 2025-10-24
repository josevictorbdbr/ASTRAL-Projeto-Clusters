import seaborn as sns
import matplotlib.pyplot as plt

def show_results(df):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8,4))
    sns.barplot(data=df, x="Algoritimo", y="F1")
    plt.title("Comparacao de algoritmos - F1")
    plt.tight_layout()
    plt.show() 