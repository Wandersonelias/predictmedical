# 1 - Chamar o framework scikit-learn para usar o TF-DF
# 2 - Instanciar o modelo de vetorização dos dados
# 3 - Pegar os dados que serão vetorizados
from sklearn.feature_extraction.text import TfidfVectorizer
from datasetService import dataset_completo

def Vetoriazacao():
    vetoriazador_tfdf = TfidfVectorizer()
    df = dataset_completo()
    X_features = df["sintomas"].astype('str')
    dados_vetorizados = vetoriazador_tfdf.fit(X_features)
    X_features_vetorizadas = dados_vetorizados.transform()
    return X_features_vetorizadas, vetoriazador_tfdf


