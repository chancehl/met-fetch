# pylint: disable=invalid-name,too-many-instance-attributes
# matching MET API model format
from typing import List, Literal, Optional
from dataclasses import dataclass

from models.constituent import Constituent
from models.measurements import Measurement
from models.tag import Tag

CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"


@dataclass
class MuseumArtwork:
    objectID: int
    isHighlight: bool
    accessionNumber: str
    accessionYear: str
    isPublicDomain: bool
    primaryImage: Optional[str]
    primaryImageSmall: Optional[str]
    additionalImages: List[str]
    constituents: List[Constituent]
    department: str
    objectName: str
    title: str
    culture: Optional[str]
    period: Optional[str]
    dynasty: Optional[str]
    reign: Optional[str]
    portfolio: Optional[str]
    artistRole: str
    artistPrefix: Optional[str]
    artistDisplayName: str
    artistDisplayBio: str
    artistSuffix: Optional[str]
    artistAlphaSort: str
    artistNationality: Optional[str]
    artistBeginDate: Optional[str]
    artistEndDate: Optional[str]
    artistGender: Optional[str]
    artistWikidata_URL: Optional[str]
    artistULAN_URL: Optional[str]
    objectDate: Optional[str]
    objectBeginDate: int
    objectEndDate: int
    medium: Optional[str]
    dimensions: Optional[str]
    measurements: List[Measurement]
    creditLine: Optional[str]
    geographyType: Optional[str]
    city: Optional[str]
    state: Optional[str]
    county: Optional[str]
    country: Optional[str]
    region: Optional[str]
    subregion: Optional[str]
    locale: Optional[str]
    locus: Optional[str]
    excavation: Optional[str]
    river: Optional[str]
    classification: str
    rightsAndReproduction: Optional[str]
    linkResource: Optional[str]
    metadataDate: str
    repository: str
    objectURL: str
    tags: List[Tag]
    objectWikidata_URL: Optional[str]
    isTimelineWork: bool
    GalleryNumber: Optional[str]

    # convert all nested subfields to dataclass
    def __post_init__(self):
        if self.constituents is not None and len(self.constituents) > 0:
            self.constituents = [
                Constituent(**constituent)
                for constituent in self.constituents
                if isinstance(constituent, dict)
            ]

        if self.tags is not None and len(self.tags) > 0:
            self.tags = [Tag(**tag) for tag in self.tags if isinstance(tag, dict)]


def get_artist_name(artwork: MuseumArtwork) -> str:
    artists = artwork.constituents

    return artists[0].name if artists is not None else "Unknown artist"


def is_valid_artwork(artwork, processed: List[MuseumArtwork]) -> bool:
    return (
        artwork.objectID is not None
        and artwork.primaryImage is not None
        and len(artwork.primaryImage) > 0
        and not is_already_processed(artwork.objectID, processed)
    )


def is_already_processed(artwork_id: int, processed: List[MuseumArtwork]) -> bool:
    return any(artwork.objectID == artwork_id for artwork in processed)


def print_report(artwork: List[MuseumArtwork], outdir: str) -> None:
    print("Downloaded the following pieces:\n")

    for art in artwork:
        print(f"* {format_artwork_data(art)}")

    print(f"\nSaved artwork to: {outdir}")


def format_artwork_data(artwork: MuseumArtwork):
    artist_name = get_artist_name(artwork)

    return f'"{format_with_color(artwork.title, CYAN)}" by {format_with_color(artist_name, GREEN)} ({artwork.objectDate}, {artwork.department} department)'


def format_with_color(s: str, color: Literal["\u001b[32m", "\u001b[36m"]) -> str:
    return f"{color}{s}{RESET}"
