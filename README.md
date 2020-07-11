# The Last of Us data scraper (technically can do other pages too)

Requirements: `python2`, `pandas` (and it's dependencies), `BeautifulSoup` (and it's dependecies), `requests` (and it's dependencies)

Simply run `python2 scrape.py` and wait until it finishes.
Then run `python2 process.py`

Scripts scrap all reviews in random page order (in case metacritic denies you) to get most fair data. 
You can specify number of rows to process by changing `READ_N_ROWS`, if `None` it will process all. 
