#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snacks_crud.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
# from .models import 
# from django.urls import reverse_lazy

# class ListView(ListView):
#     template_name = '_list.html'
#     model= 

# class DetailView(DetailView):
#     template_name= '_detail.html'
#     model= 
# class CreateView(CreateView):
#     template_name= '_create.html'
#     model= 
#     fields = ['title', 'purchaser', 'description']

# class UpdateView(UpdateView):
#     template_name= '_update.html'
#     model= 
#     fields = ['title', 'purchaser', 'description']
# class DeleteView(DeleteView):
#     template_name= '_delete.html'
#     model= 
#     success_url = reverse_lazy('_list')