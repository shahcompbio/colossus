#!/bin/bash
set -v
cd /home/ubuntu/colossus
git pull
source venv/bin/activate
pip3 install -r requirements.txt --ignore-installed
python3 manage.py migrate