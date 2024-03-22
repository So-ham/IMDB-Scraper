from utils import save_to_csv, save_to_json

from scrape import scrape_imdb_movies
import urllib.parse


def main():
    genre = input("Enter the genre to search for (e.g., comedy, action): ")
    movies = scrape_imdb_movies(genre)
    save_format = input("Enter the format to save the data (json/csv): ")

    if save_format.lower() == 'json':
        save_to_json(movies, genre +'_movies.json')
        print("Data saved to movies.json")
    elif save_format.lower() == 'csv':
        save_to_csv(movies, genre +'_movies.csv')
        print("Data saved to movies.csv")
    else:
        print("Invalid save format. Please enter 'json' or 'csv'.")

if __name__ == '__main__':
    main()
    
