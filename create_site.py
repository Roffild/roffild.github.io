import os
from datetime import datetime

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

def gettime(filename):
    return datetime.utcfromtimestamp(os.path.getmtime(filename)).isoformat()

url = 'https://roffild.com/'
with open('sitemap.xml', 'w', encoding='utf-8') as sm:
    sm.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    sm.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    sm.write('<url><loc>' + url + '</loc><lastmod>' + gettime('index.md') + '</lastmod><priority>1.00</priority></url>\n')
    sm.write('<url><loc>' + url + 'index_ru.md</loc><lastmod>' + gettime('index_ru.md') + '</lastmod><priority>1.00</priority></url>\n')
    for root, folder, name in os.walk('mql5'):
        purl= url + root.replace('\\', '/') + '/'
        print(root, folder, name, sep='  ')
        print(purl)
        for fl in name:
            if fl.find('.htm') > 0:
                print(root + fl)
                sm.write('<url><loc>' + purl + fl.replace('\\', '/') + '</loc><lastmod>' + gettime(root + '/' + fl) + '</lastmod></url>\n')
                print(purl + fl)
    for root, folder, name in os.walk('java'):
        purl= url + root.replace('\\', '/') + '/'
        print(root, folder, name, sep='  ')
        print(purl)
        for fl in name:
            if fl.find('.htm') > 0:
                print(root + fl)
                sm.write('<url><loc>' + purl + fl.replace('\\', '/') + '</loc><lastmod>' + gettime(root + '/' + fl) + '</lastmod></url>\n')
                print(purl + fl)
    sm.write('</urlset>\n')
