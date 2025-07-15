
from django.contrib import admin # type: ignore
from django.urls import path  # type: ignore
from my_app import views
from my_app import position_views
from my_app import staff_views


urlpatterns = [
    path("", views.home),
    path("content", views.content),
    
    #categories
    path("categories", views.categories, name="categories"),
    path("category/create", views.create_category, name="category-create"),
    path("category/store", views.store_category, name="categories-store"),
    path("category/edit/<int:category_id>", views.edit_category, name="category-edit"),
    path("category/update/<int:category_id>", views.update_category, name="category-update"),
    path("category/delete/<int:category_id>", views.delete_category, name="category-delete"),
    
    #product
    path("product", views.categories, name="categories"),
    path("product/create", views.create_category, name="category-create"),
    path("product/store", views.store_category, name="categories-store"),
    path("product/edit/<int:category_id>", views.edit_category, name="category-edit"),
    path("product/update/<int:category_id>", views.update_category, name="category-update"),
    path("product/delete/<int:category_id>", views.delete_category, name="category-delete"),
    
    # position
    path("positions", position_views.position_list, name="positions"),
    path("position_create", position_views.position_create, name="position-create"),
    path("position_store", position_views.position_store, name="position-store"), 
    path("position_edit/<int:id>", position_views.position_edit, name="position-edit"),
    path("position_update/<int:id>", position_views.position_update, name="position-update"),
    path("position_delete/<int:position_id>", position_views.destroy, name="position-delete"),
    
    # staff
    path("staffs", staff_views.staff_list, name="staffs"),
    path("staffs_create", staff_views.staff_create, name="staff-create"),
    path("staffs_store", staff_views.staff_store, name="staff-store"),
    path("staffs_edit/<int:staff_id>", staff_views.staff_edit, name="staff-edit"),
    path("staffs_update/<int:staff_id>", staff_views.staff_update, name="staff-update"),
    path("staffs_delete/<int:staff_id>", staff_views.staff_delete, name="staff-delete"),
    path("staff/<int:staff_id>", staff_views.staff_detail, name="staff-detail"),
]
