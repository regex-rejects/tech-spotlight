import requests
import urllib
from urllib.parse import urlparse
from bs4 import BeautifulSoup

"""
Scrape indeed.com for the job title software engineer

Example URL https://www.indeed.com/jobs?q=Software%20Engineer&l=remote&fromage=3&start=10&vjk=433b6a457d0b609e
Query = the job title to search
L = the location in put "remote" - "Seattle" etc.
fromage = the age of the posts, we will start with 3
start = we can increment this by 10 for each itteration to get new job posts each time.

We may also need to handle some job cards that are adds for indeed. (these can show up among the job posts)

within the job posts we want to scrape into id="jobDescriptionText"

find a way to itterate through the cards on indeed
for each card grab its id="jobDescriptionText" 
thats the document we are saving to later search for terms.




"""
# Done: build and test URL
# Done: select each job card
# TODO: scrape one full job post via description
# TODO:


def scraper(job_title, location, age):
    start = 0  # we will want to increment this by 10 for each loop through

    get_vars = {'q': job_title, 'l': location, 'fromage': age, 'start': start}
    url = 'https://www.indeed.com/jobs?' + urllib.parse.urlencode(get_vars)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    jobs_soup = soup.find(class_='jobsearch-ResultsList') # gets all job cards from within the page for a given search

    # split jobs_soup at the li to get the individual job postings.



    return print(jobs_soup)


scraper('software engineer', 'remote', '3')

"""

def get_user_input():
    pass


def format_url(job_title, location, age):
    get_vars = {'q' : job_title, 'l' : location, 'fromage' : age}
    url = 'https://www.indeed.com/jobs?' + urllib.parse.urlencode(get_vars)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    jobs_soup = soup.find(id="resultsCol")
    return soup


def get_raw_html():
    pass


test = format_url('software engineer', 'remote', 3)

print(test)


"""