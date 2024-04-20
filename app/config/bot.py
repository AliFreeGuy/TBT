from os import environ as env

BOT_SESSION = env.get('BOT_SESSION') or env.get('BOT_NAME')
API_ID = env.get('API_ID')
API_HASH = env.get('API_HASH')
BOT_TOKEN = env.get('BOT_TOKEN')
WORK_DIR = env.get('WORK_DIR') or '/tmp'
PROXY = {"scheme": env.get("PROXY_SCHEME"),
         "hostname": env.get("PROXY_HOSTNAME"),
         "port": int(env.get("PROXY_PORT"))}
DEBUG = env.get('BOT_DEBUG')
REDIS_HOST = env.get('REDIS_HOST')
REDIS_PORT = env.get('REDIS_PORT')
REDIS_DB= env.get('REDIS_DB')
REDIS_PASS = env.get('REDIS_PASS')