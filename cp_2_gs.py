import sys
import os
from functools import reduce

def read_csv(name):
  print("Opening "+name)

  csv = []
  with open(name) as fp:
    line = []
    for l in fp:
      line = l.strip().split(",")
      csv.append(line)
  return csv

def merge_sheets(csv, netid_list):
  totals = {}
  for i in netid_list[1:]:
    totals[i[0]] = i[1]

  for i in csv[1:]:
    if i[csv[0].index("Username")] in totals:
      i[-1] = totals[i[csv[0].index("Username")]]

  return csv

def print_csv(csv, name):
  with open(name, "w+") as f:
    for line in csv:
      f.write(",".join(map(lambda x: str(x), line))+"\n")

# Read in the input CSV file:
csv = []
mp21_total = []

csv = read_csv(sys.argv[1])
mp21_total = read_csv(sys.argv[2])
csv = merge_sheets(csv, mp21_total)
print_csv(csv, "mp21_grade_center.csv")
