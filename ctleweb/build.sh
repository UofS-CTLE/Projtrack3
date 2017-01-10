#!/bin/bash
echo This script runs all cleaning, compiling/optimizing, database building, and testing.
rm db.sqlite3
rm -rf projtrack/migrations/*
files=$(find . -name "__pycache__")
rm -rf $files
source_files=$(find . -name "*.py" ! -name "manage.py")
python -m py_compile $source_files
python manage.py makemigrations
python manage.py migrate
python manage.py test
