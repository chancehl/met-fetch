"""met.py"""
import os
from pathlib import Path
from typing import List
import requests


TIMEOUT = 3000
SEARCH_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search"
DETAILS_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"


def search_artwork(query: str) -> List[int]:
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

        exit(1)


def get_artwork(object_id: int) -> dict:
    """Queries the MET API for a specific object"""
    try:
        # make detail GET request
        details_response = requests.get(
            url=f"{DETAILS_URL}/{object_id}", timeout=TIMEOUT
        )

        # deserialize details response
        details_response_data = details_response.json()

        # return data
        return details_response_data
    except requests.RequestException as e:
        print("Error while getting artwork from the MET API: ", e)

        exit(1)


def download_artwork(object_id: int, image_url: str, location: str):
    """Downloads artwork to disk"""
    try:
        # download image
        response = requests.get(url=image_url, timeout=TIMEOUT)

        # check if outdir exists, if not create it
        path = Path(location)

        if not path.exists():
            path.mkdir(parents=True)

        # create file
        f = open(os.path.join(location, f"{object_id}.png"), "wb")

        # write to file
        f.write(response.content)

        # close file
        f.close()
    except requests.RequestException as e:
        print("Error while downloading artwork: ", e)

        exit(1)
