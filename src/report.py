from typing import List
import json

from models.artwork import MuseumArtwork


def generate_report(art: List[MuseumArtwork]) -> None:
    """
    Generates a JSON dump of the artwork that was downloaded by the tool
    """
    with open("report.json", "w") as file:
        json.dump(art, file, indent=4)


def print_report_to_console(artwork: List[MuseumArtwork], outdir: str) -> None:
    print("Downloaded the following pieces:\n")

    for art in artwork:
        print(f"* {art.generate_summary()}")

    print(f"\nSaved artwork to: {outdir}")
