from django.urls import path
from . import views

urlpatterns = [
    path("", views.expense_list, name="expense_list"),
    path("add/", views.add_expense, name="add_expense"),
    path("<int:id>/edit/", views.edit_expense, name="edit_expense"),
]