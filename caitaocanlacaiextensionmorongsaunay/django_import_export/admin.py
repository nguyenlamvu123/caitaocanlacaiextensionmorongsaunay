from django.contrib import admin

# Register your models here.
from import_export import resources
from .models import Book
##from core.models import Book
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
##
class BookResource(resources.ModelResource):
    published = Field(attribute='published', column_name='published_date')
    class Meta:
        model = Book
        import_id_fields = ('isbn',)
        fields = ('id', 'name', 'price',)
        widgets = {
                'published': {'format': '%d.%m.%Y'},
                }
        #exclude = ('imported', )
        export_order = ('id', 'price', 'author', 'name')

    def dehydrate_full_title(self, book):
        return '%s by %s' % (book.name, book.author.name)

    #delete = fields.Field(widget=widgets.BooleanWidget())
    
    def for_delete(self, row, instance):
        return self.fields['delete'].clean(row)

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(Book, BookAdmin)
