import requests
import logging

logger = logging.getLogger(__name__)

def fetch_data(url):
    """Fetch data from a given URL and return the JSON response."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError on bad status
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from {url}: {e}")
        return None
