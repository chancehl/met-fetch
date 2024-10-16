from typing import List
from dataclasses import dataclass

from decorators.ignore_unknown_properties import ignore_unknown_properties


@ignore_unknown_properties
@dataclass
class Artist:
    constituentID: str
    name: str


@ignore_unknown_properties
@dataclass
class Tag:
    term: str


@ignore_unknown_properties
@dataclass
# Heads up: this class uses camelCase in order to match the response returned by the MET APi
class MuseumArtwork:
    objectID: int
    primaryImage: str
    constituents: List[Artist]
    department: str
    title: str
    artistDisplayName: str
    artistBeginDate: str
    artistEndDate: str
    objectDate: str
    medium: str
    dimensions: str
    tags: List[Tag]
    isHighlight: bool

    # convert all nested subfields to dataclass
    def __post_init__(self):
        if self.constituents is not None and len(self.constituents) > 0:
            self.constituents = [
                Artist(**artist)
                for artist in self.constituents
                if isinstance(artist, dict)
            ]

        if self.tags is not None and len(self.tags) > 0:
            self.tags = [Tag(**tag) for tag in self.tags if isinstance(tag, dict)]


CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"


def get_artist_name(artwork: MuseumArtwork) -> str:
    artists = artwork.constituents

    return artists[0].name if artists is not None else "Unknown artist"


def is_valid_artwork(artwork, processed: List[MuseumArtwork]) -> bool:
    if (
        artwork.objectID is not None
        and artwork.primaryImage is not None
        and len(artwork.primaryImage) > 0
        and not is_already_processed(artwork.objectID, processed)
    ):
        return True

    return False


def is_already_processed(artwork_id: int, processed: List[MuseumArtwork]) -> bool:
    return any(a.objectID == artwork_id for a in processed)


def print_report(artwork: List[MuseumArtwork], outdir: str) -> None:
    print("Downloaded the following pieces:\n")

    for art in artwork:
        print(f"* {print_artwork(art)}")

    print(f"\nSaved artwork to: {outdir}")


def print_artwork(artwork: MuseumArtwork):
    artist_name = get_artist_name(artwork)

    return f'"{print_artwork_title(artwork.title)}" by {print_artist_name(artist_name)} ({artwork.objectDate}, {artwork.department} department)'


def print_artwork_title(title: str) -> str:
    return f"{CYAN}{title}{RESET}"


def print_artist_name(name: str) -> str:
    return f"{GREEN}{name}{RESET}"
