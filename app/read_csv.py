import csv

#creamos la función
def read_csv(path):
  # le damos permiso solo lectura
  with open(path, 'r') as csvfile:
    # creamos la variable donde alojaremos el csv, delimitado por comas
    reader = csv.reader(csvfile, delimiter= ',')
    # obtenemos la primera columna con  las cabeceras del csv
    header = next(reader)
    # creamos una lista donde guardaremos el resultado final
    data = []
    # iteraremos fila por fila
    for row in reader:
      # unimos las cabeceras con cada fila
      iterable = zip(header, row)
      # lo convertimos en una lista
      # print(list(iterable))
      # crearemos un diccionario
      country_dict = {key: value for key, value in iterable}
      # agregamos cada iteracion a la lista final
      data.append(country_dict)
    return data
     
# le indicamos la ruta de donde sacaremos el archivo
if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])