from django.shortcuts import render
from django.http import HttpResponse 
from .models import Staff
from .models import Position
from django.shortcuts import redirect,get_object_or_404
import sweetify

def staff_list(request):
    return render(request, "pages/staff/index.html", {
        'staffs': Staff.objects.all()
    }) 

def staff_create(request):
    return render(request, "pages/staff/create.html",{
        "positions" : Position.objects.all()
    })

def staff_store(request):
    if request.method == "POST":
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        gender = request.POST.get("gender")
        date_of_birth = request.POST.get("date_of_birth")
        position_id = request.POST.get("position")
        # Add other fields as needed
        Staff.objects.create(
            last_name=last_name,
            first_name=first_name,
            gender=gender,
            date_of_birth=date_of_birth,
            position_id=position_id
        )
        sweetify.success(request, "Staff created successfully!")
        return redirect("staffs")
    return redirect("staffs")

def staff_edit(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    return render(request, "pages/staff/edit.html", {
        "staff": staff,
        "positions": Position.objects.all()
    })

def staff_update(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    if request.method == "POST":
        staff.last_name = request.POST.get("last_name")
        staff.first_name = request.POST.get("first_name")
        staff.gender = request.POST.get("gender")
        staff.date_of_birth = request.POST.get("date_of_birth")
        position_id = request.POST.get("position")
        if position_id:
            staff.position_id = position_id
        # Update other fields as needed
        staff.save()
        sweetify.success(request, "Staff updated successfully!")
        return redirect("staffs")
    return redirect("staffs")

def staff_delete(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    staff.delete()
    sweetify.success(request, "Staff deleted successfully!")
    return redirect("staffs")

def staff_detail(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    return render(request, "pages/staff/detail.html", {"staff": staff})