# for XML_sort virtualenv

import os
import sys
import xmltodict
import xml.etree.ElementTree as ETree

directory_name = sys.argv[1]
# run program as python XML_input_output.py "C:\\directory path"

#Output file
CSV = open("SMC descriptions.csv", "w") 

for file in os.listdir(directory_name):
    if file.endswith(".xml"):
        #print(os.path.join(directory_name, file))
        file = os.path.join(directory_name, file)
        #with open(file) as article_to_parse:
        #    article_dict = xmltodict.parse(article_to_parse.read())
        
        article = ETree.parse(file).getroot()
            
        #print(article_dict['root']['details']['id']['#text'] + " - " + article_dict['root']['details']['description']['#text'])
        
        #print(article)
        
        #processing the file and looking for the text under description and id. These are under details which is under root tag.
        for child in article:
            if child.tag == "details":
                    description = ""
                    id = ""
                    for detail in child:
                        if detail.tag == "description":
                            #print(detail.text)
                            description = detail.text
                        if detail.tag == "id":
                            print(detail.text)  
                            id = detail.text
                    CSV.write(id + "," + "'" + description + "'\n")
        