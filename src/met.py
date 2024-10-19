from typing import List
import sys
import requests

from models.artwork import MuseumArtwork


TIMEOUT = 3000
SEARCH_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search"
DETAILS_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"


def search_for_artwork(query: str) -> List[int]:
    """Queries the MET API for artwork matching a value"""
    try:
        # make search GET request
        search_response = requests.get(
            url=SEARCH_URL, params={"q": query}, timeout=TIMEOUT
        )

        # deserialize search response
        search_response_data = search_response.json()

        # grab all object ids
        object_ids = search_response_data["objectIDs"]

        # return object ids
        return object_ids
    except requests.RequestException as e:
        print("Error while searching for artwork: ", e)

        sys.exit(1)


def get_artwork(object_id: int) -> MuseumArtwork:
    """Queries the MET API for a specific object"""
    try:
        # make detail GET request
        details_response = requests.get(
            url=f"{DETAILS_URL}/{object_id}", timeout=TIMEOUT
        )

        # deserialize details response
        details_response_data = details_response.json()

        # return data
        return MuseumArtwork(**details_response_data)
    except requests.RequestException as e:
        print("Error while getting artwork from the MET API: ", e)

        sys.exit(1)


def get_image_bytes(url: str) -> bytes:
    """Gets an image from a specified url"""
    try:
        # download image
        response = requests.get(url=url, timeout=TIMEOUT)

        return response.content
    except requests.RequestException as e:
        print("Error while downloading artwork: ", e)

        sys.exit(1)
