import unittest
from unittest.mock import patch
from scraper import scrape_imdb_movies, scrape_movie_details

class TestIMDBScraper(unittest.TestCase):
    @patch('scraper.requests.get')
    def test_scrape_imdb_movies(self, mock_get):
        # Mock the genre search response
        search_html_content = '''
        <html>
        <body>
        <a href="/title/tt123456/" class="ipc-metadata-list-summary-item__t">Movie Title</a>
        </body>
        </html>
        '''
        # Configure mock for the search response
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = search_html_content.encode('utf-8')

        # Call the function
        movies = scrape_imdb_movies('comedy')

        # Check if the function returns a list containing a dictionary with expected movie details
        self.assertIsInstance(movies, list)
        self.assertGreater(len(movies), 0)  # Ensuring at least one movie is found
        self.assertIn('Title', movies[0])

    @patch('scraper.requests.get')
    def test_scrape_movie_details(self, mock_get):
        # Mock HTML response for a specific movie details page
        details_html_content = '''
        <html>
        <head><title>Test Movie (2021)</title></head>
        <body>
        <span class="sc-bde20123-1 cMEQkK">8.5</span>
        <a class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link">Director Name</a>
        <span class="sc-466bb6c-0 hlbAws">A brief plot summary.</span>
        </body>
        </html>
        '''
        # Configure mock for the movie details response
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = details_html_content.encode('utf-8')

        # Call the function
        movie_details = scrape_movie_details("https://fakeurl.com/movie_details")

        # Validate expected keys and values
        self.assertEqual(movie_details['Title'], 'Test Movie')
        self.assertEqual(movie_details['Year'], '(2021)')
        self.assertEqual(movie_details['Rating'], '8.5')
        self.assertEqual(movie_details['Directors'], 'Director Name')
        self.assertEqual(movie_details['Plot Summary'], 'A brief plot summary.')

if __name__ == '__main__':
    unittest.main()
