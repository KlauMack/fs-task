from django import forms

# Form to filter Recipe table
class RecipeFilterForm(forms.Form):
    title = forms.CharField(required=False)
    ingredients = forms.CharField(required=False)
    cooking_time = forms.DurationField(required=False)
