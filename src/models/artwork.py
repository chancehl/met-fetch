"""artwork.py"""

from typing import TypedDict, List
from utils.print import CYAN, GREEN, color


class Artist(TypedDict):
    name: str


class Tag(TypedDict):
    term: str


# Heads up: this class uses camelCase in order to match the response returned by the MET APi
class MuseumArtwork(TypedDict):
    objectID: int
    primaryImage: str
    constituents: List[Artist]
    department: str
    title: str
    artistBeginDate: str
    artistEndDate: str
    objectDate: str
    medium: str
    dimensions: str
    tags: List[Tag]


def get_artist_name(artwork: MuseumArtwork) -> str:
    artists = artwork.get("constituents")

    return artists[0].get("name") if artists is not None else "Unknown artist"


def format_artwork_name(artwork: MuseumArtwork):
    artist_name = get_artist_name(artwork)
    department = artwork.get("department")
    title = artwork.get("title")
    object_date = artwork.get("objectDate")

    return f'"{color(title, CYAN)}" by {color(artist_name, GREEN)} ({object_date}, {department} department)'


def is_valid_artwork(artwork, processed: List[MuseumArtwork]) -> bool:
    artwork_id = artwork["objectID"]
    image_url = artwork["primaryImage"]

    if (
        image_url is not None
        and len(image_url) > 0
        and not is_already_processed(artwork_id, processed)
    ):
        return True

    return False


def is_already_processed(artwork_id: int, processed: List[MuseumArtwork]) -> bool:
    return any(a.get("objectID") == artwork_id for a in processed)


def print_report(artwork: List[MuseumArtwork], outdir: str) -> None:
    print("Downloaded the following pieces:\n")

    for art in artwork:
        print(f"* {format_artwork_name(art)}")

    print(f"\nSaved artwork to: {outdir}")
