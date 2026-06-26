from django.shortcuts import render
from django.apps import apps

def recognize_digit(request):
    """view function that renders the upload.htlm page where the actual image processing occures"""
    return render(request, 'handwr_recognizer/handwr_recognizer/upload.html')
def home(request):
    """view function that renders the home intro page"""
    return render(request, 'handwr_recognizer/handwr_recognizer/home.html')
