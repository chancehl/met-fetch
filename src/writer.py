from pathlib import Path


def write_bytes(name: str, img: bytes, outdir: str) -> None:
    """Save artwork image to the specified output directory."""
    path = Path(outdir)

    if not path.exists():
        path.mkdir(parents=True)

    with open(path / name, "wb") as file:
        file.write(img)
