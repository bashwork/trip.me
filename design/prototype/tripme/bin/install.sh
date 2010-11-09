#!/bin/bash
# --------------------------------------------------------- #
# setup virtualenv
# --------------------------------------------------------- #
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "please install virtualenv to continue"
    exit -1
fi

# --------------------------------------------------------- #
# get source code
# --------------------------------------------------------- #
# git svn clone http://code.google.com
# git svn rebase

# --------------------------------------------------------- #
# install python requirements
# --------------------------------------------------------- #
pip install -r ../../requirements.txt
