from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Field
#
#
class registration_form(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column('username',css_class='form-group col-md-12 mb-0'),
            Column('email',css_class='form-group col-md-12 mb-0'),
            Column('password1',css_class='form-group col-md-12 mb-0'),
            Column('password2',css_class='form-group col-md-12 mb-0'),
            Submit('submit', 'Sign Up',css_class="btn btn-success pos1")
        )
        self.fields['username'].label = "Username :"
        self.fields['email'].label = "Email :"
        self.fields['password1'].label = "Password :"
        self.fields['password2'].label = "Confirm Password :"
