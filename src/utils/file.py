from dataclasses import field
import os
import csv
import json

JSON_EXTENSION = '.json'
CSV_EXTENSION = '.csv'
CSV_DELEMITER = ','

def read_file(path):
  _, file_extension = os.path.splitext(path)

  try:
    file = open(path, mode='r')
  except OSError:
    print(f"Could not open file: {path}")
  raise

  data = {}

  with file:
    if (file_extension == JSON_EXTENSION):
      data = json.load(file)
      return data
    elif (file_extension == CSV_EXTENSION):
      data = csv.DictReader(file, delimiter=CSV_DELEMITER)
      return data
    else:
      raise Exception(f"Reading file extension: {file_extension} is not supported")

def write_to_csv(path, rows):
  try:
    file = open(path, mode='w')
  except OSError:
    print("Could not open file: {path}")
    raise

  if (len(rows) == 0): return

  with file:
    fieldnames = list(rows[0].keys())

  print(f"writing to file: {file} with fieldnames: {fieldnames}")
  writer = csv.DictWriter(file, fieldnames=fieldnames)

  failures = []

  for row in rows:
    try:
      writer.writerow(row)
    except csv.Error:
      failures.append
    print(f"Error writing to csv for row: {csv.Error}")

    print(f"{len(rows)-len(failures)} of {len(rows)} rows inserted successfully")
