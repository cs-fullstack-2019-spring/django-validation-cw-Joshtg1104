from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CarModel
from .forms import CarForm


# Create your views here.
#functions registers car info but I couldn't get the transition to work in time
def index(request):
    if (request.method == "POST"):
        form = CarForm(request.POST)
        if (form.is_valid()):
            CarModel.objects.create(make=request.POST["make"], model=request.POST["model"], year=request.POST["year"],
                                    mpg=request.POST["mpg"])
        else:
            context = {
                "error": form.errors,
                "form": form,
                "allCars": CarModel.objects.all()
            }
            return render(request, "ValidApp/car_registry.html", context)
    context = {
        "allCars": CarModel.objects.all(),
        "form": CarForm()
    }
    return render(request, "ValidApp/car_registry.html", context)
