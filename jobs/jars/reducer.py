import sys

wordCount = {}

for line in sys.stdin:
    line = line.strip()
    word, count, pag = line.split('\t')

    try:
        count = int(count)
    except ValueError:
        continue

    if word in wordCount:
        if pag in wordCount[word]:
            wordCount[word][pag] += count
        else:
            wordCount[word][pag] = count
    else:
        wordCount[word] = {}
        wordCount[word][pag] = count

print('\n')

for x in wordCount:
    palabra = x
    for y in wordCount[x]:
        palabra += '¬' + y + '¬' +str(wordCount[x][y])
    
    print(palabra)