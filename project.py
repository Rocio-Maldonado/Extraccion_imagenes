import pandas as pd

def extract_info():
    df = pd.read_excel("/home/rocio/Desktop/Proyectos/imagenes.xlsx")
    data_1 = df.iloc[ 2 : 2]
    print( data_1 )
extract_info()


    