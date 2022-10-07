Para crear el entorno virtual para el proyecto (por ejemplo en visual studio code):
1. copiar el directorio src
2. copiar el archivo requerimientos.txt
3. copiar el archivo .env
4. crear el entorno virtual "env" ejecutando: virtualenv -p python3 env
5. activar el nuevo entorno ejecutando: .\env\scripts\activate

Para instalar las dependencias necesarias, dentro del entorno virtual ejecutar:
pip install -r .\requerimientos.txt

Las variables de entorno se encuentran en el archivo conf.env

Para crear la base de datos postgreSQL ejecutar el script creacion_bd.sql

Para crear las tablas y actualizar la información ejecutar desde el nuevo entorno virtual el script:
.\src\Alkemy_challenge.py