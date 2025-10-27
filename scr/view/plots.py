import seaborn as sns
import matplotlib.pyplot as plt

def mostrar_resultados(df):
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8,4))
    sns.barplot(data=df, x="Algoritimo", y="F1")
    plt.title("Comparacao de algoritmos - F1")
    plt.tight_layout()
    plt.show() 