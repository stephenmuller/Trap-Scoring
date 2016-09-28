Clone the repo:


Make a virtual env for it:
virtualenv venv

Activate the venv:
(osx)
source vev/bin/Activate

Install requirements:
 pip install -r requirements.txt

Migrate the Database to SQLITE3
python manage.py migrate

Make an admin account, which handily adds a user to the database:
python manage.py createsuperuser

Open up the shell:
python manage.py shell

Run these commands:
from trap_scorekeeping import dbinit
dbinit.init_basic_defaults()


Then run the server:
python manage.py runserver

Finally Navigate to the default URL and play with it:
localhost:8000
