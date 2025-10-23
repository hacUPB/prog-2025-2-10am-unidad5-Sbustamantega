lista = ["the show must go on", "Dont cry", "verano traidor", "Why´d you only call me when you are high", "still loving you"]
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
modo = "w" # escritura - sobreescribe el archivo si ya existe

nombre_archivo = "canciones.txt"
fp = open(ubicacion + "\\" + nombre_archivo, modo, encoding="utf-8")
for cancion in lista:
    fp.write(cancion + "\n")
fp.close()
