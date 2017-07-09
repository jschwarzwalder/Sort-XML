# for XML_sort virtualenv

import os
for file in os.listdir("/mydir"):
    if file.endswith(".xml"):
        print(os.path.join("/mydir", file))
        