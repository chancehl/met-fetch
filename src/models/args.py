from utils.print import Color, color


DEFAULT_SAVE_LOCATION = "./images"


class ArgumentException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_save_location(args) -> str:
    return args.outdir if args.outdir is not None else DEFAULT_SAVE_LOCATION


def validate_args(args):
    if args.count > 1 and (args.random is None or args.random == False):
        raise ArgumentException(
            "If the -r/--random flag is not passed, then count can only be 1."
        )


def get_count_from_args(args) -> int:
    return args.count if args.random is not None and args.random == True else 1
