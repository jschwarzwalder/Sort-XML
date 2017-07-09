import xmltodict

with open('sample.xml') as fd:
    doc = xmltodict.parse(fd.read())

print(doc['mydocument']['@has'])
print(doc['mydocument']['and']['many'])
print(doc['mydocument']['plus']['@a'])
print(doc['mydocument']['plus']['#text'])
print(doc['mydocument'])