from hdfs import InsecureClient

# Datos de conexión
HDFS_HOSTNAME = '172.23.0.6'
HDFSCLI_PORT = 9870
HDFSCLI_CONNECTION_STRING = f'http://{HDFS_HOSTNAME}:{HDFSCLI_PORT}'

# En nuestro caso, al no usar Kerberos, creamos una conexión no segura
hdfs_client = InsecureClient(HDFSCLI_CONNECTION_STRING)

# Leemos el fichero de 'El quijote' que tenemos en HDFS
fichero = '/test/carpeta1/Chile.txt'
with hdfs_client.read(fichero) as reader:
    texto = reader.read()

print(texto)
