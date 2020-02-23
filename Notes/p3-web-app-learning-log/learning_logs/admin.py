from django.contrib import admin

# import model(s) from an app,
# then tell Django to manage model through admin site
from learning_logs.models import Topic, Entry
admin.site.register(Topic) 
admin.site.register(Entry)