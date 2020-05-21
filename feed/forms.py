from django import forms
from .models import bidders, donators, service, feedback_mosquitokilling, completion_pondcleaning, completion_treeplantation, completion
from easy_maps.widgets import AddressWithMapWidget


all_categories = (('Pond Cleaning', 'Pond Cleaning'),
			('Tree Planting', 'Tree Planting'),
			('Maintenance of an Area', 'Maintenance of an Area'),
			('Mosquito-Killing', 'Mosquito-Killing'))

class donate_form(forms.Form):
	fund = forms.IntegerField()

class search_form(forms.Form):
	categories = forms.MultipleChoiceField(choices = all_categories, widget=forms.CheckboxSelectMultiple, 
    label="Choose Category", required=True, error_messages={'required': 'myRequiredMessage'})


class post_form(forms.Form, forms.ModelForm):
	categories = forms.ChoiceField(choices = all_categories,
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


# class completion_form(forms.ModelForm):

# 	class Meta:
# 		model = service
# 		fields = ['complete_info','service_post_Img']

class mosquitokilling(forms.ModelForm):
	quantity_applied = forms.IntegerField(label="Approx Quantity in ml")
	spray_used = forms.CharField(label="Name of the Spray Used")
	natural_repallant = forms.CharField(required=False,label="Natural Repallant Used (if any)")
	class Meta:
		model = feedback_mosquitokilling
		fields = ['spray_used','quantity_applied','eliminated_standing_water','natural_repallant','other_info','service_post_Img']


class pondcleaning(forms.ModelForm):

	class Meta:
		model = completion_pondcleaning
		fields = ['drainage_done','automatic_skimmer','pond_net_used','vaccum','beneficial_bacteria','algae_treatment','other_info','service_post_Img']


class treeplantating(forms.ModelForm):

	water_quantity = forms.IntegerField(label="Quantity of Water Used (in ml)")
	depth_dug = forms.IntegerField(label="Depth of the Soil Dug (in feet)")
	class Meta:
		model = completion_treeplantation
		fields = ['fertilizer_used','plant_variety','depth_dug','water_quantity','residential_obstruction','other_info','service_post_Img']

class otherservices(forms.ModelForm):

	class Meta:
		model = completion
		fields = ['other_info','service_post_Img']