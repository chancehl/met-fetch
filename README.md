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
pip install -g venv
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

-r, --random: Selects a random object.
-o, --outdir: Specifies the save location.
-n, --count: Number of images to return.
-v, --verbose: Displays log output.

Example:

```bash
python ./src/fetch.py "still life" -n 3 -r -o ./images
```

## Contributing

Don't.

## License

See `LICENSE` file
