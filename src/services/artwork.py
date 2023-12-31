import os
from typing import TypedDict, List
from typing_extensions import Self
from utils.print import color, Color


class Artist(TypedDict):
    name: str


class Tag(TypedDict):
    term: str


# Heads up: this class uses camelCase in order to match the response returned by the MET APi
class Artwork(TypedDict):
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


class ArtworkService:
    def __init__(self) -> None:
        pass

    def report(self: Self, artwork: Artwork):
        os.system("")

        primary_artist = artwork.get("constituents")[0]
        artist_name = primary_artist.get("name")
        department = artwork.get("department")
        title = artwork.get("title")
        object_date = artwork.get("objectDate")

        print(
            f'"{color(title, Color.CYAN)}" by {color(artist_name, Color.GREEN)} ({object_date}, {department} department)'
        )

        pass
