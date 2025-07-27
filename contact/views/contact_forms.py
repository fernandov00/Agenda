from django.shortcuts import render
from contact.forms import ContactForm


def create(request):
    search = request.POST.get('first-name')
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            
        return render(
            request, 
            'contact/create.html', 
            context,
        )
    
    context = {
        'form': ContactForm
    }
    return render(
            request, 
            'contact/create.html', 
            context,
        )