from django.urls import path
from drill_app import views

urlpatterns = [
    path('', views.index, name='Catalogue'),
    path('book_rent', views.book_rent, name='RentedBooks'),
    path('book_rent_form', views.book_rent_form, name='BookRentForms'),
    path('book_buy', views.book_buy, name='BoughtBooks'),
    path('book_buy_form', views.book_buy_form, name='BookBuyForms'),
    path('book_sell', views.book_sell, name='SoldBooks'),
    path('book_sell_form', views.book_sell_form, name='BookSellForms'),
    path('search', views.search, name='Search'),
]
