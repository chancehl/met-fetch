"""args.py"""
DEFAULT_SAVE_LOCATION = "./images"


class ArgumentException(Exception):
    """Custom exception class"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_save_location(args) -> str:
    """Gets the save location based on the user-provided args"""
    return args.outdir if args.outdir is not None else DEFAULT_SAVE_LOCATION


def validate_args(args):
    """Raises an exception if the provided arguments are invalid"""
    if args.count > 1 and (args.random is None or args.random is False):
        raise ArgumentException(
            "If the -r/--random flag is not passed, then count can only be 1."
        )


def get_count_from_args(args) -> int:
    """Gets the count based on the user provided args"""
    return args.count if args.random is not None and args.random is True else 1
