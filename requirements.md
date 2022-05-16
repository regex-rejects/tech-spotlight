# Software Requirements

## Vision

This product provides users with relevant and up-to-date job search data, in particular for software engineering roles with remote location. The user interface is either a Kaggle dataset/notebook, a Command Line Interface (CLI), or both. The data is extracted via web-scraping from Indeed.

This application helps users who are currently making decisions relevant to their job search. It does the work for them, so they do not need to comb through a variety of different job listings on Indeed to get the context they need to understand what roles are out there, what salary ranges are accessible, and even what programming languages seem to be garnering the highest salaries in the current software climate.

## Scope

* What our product does:
  * Collects the most relevant tech terms from Stackshare.io
  * Uses those terms as basis for creating search criteria for scraping of Indeed job data
  * Parses scraped job data and assembles into presentable and useful format within a data set
  * Present data set and analysis of data in Kaggle notebook
  * Potentially created CLI for users to access relevant information about the data set

* What our product will not do:
  * Have a frontend user interface outside of command-line or Kaggle (i.e. a deployed frontend site to query or display data)

### MVP

* Minimum Viable Product:
  * Occurrences of tech terms for a given search (for our dataset)
    * queries include: job_title (Software Engineer), location (Remote), from_age: 3 days (since posting, but also cap at first 300 job posts, to start)

### Stretch

* Stretch Goals:
  * get salary data - draw a correlation between salary data and tech terms
  * keep the href for a given search so a user can connect the search data they get back with jobs

## Functional Requirements

1. Data scraped from Indeed using specific criteria
2. Data parsed for only relevant, desired text content
3. Time-efficient data collection and parsing
4. Data set assembled
5. Data analyzed and displayed in user-friendly, accessible format

## Data Flow

Stackshare.io terms data
-> criteria for Indeed scrape
--> Indeed job data
---> Parsed job data
----> Assembled data set
-----> Kaggle and/or CLI

## Non-Functional Requirements (301 & 401 only)

1. Security: ensure web scrapers are designed to not get flagged by a site's robots.txt
2. Usability: Kaggle and/or CLI data is user-friendly, easy to understand, and uniquely edifying
3. Testability: test driven development (TDD) ensures functions and methods are designed properly before full implementation of large-scale scraping or parsing
