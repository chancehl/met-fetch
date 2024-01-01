from typing import TypedDict, List
from utils.print import Color, color


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


def print_artwork(artwork: MuseumArtwork):
    artist_name = get_artist_name(artwork=artwork)
    department = artwork.get("department")
    title = artwork.get("title")
    object_date = artwork.get("objectDate")

    print(
        f'"{color(title, Color.CYAN)}" by {color(artist_name, Color.GREEN)} ({object_date}, {department} department)'
    )
