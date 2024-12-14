from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")

# from django.db import models
# from django.contrib.auth.models import User
# class Receipe(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     receipe_name = models.CharField(max_length=100)
#     receipe_description = models.TextField()
#     receipe_image = models.ImageField(upload_to=1)
#     receipe_view_count = models.PositiveIntegerField(default=1)
# from django.shortcuts import render, redirect
# from .models import Receipe

