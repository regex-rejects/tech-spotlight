import requests
import urllib
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
import random
import sys

"""
Scrape indeed.com for the job title software engineer

Example URL https://www.indeed.com/jobs?q=Software%20Engineer&l=remote&fromage=3&start=10&vjk=433b6a457d0b609e
Query = the job title to search
L = the location in put "remote" - "Seattle" etc.
fromage = the age of the posts, we will start with 3
start = we can increment this by 10 for each iteration to get new job posts each time.

We may also need to handle some job cards that are adds for indeed. (these can show up among the job posts)

within the job posts we want to scrape into id="jobDescriptionText"

find a way to iterate through the cards on indeed
for each card grab its id="jobDescriptionText" 
that's the document we are saving to later search for terms.
"""


def soup_kitchen(job_title, location, age, start):
    """

    :param job_title:
    :param location:
    :param age:
    :param start:
    :return:
    """
    get_vars = {'q': job_title, 'l': location, 'fromage': age, 'start': start}
    url = 'https://www.indeed.com/jobs?' + urllib.parse.urlencode(get_vars)
    print("your search URL: " + url)
    soup = job_soup(url)
    results = soup.find(class_='jobsearch-ResultsList')
    return results


def job_soup(job_url):
    """

    :param job_url:
    :return:
    """
    page = requests.get(job_url)
    post_soup = BeautifulSoup(page.content, 'html.parser')
    time.sleep(random.random())
    return post_soup


def sleepy_pill():
    """

    :return:
    """
    sleep_time = random.randint(240, 360)
    print(f'nap for {sleep_time} this many zzzz\'s (seconds)')
    time.sleep(sleep_time)
    return


def get_input():
    """
    Function called during scrape execution, this forces a pause to get user input, Helping to avoid rate limit.
    Asks if user wants to continue or stop the scrape.
    :return:
    """
    print(">> Consider swapping IP address with a VPN to avoid rate limit. <<")
    input_ = input(">> 'c' to continue your scrape, 'q' to quit here <<")
    input_ = input_.lower()
    if input_ == 'c':
        print('>> Continuing scrape <<')
        return
    elif input == 'q':
        print(">> are you sure you want to stop the scrape? <<")
        confirm = input(">> 'quit' to quit scraping, 'c' to continue << ")
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
        >>> unfortunately scraper cannot recover from   <<<
        >>> this. You will need to start over. Try,     <<<
        >>> using a vpn, to swap your IP address mid    <<<
        >>> scrape.                                     <<<
        >>> We successfully scraped {scraped_jobs}      <<<
        >>> out of the attempted {scrapes} total.       <<<
        >>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<
    """)
    sys.exit()



def scraper(job_title, location, age):
    """

    :param job_title:
    :param location:
    :param age:
    :return:
    """
    start = 0
    scrapes = 15
    scraped_jobs = 0
    job_id_set = set()
    break_time = 0
    while scraped_jobs < scrapes:
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

                    # function takes in job_id, appends to end of indeed URL, sends url through job_soup,
                    # creates description and returns description.text
                    # job_url = 'https://www.indeed.com/viewjob?jk=' + str(job_id)
                    #
                    # post_soup = job_soup(job_url)
                    # description = post_soup.find(class_='jobsearch-jobDescriptionText')
                    description = job_id_to_description(job_id)

                    with open('test_scrape.txt', 'a+', encoding='utf-8') as f:
                        f.write(description)
                    print(str(job_id) + " Num scraped: " + str(scraped_jobs))
        start += 10
    return print('scrape finished')


def job_id_to_description(job_id):
    job_url = 'https://www.indeed.com/viewjob?jk=' + str(job_id)
    post_soup = job_soup(job_url)
    description = post_soup.find(class_='jobsearch-jobDescriptionText')
    return description.text

if __name__ == '__main__':
    scraper('software engineer', 'remote', '7')
