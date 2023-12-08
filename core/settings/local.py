from pathlib import Path
import os
import environ
# from django.templatetags.static import static
# from django.urls import reverse_lazy
import cloudinary
from django.utils.translation import gettext_lazy as _



# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = os.getenv('SECRET_KEY')
SECRET_KEY = 'django-insecure-$ok6*buoc-06t2^p&3aff(ki84i-9(gji!73pwsf7!%44sjrfs'


# DEBUG = os.getenv('DEBUG')
DEBUG = False
FORCE_SCRIPT_NAME = '/'
# Application definition

INSTALLED_APPS = [
    # 'admin_volt.apps.AdminVoltConfig',
    # "django_admin_tailwind",
    # "unfold",  # before django.contrib.admin
    # "unfold.contrib.filters",  # optional, if special filters are needed
    # "unfold.contrib.forms",  # optional, if special form elements are needed
    # "unfold.contrib.import_export",  # optional, if django-import-export package is used
    # "unfold.contrib.guardian",  # optional, if django-guardian package is used
    # "unfold.contrib.simple_history",
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'taggit',
    'drf_yasg',
    'ckeditor',
    'ckeditor_uploader',
    'embed_video',
    'main',
    'program',
    'sermon',
    'rest_framework',
    'cloudinary',
    'corsheaders',
    'djangoql',
    'import_export',
    'fontawesomefree'
]



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', #new
    # 'core.middleware.AdminCORSMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, '../locale')
]

LANGUAGE_CODE = 'en'



TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# SECURE_SSL_REDIRECT = True
# # Configure the SECURE_HSTS_INCLUDE_SUBDOMAINS setting if needed.
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# # Include the SECURE_HSTS_PRELOAD setting if you want to submit your site to the HSTS preload list.
# SECURE_HSTS_PRELOAD = True

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_ROOT = os.path.join(BASE_DIR, '../main\\static')
COMPRESS_ENABLED = True

STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)
# STATICFILES_DIRS = [os.path.join(BASE_DIR, '../main\\static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_uploads')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

####################################
    ##  CKEDITOR CONFIGURATION ##
####################################
# for uploading images and the rest using ckeditor
# https://django-ckeditor.readthedocs.io/en/latest/

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'my_uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 550,
    },
}


###################################
    ##  TAG CASE SENSITIVE ##
#################################### 
TAGGIT_CASE_INSENSITIVE = True

###############   JAZZMIN SETTINGS ###################
# UNFOLD = {
#     "SITE_TITLE": "MFM Admin",
#     "SITE_HEADER": "MFMCAM",
#     "SITE_URL": "/",
#     # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
#     "SITE_ICON": {
#         "light": lambda request: static("img/logo.png"),  # light mode
#         "dark": lambda request: static("img/logo.png"),  # dark mode
#     },
#     # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
#     "SITE_LOGO": {
#         "light": lambda request: static("img/logo.png"),  # light mode
#         "dark": lambda request: static("img/logo.png"),  # dark mode
#     },
#     "SITE_SYMBOL": "speed",  # symbol from icon set
#     "SHOW_HISTORY": True, # show/hide "History" button, default: True
#     "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
#     "ENVIRONMENT": "sample_app.environment_callback",
#     "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
#     "LOGIN": {
#         "image": lambda request: static("img/logo.png"),
#         "redirect_after": lambda request: reverse_lazy("admin:APP_MODEL_changelist"),
#     },
#     "STYLES": [
#         lambda request: static("css/style.css"),
#     ],
#     "SCRIPTS": [
#         lambda request: static("js/script.js"),
#     ],
#     "COLORS": {
#         "primary": {
#             "50": "250 245 255",
#             "100": "243 232 255",
#             "200": "233 213 255",
#             "300": "216 180 254",
#             "400": "192 132 252",
#             "500": "168 85 247",
#             "600": "147 51 234",
#             "700": "126 34 206",
#             "800": "107 33 168",
#             "900": "88 28 135",
#             "950": "59 7 100",
#         },
#     },
#     "EXTENSIONS": {
#         "modeltranslation": {
#             "flags": {
#                 "en": "🇬🇧",
#                 "fr": "🇫🇷",
#                 "nl": "🇧🇪",
#             },
#         },
#     },
#     "SIDEBAR": {
#         "show_search": True,  # Search in applications and models names
#         "show_all_applications": True,  # Dropdown with all applications and models
#         "navigation": [
#             {
#                 "title": _("Navigation"),
#                 "separator": True,  # Top border
#                 "items": [
#                     {
#                         "title": _("Dashboard"),
#                         "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
#                         "link": reverse_lazy("admin:index"),
#                         "badge": "sample_app.badge_callback",
#                         "permission": lambda request: request.user.is_superuser,
#                     },
#                     {
#                         "title": _("Users"),
#                         "icon": "people",
#                         "link": reverse_lazy("admin:users_user_changelist"),
#                     },
#                 ],
#             },
#         ],
#     },
#     "TABS": [
#         {
#             "models": [
#                 "app_label.model_name_in_lowercase",
#             ],
#             "items": [
#                 {
#                     "title": _("Your custom title"),
#                     "link": reverse_lazy("admin:app_label_model_name_changelist"),
#                     "permission": "sample_app.permission_callback",
#                 },
#             ],
#         },
#     ],
# }


# def dashboard_callback(request, context):
#     """
#     Callback to prepare custom variables for index template which is used as dashboard
#     template. It can be overridden in application by creating custom admin/index.html.
#     """
#     context.update(
#         {
#             "sample": "example",  # this will be injected into templates/admin/index.html
#         }
#     )
#     return context


# def environment_callback(request):
#     """
#     Callback has to return a list of two values represeting text value and the color
#     type of the label displayed in top right corner.
#     """
#     return ["Production", "danger"] # info, danger, warning, success


# def badge_callback(request):
#     return 3

# def permission_callback(request):
#     return request.user.has_perm("sample_app.change_model")



###############   JAZZMIN SETTINGS ###################
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "MFM Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "MFMCAM",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "MFMCAM",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "img/logo.png",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "img/logo.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "img/logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to MFMCAM WEBSITE",

    # Copyright on the footer
    "copyright": "Acme MooglesMe",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": 'img/logo.png',
}


