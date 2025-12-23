from django.contrib import admin
from .models import Contact, Feedback, Subscription, Camera

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company_name', 'website','message', 'created_at')
    search_fields = ('name', 'email', 'company_name', 'website','message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):  
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',) 

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)
    ordering = ('-subscribed_at',)
    
@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'is_high_quality', 'timestamp', 'image')
    list_filter = ('country', 'is_high_quality')
    search_fields = ('title', 'country')