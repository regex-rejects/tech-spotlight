import re

with open('../datasets/placeholder.txt', 'rt') as f: # BRING IN RAW FILE
  text_content = f.read()

def open_term_file():
  with open('../datasets/tech_list.txt', 'rt') as l: # BRING IN TERMS
    list_content = l.readlines()
    tech_terms = []
    for line in list_content:
      line_stripped = line.strip('\n')
      tech_terms.append(line_stripped)
  return tech_terms


def get_terms():
  term_list = open_term_file()
  for term in term_list:
    pattern = r'' + re.escape(term)
    # pattern = 
    # print(pattern)
    match = re.findall(pattern, text_content, re.IGNORECASE)
    lower_match = []
    for item in match:
      lower_match.append(item.lower())
    print(lower_match)

'''
1. Bring in the raw data file [X]
2. Bring in the term list [X]
3. loop through each key in our dictionary []
4. create a regex for each key in our dictionary(potentially some weird neat cool regex that will match all them) []
5. input regex key in our findall() for each dict key []
6. increment to the dictionary for each occurrance of key []
7. write the counts+terms to new file (csv) []
'''

get_terms()
