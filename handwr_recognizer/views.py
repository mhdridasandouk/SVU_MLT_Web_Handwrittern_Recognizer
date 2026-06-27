from django.shortcuts import render
from django.apps import apps
from .preprocess import detect_and_predict

def recognize_digit(request):
    """view function that renders the upload.htlm page where the  image processing occures"""
    digits = None
    error = None
    annotated_img = None
    show_image = False

    if request.method == 'POST' and request.FILES.get('digit_image'):
        image_file = request.FILES['digit_image']
        action = request.POST.get('action', '')

        config = apps.get_app_config('digit_reco_app')
        model = config.model          # the loaded Pipeline

        try:
            with_image = (action == 'show_image')
            digits, annotated_img = detect_and_predict(
                image_file, model, return_image=with_image
            )
            if with_image:
                show_image = True
        except Exception as e:
            error = f"Processing error: {e}"

    context = {
        'digits': digits,
        'error': error,
        'annotated_img': annotated_img,
        'show_image': show_image,
    }
    return render(request, 'handwr_recognizer/upload.html', context)
def home(request):
    """view function that renders the home intro page"""
    return render(request, 'handwr_recognizer/home.html')