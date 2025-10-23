path = "C:\\Users\\B09S202est\\Desktop\\Archivos"

nombre_archivo = "frutas.txt"
modo = "a" #solo escritura - sobreescribe el archivo si ya existe
fp = open(path+"\\"+nombre_archivo, modo, encoding="utf-8")
frase = input("por favor ingrese una frase: ")
edad = int(input("por favor ingrese su edad: "))
estatura = float(input("por favor ingrese su estatura: "))

fp.write(frase + "\n")
fp.write(str(edad) + "\n")
fp.write(str(estatura))
fp.close()

