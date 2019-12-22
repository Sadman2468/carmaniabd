from django import forms
from .models import Contact, Giverent_field, sell_car_post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Field

class Contact_form(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'    #['name','email','message']
        #widgets = {
        #     'email' : forms.TextInput(attrs={'placeholder':'Email','required':True}),
        #     'name' : forms.TextInput(attrs={'placeholder':'Full-Name','required':True}),
         #    'message' : forms.Textarea(
         #                    attrs={'required':True,
         #                           'rows': 200,
         #                           'cols':50,
         #                           'style':'resize:none;',
         #                          'placeholder':'message'
         #            })
         # }

    # helper = FormHelper()
    # helper.form_method = 'POST'
    # helper.add_input(Submit('Submit','Submit', css_class='btn-primary pos'))
    # helper.layout = Layout(
    #     Column('name',css_id="form-group1",placeholder="Name"),
    #     Column('email',css_class='',placeholder="Email"),
    #     Column('message',css_class='',placeholder="Message")
    # )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column('name',css_class='form-group col-md-12 mb-0'),
            Column('email',css_class='form-group col-md-12 mb-0'),
            Column('message',css_class='form-group col-md-12 mb-0'),
            Submit('submit', 'Submit',css_class="btn-success pos")
        )
        self.fields['name'].label = "Name :"
        self.fields['email'].label = "Email :"
        self.fields['message'].label = "Message :"
        self.fields['message'].widget.attrs['style'] = 'resize:none'
        self.fields['name'].widget.attrs['placeholder'] = 'Full-Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'

class Giverent_form(forms.ModelForm):

    class Meta:
        model = Giverent_field
        fields = ['car_name','car_type','image','seat_capacity','contact_number','location']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column('car_name',css_class='form-group col-md-12 mb-0'),
            Column('car_type',css_class='form-group col-md-12 mb-0'),
            Column('image',css_class='form-group col-md-12 mb-0'),
            Column('seat_capacity',css_class='form-group col-md-12 mb-0'),
            Column('contact_number',css_class='form-group col-md-12 mb-0'),
            Column('location',css_class='form-group col-md-12 mb-0'),
            Submit('submit', 'Submit',css_class="btn-success pos")
        )
        self.fields['car_name'].label = "Car Name :"
        self.fields['car_type'].label = "car type :"
        self.fields['image'].label = "image :"
        self.fields['seat_capacity'].label = "Seat capacity :"
        self.fields['contact_number'].label = "Contact number :"
        self.fields['location'].label = "location :"


# class form_post(forms.ModelForm):
#
#     class Meta:
#         model = sell_car_post
#         fields = ['car_name','registration_date','car_detail']
#
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Column('car_name',css_class='form-group col-md-12 mb-0'),
#             Column('registration_date',css_class='form-group col-md-12 mb-0'),
#             Column('car_detail',css_class='form-group col-md-12 mb-0'),
#             Submit('submit', 'Post',css_class="btn btn-success pos1")
#         )
#         self.fields['car_name'].label = "Car Name :"
#         self.fields['registration_date'].label = "Registration Date :"
#         self.fields['car_detail'].label = "Details of Car :"
#         self.fields['car_detail'].widget.attrs['style'] = 'resize:none'
