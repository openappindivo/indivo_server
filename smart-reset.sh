#!/bin/bash
utils/reset.sh -bs
python manage.py shell < load_smart_data.py