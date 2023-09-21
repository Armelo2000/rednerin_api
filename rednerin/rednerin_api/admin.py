from django.contrib import admin

# Register your models here.

from . models import *

class UrlInline(admin.TabularInline):
    model = Url
    extra = 1

class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork
    extra = 1

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class Inliner(admin.ModelAdmin):
    inlines = [UrlInline, SocialNetworkInline, PhotoInline, VideoInline]

admin.site.register(Speacher, Inliner)

#admin.site.register(Speacher)
admin.site.register(SpeacherInfo)
#admin.site.register(Subject)
#admin.site.register(Url)
#admin.site.register(SocialNetwork)
#admin.site.register(Photo)
#admin.site.register(Video)
admin.site.register(Contact)


