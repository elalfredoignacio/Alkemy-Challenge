
# Carga de librerías

import pandas as pd
import requests
#import csv
from datetime import datetime
import os
from sqlalchemy import create_engine
from decouple import config
import logging



# carga de variables de entorno definidas en archivo .env

#datos
url_museos = config('link_museos')
url_cines = config('link_cines')
url_bibliotecas = config ('link_bibliotecas')

# SQL
user = config('sql_user')
pswd = config('sql_password')
host = config('sql_host')
port = config('sql_port')
bd = config('bd_name')



# Función que convierte el número del mes actual en texto
def texto_mes(m):
  if m == '01':
    return 'enero'
  elif m == '02':
    return 'febrero'
  elif m == '03':
    return 'marzo'
  elif m == '04':
    return 'abril'
  elif m == '05':
    return 'mayo'
  elif m == '06':
    return 'junio'
  elif m == '07':
    return 'julio'
  elif m == '08':
    return 'agosto'
  elif m == '09':
    return 'septiembre'
  elif m == '10':
    return 'octubre'
  elif m == '11':
    return 'noviembre'
  else:
    return 'diciembre'



now = datetime.now()
mes = texto_mes(now.strftime('%m'))
root_dir = os.path.abspath(os.curdir) # para saber el directorio raíz



# se crea estructura de directorios para museos
os.chdir(root_dir)  # me posiciono en el directorio raíz
ruta_m = now.strftime('museos/%Y-'+mes) #ruta del directorio destino
os.makedirs(ruta_m, exist_ok=True) # se crea el directorio y sobreescribe si existe
os.chdir(ruta_m) # se posiciona en el directorio creado

# se obtiene y se guarda el archivo csv de museos
archivo_museo = now.strftime('museos-%d-%m-%Y.csv')
req = requests.get(url_museos)
url_content = req.content
# opens the file in binary format for writing
csv_file = open(archivo_museo, 'wb')
csv_file.write(url_content)
csv_file.close()



# se crea estructura de directorios para salas de cine
os.chdir(root_dir)  # me posiciono en el directorio raíz
ruta_c = now.strftime('cines/%Y-'+mes) #ruta del directorio destino
os.makedirs(ruta_c, exist_ok=True) # se crea el directorio y sobreescribe si existe
os.chdir(ruta_c) # se posiciona en el directorio creado

# se obtiene y se guarda el archivo csv de salas de cines
archivo_cine = now.strftime('cines-%d-%m-%Y.csv')
req = requests.get(url_cines)
url_content = req.content
# opens the file in binary format for writing
csv_file = open(archivo_cine, 'wb') 
csv_file.write(url_content)
csv_file.close()




# se crea estructura de directorios para bibliotecas populares
os.chdir(root_dir)  # me posiciono en el directorio raíz
ruta_b = now.strftime('bibliotecas/%Y-'+mes) #ruta del directorio destino
os.makedirs(ruta_b, exist_ok=True) # se crea el directorio y sobreescribe si existe
os.chdir(ruta_b) # se posiciona en el directorio creado

# se obtiene y se guarda el archivo csv de bibliotecas populares
archivo_biblioteca = now.strftime('bibliotecas-%d-%m-%Y.csv')
req = requests.get(url_bibliotecas)
url_content = req.content
# opens the file in binary format for writing
csv_file = open(archivo_biblioteca, 'wb') 
csv_file.write(url_content)
csv_file.close()



# importo datasets
file_m = str(root_dir + '/' + ruta_m + '/' + archivo_museo)
file_c = str(root_dir + '/' + ruta_c + '/' + archivo_cine)
file_b = str(root_dir + '/' + ruta_b + '/' + archivo_biblioteca)
df_m = pd.read_csv(file_m)
df_c = pd.read_csv(file_c)
df_b = pd.read_csv(file_b)


#df_m.info()  # información del dataset
#df_m.columns  # información de las columnas


# me quedo solamente con las columnas que me sirven 
df_museos = df_m[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria', 'provincia', 'localidad', 'nombre', 'direccion', 'CP', 'telefono', 'Mail', 'Web']]



#df_b.info() # información del dataset
#df_b.columns # información de las columnas



# me quedo solamente con las columnas que me sirven 
df_bibliotecas = df_b[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'CP', 'Teléfono', 'Mail', 'Web']]


#df_c.info()  # información del dataset
#df_c.columns  # información de las columnas


# me quedo solamente con las columnas que me sirven 
df_cines = df_c[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Dirección', 'CP', 'Teléfono', 'Mail', 'Web']]


# uniformizo nombres de columnas del df museos
df_museos = df_museos.rename(columns = {'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia', 'IdDepartamento': 'id_departamento', 'categoria': 'categoría', 'direccion': 'domicilio', 'CP': 'código postal', 'telefono': 'número de teléfono', 'Mail': 'mail', 'Web': 'web'})
#df_museos.columns



# uniformizo nombres de columnas del df bibliotecas 
df_bibliotecas = df_bibliotecas.rename(columns = {'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia', 'IdDepartamento': 'id_departamento', 'Categoría': 'categoría', 'Provincia': 'provincia', 'Localidad': 'localidad', 'Nombre': 'nombre', 'Domicilio': 'domicilio', 'CP': 'código postal', 'Teléfono': 'número de teléfono', 'Mail': 'mail', 'Web': 'web'})
#df_bibliotecas.columns


# uniformizo nombres de columnas del df cines 
df_cines = df_cines.rename(columns = {'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia', 'IdDepartamento': 'id_departamento', 'Categoría': 'categoría', 'Provincia': 'provincia', 'Localidad': 'localidad', 'Nombre': 'nombre', 'Dirección': 'domicilio', 'CP': 'código postal', 'Teléfono': 'número de teléfono', 'Mail': 'mail', 'Web': 'web'})
#df_cines.columns


#normalizo todos los datos en una única tabla
df_total = pd.concat([df_museos, df_bibliotecas, df_cines], axis=0)
df_total = df_total.reset_index(drop=True)
# se reestablecen los índices. drop=True opción evita agregar una nueva columna de índice con valores de índice antiguos
# Dataframe df_total: info normalizada de Museos, Salas de Cine y Bibliotecas Populares


# Obtención de dataframe de Cantidad de registros totales por categoría
freq_cat = df_total['categoría'].value_counts() 
#print(freq_cat) 

#type(freq_cat)

df_categoria = pd.DataFrame(freq_cat) #lo convierto en Data Frame
df_categoria.index.names = ['Categoría'] # renombro la columna de indices
df_categoria.columns = ['cant_reg'] # renombro la columna de cantidades
# df_categoria: Dataframe con cantidad de registros totales por categoría


# Obtención de dataframe de Cantidad de registros totales por fuente
# alternativa 1
freq_fuente_m = df_m['fuente'].value_counts() 
freq_fuente_b = df_b['Fuente'].value_counts() 
freq_fuente_c = df_c['Fuente'].value_counts() 
# creo un dataset a partir de las series
df_stitched = pd.concat([freq_fuente_m, freq_fuente_b, freq_fuente_c], axis=0)
#df_stitched.shape


# Obtención de dataframe de Cantidad de registros totales por fuente
# alternativa 2
freq_fuente_b = df_b.groupby(['Fuente']).size()
freq_fuente_m = df_m.groupby(['fuente']).size()
freq_fuente_c = df_c.groupby(['Fuente']).size()
df_stitched = pd.concat([freq_fuente_m, freq_fuente_b, freq_fuente_c], axis=0)
#df_stitched.shape


df_fuente = pd.DataFrame(df_stitched) # lo convierto a Dataframe
df_fuente.index.names = ['Fuente'] # renombro la columna de indices
df_fuente.columns = ['cant_reg'] # renombro la columna de cantidades
## df_fuente: dataframe de Cantidad de registros totales por fuente


# Obtención de dataframe de Cantidad de registros por provincia y categoria
freq = df_total.groupby(['provincia', 'categoría']).size() 
#print(freq)


df_prov_cat = pd.DataFrame(freq, columns = ['cant_reg'])
# df_prov_cat: Dataframe con cantidad de registros por provincia y categoría


# agrupo ds de cines por provincia, sustituyendo NAN por cero
df_c.temp = pd.DataFrame(df_c, columns=['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA'])
df_c.temp['espacio_INCAA'] = df_c.temp['espacio_INCAA'].fillna(0) 
#df_c.temp.head(20)


# sustituyo ´SI´y ´si´en espacio INCAA por 1, y lo llevo a numérico para realizar la suma
df_c.temp.loc[df_c.temp.espacio_INCAA.str.lower() == 'si', 'espacio_INCAA']=1
df_c.temp['espacio_INCAA'] = df_c.temp['espacio_INCAA'].astype(int)
#df_c.temp.info()


# agrupo ds de cines por provincia
df_info_cines = df_c.temp.groupby(by=['Provincia']).sum()
# df_info_cines: Dataframe con información de cines con Cantidad de pantallas, Cantidad de butacas
# y cantidad de espacios INCAA por provincia


df_total = df_total.set_index('categoría') # establezco categoria como índice en ds_total
                                            # (al pasar a SQL se agrega otra columna index)


#agrego a todos los dataframes la fecha de la carga como nueva columna
ahora = datetime.now()
fecha = ahora.strftime('%d/%m/%Y')
df_total ['fecha carga'] = fecha 
df_categoria ['fecha carga'] = fecha 
df_fuente ['fecha carga'] = fecha 
df_prov_cat ['fecha carga'] = fecha 
df_info_cines ['fecha carga'] = fecha 


# CREACIÓN DE TABLAS EN LA DATOS POSTGRES "alkemy" (creacion_bd.sql)

datos_conexion = 'postgresql://' + user + ':' + pswd + '@' + host + ':' + port + '/' + bd
engine = create_engine(datos_conexion)


df_total.to_sql("Total", con=engine, if_exists="replace")
df_categoria.to_sql("Categorias", con=engine, if_exists="replace")
df_fuente.to_sql("Fuentes", con=engine, if_exists="replace")
df_prov_cat.to_sql("Provincias_categorias", con=engine, if_exists="replace")
df_info_cines.to_sql("Info_cines", con=engine, if_exists="replace")


print("""En la base de datos Alkemy, se crearon las siguiente tablas:
      Total
      Categorias
      Fuentes
      Provincias_categorias
      Info_cines""")




