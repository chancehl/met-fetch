# pylint: disable=invalid-name
# matching MET API model format
from dataclasses import dataclass
from typing import Optional


@dataclass
class ElementMeasurements:
    Height: float
    Width: float


@dataclass
class Measurement:
    elementName: str
    elementDescription: Optional[str]
    elementMeasurements: ElementMeasurements
