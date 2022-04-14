# Databases Random Data Generator

## Quickstart

```bash
# Create a virtual environment in the current directory by running
python3 -m venv .venv

# Load the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run a python file
python3 main.py

# to leave virtual environment
deactivate

# if you install any python packages that are not nin the requirements.txt file
# run the following command before pushing to the repo!
pip freeze > requirements.txt
```

## Generating mock sql data

run `python3 mock.py`

navigate to `example.sql`

use find and replace, find all `None` and replace with `DEFAULT`
