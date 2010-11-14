#!/bin/bash
# ----------------------------------------------- # 
# configuration
# ----------------------------------------------- # 
CONFIG = "`pwd`"
VEROOT = "/home/devel/env/"

# ----------------------------------------------- # 
# main runner
# ----------------------------------------------- # 
. ${CONFIG}/django_bash_completion
source ${VEROOT}/django/bin/activate
git svn rebase
xrandr --output VGA-0 --auto --mode 1024x768 --same-as LVDS
