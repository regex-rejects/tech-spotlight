import re
import csv


def open_text(read_file):
    with open(read_file, 'rt') as f:  # BRING IN RAW FILE
        text_content = f.read()
    return text_content


def open_terms(terms_file):
    with open(terms_file, 'rt') as f:  # BRING IN TERMS
        list_content = f.readlines()
        tech_terms = []
        for line in list_content:
            line_stripped = line.strip('\n')
            tech_terms.append(line_stripped)
    return tech_terms


def get_terms(read_file, terms_file):
    text_content = open_text(read_file)
    term_list = open_terms(terms_file)
    data_list = []
    # match_num = 0
    for term in term_list:
        if term == "Amazon EC2":
            pattern = r'Amazon EC2\W[^C]'
        if term == "Angular":
            pattern = r'\WAngular\D[^jsJS]'
        if term == "Apache Tomcat":
            pattern = r'Tomcat'
        elif term == "CSS 3":
            pattern = r'CSS'
        elif term == "Docker":
            pattern = r'Docker\W[^C]'
        elif term == "ExpressJS":
            pattern = r'Express'
        elif term == "Git":
            pattern = r'Git[^HL]'
        elif term == "GitHub":
            pattern = r'GitHub\W[^P]'
        elif term == "HTML5":
            pattern = r'HTML'
        elif term == "Java":
            pattern = r'Java[^S]'
        elif term == "JQuery":
            pattern = r'JQuery\W[^U]'
        elif term == ".NET CORE":
            pattern = r'.NET\sC[oO][rR][eE]\W'
        elif term == "NoSQL":
            pattern = r'\WNoSQL\W'
        elif term == "React":
            pattern = r'React\W[^N]'
        elif term == "SQL":
            pattern = r'\WSQL\W'
        elif term == "Twilio":
            pattern = r'Twilio\W[^S]'
        elif term == "Visual Studio":
            pattern = r'Visual Studio\W[^C]'
        else:
            pattern = r'' + re.escape(term)
        match = 0
        text_posts_list = text_content.split('__New Job__')
        for post in text_posts_list:
            match_list = re.findall(pattern, post, re.IGNORECASE)
            if len(match_list) > 0:
                match += 1
        data_list.append((term, match))
    return data_list



def write_data(read, terms, write):
    data_list = get_terms(read, terms)
    header = ["Term", "Frequency"]
    with open(write, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data_list)


if __name__ == '__main__':
    write_data('./datasets/sf_300jobs_raw.txt', 'datasets/tech_list.txt', './datasets/new_sf_300_jobs.csv')
