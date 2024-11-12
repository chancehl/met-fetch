from io import BytesIO
from pathlib import Path
from PIL import Image, ExifTags

from models.artwork import MuseumArtwork


def write_bytes(name: str, img: bytes, outdir: str) -> None:
    """Save artwork image to the specified output directory."""
    path = Path(outdir)

    if not path.exists():
        path.mkdir(parents=True)

    with open(path / name, "wb") as file:
        file.write(img)


def write_bytes_with_exif(artwork: MuseumArtwork, img: bytes, outdir: str) -> None:
    path = Path(outdir)

    if not path.exists():
        path.mkdir(parents=True)

    image = Image.open(BytesIO(img))

    exif = Image.Exif()
    exif[ExifTags.Base.ImageDescription] = artwork.objectID
    exif[ExifTags.Base.Artist] = artwork.artistDisplayName
    exif[ExifTags.Base.DocumentName] = artwork.title

    image.save(path / f"{artwork.objectID}.jpg", exif=exif)
