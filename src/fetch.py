import argparse
import os

from api.met import download_artwork, get_artwork, search_artwork
from models.artwork import print_artwork
from models.args import (
    get_save_location,
    get_count_from_args,
    validate_args,
    ArgumentException,
)
from utils.print import color, Color
from random import choice

NUM_RETRIES = 3
FUZZY_SEARCH_THRESHOLD = 20


def main():
    os.system("")

    # parser object
    parser = argparse.ArgumentParser(
        description="A CLI tool for setting artwork from the Metropolitan Museum of Art as your desktop background"
    )

    # query argument
    parser.add_argument(
        "query", nargs="?", type=str, default=None, help="Query help text"
    )

    # random argument
    parser.add_argument(
        "-r",
        "--random",
        type=bool,
        metavar="random",
        action=argparse.BooleanOptionalAction,
        help="Selects a random object from the objects returned. If no query is provided, this will search for a random object.",
    )

    # outfile argument
    parser.add_argument(
        "-o",
        "--outdir",
        type=str,
        default=None,
        metavar="outdir",
        help="The location to save the images to.",
    )

    # count argument
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=1,
        metavar="count",
        help="The count of images to return",
    )

    # verbose argument
    parser.add_argument(
        "-v",
        "--verbose",
        type=bool,
        metavar="verbose",
        action=argparse.BooleanOptionalAction,
        help="Displays log output when set. Default=False.",
    )

    # parse args
    args = parser.parse_args()

    # valdiate args
    try:
        validate_args(args=args)
    except ArgumentException as e:
        print(color(f"Failed to validate arguments: {e}", Color.RED))

        exit(1)

    # determine appropriate count
    total_count = get_count_from_args(args=args)

    count = 0

    viewed = []

    # search for the query before looping
    object_ids = search_artwork(query=args.query)

    while count <= total_count:
        attempt = 0

        # sometimes the API responds with a piece of art that does not have an image
        # when that happens, just retry
        while attempt < NUM_RETRIES:
            # # if not random take the first, else take a random one from the first 20
            object_id = (
                object_ids[attempt]
                if not args.random
                else choice(object_ids[0:FUZZY_SEARCH_THRESHOLD])
            )

            artwork = get_artwork(id=object_id)

            image_url = artwork.get("primaryImage")
            artwork_id = artwork.get("objectID")

            if image_url is None or len(image_url) == 0:
                print(
                    f"Skipping artwork id {artwork_id} because it is missing an image."
                )

                attempt += 1
            elif artwork_id in viewed:
                print(
                    f"Skipping artwork id {artwork_id} because it has already been downloaded."
                )

                attempt += 1
            else:
                # determine save location
                save_location = get_save_location(args=args)

                # download the file to specified location
                download_artwork(
                    id=artwork_id,
                    image_url=image_url,
                    location=save_location,
                )

                # generate report
                print_artwork(artwork=artwork)

                # save this so we don't redownload the same image
                viewed.append(artwork_id)

                # break out of loop if we've made it here
                break

        count += 1

    # exit process
    exit(0)


if __name__ == "__main__":
    main()
