# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k$0*h6g2%pa6v4k5w9w+yqvmq9s0!iuox6u1q^w@ddc$n)s*pd'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
