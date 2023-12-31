import argparse
import os

from services.met import MetropolitanMeseumOfArtService
from utils.print import color, Color

DEFAULT_SAVE_LOCATION = "./images"
NUM_RETRIES = 3


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

    # instantiate services
    artwork_service = MetropolitanMeseumOfArtService()

    image_count = 0

    while image_count < args.count:
        attempt = 0

        # sometimes the API responds with a piece of art that does not have an image
        # when that happens, just retry
        while attempt < NUM_RETRIES:
            met_artwork = artwork_service.get_artwork(args.query, args.random)

            image_url = met_artwork.get("primaryImage")
            image_id = met_artwork.get("objectID")

            if image_url is None or len(image_url) == 0:
                attempt += 1
            else:
                # determine save location
                save_location = (
                    args.outdir if args.outdir is not None else DEFAULT_SAVE_LOCATION
                )

                # download the file to specified location
                artwork_service.download_artwork(image_id, image_url, save_location)

                # generate report
                artists = met_artwork.get("constituents")
                artist_name = (
                    artists[0].get("name") if artists is not None else "Unknown"
                )
                department = met_artwork.get("department")
                title = met_artwork.get("title")
                object_date = met_artwork.get("objectDate")

                print(
                    f'{image_count+1}.) "{color(title, Color.CYAN)}" by {color(artist_name, Color.GREEN)} ({object_date}, {department} department)'
                )

                # break out of loop if we've made it here
                break

        image_count += 1

    # exit process
    exit(0)


if __name__ == "__main__":
    main()
