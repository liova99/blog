from app.passwords import *

# ============== INFO  ================================
# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
# ============== END INFO ==============================
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True
WTF_CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = CSRF_KEY

# Secret key for signing cookies, and WTF
SECRET_KEY = SECRET_KEY

MAIL_SERVER = "smtp.zoho.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = zoho_username
MAIL_PASSWORD = zoho_password