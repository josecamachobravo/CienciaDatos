import pandas as pd
import matplotlib.pyplot as plt
import random

ruta = r'https://raw.githubusercontent.com/josecamachobravo/CienciaDatos/main/CienciaDatos/Poblacion_medellin_2018.csv'
df = pd.read_csv(ruta)

print(df.head())

print(df.tail())

print(df.describe())

# Grafico Mostrar cantidad de gente por códigos seleccionados al azar
codigos_aleatorios = random.sample(df['Código'].unique().tolist(), k=4)
df_seleccionados = df[df['Código'].isin(codigos_aleatorios)]
cantidad_gente = df_seleccionados.groupby('Código')['Total_2018'].sum()

plt.figure(figsize=(10, 6))
plt.bar(cantidad_gente.index, cantidad_gente.values)
plt.xlabel('Código')
plt.ylabel('Cantidad de Gente')
plt.title('Cantidad de Gente por Código (Selección Aleatoria)')
plt.show()


# Graficar cantidad de gente por cada 'Tipo_división_geográfica'
df_sin_total = df[df['Tipo_división_geográfica'] != 'Total Medellín']
grupo_tipo = df_sin_total.groupby('Tipo_división_geográfica')['Total_2018'].sum()

plt.figure(figsize=(10, 6))
plt.bar(grupo_tipo.index, grupo_tipo.values)
plt.xlabel('Tipo de División Geográfica')
plt.ylabel('Cantidad de Gente')
plt.title('Cantidad de Gente por Tipo de División Geográfica')
plt.show()

# Grafiar la cantidad de gente que se determina por 6 Código al azar(grafico torta)
codigos_azar = random.sample(df['Código'].unique().tolist(), 6)

df_azar = df[df['Código'].isin(codigos_azar)]

gente_por_codigo = df_azar.groupby('Código')['Total_2018'].sum()

plt.figure(figsize=(8, 8)) 
plt.pie(gente_por_codigo, labels=gente_por_codigo.index, autopct='%1.1f%%')
plt.title('Cantidad de Gente por Código (Muestra Aleatoria)')
plt.axis('equal')
plt.show()