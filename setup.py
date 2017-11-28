from distutils.core import setup

setup(
    name='Projtrack3',
    version='3.1.0',
    packages=['ctleweb.ctleweb', 'ctleweb.projtrack', 'ctleweb.projtrack.migrations'],
    url='ctleweb.scranton.edu/projtrack3/',
    license='GPL',
    author='University of Scranton CTLE',
    author_email='uofsctle@gmail.com',
    description='', requires=['django']
)
