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
    python3 manage.py createsuperuser
}

function run_tests {
    python3 manage.py test
}

function clean {
    rm db.sqlite3
    rm -rf projtrack/migrations/*
    files=$(find . -name "__pycache__")
    rm -rf $files
}

function compile {
    source_files=$(find . -name "*.py" ! -name "manage.py")
    python3 -m py_compile $source_files
}

function migrate {
    python3 manage.py makemigrations projtrack
    python3 manage.py migrate
}

function deploy {
    git add *
    git commit
    git push
}

function run {
    python3 manage.py runserver 8080
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

    test)
        run_tests
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
        all && clean && deploy
        ;;

    all)
        all
        ;;

    *)
        script_help
        ;;

    esac
