import re
import csv

"""
Global 
TODO: refactor with OOP structure.
TODO: Type hint the methods/function.
TODO: add line comments where code is vauge.
TODO: work in commitizen and pre-commits.
"""


def open_text(read_file):
    """
    Function opens and reads the text file of job description
    content from Indeed.com
    :param read_file: job description text file
    :return: content of text file as a string
    """
    with open(read_file, 'rt') as f:
        text_content = f.read()
    return text_content


def open_terms(terms_file):
    """
    Function opens text file containing the list of common
    tech terms, reading each line and stripping the terms
    into a list
    :param terms_file: text file of terms
    :return: list containing strings of each term
    """
    with open(terms_file, 'rt') as f:
        list_content = f.readlines()
        tech_terms = []
        for line in list_content:
            line_stripped = line.strip('\n')
            tech_terms.append(line_stripped)
    return tech_terms


# TODO: refactor this for loop, perhaps map over the patterns rather than the if else statements.
def get_terms(read_file, terms_file):
    """
    Function calls open_text() and open_terms() functions
    to search the job description text content for each
    tech term string to count the number of posts that
    mention each terms
    :param read_file: job description text file
    :param terms_file: text file of terms
    :return: list containing each term and the
    corresponding number of posts mentioning it
    """
    text_content = open_text(read_file)
    term_list = open_terms(terms_file)
    data_list = []
    for term in term_list:
        if term == "Amazon EC2":
            pattern = r'Amazon EC2\W[^C]'
        elif term == "Angular":
            pattern = r'\WAngular\D[^jsJS]'
        elif term == "Apache Tomcat":
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
    """
    Function calls get_terms() function to get
    list of term occurrence frequency, then opens
    and writes data to a comma-separated values (CSV)
    file with appropriate labels
    :param read: job description text file
    :param terms: text file of terms
    :param write: csv file to which data list is written
    :return: none
    """
    data_list = get_terms(read, terms)
    header = ["Term", "Frequency"]
    with open(write, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data_list)


if __name__ == '__main__':
    write_data('./datasets/sf_300jobs_raw.txt', 'datasets/tech_list.txt', './datasets/new_sf_300_jobs.csv')
