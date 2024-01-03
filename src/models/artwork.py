"""artwork.py"""
from typing import TypedDict, List
from utils.print import CYAN, GREEN, color


class Artist(TypedDict):
    """Represents the constituents object within the MET API payload"""

    name: str


class Tag(TypedDict):
    """Repesents the tag object within the MET API payload"""

    term: str


# Heads up: this class uses camelCase in order to match the response returned by the MET APi
class MuseumArtwork(TypedDict):
    """Represents the museum artwork object within the MET API payload"""

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
    """Gets an artists name based on the MET API response"""
    artists = artwork.get("constituents")

    return artists[0].get("name") if artists is not None else "Unknown artist"


def print_artwork(artwork: MuseumArtwork):
    """Pretty prints a MET artwork object"""
    artist_name = get_artist_name(artwork=artwork)
    department = artwork.get("department")
    title = artwork.get("title")
    object_date = artwork.get("objectDate")

    print(
        # pylint: disable-next=line-too-long
        f'"{color(title, CYAN)}" by {color(artist_name, GREEN)} ({object_date}, {department} department)'
    )
