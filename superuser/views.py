from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


# Create your views here.


def contact_list(request):
    contacts = Contact.objects.all().order_by('name')
    return render(request, 'dashboard/addressbook.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'dashboard/addressbook.html', {'contact': contact})

def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('addressbook_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'dashboard/addressbook.html', {'form': form})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('addressbook', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'dashboard/addressbook_edit.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')