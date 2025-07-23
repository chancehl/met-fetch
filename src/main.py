import os
import sys
from random import choice
from typing import List

from yaspin import yaspin
from yaspin.spinners import Spinners

from met import get_artwork, search_for_artwork, get_image_bytes
from models.artwork import MuseumArtwork
from models.args import CommandLineArguments
from report import print_report_to_console
from writer import write_bytes_with_exif


def main():
    """Main function to orchestrate artwork searching and downloading."""

    # Initialize ANSI terminal colors on Windows/Linux
    os.system("")

    # Parse command line arguments
    arguments = CommandLineArguments()
    count = arguments.get_count()
    outdir = arguments.get_outdir()
    query = arguments.get_query()
    fuzziness = arguments.get_fuzziness()
    exact = arguments.get_exact()

    # List to keep track of processed artworks
    processed: List[MuseumArtwork] = []

    spinner = yaspin(Spinners.dots, text="Searching for artwork...", color="cyan")
    spinner.start()

    matching_ids = search_for_artwork(query)
    if len(matching_ids) == 0:
        spinner.stop()
        print(f'Did not find any results for query "{query}"')
        sys.exit(1)

    while len(processed) < count:
        chosen_piece = None

        if exact:
            chosen_piece = matching_ids[len(processed)]
        else:
            chosen_piece = choice(matching_ids[:fuzziness])

        artwork = get_artwork(chosen_piece)

        primary_img_url = "" if artwork.primaryImage is None else artwork.primaryImage

        already_processed = any(a.objectID == artwork.objectID for a in processed)

        if len(primary_img_url) > 0 and not already_processed:
            spinner.text = f"Downloading {artwork.generate_summary()}"

            # download image bytes and generate a file name
            image_bytes = get_image_bytes(primary_img_url)
            name = artwork.get_file_name()

            # write bytes to disk
            write_bytes_with_exif(artwork, image_bytes, outdir)

            # Save to avoid re-downloading
            processed.append(artwork)

    # stop spinner
    spinner.stop()

    # process results
    if len(processed) > 0:
        print_report_to_console(processed, outdir)
    else:
        print("No results were processed")

    # Exit process
    sys.exit(0)


if __name__ == "__main__":
    main()
