# LibraryProject

Small Django project for learning core concepts: models, views, templates, and admin for a simple library catalog.

## Prerequisites
- Python 3.8+
- pip

## Quick setup
```bash
# create virtualenv 
python -m venv .venv
# activate 
pip install -r requirements.txt

# apply migrations and create admin
python manage.py migrate
python manage.py createsuperuser
```

## Run-+
```bash
python manage.py runserver
# Open http://127.0.0.1:8000/
```

## Tests
```bash
python manage.py test
```

## Contributing
Small, focused changes welcome. Open an issue or PR with a clear description.

## License
See LICENSE or choose an appropriate open-source license.