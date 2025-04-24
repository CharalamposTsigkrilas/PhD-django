from django.contrib import admin
from phds.models import JournalPublication, ConferencePublication, Teaching, AnnualReport

# Register your models here.

admin.site.register(JournalPublication)
admin.site.register(ConferencePublication)
admin.site.register(Teaching)

admin.site.register(AnnualReport)