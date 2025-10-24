from models.features import load_sequences, generate_kmer_matrix
from controllers.pipeline import run_pipeline
from view.plots import show_results


def main():
    path = "../data/astral-scopedom-seqres-2.08.fa"

    #leitura dos dados
    seqs, labels = load_sequences(path)
    print("seqs:", len(seqs))

    seqs = seqs[:1000]
    labels = labels[:1000]

    #extrai os atributos
    X = generate_kmer_matrix(seqs)
    print("shape:", X.shape)

    #roda pipeline
    results = run_pipeline(X, labels)
    print("\n=== resultados ===")
    print(results)

    #mostra grafico
    show_results(results)

if __name__ == "__main__":
    main()