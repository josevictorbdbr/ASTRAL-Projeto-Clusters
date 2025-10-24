from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering, SpectralClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score, f1_score
from sklearn.preprocessing import LabelEncoder
from joblib import dump
import  pandas as pd

def run_pipeline(X, labels_true):
    #reduz as dimensoes
    pca = PCA(n_components=300)
    X_pca = pca.fit_transform(X)

    #converte para numeros
    le = LabelEncoder()
    y_true = le.fit_transform(labels_true)

    #lista de algoritmos
    algorithms = {
        "KMeans": KMeans(n_clusters=len(set(y_true)), random_state=42),
        "DBSCAN": DBSCAN(eps=1.5, min_samples=10),
        "Agglomerative": AgglomerativeClustering(n_clusters=len(set(y_true))),
        "Spectral": SpectralClustering(n_clusters=len(set(y_true)), random_state=42)
    }

    results = []

    for name, model in algorithms.items(): 
        try:
            y_pred = model.fit_predict(X_pca)
            sil = silhouette_score(X_pca, y_pred)
            db = davies_bouldin_score(X_pca, y_pred)
            f1 = f1_score(y_true, y_pred, average='macro')
            results.append((name, sil, db, f1))
        except Exception as e:
            print(f"Erro {name}: {e}") 

    df_results = pd.DataFrame(results, columns=["Algoritimo", "Silhouette", "DaviesBouldin", "F1"])
    dump(df_results, "results.joblib")
    return df_results