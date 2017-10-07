from django.contrib import admin
from .models import Contacte

from import_export.admin import ImportExportModelAdmin

class BookAdmin(ImportExportModelAdmin):
    list_display   = ('id', 'nom', 'prenom', 'ville', 'date')
    list_filter    = ('nom','ville',)
    date_hierarchy = 'date'
    ordering       = ('date', 'nom' , 'ville' )
    search_fields  = ('nom', 'prenom' , 'date' , 'telephone' , 'mail' , 'ville')
    pass

"""
class ContacteAdmin(admin.ModelAdmin):
    list_display   = ('id', 'nom', 'prenom', 'ville', 'date')
    list_filter    = ('nom','ville',)
    date_hierarchy = 'date'
    ordering       = ('date', 'nom' , 'ville' )
    search_fields  = ('nom', 'prenom' , 'date' , 'telephone' , 'mail' , 'ville')
"""



#admin.site.register(Contacte , ContacteAdmin )
admin.site.register(Contacte , BookAdmin )
# Register your models here.




#class BookAdmin(ImportExportModelAdmin):
#    resource_class = BookResource
