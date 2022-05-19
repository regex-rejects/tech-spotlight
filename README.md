# Tech Spotlight

## Project Description

Welcome to Tech Spotlight. The goal of this project is to search through relevant job postings and find the frequency of technologies associated with those jobs.

This is achieved in two parts: a scraper that scrapes data off Indeed.com with four queries, job title, location, age of posting, and a number of jobs to scrape, and a Kaggle notebook that tells the story about what technologies, frameworks, and libraries were found and how frequently they were posted.

## Project Authors

**Team Spotlight**

- Benjamin Carter: [GitHub](https://github.com/MotoBenny) and [LinkedIn](https://www.linkedin.com/in/benjamin-carter-dev/)

- Nicholas Mercado: [GitHub](https://github.com/Nicholas-Mercado) and [LinkedIn](https://www.linkedin.com/in/nicholasmercado/)

- Christopher Yamas: [GitHub](https://github.com/chrisyamas)  and [LinkedIn](https://www.linkedin.com/in/chrisyamas/)

- Eden Brekke: [GitHub](https://github.com/eden-brekke) and [LinkedIn](https://www.linkedin.com/in/eden-brekke/)

## How to install/Use

### Scraper

```py

    git clone https://github.com/regex-rejects/tech-spotlight.git

    Create visual python environment (venv)

        example:
            python3 -m venv .venv (mac/wsl)
            py -m venv .venv (windows native)

    activate virtual environment
        example:
            source .venv/bin/activate (mac/wsl)
            .\.venv\Scripts\activate (windows native)

    pip install -r requirements.txt

    Run web scraper:
         python tech_spotlight/scraper.py

```

### Kaggle Notebook

[Indeed Past 7 Day 900 Listing Term Data 18 May 2022]("https://www.kaggle.com/code/edenbrekke/indeed-past-7-day-900-listing-term-data-18may2022")

Upload output csv file to new notebook and use above code as reference

## Version

Version 1.0

## Technologies Used

[Kaggle](https://www.kaggle.com/)

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

