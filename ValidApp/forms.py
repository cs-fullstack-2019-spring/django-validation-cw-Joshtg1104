from django import forms
from .models import CarModel


class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = "__all__"
        labels = {"mpg": "MPG (Miles Per Gallon"}

    def clean_mpg(self):
        milesData= self.cleaned_data["mpg"]
        if milesData < 20:
            raise forms.ValidationError("That's less than a truck!!!")
        elif milesData > 500:
            raise forms.ValidationError("That's impossible (in 2019)")
        return milesData

    def clean_year(self):
        yearData = self.cleaned_data["year"]
        if yearData < 2019:
            raise forms.ValidationError("That's not new!!!")
        return yearData


# Miles per gallon less than 20. Say"That's less than a truck!!!"
# Miles per gallon that's greater than 500. Say "That's impossible (in 2019)
# Any year that's less than 2019. Say "That's not new!!!"
