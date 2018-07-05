import os
from datetime import datetime

def readme(fromf, tof):
    url = 'https://github.com/Roffild/RoffildLibrary/blob/master/'
    with open(fromf, 'r', encoding='utf-8-sig') as org:
        with open(tof, 'w+', encoding='utf-8-sig') as md:
            md.write('---\n')
            md.write('title: ' + org.readline().replace('# ', ''))
            md.write('---\n')
            for line in org:
                md.write(line.replace('](', '](' + url).replace(url + 'http', 'http'))
            md.write('\n[English](https://roffild.com/), [Russian](https://roffild.com/ru/)\n')

readme('../RoffildLibrary/README.md', 'index.md')
readme('../RoffildLibrary/README_ru.md', 'ru/index.md')

def gettime(filename):
    return datetime.utcfromtimestamp(os.path.getmtime(filename)).isoformat(timespec='seconds') + '+00:00'

def siteurl(url, path, ext, onlyroot = False, priority = '0.5'):
    for root, folder, name in os.walk(path):
        purl = url + root.replace('\\', '/').replace('./', '') + '/'
        if root == '.':
            purl = url
        for fl in name:
            if fl.find(ext) > 0:
                mtime = gettime(root + '/' + fl)
                if ext.find('htm') < 0:
                    fl = fl.replace(ext, '.html')
                sm.write('<url><loc>' + purl + fl.replace('\\', '/') + '</loc><lastmod>' + mtime + '</lastmod><priority>' + priority + '</priority></url>\n')
        if onlyroot and root == path:
            return 0

url = 'https://roffild.com/'
with open('sitemap.xml', 'w', encoding='utf-8') as sm:
    sm.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    sm.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    siteurl(url, '.', '.md', True, '1.0')
    siteurl(url, 'ru', '.md', False, '1.0')
    siteurl(url, 'mql5', '.htm')
    siteurl(url, 'java', '.htm')
    sm.write('</urlset>\n')
