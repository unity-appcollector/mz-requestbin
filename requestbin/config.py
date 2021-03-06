import os, urlparse
DEBUG = True
REALM = os.environ.get('REALM', 'local')

ROOT_URL = "http://localhost:4000"

PORT_NUMBER = 4000

ENABLE_CORS = False
CORS_ORIGINS = "*"

FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", "QA1H9Ho880mq6t6Uo1Kcx9En8A3sZEDKXVXfVdZvmGvLr9Q9HshwmVa9QSCH")

BIN_TTL = 0
STORAGE_BACKEND = "requestbin.storage.memory.MemoryStorage"
MAX_RAW_SIZE = int(os.environ.get('MAX_RAW_SIZE', 1024*10))
IGNORE_HEADERS = []
MAX_REQUESTS = 100
CLEANUP_INTERVAL = 0

REDIS_URL = ""
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_DB = 9

REDIS_PREFIX = "requestbin"

BUGSNAG_KEY = ""

if REALM == 'prod':
    DEBUG = False
    ROOT_URL = "https://requestbin.stg.mz.internal.unity3d.com/"

    FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", FLASK_SESSION_SECRET_KEY)

    STORAGE_BACKEND = "requestbin.storage.redis.RedisStorage"

    REDIS_URL = os.environ.get("REDIS_URL", "")
    url_parts = urlparse.urlparse(REDIS_URL)
    REDIS_HOST = os.environ.get("REDIS_HOST", url_parts.hostname)
    REDIS_PORT = os.environ.get("REDIS_PORT", url_parts.port)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", url_parts.password)
    REDIS_DB = os.environ.get("REDIS_DB", url_parts.fragment)

    BUGSNAG_KEY = os.environ.get("BUGSNAG_KEY", BUGSNAG_KEY)

    IGNORE_HEADERS = """
X-Varnish
X-Forwarded-For
X-Heroku-Dynos-In-Use
X-Request-Start
X-Heroku-Queue-Wait-Time
X-Heroku-Queue-Depth
X-Real-Ip
X-Forwarded-Proto
X-Via
X-Forwarded-Port
""".split("\n")[1:-1]
