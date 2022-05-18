import re
import csv

with open('/Users/bencarter/projects/Code401/tech-spotlight/tech_spotlight/complete_scrape_may_17_900_jobs.txt', 'rt') as f:  # BRING IN RAW FILE
    text_content = f.read()


def open_term_file():
    with open('/Users/bencarter/projects/Code401/tech-spotlight/datasets/tech_list.txt', 'rt') as l:  # BRING IN TERMS
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
        if term == "Amazon EC2":
            pattern = r'Amazon EC2\W[^C]'
        elif term == "Docker":
            pattern = r'Docker\W[^C]'
        elif term == "Git":
            pattern = r'Git[^HL]'
        elif term == "GitHub":
            pattern = r'GitHub\W[^P]'
        elif term == "Java":
            pattern = r'Java[^S]'
        elif term == "JQuery":
            pattern = r'JQuery\W[^U]'
        elif term == "React":
            pattern = r'React\W[^N]'
        elif term == "Twilio":
            pattern = r'Twilio\W[^S]'
        elif term == "Visual Studio":
            pattern = r'Visual Studio\W[^C]'
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

with open('may_17_900_jobs.csv', 'w') as f:
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
