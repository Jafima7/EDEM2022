import pandas as pd
import chunk
import re

# Leer CSV
pokemon_csv_df = pd.read_csv('pokemon_data.csv', 
                         dtype={
                           "Name": str,
                           "Type 1": str,
                           "Speed": int,
                           "Generation": int
                         })
# Leer de un Excel
pokemon_excel_df = pd.read_excel('pokemon_data.xlsx')

# Leer de un TXT
pokemon_txt_df = pd.read_csv('pokemon_data.txt', delimiter='\t')


# Imprimir los Valores
print(pokemon_csv_df)

# Imprimir los cinco primeros
print(pokemon_csv_df.head(5))

# Imprimir los 5 ultimos
print(pokemon_csv_df.tail(5))

# Obtener nombres de columnas
print(pokemon_csv_df.columns)

# Obtener todos los nombres
nombres = pokemon_csv_df['Name']
print(*nombres)

# Obtener todos los nombres  sus velocidades
# Opcion 1
nombres_velocidades = pokemon_csv_df[['Name', 'Speed']]
print(nombres_velocidades)

# Opcion 2
lista_columnas = ['Name','Speed']
nombres_velocidades = pokemon_csv_df[lista_columnas]
print(nombres_velocidades)

# Obtener los primeros 5 nombres
primeros_5 = pokemon_csv_df['Name'][0:5]
print(primeros_5)

# Obtener primera fila
print(pokemon_csv_df.iloc[0])

# Obtener las 3 primeras filas
print(pokemon_csv_df.iloc[0:3])

# Obtener las 3 ultimas filas
print(pokemon_csv_df.iloc[-3:])


