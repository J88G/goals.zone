from django import forms
from django.contrib import admin

from .models import Webhook, Tweet


class WebhookAdminForm(forms.ModelForm):
    class Meta:
        model = Webhook
        fields = ['title',
                  'destination',
                  'event_type',
                  'webhook_url',
                  'message',
                  'link_regex',
                  'author_filter',
                  'include_tournaments',
                  'include_categories',
                  'include_teams',
                  'exclude_tournaments',
                  'exclude_categories',
                  'exclude_teams']
        widgets = {
            'message': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }


class WebhookAdmin(admin.ModelAdmin):
    filter_horizontal = ['include_tournaments',
                         'include_categories',
                         'include_teams',
                         'exclude_tournaments',
                         'exclude_categories',
                         'exclude_teams']
    form = WebhookAdminForm


class TweetAdminForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['title',
                  'event_type',
                  'consumer_key',
                  'consumer_secret',
                  'access_token_key',
                  'access_token_secret',
                  'message',
                  'link_regex',
                  'author_filter',
                  'include_tournaments',
                  'include_categories',
                  'include_teams',
                  'exclude_tournaments',
                  'exclude_categories',
                  'exclude_teams']
        widgets = {
            'message': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }


class TweetAdmin(admin.ModelAdmin):
    form = TweetAdminForm


admin.site.register(Webhook, WebhookAdmin)
admin.site.register(Tweet, TweetAdmin)
