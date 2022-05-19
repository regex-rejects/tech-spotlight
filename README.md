# Tech Spotlight

## Project Description

Welcome to Tech Spotlight. The goal of this project is to search through relevant job postings and find the frequency of technologies associated with those jobs.

This is achieved in two parts: a scraper that scrapes data off Indeed.com with three queries, location, age of posting and number of postings and a Kaggle notebook that tells the story about what technologies, frameworks and libraries were found and how frequently they were posted.

## Project Authors

**Team Beacon**

- Benjamin Carter
- Eden Brekke
- Nicholas Mercado
- Christopher Yamas

## How to install/Use

### Scraper

```py

    git clone https://github.com/regex-rejects/tech-spotlight.git

    Create visual python environment (venv)

        example: 
            python3 -m venv .venv

    activate virtual environment

        example:
            source .venv/bin/activate

    pip install -r requirements

    Run web scraper:
    
         python tech_spotlight/scraper.py

```

### Kaggle Notebook

[link to Kaggle]("https://www.kaggle.com/code/edenbrekke/indeed-past-7-day-900-listing-term-data-18may2022")

Upload output csv file to new notebook and use above code as reference

## Version

Version 1.0

## Technologies Used

Kaggle

### libraries

- numpy
- pandas
- seaborn
- matplotlib
- requests
- urllib
- bs4
- time
- random
- sys
- csv

## Acknowledgments

- JB Tellez
- David Hecker
- Adam Owada
- Aaron Imbrock
- Joseph Streifel
- Aaron Imbrock
- Chloe Nott

## Known issues
