import os
from datetime import datetime

def readme(fromf, tof):
    url = 'https://github.com/Roffild/RoffildLibrary/blob/master/'
    with open(fromf, 'r', encoding='utf-8-sig') as org:
        with open(tof, 'w+', encoding='utf-8-sig') as md:
            md.write('{% include google.html %}{% include header.html %}\n')
            org.readline()
            for line in org:
                md.write(line.replace('](', '](' + url).replace(url + 'http', 'http'))
            md.write('\n[English](https://roffild.com/), [Russian](https://roffild.com/index_ru.html)\n')

readme('../RoffildLibrary/README.md', 'index.md')
readme('../RoffildLibrary/README_ru.md', 'index_ru.md')

def gettime(filename):
    return datetime.utcfromtimestamp(os.path.getmtime(filename)).isoformat(timespec='seconds') + '+03:00'

url = 'https://roffild.com/'
with open('sitemap.xml', 'w', encoding='utf-8') as sm:
    sm.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    sm.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    sm.write('<url><loc>' + url + '</loc><lastmod>' + gettime('index.md') + '</lastmod><priority>1.00</priority></url>\n')
    sm.write('<url><loc>' + url + 'index_ru.md</loc><lastmod>' + gettime('index_ru.md') + '</lastmod><priority>1.00</priority></url>\n')
    for root, folder, name in os.walk('mql5'):
        purl= url + root.replace('\\', '/') + '/'
        for fl in name:
            if fl.find('.htm') > 0:
                sm.write('<url><loc>' + purl + fl.replace('\\', '/') + '</loc><lastmod>' + gettime(root + '/' + fl) + '</lastmod></url>\n')
    for root, folder, name in os.walk('java'):
        purl= url + root.replace('\\', '/') + '/'
        for fl in name:
            if fl.find('.htm') > 0:
                sm.write('<url><loc>' + purl + fl.replace('\\', '/') + '</loc><lastmod>' + gettime(root + '/' + fl) + '</lastmod></url>\n')
    sm.write('</urlset>\n')
