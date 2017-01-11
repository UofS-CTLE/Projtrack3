#!/bin/bash

function script_help {
    echo This script runs all cleaning, compiling/optimizing, database building, and testing.
    echo usage:
    echo -e '\t./build.sh [command]'
    echo -e '\tcompile: creates python bytecode files for all source'
    echo -e '\tclean: cleans out all non-source files'
    echo -e '\tmigrate: creates the database'
    echo -e '\trun: runs the development server'
    echo -e '\tdeploy: deploys the app to production'
    echo -e '\tall-run: cleans, compiles, migrates, and starts the development server'
    echo -e '\tall-deploy: cleans, compiles, migrates, and deploys to production'
}

function all {
    clean
    compile
    migrate
    run_tests
    python manage.py createsuperuser
}

function run_tests {
    python manage.py test
}

function clean {
    rm db.sqlite3
    rm -rf projtrack/migrations/*
    files=$(find . -name "__pycache__")
    rm -rf $files
}

function compile {
    source_files=$(find . -name "*.py" ! -name "manage.py")
    python -m py_compile $source_files
}

function migrate {
    python manage.py makemigrations projtrack
    python manage.py migrate
}

function deploy {
    echo No deploy function implemented.
}

function run {
    python manage.py runserver 8080
}

case "$1" in
    compile)
        compile
        ;;

    clean)
        clean
        ;;

    migrate)
        migrate
        ;;

    run)
        run
        ;;

    deploy)
        deploy
        ;;

    all-run)
        all
        run
        ;;

    all-deploy)
        all
        deploy
        ;;

    all)
        all
        ;;

    *)
        script_help
        ;;

    esac
