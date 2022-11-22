import re

busqueda = ['Chile', 'Argentina', 'Bolivia', 'Perú', 'Mexico', 'Brazil', 'Paraguay', 'Ecuador', 'Venezuela', 'Uruguay']

bandera = 0
wordCount = {}

for pais in busqueda:
    if bandera == 0 :
        lectura = open('./carpeta1/' + pais + '.txt')
        for line in lectura:
            line = re.sub(r'\W+',' ',line.strip())
            words = line.split()

            for word in words:
                if word in wordCount:
                    if pais in wordCount[word]:
                        wordCount[word][pais] += 1
                    else:
                        wordCount[word][pais] = 1
                else:
                    wordCount[word] = {}

        bandera += 1
    else:
        lectura = open('./carpeta2/' + pais + '.txt')
        for line in lectura:
            line = re.sub(r'\W+',' ',line.strip())
            words = line.split()

            for word in words:
                if word in wordCount:
                    if pais in wordCount[word]:
                        wordCount[word][pais] += 1
                    else:
                        wordCount[word][pais] = 1
                else:
                    wordCount[word] = {}

        bandera -= 1

with open("MapReducer.txt", "w") as text_file:
    text_file.write("%s" % wordCount)
