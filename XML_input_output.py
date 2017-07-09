# for XML_sort virtualenv

import os
import sys

directory_name = sys.argv[1]

for file in os.listdir(directory_name):
    if file.endswith(".xml"):
        print(os.path.join(directory_name, file))
        