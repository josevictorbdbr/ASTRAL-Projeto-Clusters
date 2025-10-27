from models.features import carregar_sequencias, gerar_matriz_kmer
from controllers.pipeline import rodar_pipeline
from view.plots import mostrar_resultados
import numpy as np
import random

np.random.seed(42)
random.seed(42)

def main():

    path = "./data/astral-scopedom-seqres-2.08.fa"

    #leitura dos dados para obter as sequencias e labels
    seqs, labels = carregar_sequencias(path)
    print("seqs:", len(seqs))

    seqs = seqs[:1000]
    labels = labels[:1000]

    #extrai os atributos e gera a matriz
    X = gerar_matriz_kmer(seqs)
    print("shape:", X.shape)

    #roda pipeline
    results = rodar_pipeline(X, labels)
    print("\n=== resultados ===")
    print(results)

    #mostra grafico com resultados
    mostrar_resultados(results)

if __name__ == "__main__":
    main()