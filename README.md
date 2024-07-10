# Superlists with priority
1. Clone repo
    git clone https://github.com/aurimrv/superlists.git
2. Create SQLite database
    python manage.py migrate
3. Startup Django server
    python manage.py runserver
4. Run tests
    python manage.py test functional_tests /
    python manage.py test lists
