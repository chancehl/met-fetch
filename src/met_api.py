import os
from pathlib import Path
import re
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


def download_artwork(artwork: MuseumArtwork, location: str):
    """Downloads artwork to disk"""
    try:
        # throw if we don't have an image to download
        if artwork.primaryImage is None:
            raise TypeError(f"artwork ${artwork.objectID} is missing primary image")

        # download image
        response = requests.get(url=artwork.primaryImage, timeout=TIMEOUT)

        # check if outdir exists, if not create it
        path = Path(location)

        if not path.exists():
            path.mkdir(parents=True)

        name = generate_pretty_filename(artwork)

        # create file
        with open(os.path.join(location, f"{name}.png"), "wb") as f:
            # write to file
            f.write(response.content)
    except requests.RequestException as e:
        print("Error while downloading artwork: ", e)

        sys.exit(1)


def generate_pretty_filename(artwork: MuseumArtwork) -> str:
    # Ensure required field objectID exists
    object_id = str(artwork.objectID)

    # Get the title and artistDisplayName from the dictionary
    title = artwork.title
    artist_display_name = artwork.artistDisplayName

    # Combine title and artist if both exist, otherwise fallback to just title or artist
    if title and artist_display_name:
        base_name = f"{artist_display_name}-{title}"
    elif title:
        base_name = title
    elif artist_display_name:
        base_name = artist_display_name
    else:
        base_name = object_id  # Fallback to just the objectID if no title or artist

    # Clean the base name to only include alphanumeric characters and underscores
    base_name = re.sub(r"[^a-zA-Z0-9]+", "_", base_name.strip())

    # Enforce a reasonable length limit (e.g., 50 characters), include objectID at the end
    if len(base_name) > 45:
        base_name = base_name[:45].rstrip(
            "_"
        )  # Truncate and remove trailing underscores

    # Append the objectID to ensure uniqueness
    pretty_filename = f"{base_name}_{object_id}"

    return pretty_filename.lower()
