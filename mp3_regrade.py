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

def format_response_sheet(csv):
  index_list = [csv[0].index("Timestamp"), csv[0].index("Email Address"), csv[0].index("QCC")]
  print(index_list)
  formatted_csv = []
  for line in csv:
    for i in range(0, len(index_list)):
      del line[index_list[i]-i]
    formatted_csv.append(line)

  for j in range(1, len(formatted_csv)):
    for i in range(1, len(formatted_csv[j])):
      if(formatted_csv[j][i] == ''):
        formatted_csv[j][i] = '0.0'
      try:
        formatted_csv[j][i] = float(formatted_csv[j][i])
      except:
        formatted_csv[j][i] = float(int(formatted_csv[j][i]))

  return formatted_csv

def do_sum(a,b): return a+b

def merge_regrade(csv):
  idx = [csv[0].index(sys.argv[2]), csv[0].index(sys.argv[3])]
  print("Start Index: " + str(idx[0]) + " End Index: " + str(idx[1]))
  students = {}
  merged = {}
  for line in csv[1:]:
    if(line[0] in students and not(line[0] in merged)):
      merged_line = []
      for i in range(idx[0], idx[1]):
        a = students[line[0]][i]
        b = line[i]
        c = (a + b)/2
        if(b > a):
          merged_line.append(c)
        else:
          merged_line.append(a)
      students[line[0]] = students[line[0]][0:idx[0]] + merged_line + students[line[0]][idx[1]:]
      merged[line[0]] = True;
    else:
      students[line[0]] = line;

  merged_csv = []
  merged_csv.append(csv[0])
  for student, data in students.items():
    #line = []
    #line.append(student)
    #line = line + data
    merged_csv.append(data)

  return merged_csv

def print_csv(csv, name):
  with open(name, "w+") as f:
    for line in csv:
      f.write(",".join(map(lambda x: str(x), line))+"\n")

def calc_sum(csv):
  score = []
  score.append(["group", "total"])
  for line in csv[1:]:
    l = []
    l.append(line[0])
    l.append(reduce(do_sum, line[1:]))
    score.append(l)
  return score


# Read in the input CSV file:
csv = []
mp21_total = []
mp21_compass_csv = []

csv = read_csv(sys.argv[1])
fname = (sys.argv[1].split("/")[1]).split(".")[0]
print(fname+"\n")
csv = format_response_sheet(csv)
csv = merge_regrade(csv)
mp3_total = calc_sum(csv)
print_csv(mp3_total, "output/"+fname+"_totals.csv")
print_csv(csv, "output/"+fname+"_regraded.csv")
print(mp3_total)
