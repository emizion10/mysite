from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse
from .models import menu,student,payment,ordercreated
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.views.generic import ListView,DetailView,CreateView,UpdateView
import datetime


def about(request):
  return render(request,"about.html",{})
def login(request):
  return render(request,"login.html",{})

class CreateMenu(CreateView):
    model=menu

    def get_success_url(self):
        return reverse('manage_menu')
    form_class = MenuForm
    template_name = 'new_menu.html'

class ManageMenu(ListView):
     context_object_name='menu_list'
     model= menu
     def get_queryset(self):

        return menu.objects.all()

     template_name= 'manage_menu.html'

class UpdateMenu(UpdateView):
    model = menu
    fields = ['item_name','qty','price']
    template_name= 'update_menu.html'

    def get_success_url(self):
        return reverse('manage_menu')



class ManageStudents(ListView):
    context_object_name = 'student_list'
	# model=student
    def get_queryset(self):
        return student.objects.all()
    template_name = 'manage_students.html'

class StudentProfile(DetailView):
    model = student
    context_object_name='student'
    template_name= 'student_profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(StudentProfile, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['order_list'] = ordercreated.objects.filter(owner=self.object.stud)
        return context

    # def get_object(self):
    #    std = get_object_or_404(student,pk=self.kwargs['pk'])
    #    # fee_paid.pay_date = datetime.date.today()
    #    # fee_paid.save()
    #    std.pay()
    #    return std


# def payfees(request,pk):
#
#     std = student.objects.get(pk=pk)
#     std.pay()
#     ord = ordercreated.objects.filter(owner=std.stud)
#
#     return render(request,'student_profile.html',{'student':std,'order_list':ord})
#



class ProfileView(ListView):
    context_object_name='order_list'
    model=ordercreated
    def get_queryset(self):
        return ordercreated.objects.filter(owner=self.request.user).order_by('-enter_date')
    template_name= 'profile.html'
    paginate_by = 6

class ManageOrders(ListView):
    context_object_name='order_list'
    model=ordercreated
    def get_queryset(self):
        return ordercreated.objects.filter(enter_date=datetime.date.today(),status=False)
    template_name= 'vo.html'

class OrderDetail(DetailView):
    model = ordercreated
    context_object_name='n'
    def get_object(self):
       order = get_object_or_404(ordercreated,pk=self.kwargs['pk'])
       # fee_paid.pay_date = datetime.date.today()
       # fee_paid.save()
       order.pay()
       return order
       # return Fees.objects.filter(pk=self.kwargs['pk'])
    template_name= 'order_detail.html'


def placeorder(request):
	m_list = menu.objects.all()

	if request.method == "POST":
		form = ordernow(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			avail = form.cleaned_data['i_id'].qty

			req = form.cleaned_data['quantity_order']
			if (req>avail):
				messages.success(request,'enter valid no of item less than max limit')
			else:
				m = menu.objects.get(id=form.cleaned_data['i_id'].id)
				m.qty = m.qty - req
				pri = m.price
				f.amount = pri*req
				m.save()
				print(avail,req)
				f.owner = request.user
				f.save()
	else :
		form = ordernow()
	return render(request,'order.html',{'form':form,'m_list':m_list})




class MenuList(ListView):
	context_object_name = 'menu_list'
	model = menu
	template_name = 'home.html'

class MList(ListView):
	context_object_name = 'm_list'
	model = menu
	template_name = 'order.html'
