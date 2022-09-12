from email.mime import image
import openpyxl
import base64
from openpyxl_image_loader import SheetImageLoader
import pandas as pd


def extraer_texto():
    df = pd.read_excel("/home/rocio/Desktop/Proyectos/imagenes.xlsx") 
    data_1 = df.iloc[::3]
    print(data_1)


#def extraer_imagen():

    #pxl_doc = openpyxl.load_workbook('imagenes.xlsx')
    #sheet = pxl_doc['Hoja1']
    #image_loader = SheetImageLoader(sheet)

    #lista = []
    #for i in range(1,5):
        
      # #base64.encodestring(lista)

       # msg = base64.encrypt(lista)
        #msgb64 = base64.b64encode(msg)
        #print(msgb64)
    
#     image = open('deer.gif', 'rb') #open binary file in read mode
# image_read = image.read()
# image_64_encode = base64.encodestring(image_read)


extraer_texto()
#extraer_imagen()