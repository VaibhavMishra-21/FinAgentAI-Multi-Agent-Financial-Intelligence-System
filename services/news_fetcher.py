import requests

class NewsFetcher:

    def get_news(self, company):

        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={company}&sortBy=publishedAt&apiKey=YOUR_KEY"
        )

        response = requests.get(url)

        return response.json()
