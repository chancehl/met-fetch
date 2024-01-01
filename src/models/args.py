from utils.print import Color, color


DEFAULT_SAVE_LOCATION = "./images"


def get_save_location(args) -> str:
    return args.outdir if args.outdir is not None else DEFAULT_SAVE_LOCATION


def validate_args(args) -> bool:
    errors = []

    if args.count > 1 and (args.random is None or args.random == False):
        errors.append(
            "If the -r/--random flag is not passed, then count can only be 1."
        )

    if len(errors) > 0:
        print(color("Invalid arguments:\n", Color.RED))

        for index, error in enumerate(errors):
            print(f"error {index+1}: {error}")

    return len(errors) == 0


def get_count_from_args(args) -> int:
    return args.count if args.random is not None and args.random == True else 1
