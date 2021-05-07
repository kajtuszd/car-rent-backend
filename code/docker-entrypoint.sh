#!/bin/bash

ownership() {
    # Fixes files ownership
    # source: https://github.com/BD2KGenomics/cgl-docker-lib/blob/master/mutect/runtime/wrapper.sh#L5
    user_id=$(stat -c '%u:%g' /code)
    chown -R ${user_id} /code
}

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

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations || exit 1
python manage.py migrate || exit 1

# echo ''
# echo '--------------------------'
# echo 'Pylint'
# echo '--------------------------'
# echo ''
# find . -type f -name "*.py" | xargs pylint

echo ''
echo '--------------------------'
echo 'Ownership fixes'
echo '--------------------------'
echo ''
ownership

echo ''
echo '-------------------------'
echo 'Run command'
echo $@
echo '-------------------------'
echo ''
python manage.py $@ || exit 1
