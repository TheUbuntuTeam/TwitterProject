# twitter client example

## What is twitter client example

- uses the twitter api to fetch tweets searching for a term
- saves tweets into postgres db


## Build

to build the package do:

    python setup.py sdist

You can find your package archive in `dist/extract_script-0.1.tar.gz`


## Publish

Copy archive from `dist` directory into dropbox and
share its url.

If you have your dropbox configured to sync automatically do:

    python publish.py


## Install

To install this package on your server run:

    pip install  https://s3.amazonaws.com/tsid-marco-test/app.tar.gz


## Run

To run the app on your servers do:

    python -m twitter_example XXXXX YYYYY



## Test

    ????


## Logging and monitoring

The app will log all its activity on a file named `twitter_example.log`
