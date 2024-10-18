import os
from random import choice
import sys

from yaspin import yaspin
from yaspin.spinners import Spinners
from met_api import download_artwork, get_artwork, search_for_artwork
from models.artwork import is_valid_artwork, format_artwork_data, print_report
from models.args import CommandLineArguments


def main():
    # this is needed in order to initialize the ANSI terminal colors on Windows, Linux
    os.system("")

    arguments = CommandLineArguments()

    count = arguments.get_count()
    outdir = arguments.get_outdir()
    query = arguments.get_query()
    fuzziness = arguments.get_fuzziness()

    processed = []

    with yaspin(
        Spinners.dots, text="Searching for artwork...", color="cyan"
    ) as spinner:
        # search for the query before looping
        matching_pieces = search_for_artwork(query)

        while len(processed) < count:
            random_id = choice(matching_pieces[0:fuzziness])

            artwork = get_artwork(object_id=random_id)

            if is_valid_artwork(artwork, processed):
                # update spinner
                spinner.text = f"Downloading {format_artwork_data(artwork)}"

                # download the file to specified location
                download_artwork(artwork, outdir)

                # save this so we don't re-download the same image
                processed.append(artwork)

    # print report to console
    print_report(processed, outdir)

    # exit process
    sys.exit(0)


if __name__ == "__main__":
    main()
