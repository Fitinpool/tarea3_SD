import wikipedia as wiki
import os
import errno

try:
    os.mkdir('carpeta1')
    os.mkdir('carpeta2')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

busqueda = ['Chile', 'Argentina', 'Bolivia', 'Perú', 'Mexico', 'Brazil', 'Paraguay', 'Ecuador', 'Venezuela', 'Uruguay']

bandera = 0

for pais in busqueda:

    busquedaWiki = wiki.page(pais)

    if bandera == 0 :
        with open('./carpeta1/' + pais + ".txt", "w") as text_file:
            text_file.write("%s" % busquedaWiki.content)
        bandera += 1
    else:
        with open('./carpeta2/' + pais + ".txt", "w") as text_file:
            text_file.write("%s" % busquedaWiki.content)
        bandera -= 1

