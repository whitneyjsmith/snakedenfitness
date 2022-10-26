from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

#from .forms import NameForm
from .forms import MealForm
from .models import Meal


@login_required
def diet_home(request):
    return render(request, 'diet/diet_home.html', {})


@login_required
def dietitian_home(request):
    return render(request, 'diet/dietitian_home.html', {})

@login_required
def meal_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MealForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Meal()
            obj.name = form.cleaned_data['name']
            obj.meal_type = form.cleaned_data['meal_type']
            obj.calories = form.cleaned_data['calories']
            obj.carbs = form.cleaned_data['carbs']
            obj.sugars = form.cleaned_data['sugars']
            obj.protein = form.cleaned_data['protein']
            obj.user = User(request.user.id)
            obj.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/diet/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MealForm()

    return render(request, 'diet/meal_form.html', {'form': form})


@login_required
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()


@login_required
def user_meal_data(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'diet/meal_log.html', {'meals': meals})

@login_required
def trainer_meal_data(request):
    meals = Meal.objects.all()
    return render(request, 'diet/pro_meal_log.html', {'meals': meals})
