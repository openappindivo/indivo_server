#!/bin/bash
utils/reset.sh -bcs
python manage.py shell < load_meds.py