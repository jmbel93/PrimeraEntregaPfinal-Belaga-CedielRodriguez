from django.contrib import admin
from drill_app.models import BooksForRent, BuyABook, RentABook, SellABook
admin.site.register(BooksForRent)
admin.site.register(BuyABook)
admin.site.register(RentABook)
admin.site.register(SellABook)
