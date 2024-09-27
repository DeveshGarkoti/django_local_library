from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)


class AuthorInstanceInline(admin.TabularInline):
    model = Book


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [
        'first_name',
        'last_name',
        ('date_of_birth','date_of_death')
    ]

    inlines = [AuthorInstanceInline]

# Register the main class with associated model
admin.site.register(Author, AuthorAdmin)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')

    inlines = [BookInstanceInline]

    def display_genre(self,obj):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in obj.genre.all()[:3])

    display_genre.short_description = 'Genre'





# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status', 'due_back', 'id','borrower' )
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability',{
            'fields':('status', 'due_back', 'borrower')
        })
    )
