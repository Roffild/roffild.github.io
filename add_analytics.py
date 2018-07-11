import os

analytics = ''

with open('_includes/analytics.html', 'r', encoding='utf-8-sig') as org:
    analytics = org.readlines()

def test(filename):
    if filename.find('.htm') < 0:
        return False
    with open(filename, 'r', encoding='utf-8-sig') as md:
        for line in md:
            if line.find('</head>') > -1 and line.find('<!-- analytics -->') < 0:
                return True
    return False

def inc(filename):
    text = ''
    with open(filename, 'r', encoding='utf-8-sig') as md:
        text = md.readlines()
    with open(filename, 'w', encoding='utf-8-sig') as md:
        for line in text:
            if line.find('</head>') > -1 and line.find('<!-- analytics -->') < 0:
                md.writelines(analytics)
                md.write('<!-- analytics -->')
            md.write(line)

def scan(path):
    for root, folder, name in os.walk(path):
        for file in name:
            full = os.path.join(root, file)
            if test(full):
                print(full)
                inc(full)

scan('mql5')
scan('java')
