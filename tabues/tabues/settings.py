"""
Django settings for tabues project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from .local_settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wr(ahz71x$9=(_#j(r7(qc&1ur^64x#nrd!$ej6+fbeo4_m_s!'


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'Blog',
	'colaborador',
	'Eventos',
	'recursos_educativos',
	'user',

	#third parties
	'ckeditor',
	'sorl.thumbnail',
	'taggit',
	'taggit_autosuggest',
	'location_field.apps.DefaultConfig',
]

AUTH_USER_MODEL = 'user.User'

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tabues.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'tabues.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-ni'

TIME_ZONE = 'America/Managua'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
   os.path.join(BASE_DIR, "static_media"),
)


CKEDITOR_UPLOAD_PATH = "uploads/"


CKEDITOR_CONFIGS = {
	'default': {
		'extraPlugins': ','.join([
			# 'image2',
			'uploadimage', # the upload image feature
			# your extra plugins here
			'div',
			'autolink',
			'embed',
			'autoembed',
			
			'autogrow',
			# 'devtools',
			'widget',
			'lineutils',
			'clipboard',
			'dialog',
			'dialogui',
			'elementspath'
		]),
		'toolbar': [
			{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ], 'items': [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ] },
			{ 'name': 'clipboard', 'groups': [ 'clipboard', 'undo' ], 'items': [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
			{ 'name': 'editing', 'groups': [ 'find', 'selection', 'spellchecker' ], 'items': [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ] },
			#{ 'name': 'forms', 'items': [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField' ] },
			'/',
			{ 'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ], 'items': [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ] },
			{ 'name': 'paragraph', 'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ], 'items': [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ] },
			{ 'name': 'links', 'items': [ 'Link', 'Unlink', 'Anchor' ] },
			{ 'name': 'insert', 'items': [ 'Image', 'Youtube', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe' ] },
			'/',
			{ 'name': 'styles', 'items': [ 'Styles', 'Format', 'Font', 'FontSize' ] },
			{ 'name': 'colors', 'items': [ 'TextColor', 'BGColor' ] },
			{ 'name': 'tools', 'items': [ 'Maximize', 'ShowBlocks', ] },
			 {
	}

		],
		'height': '300px',
		'width': 'auto',
	},

}

LOCATION_FIELD_PATH = STATIC_URL + 'location_field'

LOCATION_FIELD = {
	'map.provider': 'openstreetmap',
	'map.zoom': 15,

	'search.provider': 'nominatim',
	'search.suffix': '',

	# OpenStreetMap
	'provider.openstreetmap.max_zoom': 18,

	# misc
	'resources.root_path': LOCATION_FIELD_PATH,
	'resources.media': {
		'js': [
			LOCATION_FIELD_PATH + '/js/jquery.livequery.js',
			LOCATION_FIELD_PATH + '/js/form.js',
		],
	},
}

AUTH_USER_MODEL = 'user.User'












