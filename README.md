# IMDB-Scraper

### Steps:
  - make sure python3 is installed (preferably Python 3.12.2)
  - git clone the repo
  - `cd to/the/directory`
  - run `pip install -r requirements.txt`
  - run `python main.py`
  - Search anything you want to search on IMDB website
  - You will see the movies that the program is scraping
  - choose csv or json
  - open the desired file at (your_search_term)_movies.(desired_file_type)

Side Note:
  - Logging and error handling is added.
  - Unit tests for scraper functions are added.
    - run `python -m unittest test_scraper.py`
  - Added multi-threading.
  - User can search anything they want.
