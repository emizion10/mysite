from django.db import models
from django.shortcuts import render,get_object_or_404

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class student(models.Model):
	stud = models.OneToOneField(User,on_delete=models.CASCADE)
	# sid=models.CharField(max_length=250)
	# psw=models.CharField(max_length=250)
	name=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	ph_no=models.CharField(max_length=11)
	bill = models.IntegerField(default=0)

	def __str__(self):
		return self.name

	def pay(self):
		self.bill = 0
		self.save()
# @receiver(post_save,sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         student.objects.create(stud=instance)
#     instance.student.save()


class ordercreated(models.Model):
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	status = models.BooleanField(default=False)
	i_id = models.ForeignKey('menu',on_delete=models.CASCADE)
	quantity_order = models.IntegerField()
	message = models.CharField(max_length=200)
	amount = models.IntegerField(default=0)
	enter_date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return self.message

	def pay(self):
		st = get_object_or_404(student,stud=self.owner)
		st.bill = st.bill + self.amount
		st.save()
		self.status=True
		self.save()


class menu(models.Model):

	item_name=models.CharField(max_length=100)
	qty=models.IntegerField()
	price=models.IntegerField()
	ordered = models.IntegerField(default=0)
	def __str__(self):
		return self.item_name


"""
class order(models.Model):
	order_id=models.IntegerField()
	item_id=models.ForeignKey(menu,on_delete=models.CASCADE)
	stud_id=models.ForeignKey(student,on_delete=models.CASCADE)
"""
class payment(models.Model):
	bill_id=models.IntegerField()
#	order_id=models.ForeignKey(order,on_delete=models.CASCADE)
	item_id=models.ForeignKey(menu,on_delete=models.CASCADE)
	std=models.ForeignKey(student,on_delete=models.CASCADE)
	amt=models.DecimalField(max_digits=10,decimal_places=2)
