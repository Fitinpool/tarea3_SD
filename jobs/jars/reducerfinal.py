import sys

wordCount = {}

for line in sys.stdin:
    line = line.strip()
    words = line.split('¬')

    word = words.pop(0)

    if word in wordCount:
        for x in words:
            wordCount[word].append(x)
    else:
        wordCount[word] = []
        for x in words:
            wordCount[word].append(x)

for x in wordCount:
    palabra = x
    for y in wordCount[x]:
        palabra += '¬' + y
    
    print(palabra)


    