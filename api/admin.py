from django.contrib import admin

# Register your models here.
# api/admin.py
from django.contrib import admin
from .models import Profile, Expertise, Project, Skill, Focus, Career

# Customizing the Admin Headers
admin.site.site_header = "DynoBIO Administration"
admin.site.site_title = "Mark Traverse Bio Portal"
admin.site.index_title = "Welcome to your Bio Management"

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'location')


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('label',)
    search_fields = ('label',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('label', 'value')
    list_editable = ('value',) # Edit percentages directly from the list view
    sortable_by = ('value',)

@admin.register(Focus)
class FocusAdmin(admin.ModelAdmin):
    list_display = ('item', 'enabled', 'updated_at')
    list_filter = ('enabled',)
    list_editable = ('enabled',)

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('period', 'role', 'description')
    search_fields = ('period', 'role', 'description')
    list_filter = ('period',)

