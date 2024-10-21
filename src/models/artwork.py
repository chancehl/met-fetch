# pylint: disable=invalid-name,too-many-instance-attributes
# matching MET API model format
import re
from typing import List, Optional, Self
from dataclasses import dataclass

from models.constituent import Constituent
from models.measurements import Measurement
from models.tag import Tag
from format import format_with_color

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

    def __post_init__(self: Self):
        """Post-initialization processing to convert nested dictionaries into objects."""
        if self.constituents:
            self.constituents = [
                Constituent(**const) if isinstance(const, dict) else const
                for const in self.constituents
            ]

        if self.tags:
            self.tags = [
                Tag(**tag) if isinstance(tag, dict) else tag for tag in self.tags
            ]

    def get_file_name(self: Self) -> str:
        """Generate a clean filename based on artwork's title or artist."""
        base_name = self.artistDisplayName or self.title or str(self.objectID)

        # Clean the base name to only include alphanumeric characters and underscores
        base_name = re.sub(r"[^a-zA-Z0-9]+", "_", base_name.strip())

        # Truncate the name if too long
        base_name = base_name[:45].rstrip("_") if len(base_name) > 45 else base_name

        return f"{base_name}_{self.objectID}.png".lower()

    def get_artist_name(self: Self) -> str:
        """Return the name of the first artist, or 'Unknown artist'."""
        return self.artistDisplayName if self.artistDisplayName else "Unknown artist"

    def generate_summary(self: Self) -> str:
        """Generate a formatted summary of the artwork."""
        artist_name = self.get_artist_name()
        return f'"{format_with_color(self.title, CYAN)}" by {format_with_color(artist_name, GREEN)} ({self.objectDate}, {self.department} department, piece no. {self.objectID})'
