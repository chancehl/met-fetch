# met-fetch

## Description

This project is a CLI tool for downloading artwork from the Metropolitan Museum of Art. It uses the MET API for artwork search and display.

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
-o, --outdir: Specifies the save location.
-n, --count: Number of images to return.
-v, --verbose: Displays log output.
```

Example:

```bash
python ./src/fetch.py "still life" -n 3 -o ./images
```

Help:

```
usage: fetch.py [-h] [-o outdir] [-n count] [-v | --verbose | --no-verbose] [-s | --skip-report | --no-skip-report] [query]

A CLI for downloading images of artwork contained within the MET collection

positional arguments:
  query                 Query help text

options:
  -h, --help            show this help message and exit
  -o outdir, --outdir outdir
                        The location to save the images to.
  -n count, --count count
                        The count of images to return
  -v, --verbose, --no-verbose
                        Displays log output when set. Default=False.
  -s, --skip-report, --no-skip-report
                        Whether or not the tool should generate the report.json file.
```

## Contributing

Don't.

## License

See `LICENSE` file
