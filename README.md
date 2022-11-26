# Tarea 3

Para empezar ejecutamos 

```sh
docker volume prune
```

Para poder limpiar volumenes anteriores que puedan interferir con nuestro docker, luego ejecutamos docker-compose
```sh
docker-compose up --build -d
```

Y verificamos que se haya encendido en http://localhost:9870/.

Este repositorio no cuenta con las busquedas que usaremos por lo que necesitaremos cargarlas con un archivo python que buscar paises en wikipedia y mueve la info a txt

```sh
python3 obtenerDatos.py
```

Una vez con los datos nos metemos al contenedor namenode que nos permite dar ordenes a hadoop a sus datanode

```sh
docker exec -it namenode bash
```

Una vez aqui todas nuestras carpetas del local "/jobs/" se compartiran con el contenedor asi que nos metemos jars donde se encuentra nuestros mapper y reducer

```sh
cd jars
```

Ahora para empezar borramos cualquier rastro de archivos que vayamos a utilizar y los volvemos a crear con las carpetas que usaremos ademas de sus contenidos

```sh
hadoop fs -rm -r -f /test
hadoop fs -mkdir -p /test/
hadoop fs -mkdir -p /test/inputresultados
hadoop fs -copyFromLocal -f /app/data/carpeta1 /test/
hadoop fs -copyFromLocal -f /app/data/carpeta2 /test/
```

Ya ubicados en "/jars" y con las carpetas en datanode creadas, procedemos a ejecutar nuestro mapper y reducer en cada carpeta

```sh
mapred streaming -files mapper.py,reducer.py \
-input /test/carpeta1 \
-output /test/outcarpeta1 \
-mapper "python mapper.py" \
-reducer "python reducer.py"

mapred streaming -files mapper.py,reducer.py \
-input /test/carpeta2 \
-output /test/outcarpeta2/ \
-mapper "python mapper.py" \
-reducer "python reducer.py"
```

Una vez que tengamos cada archivo procedemos a modificarles el nombre y moverlos a una carpeta donde terminaremos uniendo la carpeta 1 y 2

```sh
hadoop fs -mv /test/outcarpeta1/part-00000 /test/outcarpeta1/r1.txt
hadoop fs -mv /test/outcarpeta2/part-00000 /test/outcarpeta2/r2.txt
hadoop fs -mv /test/outcarpeta1/r1.txt /test/inputresultados/
hadoop fs -mv /test/outcarpeta2/r2.txt /test/inputresultados/
hadoop fs -ls /test/inputresultados
```

Finalmente ejecutamos el mapreduce para unirlos

```sh
mapred streaming -files mapperfinal.py,reducerfinal.py \
-input /test/inputresultados \
-output /test/final \
-mapper "python mapperfinal.py" \
-reducer "python reducerfinal.py"
```

Para poder ver el resultados ejecutamos el ultimo comando en el contenedor el cual copia el archivo final de hadoop al local

```sh
hdfs dfs -get /test/final/final.txt /app/data/final/
exit
```
Ahora en el local iniciamos la api para ver su ejecucion en localhost:8000/

```sh
cd api
python3 api.py
```
