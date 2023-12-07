from .local import *

ALLOWED_HOSTS = ['.backendcam-64bo4zjn.b4a.run', 'backendcam-64bo4zjn.b4a.run']

# Setup support for proxy headers
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
FORCE_SCRIPT_NAME = '/'
# SECURE_SSL_REDIRECT = True

CSRF_TRUSTED_ORIGINS = ['https://backendcam-64bo4zjn.b4a.run',]
CSRF_COOKIE_DOMAIN = 'https://backendcam-64bo4zjn.b4a.run'


DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}


###################################
    ##  CLOUDINARY IMAGE AND VIDEO UPLOAD SETTINGS ##
#################################### 
cloudinary.config( 
  cloud_name = os.getenv('CLOUDINARY_NAME'), 
  api_key =  os.getenv('API_KEY'), 
  api_secret =  os.getenv('API_SECRET'),
  secure =  os.getenv('SECURE')
)


