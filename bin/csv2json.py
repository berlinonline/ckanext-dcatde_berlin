# -*- coding: utf-8 -*-

import csv
import json
import sys

if len(sys.argv) != 4:
  print "usage: python csv2json.py CSV_FILE_PATH INDEX_COLUMN_NAME JSON_FILE_PATH"
  sys.exit()

csv_file_path = sys.argv[1]
index_column_name = sys.argv[2]
json_file_path = sys.argv[3]

f = open(csv_file_path, 'rb')
reader = csv.reader(f)
headers = reader.next()
index_column = 0
if index_column_name in headers:
  index_column = headers.index(index_column_name)
else:
  print("Cannot find column header '{}', using first column '{}' as index.".format( index_column_name, headers[0]))

data = {}

for row in reader:
  entry = {}
  for index, value in enumerate(row):
    if index != index_column:
      entry[headers[index]] = value
  data[row[index_column]] = entry

with open(json_file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True)