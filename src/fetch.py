import os
import sys

from yaspin import yaspin
from yaspin.spinners import Spinners
from services.met import download_artwork, get_artwork, search_for_artwork
from utils.list import pick_random_object
from models.artwork import is_valid_artwork, print_artwork_name
from models.args import CommandLineArguments


def main():
    """This is the entrypoint of the application"""

    # this is needed in order to initialize the ANSI terminal colors on Windows, Linux
    os.system("")
    arguments = CommandLineArguments()

    count = arguments.get_count()
    outdir = arguments.get_outdir()
    query = arguments.get_query()

    viewed = []
    downloaded_pieces = 0

    with yaspin(
        Spinners.dots, text="Searching for artwork...", color="cyan"
    ) as spinner:
        # search for the query before looping
        matching_pieces = search_for_artwork(query)

        while downloaded_pieces < count:
            random_id = pick_random_object(matching_pieces)

            artwork = get_artwork(object_id=random_id)

            if is_valid_artwork(artwork, viewed):
                # Update spinner
                spinner.text = f"Downloading {print_artwork_name(artwork)}"

                # download the file to specified location
                download_artwork(artwork, outdir)

                # save this so we don't re-download the same image
                viewed.append(artwork["objectID"])

                # increment count after successful download
                downloaded_pieces += 1

    # exit process
    sys.exit(0)


if __name__ == "__main__":
    main()
