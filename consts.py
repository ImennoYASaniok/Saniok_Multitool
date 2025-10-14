from decouple import config

TYPE_TOKEN = 'EXTRA_TOKEN' # TOKEN
TOKEN = config(TYPE_TOKEN)
ADMINS = list(map(int, config('ADMINS').split(',')))