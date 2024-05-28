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
    pass


def get_count_from_args(args) -> int:
    """Gets the count based on the user provided args"""
    return args.count if args.count is not None else 1
