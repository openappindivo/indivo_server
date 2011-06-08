#!/bin/bash
utils/reset.sh -bs
python manage.py shell < load_smart_data.py
for p in smart_patients/*.py; do python manage.py shell < $p; done
