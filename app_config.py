#!/usr/bin/env python

"""
Project-wide application configuration.

DO NOT STORE SECRETS, PASSWORDS, ETC. IN THIS FILE.
They will be exposed to users. Use environment variables instead.
See get_secrets() below for a fast way to access them.
"""

import os

"""
NAMES
"""
# Project name used for display
PROJECT_NAME = 'quotable'

# Project name in urls
# Use dashes, not underscores!
PROJECT_SLUG = 'quotable'

# The name of the repository containing the source
REPOSITORY_NAME = 'quotable'
REPOSITORY_URL = 'git@github.com:niteshvgupta/%s.git' % REPOSITORY_NAME

# The name to be used in paths on the server
PROJECT_FILENAME = 'quotable'

"""
DEPLOYMENT
"""
FILE_SERVER = '212.47.234.194'
S3_BUCKET = 'test.wbur.org'
ASSETS_S3_BUCKET = 'test.wbur.org'

# These variables will be set at runtime. See configure_targets() below
DEBUG = True

"""
COPY EDITING
"""
COPY_GOOGLE_DOC_KEY = '0AlXMOHKxzQVRdHZuX1UycXplRlBfLVB0UVNldHJYZmc'


