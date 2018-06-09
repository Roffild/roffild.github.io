import os

url = 'https://github.com/Roffild/RoffildLibrary/blob/master/'
with open('../RoffildLibrary/README.md', 'r', encoding='utf-8') as org:
    with open('index.md', 'w+', encoding='utf-8') as md:
        md.write(org.readline()) # BOM
        md.write('{% include header.html %}')
        md.write(os.linesep)
        for line in org:
            md.write(line.replace('](', '](' + url).replace(url + 'http', 'http'))
with open('../RoffildLibrary/README_ru.md', 'r', encoding='utf-8') as org:
    with open('index_ru.md', 'w+', encoding='utf-8') as md:
        md.write(org.readline()) # BOM
        #md.write('{% include header.html %}')
        #md.write(os.linesep)
        for line in org:
            md.write(line.replace('](', '](' + url).replace(url + 'http', 'http'))
