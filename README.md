# Trap Scoring

An app that records scores and related data for generating metrics on Trap shooting. Includes all sorts of minor details to help sort out what you have the most success with and where you can improve.

For a detailed outline of the project:
[MVP Proposal](MVP.md)

# Setup
Clone the repo:
```
git clone https://github.com/stephenmuller/Trap-Scoring.git
```

Make a virtual env for it:
```
virtualenv venv
```
Activate the venv:
(osx)
```
source venv/bin/Activate
```
Install requirements:
```
pip install -r requirements.txt
```
Migrate the Database to SQLITE3
```
python manage.py migrate
```
Make an admin account, which handily adds a user to the database:
```
python manage.py createsuperuser
```
Open up the shell:
```
python manage.py shell
```
Run these commands:
```
from trap_scorekeeping import dbinit
dbinit.init_basic_defaults()
```


Then run the server:
```
python manage.py runserver
```

Finally Navigate to the default URL and play with it:

http://localhost:8000

# Usage

The basic use case for the app is to record your Trap Scores, the main focus is identifying specific targets that you miss the most, be it a specific station, or the last target of a given round, etc. There is also data on what shotgun was used, what shells were used, and time/location data that can help further isolate any variables.
There is a lot of generic 'High Score' style data presented on the main page, and each players page lists an overview of their data.
