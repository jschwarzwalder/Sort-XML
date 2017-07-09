# for XML_sort virtualenv

import os
import sys
import xmltodict
import xml.etree.ElementTree as ETree

directory_name = sys.argv[1]
# run program as python XML_input_output.py "C:\\directory path"

for file in os.listdir(directory_name):
    if file.endswith(".xml"):
        #print(os.path.join(directory_name, file))
        file = os.path.join(directory_name, file)
        #with open(file) as article_to_parse:
        #    article_dict = xmltodict.parse(article_to_parse.read())
        
        article = ETree.parse(file).getroot()
            
        #print(article_dict['root']['details']['id']['#text'] + " - " + article_dict['root']['details']['description']['#text'])
        
        #print(article)
        
        for child in article:
            if child.tag == "details":
                    for detail in child:
                        if detail.tag == "description":
                            print(detail.text)
                        if detail.tag == "id":
                            print(detail.text)  
            
        