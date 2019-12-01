from django.contrib import admin
from buzzword.user_admin_page import user_admin
from explore.models import Corpus


@admin.register(Corpus)
class CorpusAdmin(admin.ModelAdmin):
    list_display = ('slug',)

    def get_fields(self, request, obj):
        if request.user.is_superuser: 
            return super().get_fields(request, obj)
        else: # staff
            return ['disabled', 'desc', 'name']

@admin.register(Corpus, site=user_admin)
class CorpusUser(admin.ModelAdmin):
    list_display = ('slug',)
    fields = ['desc']
