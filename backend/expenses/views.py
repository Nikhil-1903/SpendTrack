from django.shortcuts import render
from .models import Expense
# -------------------------------------------------------------------------
# View: hello
#
# A view is a Python function that receives an HTTP request
# and returns an HTTP response.
#
# request  -> Information sent by the browser.
# response -> Information sent back to the browser.
# -------------------------------------------------------------------------

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
    if request.method == "GET":
        return render(request, "expenses/add_expense.html")

    elif request.method == "POST":
        return HttpResponse("Saving Expense")