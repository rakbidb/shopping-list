from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Rakha Abid Bangsawan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)