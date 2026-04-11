from services.datasetService import dataset_completo

#Exibir data 



def imprimir_dados():
    print("Dados")
    df = dataset_completo()
    return df


imprimir_dados()

if __name__ == "__main__":
    print("Wanderson Elias")