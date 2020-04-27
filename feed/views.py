from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django import forms
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.views.generic.edit import FormView, FormMixin
from .models import service, bidders, donators
from django.contrib.auth.models import User
from .forms import provider_form, post_form, search_form
from bootstrap_datepicker_plus import DatePickerInput


# all_tags = {'cleaning':'Cleaning',
# 			'planting': 'Planting',
# 			'maintenance': 'Maintenance',
# 			'grounds': 'Grounds',
# 			'parks': 'Parks',
# 			'lakes': 'Lakes',
# 			'mosquito-killing': 'Mosquito-killing'}

all_tags = ['cleaning','planting','maintenance','grounds','parks','lakes','mosquito-killing']

def home(request):

	# context = {'posts':posts}
	context = {'posts':service.objects.all()}
	return render(request,'feed/home.html', context)         # Inside the template directory.
															# the argument context now will be accessible in the template html file.


class PostListView(FormMixin, ListView):
	model = service
	template_name = 'feed/home.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5
	form_class = search_form

	def get_queryset(self):
		return service.objects.filter(status="Need Help").order_by('-date_of_creation')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tags'] = all_tags
		return context



	# def form_valid(self,form):
	# 	tags = form.instance.tags
	# 	# context['tags'] = tags
	# 	# print(context)
	# 	print(tags)
	# 	return super().form_valid(form)
	# context = {'posts':service.objects.all().order_by('-date_of_creation') , 'tags':super(self).get_context_data()}

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(PostListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	posts = service.objects.all().order_by('-date_of_creation')
	# 	context = super(self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	# for tags in self.get_form().cleaned_data.get('tags'):
	# 	# 	print(tags)
	# 	context['tags'] = context
	# 	context['posts'] = posts
	# 	print(context['tags'])
	# 	return context



class UserPostListView(ListView):
	model = service
	template_name = 'feed/user_posts.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return service.objects.filter(created_by=user).order_by('-date_of_creation')


class ProviderPostListView(ListView):
	model = service
	template_name = 'feed/user_posts.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return service.objects.filter(provider=user).filter(~Q(status="Need Help")).order_by('-date_of_creation')


class TagPostListView(ListView):
	model = service
	template_name = 'feed/user_posts.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		tag=self.kwargs.get('text')
		# tag = get_object_or_404(post, username=self.kwargs.get('text'))
		return service.objects.filter(tags__name__in=[tag]).distinct().order_by('-date_of_creation')


class PostDetailView(DetailView):
    model = service
    template_name = "feed/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
	model = service
	template_name = 'feed/post_form.html'
	success_url = '/'
	form_class = post_form

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

	def get_form(self):
		form = super(PostCreateView, self).get_form()
		form.fields['expected_date_of_completion'].widget=forms.SelectDateWidget(attrs={'class':'form-group'},
			empty_label=("Choose Year", "Choose Month", "Choose Day"),years = ('2020','2021'))
		return form


class PostBidView(LoginRequiredMixin, CreateView):
	model = bidders
	fields = ['budget','date_of_completion']
	template_name = 'feed/post_form.html'

	def get_form(self):
		form = super(PostBidView, self).get_form()
		form.fields['date_of_completion'].widget=forms.SelectDateWidget(attrs={'class':'form-group'},
			empty_label=("Choose Year", "Choose Month", "Choose Day"),years = ('2020','2021'))
		return form

	def form_valid(self, form):
		# print(form.instance.budget)
		form.instance.username = self.request.user
		Service = get_object_or_404(service, id=self.kwargs.get('pk'))
		form.instance.service = service.objects.filter(id=Service.id).first()
		# print(self.object.budget)
		return super().form_valid(form)


class PostDonateView(LoginRequiredMixin, CreateView):
	model = donators
	fields = ['fund']
	template_name = 'feed/post_form.html'


	def form_valid(self, form):
		form.instance.username = self.request.user
		Service = get_object_or_404(service, id=self.kwargs.get('pk'))
		form.instance.service = service.objects.filter(id=Service.id).first()
		return super().form_valid(form)


class BiddersListView(ListView):
	model = bidders
	template_name = 'feed/post_bidders.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'bidders'
	paginate_by = 5

	def get_queryset(self):
		Service = get_object_or_404(service, id=self.kwargs.get('pk'))
		req_service = service.objects.filter(id=Service.id).first()
		return bidders.objects.filter(service=req_service)


class DonatorsListView(ListView):
	model = donators
	template_name = 'feed/post_donators.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'donators'
	paginate_by = 5

	def get_queryset(self):
		Service = get_object_or_404(service, id=self.kwargs.get('pk'))
		req_service = service.objects.filter(id=Service.id).first()
		return donators.objects.filter(service=req_service)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = service
	fields = ['title', 'content', 'tags', 'estimate_budget','expected_date_of_completion','service_pre_Img']
	template_name = 'feed/post_form.html'

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

	def get_form(self):
		form = super(PostUpdateView, self).get_form()
		form.fields['expected_date_of_completion'].widget=forms.SelectDateWidget(attrs={'class':'form-group'},
			empty_label=("Choose Year", "Choose Month", "Choose Day"),years = ('2020','2021'))
		return form

	def test_func(self):
		service = self.get_object()
		if self.request.user == service.created_by:
			return True
		return False


def PostAssignView(request, bid_id):
	cur_bidder = bidders.objects.get(id = bid_id)
	if (request.method == 'POST'):
		cur_bidder.got_assigned = True
		cur_bidder.save()
		cur_service = cur_bidder.service
		cur_service.status = "Assigned"
		cur_service.provider = cur_bidder.username
		cur_service.save()
		return HttpResponseRedirect('/')
	return render(request, 'feed/post_confirm_assign.html', {'bidder':cur_bidder})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = service
    success_url = '/'
    template_name = 'feed/post_confirm_delete.html'

    def test_func(self):
        service = self.get_object()
        if self.request.user == service.created_by:
            return True
        return False


# class PostCreateView(LoginRequiredMixin, CreateView):
# 	model = service
# 	fields = ['title', 'content', 'tag', 'estimate_budget']
# 	template_name = 'feed/post_form.html'

# 	def form_valid(self, form):
# 		form.instance.created_by = self.request.user
# 		return super().form_valid(form)



def about(request):
	context = {'title':'About'}
	return render(request,'feed/about.html',context)        # For rendering these, we need to add our app in installed apps in setting.py file 
													#inside the sample_project directory.

# def searchByTag(request):
# 	if request.method == "POST":
# 		form = search_form(request.POST)
# 		if form.is_valid():
# 			 tags = form.cleaned_data.get('tags')
# 			 return redirect('tag-posts', args=(tags[0]))
# 	else:
# 		form = search_form()
# 	print(form)
# 	return render(request,'feed/post_form.html',{'form':form})
# def bid(request):
# 	print("entered")
# 	if request.method == "POST":
# 		form = provider_form(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			form.instance.service = request.user
# 			messages.success(request,f'Account Created for {username}!')
# 			return redirect('feed-home')
# 	else:
# 		form = provider_form()
# 	return render(request,'users/post_bid.html',{'form':form})