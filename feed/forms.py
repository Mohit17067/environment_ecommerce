from django import forms
from .models import bidders, donators, service
from easy_maps.widgets import AddressWithMapWidget


all_categories = (('Cleaning of River', 'Cleaning of river'),
			('Plantation of Trees', 'Plantation of Trees'),
			('Maintenance of an Area', 'Maintenance of an Area'),
			('Mosquito-Killing', 'Mosquito-Killing'))


class donate_form(forms.Form):
	fund = forms.IntegerField()

class search_form(forms.Form):
	categories = forms.MultipleChoiceField(choices = all_categories, widget=forms.CheckboxSelectMultiple, 
    label="Choose Category", required=True, error_messages={'required': 'myRequiredMessage'})


class post_form(forms.Form, forms.ModelForm):
	categories = forms.MultipleChoiceField(choices = all_categories, widget=forms.CheckboxSelectMultiple, 
    label="Choose Category", required=True, error_messages={'required': 'myRequiredMessage'})
	estimate_budget = forms.IntegerField()
	address = forms.CharField(max_length=300, required=False)

	class Meta:
		model = service
		# widgets = {
        #         'address': AddressWithMapWidget({'class': 'vTextField'})
        #     }
		fields = ['title', 'content', 'categories', 'estimate_budget', 'expected_date_of_completion','service_pre_Img','address']


class provider_form(forms.ModelForm):
	budget = forms.IntegerField()
	date_of_completion = forms.DateField()

	class Meta:
		model = bidders
		fields = ['username','budget','date_of_completion','service']


