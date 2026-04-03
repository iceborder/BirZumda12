from django.forms.models import ModelForm
from app.models import Contact, EmailContact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class EmailForm(ModelForm):
    class Meta:
        model = EmailContact
        fields = '__all__'