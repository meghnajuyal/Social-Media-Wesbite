from django.contrib import admin
from social import  models
from django.contrib.admin.options import ModelAdmin

# Register your models here.

class FollowUserAdmin(ModelAdmin):
    list_display=["profile","followed_by"]
    search_fields=["profile","followed_by"]
    list_filter=["profile","followed_by"]
admin.site.register(models.FollowUser,FollowUserAdmin)

class PostAdmin(ModelAdmin):
    list_display=["subject","cr_date","uploaded_by"]
    search_fields=["subject","msg","cr_date"]
    list_filter=["cr_date","uploaded_by"]

admin.site.register(models.Post,PostAdmin)

class ProfileAdmin(ModelAdmin):
    list_display=["name"]
    search_fields=["name","status","contact"]
    list_filter=["status","gender"]

admin.site.register(models.Profile,ProfileAdmin)

class CommentAdmin(ModelAdmin):
    list_display=["post","commented_by"]
    search_fields=["msg","post","commented_by"]
    list_filter=["cr_date","flag"]

admin.site.register(models.Comment,CommentAdmin)



class PostLikeAdmin(ModelAdmin):
    list_display=["post","liked_by"]
    search_fields=["post","liked_by"]
    list_filter=["cr_date"]

admin.site.register(models.PostLike,PostLikeAdmin)
