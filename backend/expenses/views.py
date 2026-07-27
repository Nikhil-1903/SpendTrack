from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello from Django!")




def expense_list(request):
    # Fetch all expenses from the database.

    # Get all expense objects from the database.
    expenses = Expense.objects.all()

    # This string will hold the response we send to the browser.
    response = ""

    # Loop through every expense object.
    for expense in expenses:
        response += expense.title + "<br>"

    # Send the final text back to the browser.
    return render(request, "expenses/expense_list.html", {"expenses" : expenses})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        # If user gives invalid values we not refresh it in the form to avoid rewrite all form again.

        if form.is_valid():
            form.save()
            return redirect("expense_list")

    else:
        form = ExpenseForm()

    return render(
        request,
        "expenses/add_expense.html",
        {"form": form},
    )
