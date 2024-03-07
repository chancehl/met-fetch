from typing import List
import json

def generate_report(art: List):
    """
    Generates a JSON dump of the artwork that was downloaded by the tool
    """
    with open("report.json", "w") as file:
        json.dump(art, file, indent=4)
