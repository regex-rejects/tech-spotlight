import requests
import urllib
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
import random
import sys
from tech_term_search import write_data


"""
Global
TODO: refactor with OOP structure
TODO: typehint menthods/function
TODO: add inline comments for vauge code or refactor for readability
TODO: impliment pre-commit / commitizen. 
TODO: rename function/methods for readability
"""


def soup_kitchen(job_title, location, age, start):
    """
    Function receives args and formats URL query for each cycle through scraper.
    :param job_title: string
    :param location: string
    :param age: int
    :param start: int default 0, increments by 10 each iteration of scraper function
    :return: complete formatted url
    """
    get_vars = {'q': job_title, 'l': location, 'fromage': age, 'start': start}
    url = 'https://www.indeed.com/jobs?' + urllib.parse.urlencode(get_vars)
    print("your search URL: " + url)
    soup = job_soup(url)
    results = soup.find(class_='jobsearch-ResultsList')
    return results


def job_soup(job_url):
    """
    uses requests to get page data to process with beautiful soup.
    sleeps application for a random time between 0.1 and 1 second.
    returns parsed instance of BS4 class element tag.
    :param job_url: completed URL with
    :return: BS4 object
    """
    page = requests.get(job_url)
    post_soup = BeautifulSoup(page.content, 'html.parser')
    time.sleep(random.random())
    return post_soup


def sleepy_pill():
    """
    gets a random sleep time, between 240 and 360 seconds, prints a sleep message to terminal.
    :return: None
    """
    sleep_time = random.randint(240, 360)
    print(f"nap for {sleep_time} this many zzzz's (seconds)")
    time.sleep(sleep_time)
    return


def get_input():
    """
    Function called during scrape execution, this forces a pause to get user input, Helping to avoid rate limit.
    Asks if user wants to continue or stop the scrape.
    :return: None
    """
    print(">> Consider swapping IP address with a VPN to avoid rate limit. <<")
    input_ = input(">> 'c' to continue your scrape, 'q' to quit here <<")
    input_ = input_.lower()
    print(input_)
    if input_ == 'c':
        print('>> Continuing scrape <<')
        return
    elif input_ == 'q':
        print(">> are you sure you want to stop the scrape? <<")
        confirm = input(">> 'quit' to quit scraping, 'c' to continue << ")
        print(confirm)
        confirm = confirm.lower()
        if confirm == 'c':
            print('>> Continuing scrape <<')
            return
        elif confirm == 'quit':
            sys.exit()
        else:
            print(">> unexpected input received <<")
            get_input()
    else:
        print(">> unexpected input received <<")
        get_input()


def nonetype_received(scrapes, scraped_jobs):
    """
    returns a message informing the user about the failed scrape, includes information about the scrape,
    exits the script.
    :param scrapes: the attempted total jobs to scrape: int
    :param scraped_jobs: the num of jobs successfully scraped: Int
    :return: None
    """
    print(f"""
        >>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<
        >>> Nonetype received, you likely hit a captcha <<<
        >>> or ran out of job posts for a given search, <<<
        >>> unfortunately scraper cannot recover from   <<<
        >>> this. You will need to start over. Try,     <<<
        >>> using a vpn, to swap your IP address mid    <<<
        >>> scrape.                                     <<<
            We successfully scraped {scraped_jobs}      
            out of the attempted {scrapes} total.       
        >>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<
    """)
    sys.exit()


def main():
    """
    prompts user for search params and calls scraper.
    :return: N/A Calls scraper
    """
    age_inputs = ['1', '3', '5', '7']
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<
        >>>>>>>>>>> Welcome to the Tech Spotlight <<<<<<<<<<
        >>> This tool, scrapes indeed for a given search <<<
        >>> query, returning both a raw text file, and   <<<
        >>> a processed .CSV file, containing the number <<<
        >>> of times a given term appears in the raw     <<<
        >>> text.                                        <<<
        >>>                                              <<<
        >>> If you would like to see the technologies we <<<
        >>> are counting, the list is under /datasets as <<<
        >>> tech_list.txt                                <<<
        >>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<
    """)
    job_tile = input("""
    > Please enter a development job title to search for, 
    i.e. 'software developer', 'software engineer',
    'dev ops engineer' etc. 
    > """)
    location = input("""
    > Please enter a location to search, i.e. 'remote',
    'seattle', 'chicago' etc. 
    > """)
    age = input("""
    > Please enter a job post age to scrape, accepted inputs 
    are as follows: 
    '1' for postings within the last 24 hours
    '3' for postings within the last 3 days
    '5' for postings within the last 5 days
    '7' for postings within the last 7 days
    > """)
    while age not in age_inputs:
        print('>>> Invalid post age received <<<')
        age = input("""
        > Please enter a job post age to scrape, accepted inputs 
        are as follows: 
        '1' for postings within the last 24 hours
        '3' for postings within the last 3 days
        '5' for postings within the last 5 days
        '7' for postings within the last 7 days
        > """)
    scrapes = input("""
    > Please enter a number of jobs to scrape,
    this determines the size of the dataset,
    keep in mind the larger the dataset the longer
    the scrape will take. 
        
    example: a scrape of 900 jobs will take 
    over an hour in most cases, and runs the risk
    of being stopped by indeed. Consider using a
    VPN if scraping more than 300 jobs.
    ---> The scraper will pause for a number of 
    minutes every 100 jobs. <---
    
    Please enter a number of jobs to scrape > """)
    filename = input("""
    > Please enter output filename, raw file
    will be a .txt file
    !! You do not need to add the .txt extension !!
    example input: dev_ops_Seattle_300_jobs
    example output: dev_ops_Seattle_300_jobs.txt
    > """)

    print(f"""
    Beginning scrape of Indeed.com for the following query
    job tile: {job_tile}
    location: {location}
    age: {age}
    scrapes: {scrapes}
    filename: {filename}
    After scraper is done the raw txt file will
    be processed into a csv file. 
    
    Your raw text file will be called: {filename}.txt
    Your processed csv file will be called: {filename}_terms.csv
    
    Your scrape will begin shortly...
    """)
    time.sleep(2)
    scraper(job_tile, location, age, int(scrapes), filename)
    raw_file_path = f"{filename}.txt"
    csv_file_path = f"{filename}_terms.csv"
    write_data(f'/Users/bencarter/projects/Code401/tech-spotlight/tech_spotlight/{raw_file_path}', '/Users/bencarter/projects/Code401/tech-spotlight/datasets/tech_list.txt', csv_file_path)
    print(f"""
    Tech Spotlight has finished the scrape and 
    processed the raw data into a csv file.
    The csv file name is : {filename}_terms.csv
    We encourage you to fork this notebook and
    import your new dataset to visualize your data.
    https://www.kaggle.com/code/edenbrekke/tech-spotlight-indeed-web-scraper-template/notebook     
    """)

    
def scraper(job_title, location, age, scrapes, filename):
    """
    Main application function, calls all other functions to perform the requested job scrape.
    :param job_title: string
    :param location: string
    :param age: string
    :param scrapes: int
    :param filename: string
    :return: raw text file
    """
    start = 0
    scrapes = scrapes
    scraped_jobs = 0
    job_id_set = set()
    break_time = 0
    while scraped_jobs < int(scrapes):
        results = soup_kitchen(job_title, location, age, start)

        if results is None:
            nonetype_received(scrapes, scraped_jobs)

        for element in results:
            a_tag = element.find('a')

            if break_time == 100:
                break_time = 0
                sleepy_pill()

            if scraped_jobs == 350 or scraped_jobs == 700:
                get_input()

            if a_tag:
                job_id = a_tag.get("data-jk")
                if job_id in job_id_set:
                    continue

                else:
                    job_id_set.add(job_id)
                    scraped_jobs = len(job_id_set)
                    break_time += 1

                    description = job_id_to_description(job_id)
                    file = str(filename) + '.txt'
                    with open(file, 'a+', encoding='utf-8') as f:
                        f.write(description)
                        f.write('\n \n _________________________________New Job______________________________ \n \n ')
                    print(str(job_id) + " Num scraped: " + str(scraped_jobs))
                    if scraped_jobs == scrapes:
                        return print('scrape finished')
        start += 10


def job_id_to_description(job_id):
    job_url = 'https://www.indeed.com/viewjob?jk=' + str(job_id)
    post_soup = job_soup(job_url)
    description = post_soup.find(class_='jobsearch-jobDescriptionText')
    return description.text


if __name__ == '__main__':
    main()
