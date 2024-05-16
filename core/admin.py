from django.contrib import admin
from .models import Service, Job, Team, Feature


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'status', 'created_at', 'updated_at')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job', 'status', 'created_at', 'updated_at')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'status', 'created_at', 'updated_at')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'updated_at')
