import os
import requests


from random import choice
from typing import Optional

FUZZY_SEARCH_THRESHOLD = 20

SEARCH_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search"
DETAILS_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"


def get_artwork(query: Optional[str], random: bool) -> dict:
    try:
        # make search GET request
        search_response = requests.get(url=SEARCH_URL, params={"q": query})

        # deserialize search response
        search_response_data = search_response.json()

        # grab all object ids
        object_ids = search_response_data["objectIDs"]

        # if not random take the first, else take a random one from the first 20
        object_id = (
            object_ids[0]
            if not random
            else choice(object_ids[0:FUZZY_SEARCH_THRESHOLD])
        )

        # make detail GET request
        details_response = requests.get(url=f"{DETAILS_URL}/{object_id}")

        # deserialize details response
        details_response_data = details_response.json()

        return details_response_data
    except Exception as e:
        print("Error while getting artwork from the MET API: ", e)

        exit(1)


def download_artwork(id: int, image_url: str, location: str):
    try:
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
    except Exception as e:
        print("Error while downloading artwork: ", e)

        exit(1)
