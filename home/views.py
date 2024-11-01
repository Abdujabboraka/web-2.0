from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib import messages
from .models import Product, Category, Image, Review
# Create your views here.


def homepage(request):
    if request.method == 'POST':
        # Handling the review form submission
        rate = request.POST.get('rate')
        content = request.POST.get('content')
        author = request.user
        address = request.POST.get('address')
        author_photo = request.POST.get('author_photo')

        # Create a new review
        Review.objects.create(rate=rate, content=content, author=author, address=address, author_photo=author_photo)
        messages.success(request, "sizning Sharxingiz saqlandi Raxmat 😊 !")
        return redirect('homepage')  # Redirect to avoid resubmission on page refresh

    # Handling GET request
    categories = Category.objects.exclude(photo='')
    products = Product.objects.all()
    reviews = Review.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'reviews': reviews,
    }

    return render(request, 'index.html', context)


def detail(request):

    return render(request, 'ShopApp/detail.html')