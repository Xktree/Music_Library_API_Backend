# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+*5f+^ueg=+k8c+5z+_ta_4moie#@z#l)35x5z9$l!+3*cqt^u'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
