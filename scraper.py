import requests
from bs4 import BeautifulSoup
import re
from constants import *
import logging

# Configure logging
logging.basicConfig(filename='scraping.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_imdb_movies(genre):
    try:
        search_url = f'https://www.imdb.com/find/?q={genre}'
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        movie_containers = soup.find_all("a", class_=MOVIE_CLASS)

        movies = []

        for container in movie_containers:
            href = container["href"]
            if "title" in href:
        
                # Construct movie details URL using the IMDb ID
                movie_details_url = f'https://www.imdb.com/{href}'
                
                # Scrape movie details page for rating, director, cast, and plot summary
                movie_details = scrape_movie_details(movie_details_url)
                
                movies.append(movie_details)
        
        return movies

    except Exception as e:
        logging.error(f"Error occurred while scraping IMDb movies: {str(e)}")
        return []

def scrape_movie_details(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        title_year = soup.find("title").get_text()
        title = title_year.split("(")[0][:-1]
        logging.info("Fetching Details of: %s", title)
        print(title)
        if '(' in title_year:
            year = re.findall(r'\(.*?\)', title_year)[0]
            
        rating_val = soup.find("span" , class_=RATING_CLASS)
        rating = None
        if rating_val:
            rating = rating_val.get_text()
        dir_cast_elements = soup.find_all("a", class_=DIR_CAST_CLASS)
        directors =dir_cast_elements[0].get_text()
        cast_list = [dir_cast_elements[i].get_text() for i in range(len(dir_cast_elements)) if i in range(2,7) ]
        cast = ''.join(" "+i for i in cast_list)
        plot_summary = soup.find("span" , class_=SUMMARY_CLASS).get_text()
        

        return {
                'Title': title if title else 'N/A',
                'Year': year if year else 'N/A',
                'Rating': rating if rating else 'N/A',
                'Directors': directors if directors else 'N/A',
                'Cast': cast if cast else 'N/A',
                'Plot Summary': plot_summary if plot_summary else 'N/A',
               }
    except Exception as e:
        logging.error("An error occurred while scraping movie details from %s: %s", url, e)
        return {
            'Title': 'N/A',
            'Year': 'N/A',
            'Rating': 'N/A',
            'Directors': 'N/A',
            'Cast': 'N/A',
            'Plot Summary': 'N/A'
        }