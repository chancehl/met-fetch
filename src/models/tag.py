# pylint: disable=invalid-name
# matching MET API model format
from dataclasses import dataclass
from typing import Optional


@dataclass
class Tag:
    term: str
    AAT_URL: Optional[str]
    Wikidata_URL: Optional[str]
