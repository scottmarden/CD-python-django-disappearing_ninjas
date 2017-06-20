# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

turtles = {
	'purple':'donatello',
	'blue': 'leonardo',
	'orange': 'michelangelo',
	'red': 'raphael',
}

# Create your views here.
def index(request):
	return render(request, 'turtle_app/index.html')

def ninjas(request):
	return render(request, 'turtle_app/ninjas.html')

def ninja_colors(request, color):
	print color
	if color in turtles:
		context = {
			'image_name': turtles[color]
			}
	else:
		context = {
			'image_name': 'notapril'
		}

	return render(request, 'turtle_app/ninja_colors.html', context)
