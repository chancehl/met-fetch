# pylint: disable=invalid-name
# matching MET API model format
from dataclasses import dataclass
from typing import Optional


@dataclass
class Constituent:
    constituentID: int
    role: str
    name: str
    constituentULAN_URL: Optional[str]
    constituentWikidata_URL: Optional[str]
    gender: Optional[str]
