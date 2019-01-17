## Setup

1. Install `python3`.
2. `git clone` this repo
3. In the project root run: `python3 -m venv ./env`. This will create a virtual environment in `env`, where the project dependencies will be installed.
4. Activate the virtual environment: `source env/bin/activate` (you'll need to do this again every time you open a new terminal and want to run the scripts)
5. Install the requirements: `pip install -r requirements.txt`
6. Get the `certs.json` from Michael, or create a new service account with Firebase privileges and download its credentials. This should be placed in the project root as `certs.json`.

## Usage

Download the user data into `data.json`.
```
$ python fetch.py
```

Count participant data from `data.json`. (You will need to fetch the data again if you want the most recent data)
```
$ python count.py
```
