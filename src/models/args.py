"""args.py"""

import argparse

DEFAULT_SAVE_LOCATION = "./images"


class ArgumentException(Exception):
    """Custom exception class"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class CommandLineArguments:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description="A CLI for downloading images of artwork contained within the MET collection"
        )

        # query argument
        self.parser.add_argument(
            "query", nargs="?", type=str, default=None, help="Query help text"
        )

        # outfile argument
        self.parser.add_argument(
            "-o",
            "--outdir",
            type=str,
            default=None,
            metavar="outdir",
            help="The location to save the images to.",
        )

        # count argument
        self.parser.add_argument(
            "-n",
            "--count",
            type=int,
            default=1,
            metavar="count",
            help="The count of images to return",
        )

        # verbose argument
        self.parser.add_argument(
            "-v",
            "--verbose",
            type=bool,
            metavar="verbose",
            action=argparse.BooleanOptionalAction,
            help="Displays log output when set. Default=False.",
        )

        # report argument
        self.parser.add_argument(
            "-s",
            "--skip-report",
            type=bool,
            metavar="skip_report",
            action=argparse.BooleanOptionalAction,
            help="Whether or not the tool should generate the report.json file.",
        )

        # parse args
        self.args = self.parser.parse_args()

    def get_args(self):
        return self.args

    def get_count(self):
        return self.args.count if self.args.count is not None else 1

    def get_outdir(self):
        return (
            self.args.outdir if self.args.outdir is not None else DEFAULT_SAVE_LOCATION
        )

    def get_query(self):
        return self.args.query
