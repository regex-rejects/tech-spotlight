from tech_spotlight.scraper import scraper


def test_scraper_exists():
    assert scraper


def test_valid_url():
    actual = scraper('software engineer', 'remote', '3')
    expected = "https://www.indeed.com/jobs?q=software+engineer&l=remote&fromage=3&start=0"
    assert actual == expected


def test_job_soup():
    pass


def test_soup_kitchen():
    pass