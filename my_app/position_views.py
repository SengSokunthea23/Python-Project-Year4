from django.shortcuts import render
from django.http import HttpResponse 
from .models import Position
from django.shortcuts import redirect,get_object_or_404
import sweetify

# def home(request):
#     return render(request,"index.html")
# def content(request):
#     return render(request,"pages/content.html")

# def categories(request): 
#     return render(request, "pages/categories/index.html", {
#         'categories': Category.objects.all()
#     })
    
# def create_category(request):
#     return render(request,"pages/categories/create.html")

# def store_category(request): 
#     if request.method == 'POST': 
#         name = request.POST.get('name')
#         status = request.POST.get('status')
#         if Category.objects.filter(name=name).exists():
#             sweetify.error(request, 'Category with this name already exists')
#             return redirect('category-create')
#         Category.objects.create(name=name, status=status) 
#         sweetify.success(request, 'Created Successfully')
#     return redirect('categories')

# def edit_category(request, category_id):
#     category = Category.objects.get(id=category_id) 
#     return render(request, "pages/categories/edit.html", {
#         'category': category
#     })
    
# def update_category(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
    
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         status = request.POST.get('status')
#         if name and status:
#             category.name = name
#             category.status = status
#             category.save()
#         sweetify.success(request, 'Update Successfully') 
#         return redirect('categories')
 
#     return redirect('category-edit', category_id=category.id)

# def delete_category(request,category_id):
#     category = get_object_or_404(Category, pk=category_id)
#     category.delete() 
#     sweetify.success(request, 'Deleted Successfully( ͡~ ͜ʖ ͡°)') 
#     return redirect('categories')


def position_list(request):
    return render(request, "pages/position/index.html", {
        'positions': Position.objects.all()
    }) 
    
def position_create(request, id=None):
    
    return render(request, "pages/position/create.html", {'id': id})
    
def position_edit(request, id=None):
    position = Position.objects.get(id=id)  
    return render(request, "pages/position/index.html", {
        'position': position
    }) 
def position_update(request,id):
    
    
    
    position = get_object_or_404(Position, pk=id)

    if request.method == 'POST':
        position_name = request.POST.get('position_name')

        if position_name:
            position.position_name = position_name
            position.save()
            sweetify.success(request, 'Update Successfully')
            return redirect('positions')
        else:
            sweetify.error(request, 'Position name is required')

    return render(request, "pages/position/edit.html", {
        'position': position
    })

def position_store(request,id=None):
    if request.method == 'POST': 
         name = request.POST.get('position_name') 
         if Position.objects.filter(position_name=name).exists():
             sweetify.error(request, 'Category with this name already exists')
             return redirect('position-create')
         Position.objects.create(position_name=name) 
         sweetify.success(request, 'Created Successfully')
    return redirect('positions')
        
def destroy(request,position_id):
    position = get_object_or_404(Position, pk=position_id)
    position.delete() 
    sweetify.success(request, 'Deleted Successfully( ͡~ ͜ʖ ͡°)') 
    return redirect('positions')

def  position_save(request):
    print(request)