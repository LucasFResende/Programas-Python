import os

simp_path = r'FORCA\img\forca_vida_6.jpg'
path6 = os.path.abspath(simp_path)
print(path6)
lista = path6.split("\\")
print(lista)
path6 = "\\\\".join(lista)
print(path6, type(path6))
