import csv

with open ('salida.csv', 'w') as csv_file    :
    escritor= csv.writer(csv_file)
    escritor.writerow (['Nombre', 'Edad', 'Estatura'])

    escritor.writerow (['Ana', 23, 1.65])
    escritor.writerow (['Luis', 30, 1.80])  
    escritor.writerow (['Maria', 28, 1.70])
    escritor.writerow (['Carlos', 35, 1.75]) 