import re
import csv

with open('./test-raw-data/does_regex_work.txt',  'rt') as f: # BRING IN RAW FILE
  text_content = f.read()

def open_term_file():
  with open('./datasets/tech_list.txt', 'rt') as l: # BRING IN TERMS
    list_content = l.readlines()
    tech_terms = []
    for line in list_content:
      line_stripped = line.strip('\n')
      tech_terms.append(line_stripped)
  return tech_terms


def get_terms():
  term_list = open_term_file()
  data_list = []
  for term in term_list:
    pattern = r'' + re.escape(term)
    # pattern = 
    # print(pattern)
    match = re.findall(pattern, text_content, re.IGNORECASE)
    lower_match = []
    for item in match:
      lower_match.append(item.lower())
    data_list.append((term, len(lower_match)))
  return data_list

header = ["Term", "Frequency"]
data_list = get_terms()

with open('./datasets/tech_term_frequency_retry.csv', 'a+') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  writer.writerows(data_list)

'''
1. Bring in the raw data file [X]
2. Bring in the term list [X]
4. create a regex for each key in our dictionary(potentially some weird neat cool regex that will match all them) [X]
5. input regex key in our findall() for each dict key [X]
6. increment to the dictionary for each occurrance of key [X]
7. write the counts+terms to new file (csv) []
'''

