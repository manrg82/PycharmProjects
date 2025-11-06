import os

ruta = os.getcwd()
print("Ruta actual: "+ruta)
print("Archivos en la ruta: ")
for filename in os.listdir(ruta):
    print(filename)
