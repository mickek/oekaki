from default import *

import json
with open('/home/dotcloud/environment.json') as f:
    env = json.load(f)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oekaki',
        'USER': env['DOTCLOUD_DB_MYSQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DB_MYSQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DB_MYSQL_HOST'],
        'PORT': int(env['DOTCLOUD_DB_MYSQL_PORT']),
    }
}
