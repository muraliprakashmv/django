from django import forms
from django.core.exceptions import ValidationError
from employee.models import student,teacher,sgpg

'''
def CheckEmail(value):
    if value.find('mytectra.com')==-1:
        raise ValidationError("Please provide mytectra.com domain emails")

def NameCheck(value):
    if value.isdigit():
        raise ValidationError("Please give a valid name")
'''


class formExample(forms.Form):
    ch = (

        ('','---Select---'),
        ('pn', 'pune'),
        ('bn', 'bengalore'),

    )

    gn =(

        ('m','Male'),
        ('f','Female')
    )


    name=forms.CharField(min_length=5,max_length=20,label="Username:" ,initial="xyz" ,required="true") # label-custom labelname,initial -default value
    email=forms.EmailField()
    city=forms.ChoiceField(choices=ch)
    gender=forms.ChoiceField(choices=gn,widget=forms.RadioSelect())
    address=forms.CharField(max_length=250,widget=forms.Textarea())
    is_active=forms.CharField(widget=forms.CheckboxInput())

    def clean(self):
        form_data=self.cleaned_data
        if 'email' in form_data and form_data ['email'].find ('mytectra.com')==-1:
            self.errors['email']=["please provide domain name as mytectra.com email"]
        return form_data

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        #fields=('name','email','address')
        fields = ('email', 'address')



class teacherForm(forms.ModelForm):
    ch = (

        ('', '---Select---'),
        ('pn', 'pune'),
        ('bn', 'bengalore'),

    )

    gn = (

        ('m', 'Male'),
        ('f', 'Female')
    )

    city = forms.ChoiceField(choices=ch)
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect())
    is_active = forms.CharField(widget=forms.CheckboxInput())
    class Meta:
        model= teacher
        fields=('name','student','email','city','gender','is_active')


class sgpgForm(forms.ModelForm):
    gn = (

        ('m', 'Male'),
        ('f', 'Female')
    )

    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect())
    is_active = forms.CharField(widget=forms.CheckboxInput())
    class Meta:
        model=sgpg
        fields=(
            'first_name',
            'middle_name',
            'last_name',
            'gender' ,
            'email_id',
            'phone1',
            'phone2',
            'parents_name',
            'parents_phone',
            'address',
            'joining_date',
            'deposit',
            'rent',
            'pending',
            'is_active',

        )
