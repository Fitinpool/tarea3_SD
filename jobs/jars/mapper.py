import sys

paises = ['Chile.txt', 'Argentina.txt', 'Bolivia.txt', 'Perú.txt', 'Mexico.txt', 'Brazil.txt', 'Paraguay.txt', 'Ecuador.txt', 'Venezuela.txt', 'Uruguay.txt']

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    if len(words) > 0: 
        if words[0] in paises:
            nombreArchivo = words.pop(0)

    for word in words:
        print('%s\t%s\t%s' % (word, 1, nombreArchivo))
