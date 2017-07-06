#!/bin/bash

if [ -n '/bin/python3' ]; then
	alias python=python
fi

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
    echo -e '\tall: performs all cleaning, compiling, and testing functions'
    echo -e '\trestart: restarts the production Apache daemon'
    echo -e '\tpopulate: populates the database'
    echo -e '\tup: activates the virtual environment'
    echo -e '\tdown: deactivates the virtual environment'
    echo -e '\tinstall: installs the project in a virtual environment'
    echo -e '\tbackup: saves an SQL dump of the database to the current home directory'
    echo -e '\trestore [filename]: recreates the database from an sql file.'
}

function all {
    compile
    migrate
    run_tests
    python manage.py createsuperuser
}

function run_tests {
    python manage.py test projtrack.tests
}

function clean {
    rm db.sqlite3
    rm -rf projtrack/migrations/*
    files=$(find . -name "__pycache__")
    files2=$(find . -iregex ".*\.\(pyc\)")
    rm -rf $files2
    rm -rf $files
}

function compile {
    source_files=$(find . -name "*.py" ! -name "manage.py")
    python -m py_compile ${source_files}
}

function migrate {
    python manage.py makemigrations projtrack
    python manage.py migrate
}

function deploy {
    git add *
    git commit
    git push
}

function run {
    python manage.py runserver 8080
}

function backup {
    sqlite3 db.sqlite3 .schema > backup.sql
    sqlite3 db.sqlite3 .dump >> backup.sql
    date=$(date +%Y%m%d)
    mv backup.sql ~/backup-$date.sql
    echo Database backed up to $HOME\backup-$date.sql
}

function restore {
    cat $1 | sqlite3 db.sqlite3
}

case "$1" in

    backup)
        backup
        ;;

    restore)
        restore $2
        ;;

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

    restart)
        sudo service httpd restart
        ;;

    populate)
        python Populate_Projtrack3.py
        ;;

    server-env)
        source /usr/local/venvs/projtrack3env/bin/activate
        ;;
	
    up)
    	source projtrack3/bin/activate
    	;;
	
    down)
    	deactivate
	;;
	
    install)
    	virtualenv projtrack3
	source projtrack3/bin/activate
    	pip install django
	pip install djangorestframework
	;;

    *)
        script_help
        ;;

    esac
