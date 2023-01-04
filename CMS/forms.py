from django import forms
from CMS.models import Customer

class CustomerForm(forms.ModelForm):
         class Meta:
                  model=Customer
                  fields='__all__'