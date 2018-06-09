import os

url = 'https://github.com/Roffild/RoffildLibrary/blob/master/'
with open('../RoffildLibrary/README.md', 'r') as org:
    with open('index.md', 'w+') as md:
        md.write(org.readline()) # BOM
        md.write('{% include header.html %}')
        md.write(os.linesep)
        for line in org:
            md.write(line.replace('](', '](' + url).replace(url + 'http', 'http'))
