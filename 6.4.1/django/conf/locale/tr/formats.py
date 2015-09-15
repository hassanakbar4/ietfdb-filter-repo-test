# -*- encoding: utf-8 -*-
# This file is distributed under the same license as the Django package.
#
from __future__ import unicode_literals

# The *_FORMAT strings use the Django date format syntax,
# see http://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
DATE_FORMAT = 'd F Y'
TIME_FORMAT = 'H:i:s'
DATETIME_FORMAT = 'd F Y H:i:s'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'd F'
SHORT_DATE_FORMAT = 'd M Y'
SHORT_DATETIME_FORMAT = 'd M Y H:i:s'
FIRST_DAY_OF_WEEK = 1  # Pazartesi

# The *_INPUT_FORMATS strings use the Python strftime format syntax,
# see http://docs.python.org/library/datetime.html#strftime-strptime-behavior
DATE_INPUT_FORMATS = (
    '%d/%m/%Y', '%d/%m/%y',     # '25/10/2006', '25/10/06'
    '%y-%m-%d',                 # '06-10-25'
    # '%d %B %Y', '%d %b. %Y',  # '25 Ekim 2006', '25 Eki. 2006'
)
DATETIME_INPUT_FORMATS = (
    '%d/%m/%Y %H:%M:%S',     # '25/10/2006 14:30:59'
    '%d/%m/%Y %H:%M:%S.%f',  # '25/10/2006 14:30:59.000200'
    '%d/%m/%Y %H:%M',        # '25/10/2006 14:30'
    '%d/%m/%Y',              # '25/10/2006'
)
DECIMAL_SEPARATOR = ','
THOUSAND_SEPARATOR = '.'
NUMBER_GROUPING = 3
