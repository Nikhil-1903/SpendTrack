from django.db import models

# -----------------------------------------------------------------------------
# Expense Model
# -----------------------------------------------------------------------------
# A model represents a table in the database.
#
# Django will automatically create a table named:
#     expenses_expense
#
# Each variable below becomes a column in that table.
# -----------------------------------------------------------------------------

class Expense(models.Model):
    """
    Stores information about a single expense.
    Every object of this class corresponds to one row in the database.
    """

    # Title of the expense e.g. "Pizza", "Netflix", "Electricity Bill"
    
    title = models.CharField(max_length = 100)


    # Expense amount
    # DecimalField is preferred over FloatField for money to avoid precision errors.
    # max_digits = total number of digits
    # decimal_places = digits after the decimal point
    amount = models.DecimalField(max_digits=10, decimal_places = 2)

    # Category of the expense
    # Example: Food, travel, Shopping
    category = models.CharField(max_length = 50)

    #Date when the expense occured.
    date = models.DateField()

    # Optional notes
    # blank=True means the user may leave it empty.
    # TextField is used so we can add any long text with no limit.
    notes = models.TextField(blank = True)

    # This function controls how an Expense object appears
    # in the Django Admin panel and during debugging.
    def __str__(self):
        return self.title