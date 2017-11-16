from PIL import Image
import zbarlight
from os import walk, getcwd


def ls(ruta = getcwd()):
     listaarchivos = []
     for (_, _, archivos) in walk(ruta):
          listaarchivos.extend(archivos)
     return listaarchivos

file2 = ls(ruta = getcwd())

print "Inciando"

f=open("apl.csv","w")
f.write("FOTO,CODIGO \n")

cont = 0
if file2:
    for file2 in file2:
        # saber si es "JPG"
        if file2.find("JPG"):
            print str(cont) + ":Buscando en:" + file2
            cont = cont + 1
            file_path = file2
            if not str(file2).find(".JPG") == -1:
                with open(file_path, 'rb') as image_file:
                    image = Image.open(image_file)
                    image.load()
                    codes = zbarlight.scan_codes('qrcode', image)
                    lista_codes = []
                    for i in codes:
                        if i not in lista_codes:
                            lista_codes.append(i)
                    if lista_codes:
                        for lista_codes in lista_codes:
                            f.write(file_path + ","  + (lista_codes) + "\n")
                            print file_path + "-->"  + "Cod: " + (lista_codes)
        else:
            print "No encuentro ficheros"
f.close()
print "Terminado"

