from typing import TypedDict, List, Optional


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
