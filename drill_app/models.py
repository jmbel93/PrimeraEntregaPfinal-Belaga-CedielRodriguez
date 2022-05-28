from django.db import models


class BooksForRent(models.Model):
    name = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)


class BooksForSale(models.Model):
    name = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    amount = models.IntegerField()


class RentABook(models.Model):
    name = models.CharField(max_length=40)
    rented_date = models.DateField()

class BuyABook(models.Model):
    name = models.CharField(max_length=40)
    amount = models.IntegerField()

class SellABook(models.Model):
    name = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    amount = models.IntegerField()