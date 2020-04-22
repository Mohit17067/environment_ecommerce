from django import forms
from .models import bidders, donators, service


all_tags = (('cleaning', 'Cleaning'),
			('planting', 'Planting'),
			('maintenance', 'Maintenance'),
			('grounds', 'Grounds'),
			('parks', 'Parks'),
			('lakes', 'Lakes'),
			('mosquito-killing', 'Mosquito-killing'))


class search_form(forms.Form):
	tags = forms.MultipleChoiceField(choices = all_tags, widget=forms.CheckboxSelectMultiple, 
    label="Choose Tags", required=True, error_messages={'required': 'myRequiredMessage'})


class post_form(forms.Form, forms.ModelForm):
	tags = forms.MultipleChoiceField(choices = all_tags, widget=forms.CheckboxSelectMultiple, 
    label="Choose Tags", required=True, error_messages={'required': 'myRequiredMessage'})
	estimate_budget = forms.IntegerField()

	class Meta:
		model = service
		fields = ['title', 'content', 'tags', 'estimate_budget', 'expected_date_of_completion','service_pre_Img']


class provider_form(forms.ModelForm):
	budget = forms.IntegerField()
	date_of_completion = forms.DateField()

	class Meta:
		model = bidders
		fields = ['username','budget','date_of_completion','service']
