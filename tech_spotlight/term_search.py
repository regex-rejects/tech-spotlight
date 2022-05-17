import re
import csv

with open('./tech_spotlight/jobs_raw.txt', 'rt') as f:  # BRING IN RAW FILE
    text_content = f.read()


def open_term_file():
    with open('./datasets/tech_list.txt', 'rt') as l:  # BRING IN TERMS
        list_content = l.readlines()
        tech_terms = []
        for line in list_content:
            line_stripped = line.strip('\n')
            tech_terms.append(line_stripped)
    return tech_terms


def get_terms():
    term_list = open_term_file()
    data_list = []
    match_num = 0
    for term in term_list:
        if term == "Java":
            pattern = r'Java[^S]'
        else:
            pattern = r'' + re.escape(term)
        match = re.findall(pattern, text_content, re.IGNORECASE)
        lower_match = []
        for item in match:
            match_num += 1
            lower_match.append(item.lower())
            print(match_num)
        data_list.append((term, len(lower_match)))
    return data_list


header = ["Term", "Frequency"]
data_list = get_terms()

with open('test_java_fix.csv', 'w') as f:
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
