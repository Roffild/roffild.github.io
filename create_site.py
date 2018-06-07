url = 'https://github.com/Roffild/RoffildLibrary/blob/master/'
with open('../RoffildLibrary/README.md', 'r') as org:
    with open('index.md', 'w+') as md:
        md.write('{% include header.html %}')
        #md.write("\r\n")
        for line in org:
            md.write(line.replace('](', '](' + url).replace(url + 'http', 'http'))