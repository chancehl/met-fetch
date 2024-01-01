import os
import requests
import random

from typing import Optional
from typing_extensions import Self


def get_artwork(self: Self, query: Optional[str], choose_random: bool) -> dict:
    SEARCH_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    DETAILS_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

    # make search GET request
    search_response = requests.get(url=SEARCH_URL, params={"q": query})

    # deserialize search response
    search_response_data = search_response.json()

    # grab all object ids
    object_ids = search_response_data["objectIDs"]

    # if random, grab a random object id from the first 20 else take first
    object_id = random.choice(object_ids[0:20]) if choose_random else object_ids[0]

    # make detail GET request
    details_response = requests.get(url=f"{DETAILS_URL}/{object_id}")

    # deserialize details response
    details_response_data = details_response.json()

    return details_response_data


def download_artwork(self: Self, id: int, image_url: str, location: str):
    # download image
    response = requests.get(image_url)

    # check if outdir exists, if not create it
    if not os.path.exists(location):
        os.mkdir(location)

    # create file
    f = open(os.path.join(location, f"{id}.png"), "wb")

    # write to file
    f.write(response.content)

    # close file
    f.close()
