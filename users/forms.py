from django.contrib.auth.forms import UserCreationForm
from .models import User


#class RegisterCustomerForm(UserCreationForm):
#    class Meta:
#        model = User
#        fields = ['email', 'username']

#class RegisterCustomerForm(UserCreationForm):
#    class Meta(UserCreationForm.Meta):
#        model = User


#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from .models import User

class RegisterCustomerForm(UserCreationForm):
#    email = forms.EmailField()  # Add this line to include the email field

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
