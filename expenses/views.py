from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date
import requests
from datetime import datetime

from .models import Expense
from .forms import ExpenseForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages

import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Expense

@login_required
def home(request):
    expenses = Expense.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/home.html', {
        'expenses': expenses,
        'form': form
    })


@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    expense.delete()
    return redirect('home')





@login_required
def summary(request):
    user = request.user

    # Handle month filter
    month_param = request.GET.get("month")

    expenses = Expense.objects.filter(user=user)

    if month_param:
        year, month = map(int, month_param.split("-"))
        expenses = expenses.filter(date__year=year, date__month=month)

    # Category-wise totals
    category_summary = (
        expenses
        .values("category")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )

    # Monthly total (filtered)
    monthly_total = expenses.aggregate(total=Sum("amount"))["total"] or 0

    # Top category
    top_category = category_summary[0] if category_summary else None

    month_str = request.GET.get("month")
    selected_month = None

    if month_str:
        selected_month = datetime.strptime(month_str, "%Y-%m")

    return render(request, 'expenses/summary.html', {
        'category_summary': category_summary,
        'monthly_total': monthly_total,
        'category_count': category_summary.count(),
        'top_category': top_category,
        'selected_month': selected_month,
    })


@login_required
def flask_summary(request):
    user_id = request.user.id
    response = requests.get(f'http://127.0.0.1:5000/summary/{user_id}')
    data = response.json()

    return render(request, 'expenses/flask_summary.html', {
        'monthly_total': data['monthly_total'],
        'categories': data['categories']
    })

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        password = request.POST.get('password')

        if request.user.check_password(password):
            user = request.user
            logout(request)
            user.delete()
            messages.success(request, "Your account has been deleted.")
            return redirect('login')
        else:
            messages.error(request, "Incorrect password.")

    return render(request, 'registration/delete_account.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def account_settings(request):
    return render(request, 'expenses/account_settings.html')

@login_required
def export_expenses_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Category', 'Amount'])

    expenses = Expense.objects.filter(user=request.user)

    for e in expenses:
        writer.writerow([
            e.date,
            e.category,
            e.amount
        ])

    return response

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    expense.delete()
    return redirect('home')
