# -*- coding: utf-8 -*-
#!python3

import re
import os
import csv



#tests for non ASCII characters

# Writes all output
output = open('output.csv', 'w', newline='', encoding='utf-8')
output_writer = csv.writer(output)
output_writer.writerow(["Path", "Document_Name", "Record_ID"])

rootdir = r"I:/Cases"
for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            #excludes thumbs.db files
            if file ==("Thumbs.db"):
                continue
#============================================================================
# Retrieves Path and Document Name
            print(subdir)
            path = (subdir).replace("\\", "/")
            doc_name = file

#Handles 1979 and 1981, adding "19" to the record name

            if "1979" in subdir or "1981" in subdir:

                record_name = re.sub(".*(\d\d[.]\d\d\d\w).*$", "19" +"\\1",
                                     file)

                output_writer.writerow([path, doc_name, record_name])

#Handles records prior to 2014

            elif "1979" not in subdir \
            and "1981" not in subdir \
            and "2016" not in subdir \
            and "2015" not in subdir\
            and "2016" not in subdir \
            and "2017" not in subdir \
            and "2018" not in subdir:

                record_name = re.sub(".*(\d\d[.]\d\d(\d)?\w).*$", "19" + "\\1",
                                     file)

#============================================================================
#Writes records in csv file

                output_writer.writerow([path, doc_name, record_name])
#============================================================================
output.close()
