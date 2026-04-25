from services.datasetService import dataset_completo
from services.vetorizacaService import vetorizacao, encode_target
#Exibir data 



def imprimir_dados():
    print("Dados")
    df = dataset_completo()
    return df["diagnostico"].value_counts()


print(encode_target())

if __name__ == "__main__":
    print("Wanderson Elias")