

import csv
'''''''''''''''
with open('C:\\Users\\B09S202est\\Documents\\programacion-2025\\prog-2025-2-10am-unidad5-Sbustamantega\\Libro1.csv', 'r') as csv_file    :
    lector = csv.reader(csv_file, delimiter=';')
    presion = []
    encabezado = next(lector)  # Leer la primera fila como encabezado
    print (encabezado[0])
    for fila in lector:
        dato = int(fila[0])
        presion.append(dato)
    
print (presion)
'''''''''''






with open('Libro1.csv', 'r') as csv_file    :
    lector = csv.reader(csv_file, delimiter=';')
    presion = []
    encabezado = next(lector)  # Leer la primera fila como encabezado
    print (encabezado[3])
    for fila in lector:
        fila[3] = fila[3].replace(',', '.')  # Reemplazar coma por punto
        dato = float(fila[3])
        presion.append(dato)
    
print (presion)
