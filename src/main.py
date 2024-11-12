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

    # List to keep track of processed artworks
    processed: List[MuseumArtwork] = []

    with yaspin(
        Spinners.dots, text="Searching for artwork...", color="cyan"
    ) as spinner:
        matching_ids = search_for_artwork(query)

        while len(processed) < count:
            artwork = get_artwork(choice(matching_ids[:fuzziness]))

            primary_img_url = (
                "" if artwork.primaryImage is None else artwork.primaryImage
            )

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

    # Print report to console
    print_report_to_console(processed, outdir)

    # Exit process
    sys.exit(0)


if __name__ == "__main__":
    main()
