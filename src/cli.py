import argparse

from services import wallpaper

DEFAULT_SAVE_LOCATION = "test.png"


def main():
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

    # retries argument
    parser.add_argument(
        "-n",
        "--num-retries",
        type=int,
        default=3,
        metavar="num_retries",
        help="The number of times to retry to get a piece of art that has an image. Default=3.",
    )

    # outfile argument
    parser.add_argument(
        "-o",
        "--outfile",
        type=str,
        default=None,
        metavar="outfile",
        help="The location to save the image to. By default the CLI will create a tmp file and then delete it after the run.",
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

    # execute program
    wallpaper_service = wallpaper.WallpaperService()

    attempt = 0

    # sometimes the API responds with a piece of art that does not have an image
    # when that happens, just retry
    while attempt < args.num_retries:
        image_url = wallpaper_service.get_wallpaper(args.query, args.random)

        if image_url is None or len(image_url) == 0:
            attempt += 1
        else:
            # determine save location
            location = (
                args.outfile if args.outfile is not None else DEFAULT_SAVE_LOCATION
            )

            # download the file to specified location
            wallpaper_service.download_wallpaper(image_url, location)

            # set the wallpaper
            wallpaper_service.set_wallpaper(location)

            # exit process
            exit(0)


if __name__ == "__main__":
    main()
