import sys

wordCount = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if word in wordCount:
        wordCount[word] += count
    else:
        wordCount[word] = count 

for x in wordCount:
    print('%s\t%s' % (x, wordCount[x]))
