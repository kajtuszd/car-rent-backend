#!/bin/bash

echo ''
echo '--------------------------'
echo 'Install missing packages'
echo '--------------------------'
echo ''
pip install -r ./requirements.txt

echo ''
echo '--------------------------'
echo 'Database migration'
echo '--------------------------'
echo ''

python manage.py makemigrations || exit 1
python manage.py migrate || exit 1

echo ''
echo '--------------------------'
echo 'Pylint'
echo '--------------------------'
echo ''
find . -type f -name "*.py" | xargs pylint

echo ''
echo '-------------------------'
echo 'Run command'
echo $@
echo '-------------------------'
echo ''
python manage.py $@ || exit 1
