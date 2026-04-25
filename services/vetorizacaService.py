# 1 - Chamar o framework scikit-learn para usar o TF-DF
# 2 - Instanciar o modelo de vetorização dos dados
# 3 - Pegar os dados que serão vetorizados
from sklearn.feature_extraction.text import TfidfVectorizer
from services.datasetService import dataset_completo
from sklearn.preprocessing import LabelEncoder

#Pré-processamento de textos
def vetorizacao():
    vetoriazador_tfdf = TfidfVectorizer()
    df = dataset_completo()
    X_features = df["sintomas"].astype('str')
    vetoriazador_tfdf.fit(X_features)
    X_features_vetorizadas = vetoriazador_tfdf.transform(X_features)
    return X_features_vetorizadas


#Função para fazer o encoding dos labels ou targets para facilitar na hora de setar valores

def encode_target():
    label_encoder = LabelEncoder()
    df = dataset_completo()
    Y_labels = df["diagnostico"].astype('str')
    encoder = label_encoder.fit(Y_labels)
    Y_encoded = label_encoder.transform(Y_labels)
    return Y_encoded

print(encode_target())