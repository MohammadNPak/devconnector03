from django.contrib import admin
from . import models
# Register your models here.


# admin.site.register(models.User)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass 
@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Github)
class GithubAdmin(admin.ModelAdmin):
    pass

    