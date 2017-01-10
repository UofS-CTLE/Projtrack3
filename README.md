# Projtrack 3

This project's dependencies include Django.

[Projtrack 3 Wiki](https://github.com/cyclerdan/Projtrack3/wiki/)

Before contributing, check out this [quick guide to Django.](https://docs.djangoproject.com/en/1.10/intro)


## Windows

### Getting Started
For a full guide, refer to [the django docs](https://docs.djangoproject.com/en/1.10/howto/windows).
Download [Git](https://git-scm.com/download/win), [Python](https://www.python.org/downloads/windows/), and [Pip](https://pip.pypa.io/en/latest/installing/)
Once **pip** is installed, run
```
> pip install django
```
Using the git command line installed with **git**, execute
```
> git clone https://github.com/cyclerdan/Projtrack3.git
```
In **cmd**, execute
```
> cd Projtrack3\ctleweb
> python manage.py runserver 8080
```
to start the development server running.
## macOS/Linux

### Getting Started
Ensure that **git**, **python**, and **pip** are present on your system. If they are, run
```
$ pip install django
$ git clone https://github.com/cyclerdan/Projtrack3.git
```
to set up the project and
```
$ cd Projtrack/ctleweb
$ python manage.py runserver 8080
```
to run the server.

## The Directory Tree
```
ctleweb/
	ctleweb/
		__init__.py
		settings.py
		urls.py
		wsgi.y
		...
	projtrack/
		migrations/
			0001_initial.py
			__init__.py
			...
		templates/
			index.html
			...
		static/
			projtrack/
				projtrack.css
				...
			...
		__init__.py
		admin.py
		apps.py
		forms.py
		models.py
		tests.py
		urls.py
		views.py
		...
	db.sqlite3
	manage.py
	...
README.md
```

# Quick Git Crash Course
When contributing to the project:
- Branch with `git branch [name]` followed by `git checkout [name]`. This will allow your changes to be made safely in a separate working tree.
- Make whatever changes you need and periodically save them by running `git add *; git commit -am "[message]"; git push origin [name]`
- When you've finished what you're working on, go to Github and file a **pull request**. The branch will then be tested before being merged with **master**.

**Only working code should ever be committed to master.**

# Testing with an admin account
Since the binary files and database files are not being shared, the administrative/user accounts will not be shared on the Github repository. In order to access admin functions, you'll need to run `python manage.py createsuperuser` to set up the environment.
