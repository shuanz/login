#Sisop
##Authentication & Authorization
###Instructions

1. Requirements::
    ~~~~
   Python 3.3+
    ~~~~
   
2. Install sqlite3::
    ~~~~
    sudo apt-get install sqlite3
    ~~~~
   
3. Install virtualenv (Optional)::
    ~~~~
    pip install virtualenv
    ~~~~
   
4. Create virtual environment (Optional)::
    ~~~~
    python3 -m virtualenv venv
   ~~~~

5. Activate virtual environment (Optional)::
    ~~~~
    source /venv/bin/activate
   ~~~~

6. Install package requirements::
    ~~~~
    pip install -r requirements.txt
   ~~~~

7. Generate secret key::

    ~~~~
   import os 
   os.urandom(24)
   ~~~~

8. Configure secret key on local_settings.py::

    `SECRET_KEY = "YOUR SECRET KEY HERE"`

9. Create database (from ../login on python cli run)::
    ~~~~
    from login import create_app, db
    app = create_app()
    app.app_context().push()
    db.create_all(app=create_app())
   ~~~~

10. Run flask::
    ~~~~
    export FLASK_APP=__init__.py
    run flask
    ~~~~