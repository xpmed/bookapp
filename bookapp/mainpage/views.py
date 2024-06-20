from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.template.loader import render_to_string

from .models import Book, Category, Review
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from .forms import BookForm
from django.template.context_processors import csrf
from decimal import Decimal
from django.http import HttpResponseForbidden


def home(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        'books': books,
        'categories': categories,
    }
    if 'search_button' in request.POST:
        search = request.POST.get('search_value')
        searched_books = books.filter(Q(title__contains=search) | Q(author__name__contains=search) | Q(author__surname__contains=search) | Q(category__category=search))
        context['books'] = searched_books
        context['searched'] = search
    if request.user.is_authenticated:
        context['userStatus'] = 'logged in'
    else:
        context['userStatus'] = 'not logged in'
    return render(request, 'mainpage/home.html', context)


def signup_page(request):
    context = {}
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            context['error'] = 'User already exist! Enter different username.'
            return render(request, 'mainpage/signup.html', context)
        except User.DoesNotExist:
            if request.POST['pass1'] != request.POST['pass2']:
                context['error'] = 'Passwords do not match! Enter the same passwords.'
                return render(request, 'mainpage/signup.html', context)
            else:
                user = User.objects.create_user(request.POST['username'], password=request.POST['pass1'])
                auth.login(request, user)
                return redirect('home_page')
    else:
        return render(request, 'mainpage/signup.html', context)

def login_page(request):
    context = {}
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home_page')
        else:
            context['error'] = 'Password or username are incorrect! try again.'
            return render(request, 'mainpage/login.html', context)
    else:
        return render(request, 'mainpage/login.html')


def logout_page(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home_page')


def get_raiting(request):
    # data = list(Book.objects.values_list('id', 'average_rating'))
    data = list(Book.objects.values())
    return JsonResponse({'data': list(data)})

def detail_view(request, id):
    context = {}
    obj = Book.objects.filter(id=id)
    reviews = Review.objects.filter(book__id=id)
    context['obj'] = obj[0]
    context['reviews'] = reviews
    if request.POST:
        rate = request.POST.get('rateValue', None)
        content = request.POST.get('contentValue', None)
        Review.objects.create(
            book=obj[0],
            content=content,
            raiting=rate,
            author=request.user,
        )
        if obj[0].average_rating:
            latest_rate = obj[0].average_rating
            av_rate = (latest_rate + Decimal(rate)) / 2
        else:
            av_rate = rate
        obj.update(average_rating=av_rate)
        reviews = Review.objects.filter(book__id=id)
        context['reviews'] = reviews
        return render(request, 'mainpage/detail.html', context)
    return render(request, 'mainpage/detail.html', context)


def get_reviews(request, id):
    data = list(Review.objects.filter(book__id=id).values())
    return JsonResponse({'data': list(data)})


def get_rating_s(request, id):
    data = Book.objects.filter(id=id)
    return JsonResponse({'average_rate': data[0].average_rating})


def add_book(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('mainpage/home.html')
        else:
            form = BookForm()
        return render(request, 'mainpage/add_book.html', {'form': form})
    else:
        return HttpResponseForbidden('Forbidden')

