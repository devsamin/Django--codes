from django import forms
from django.core import validators


class ContactForm(forms.Form):
    name = forms.CharField(label="username", help_text="Total length must be wiithing 20 cherecter",
                           required=False, widget=forms.Textarea(attrs={'id' : 'text_area','placeholder' : 'Enter you name'}),
                           )

    # file = forms.FileField()
    # email = forms.EmailField()
    age = forms.CharField(widget=forms.NumberInput)
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    birthday = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'date'}))
    apoenment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : "datetime-local"}))
    size = [('s', 'small'), ('m', 'medium'), ('L', 'larger')]
    Coices = forms.ChoiceField( choices = size, widget=forms.RadioSelect)
    # size = [('s', 'small'), ('m', 'medium'), ('L', 'large')]
    # Length = forms.ChoiceField(choices=size)
    MEAL = [('p', 'pizza'), ('b', 'beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Must be length 10 cherecter')
    #     else:
    #         return valname
    # def clean_email(self):
    #     valname = self.cleaned_data['email']
    #     if '.com' not in valname:
    #         raise forms.ValidationError('This containt must be .com')
    #     return valname

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Must be length 10 cherecter')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('This containt must be .com')


class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10, message='Enter name must be minumum 10 charecter.')])
    email = forms.CharField(
        
    validators=[validators.EmailValidator(message='Enter a valid email address.')])
    age = forms.IntegerField(validators=[validators.MinValueValidator(20, message='Minimum value 20.'), 
                                         validators.MaxValueValidator(30, message='Maximum value less 30.')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message='File extension must be PNG or PDF.')])

class PasswordValidationProject(forms.Form):
    Name = forms.CharField(widget=forms.TextInput)
    Password = forms.CharField(widget=forms.PasswordInput)
    Comfirm_Password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['Name']
        valpass = self.cleaned_data['Password']
        valcompass = self.cleaned_data['Comfirm_Password']
        if len(valname) < 10:
            raise forms.ValidationError("Name must be more then 10 chearcter.")
        if valpass != valcompass:
            raise forms.ValidationError("Password is not match")