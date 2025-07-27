import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from contact.models import Contact
Contact.objects.create(name="Fernando", lastname="Vieira", phone=54999810256, email="fvieira@gmail.com", description="Fernandao da massa")
Contact.objects.create(name="Bernardo", lastname="Bernardes", phone=99999999999, email="bbxzza@gmail.com", description="Bernardao da massa")
