from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class orderform(forms.ModelForm):
	class Meta:
		model = menu
		fields  = ('item_name','qty','price','ordered')



class MenuForm(forms.ModelForm):
    class Meta:
        model = menu
        fields = ('item_name','qty','price')

class SignUpForm(UserCreationForm):
    ph_no = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'name','email','ph_no', 'password1', 'password2', )
class ordernow(forms.ModelForm):
	class Meta:
		model = ordercreated
		fields = ('i_id','message','quantity_order',)
