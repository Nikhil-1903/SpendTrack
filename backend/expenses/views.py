from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ExpenseSerializer

def hello(request):

    return HttpResponse("Hello from Django!")




def expense_list(request):
    # Fetch all expenses from the database.

    # Get all expense objects from the database.
    # expenses = Expense.objects.all()

    category = request.GET.get("category")

    if category:
        expenses = Expense.objects.filter(category__icontains=category)
    else:
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


def edit_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)  
        # instance parameter makes it UPDATE instead of INSERT.

        if form.is_valid():
            form.save()
            return redirect("expense_list")

    else:
        form = ExpenseForm(instance=expense)

    return render(
        request,
        "expenses/add_expense.html",
        {"form": form},
    )


def delete_expense(request, id):
    # Fetch the expense object that the user wants to delete.
    expense = Expense.objects.get(id=id)

    # Show the confirmation page when the user first clicks Delete.
    if request.method == "GET":
        return render(
            request,
            "expenses/delete_expense.html",
            {"expense": expense},
        )

    # The user confirmed deletion by submitting the form.
    # Remove the expense from the database.
    expense.delete()

    # After deleting, return to the expense list.
    return redirect("expense_list")

print("Views module loaded")
print(delete_expense)

@api_view(["GET", "POST"])
def expense_api(request):
    # Fetch all expenses from the database.
    # ----------------  GET  ----------------
    if request.method == "GET":
        expenses = Expense.objects.all()

        # Convert Expense objects into JSON.
        serializer = ExpenseSerializer(expenses, many = True)

        # Return the JSON response.
        return Response(serializer.data)

    # ----------------  POST  ----------------
    # The data= keyword switches the serializer into input/validation mode.
    serializer = ExpenseSerializer(data=request.data)

    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)

@api_view(["GET", "PUT", "DELETE", "PATCH"])
def expense_detail_api(request, id):

    # Fetch the expense using its ID.
    # expense = Expense.objects.get(id=id)
    expense = get_object_or_404(Expense, id=id)

    # ------------ GET ------------
    if request.method == "GET":
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    # ------------ PUT ------------
    if request.method == "PUT":
        serializer = ExpenseSerializer(
            expense,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    # ------------ PATCH ------------
    if request.method == "PATCH":
        serializer = ExpenseSerializer(
            expense,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    # ------------ DELETE ------------
    if request.method == "DELETE":
        # Delete the existing expense from the database.
        expense.delete()

        # 204 = successful request, no response body.
        return Response(status=204)