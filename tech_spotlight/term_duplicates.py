

def open_term_file():
    with open('./datasets/tech_list.txt', 'rt') as l:  # BRING IN TERMS
        list_content = l.readlines()
        tech_terms = []
        for line in list_content:
            line_stripped = line.strip('\n')
            tech_terms.append(line_stripped)
    
    for term in tech_terms:
        count = 0
        match_list = []
        for other in tech_terms:
            if term in other and other != term:
                count += 1
                match_list.append(other)
        if count > 0:
            print(term, count, match_list)


open_term_file()

"""
('GitHub', 1, ['GitHub Pages'])
('Git', 3, ['GitHub', 'GitLab', 'GitHub Pages'])
('Docker', 1, ['Docker Compose'])
('React', 1, ['React Native'])
('jQuery', 1, ['jQuery UI'])
('Java', 1, ['JavaScript'])
('Amazon EC2', 1, ['Amazon EC2 Container Service'])
('Visual Studio', 1, ['Visual Studio Code'])
('Twilio', 1, ['Twilio SendGrid'])
"""
