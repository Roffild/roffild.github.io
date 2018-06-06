url = 'https://github.com/Roffild/RoffildLibrary/'
with open('../RoffildLibrary/README.md', 'r') as org:
    with open('index.md', 'w+') as md:
        for line in org:
            md.write(line.replace('](', '](' + url).replace(url + 'http', 'http'))