"""
Pytest configuration and shared fixtures.
"""
import pytest
import sys
import os

# Add src directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


@pytest.fixture
def sample_artwork_data():
    """Fixture providing sample artwork data for tests."""
    return {
        "objectID": 12345,
        "isHighlight": True,
        "accessionNumber": "2023.1",
        "accessionYear": "2023",
        "isPublicDomain": True,
        "primaryImage": "https://example.com/image.jpg",
        "primaryImageSmall": "https://example.com/small.jpg",
        "additionalImages": [],
        "constituents": [],
        "department": "Paintings",
        "objectName": "Painting",
        "title": "Test Artwork",
        "culture": "American",
        "period": "Modern",
        "dynasty": None,
        "reign": None,
        "portfolio": None,
        "artistRole": "Artist",
        "artistPrefix": None,
        "artistDisplayName": "Test Artist",
        "artistDisplayBio": "Test Bio",
        "artistSuffix": None,
        "artistAlphaSort": "Artist, Test",
        "artistNationality": "American",
        "artistBeginDate": "1900",
        "artistEndDate": "1980",
        "artistGender": None,
        "artistWikidata_URL": None,
        "artistULAN_URL": None,
        "objectDate": "1950",
        "objectBeginDate": 1950,
        "objectEndDate": 1950,
        "medium": "Oil on canvas",
        "dimensions": "24 x 36 in.",
        "measurements": [],
        "creditLine": "Gift of Test Donor",
        "geographyType": None,
        "city": None,
        "state": None,
        "county": None,
        "country": None,
        "region": None,
        "subregion": None,
        "locale": None,
        "locus": None,
        "excavation": None,
        "river": None,
        "classification": "Paintings",
        "rightsAndReproduction": None,
        "linkResource": None,
        "metadataDate": "2023-01-01",
        "repository": "Metropolitan Museum of Art",
        "objectURL": "https://www.metmuseum.org/art/collection/search/12345",
        "tags": [],
        "objectWikidata_URL": None,
        "isTimelineWork": False,
        "GalleryNumber": "101"
    }
