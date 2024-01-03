# met-fetch

## Description

This project is a CLI tool for setting artwork from the Metropolitan Museum of Art as desktop backgrounds. It uses the MET API for artwork search and display.

## Features

- Search for artwork by query or randomly from the MET collection.
- Set the number of artworks to retrieve.
- Choose download directory and verbosity level.

## Installation

1. Clone the git repository

```bash
git clone https://github.com/chancehl/met-fetch.git
```

2. Install `venv`

```bash
pip install -g virutalenv
```

3. Create and activate a virtual environment

```bash
python -m venv venv
source ./venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

Complete!

## Usage

```bash
python [main_script_name].py [options]

```

Options include:

```
-r, --random: Selects a random object.
-o, --outdir: Specifies the save location.
-n, --count: Number of images to return.
-v, --verbose: Displays log output.
```

Example:

```bash
python ./src/fetch.py "still life" -n 3 -r -o ./images
```

Help:

```
usage: fetch.py [-h] [-r | --random | --no-random] [-o outdir] [-n count] [-v | --verbose | --no-verbose] [query]

A CLI for downloading images of artwork contained within the MET collection

positional arguments:
  query                 Query help text

options:
  -h, --help            show this help message and exit
  -r, --random, --no-random
                        Selects a random object from the objects returned. If no query is provided, this will search for a random object.
  -o outdir, --outdir outdir
                        The location to save the images to.
  -n count, --count count
                        The count of images to return
  -v, --verbose, --no-verbose
                        Displays log output when set. Default=False.
```

## Contributing

Don't.

## License

See `LICENSE` file
