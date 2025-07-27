from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def index(request):

    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    
    return render(
        request, 
        'contact/index.html', 
        context,
    )


def search(request):

    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            Q(name__icontains=search_value) |
            Q(lastname__icontains=search_value) |         
            Q(email__icontains=search_value) 
            ) \
        .order_by('-id') \
    
    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
    }
    
    return render(
        request, 
        'contact/index.html', 
        context,
    )


def contact(request, contact_id):

    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    contact_name = f'{single_contact.name} {single_contact.lastname} - '
    context = {
        'contact': single_contact,
        'site_title': contact_name
    }
    
    return render(
        request, 
        'contact/contact.html', 
        context,
    )
