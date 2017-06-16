# Projtrack 3
***Remember to run build.sh before opening a pull request.***

This project's dependencies include Django and the Django REST Framework (starting in release 3.0.3-beta.6).

[Projtrack 3 Wiki](https://github.com/cyclerdan/Projtrack3/wiki/)

Before contributing, check out this [quick guide to Django.](https://docs.djangoproject.com/en/1.10/intro)


## Windows

### Getting Started
For a full guide, refer to [the django docs](https://docs.djangoproject.com/en/1.10/howto/windows).
Download [Git](https://git-scm.com/download/win), [Python](https://www.python.org/downloads/windows/), and [Pip](https://pip.pypa.io/en/latest/installing/)
Once **pip** is installed, run
```
> pip install django
> pip install djangorestframework
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
$ sudo pip install django
$ sudo pip install djangorestframework
$ git clone https://github.com/cyclerdan/Projtrack3.git
```
to set up the project and
```
$ cd Projtrack/ctleweb
$ python manage.py runserver 8080
```
to run the server.

# Quick Git Crash Course
When contributing to the project:
- Branch with `git branch [name]` followed by `git checkout [name]`. This will allow your changes to be made safely in a separate working tree.
- Make whatever changes you need and periodically save them by running `git add *; git commit -am "[message]"; git push origin [name]`
- When you've finished what you're working on, go to Github and file a **pull request**. The branch will then be tested before being merged with **master**.

**Only working code should ever be committed to master.**

# Testing with an admin account
Since the binary files and database files are not being shared, the administrative/user accounts will not be shared on the Github repository. In order to access admin functions on the development server, you'll need to run `python manage.py createsuperuser` to set up the environment.
