from django.contrib import admin

from learning_logs.models import Topic
admin.site.register(Topic) 
# imports "Topic", tell Django to manage model through admin site
