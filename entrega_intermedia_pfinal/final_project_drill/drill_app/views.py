from django.http import HttpResponse
from django.shortcuts import render
from drill_app.models import BooksForRent, RentABook, BuyABook, SellABook
from drill_app.forms import RentABookForm, BuyABookForm, SellABookForm


def index(request):
	return render(request, 'drill_app/catalogue.html')

def book_rent(request):
    book_rent = RentABook.objects.all()

    context_dict = {
        'book_rent': book_rent
    }

    return render(
        request=request,
        context=context_dict,
        template_name="drill_app/book_rent.html"
    )


def book_rent_form(request):
    if request.method == 'POST':
    	rent_form = RentABookForm(request.POST)
    	if rent_form.is_valid():
            data = rent_form.cleaned_data
            book_rent = RentABook(
                name=data['name'],
                rented_date=data['rented_date'],
                
            )
            book_rent.save()

            book_rent = RentABook.objects.all()
            context_dict = {
                'book_rent': book_rent
            }
            return render(
                request=request,
                context=context_dict,
                template_name="drill_app/book_rent.html"
            )

    book_rent = RentABookForm(request.POST)
    context_dict = {
        'book_rent': book_rent
    }
    return render(
        request=request,
        context=context_dict,
        template_name='drill_app/book_rent_form.html'
    )


def book_buy(request):
    book_buy = BuyABook.objects.all()

    context_dict = {
        'book_buy': book_buy
    }

    return render(
        request=request,
        context=context_dict,
        template_name="drill_app/book_buy.html"
    )

def book_buy_form(request):
    if request.method == 'POST':
    	buy_form = BuyABookForm(request.POST)
    	if buy_form.is_valid():
            data = buy_form.cleaned_data
            book_buy = BuyABook(
                name=data['name'],
                amount=data['amount'],
                
            )
            book_buy.save()

            book_buy = BuyABook.objects.all()
            context_dict = {
                'book_buy': book_buy
            }
            return render(
                request=request,
                context=context_dict,
                template_name="drill_app/book_buy.html"
            )

    book_buy = BuyABookForm(request.POST)
    context_dict = {
        'book_buy': book_buy
    }
    return render(
        request=request,
        context=context_dict,
        template_name='drill_app/book_buy_form.html'
    )

def book_sell(request):
    book_sell = SellABook.objects.all()

    context_dict = {
        'book_sell': book_sell
    }

    return render(
        request=request,
        context=context_dict,
        template_name="drill_app/book_sell.html"
    )

def book_sell_form(request):
    if request.method == 'POST':
    	sell_form = SellABookForm(request.POST)
    	if sell_form.is_valid():
            data = sell_form.cleaned_data
            book_sell = SellABook(
                name=data['name'],
				genre=data['genre'],
                amount=data['amount'],
                
            )
            book_sell.save()

            book_sell = SellABook.objects.all()
            context_dict = {
                'book_sell': book_sell
            }
            return render(
                request=request,
                context=context_dict,
                template_name="drill_app/book_sell.html"
            )

    book_sell = SellABookForm(request.POST)
    context_dict = {
        'book_sell': book_sell
    }
    return render(
        request=request,
        context=context_dict,
        template_name='drill_app/book_sell_form.html'
    )

def search(request):
	if request.GET["text_search"]:
		search_param = request.GET["text_search"]
		book_sell = BooksForRent.objects.filter(name__contains=search_param)
		context_dict = {
            'book_sell': book_sell
        }
	return render(
        request=request,
        context=context_dict,
        template_name="drill_app/catalogue.html",
    )