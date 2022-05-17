from types import NoneType
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


def scraper(job_title, location, age):
    start = 0
    scraped_jobs = 0
    scrapes = 300

    while scraped_jobs < scrapes:

        get_vars = {'q': job_title, 'l': location, 'fromage': age, 'start': start}
        url = 'https://www.indeed.com/jobs?' + urllib.parse.urlencode(get_vars)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        jobsearch_results = soup.find(class_='jobsearch-ResultsList')

        for list_elem in jobsearch_results:
            a_tag = list_elem.find('a')
            if a_tag:
                scraped_jobs += 1
                attribute = a_tag.get('data-jk')
                print(attribute)

                job_url = 'https://www.indeed.com/viewjob?jk=' + str(attribute)

                page = requests.get(job_url)
                post_soup = BeautifulSoup(page.content, 'html.parser')

                description = post_soup.find(class_='jobsearch-jobDescriptionText')
                description = description.text
                with open('jobs_raw.txt', 'a+') as f:
                    f.write(description)
        start += 10
    print(scraped_jobs)

    return


scraper('software engineer', 'remote', '3')
