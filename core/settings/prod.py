from .local import *

ALLOWED_HOSTS = ['*','.mfmyaounde-bmig8es3.b4a.run', 'mfmyaounde-bmig8es3.b4a.run']

# Setup support for proxy headers
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
FORCE_SCRIPT_NAME = '/'
# SECURE_SSL_REDIRECT = True

CSRF_TRUSTED_ORIGINS = ['https://mfmyaounde-bmig8es3.b4a.run',]
CSRF_COOKIE_DOMAIN = 'https://mfmyaounde-bmig8es3.b4a.run'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DB_ENGINE'),
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#     }
# }


###################################
    ##  CLOUDINARY IMAGE AND VIDEO UPLOAD SETTINGS ##
#################################### 
cloudinary.config( 
  cloud_name = 'ddqibt7em', 
  api_key =  '185718447627493', 
  api_secret =  'QIYTfSXOefCl72rixkvBgEzJiDs',
  secure =  True
)
# cloudinary.config( 
#   cloud_name = os.getenv('CLOUDINARY_NAME'), 
#   api_key =  os.getenv('API_KEY'), 
#   api_secret =  os.getenv('API_SECRET'),
#   secure =  os.getenv('SECURE')
# )


