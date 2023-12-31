import requests
import random
from typing import Optional
from typing_extensions import Self


class WallpaperService:
    def __init__(self) -> None:
        pass

    def get_wallpaper(
        self: Self, query: Optional[str], choose_random: bool
    ) -> Optional[str]:
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

        # grab url and return
        image_url = details_response_data.get("primaryImage")

        return image_url

    def download_wallpaper(self: Self, image_url: str, location: str):
        # download image
        response = requests.get(image_url)

        # create file
        f = open(location, "wb")

        # write to file
        f.write(response.content)

        # close file
        f.close()

    def set_wallpaper(self: Self, image_url: str):
        print(image_url)
