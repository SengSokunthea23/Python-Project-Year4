from django.shortcuts import render
from my_app.models import Category

# Create your views here.
def index(request):
    categories = Category.objects.all()
    data={"categories":categories}
    print(categories)
    return render(request,"pages/categories/index.html",data)

