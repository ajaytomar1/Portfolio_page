from django.contrib import admin
from . models import*
# Register your models here.

#
admin.site.register(Home)

#about
class profileInline(admin.TabularInline):
    model= Profile
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines=[
        profileInline,
    ]
    
#skills
class SkillsInline(admin.TabularInline):
    model= Skills
    extra= 2


@admin.register(Category)
class CatogaryAdmin(admin.ModelAdmin):
    inlines=[
        SkillsInline,
    ]

#portfolio
admin.site.register(Portfolio)

admin.site.register(Contact)
