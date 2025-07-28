from django import forms 
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        ),
        required=False
    )

    class Meta:
        model = models.Contact
        fields = (
            'name',
            'lastname',
            'phone',
            'email',
            'description',
            'category',
            'picture',

        )


    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        lastname = cleaned_data.get('lastname')

        if name == lastname:
            self.add_error(
                'lastname',
                ValidationError(
                    'primeiro nome igual ao segundo',
                    code='invalid'
                )
            )
        
        return super().clean()
    


    # OBSERVAÇÕES IMPORTANTES
    #adderror permite levantar varias exceções, enquanto raise para na primeira

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')

    #     if name == 'fernandão':
    #         self.add_error(
    #             'name',
    #             ValidationError(
    #                 'Não aceitamois fernandao'
    #             )
    #         )

    #     return name

"""
na variável widgets é possível editar os widgets do formulário
na variável attrs é possível aplicar atributos html aos widgets

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'classe-a classe-b',
                    'placeholder': 'Escreva aqui seu nome',
                }
            )
        }
É possível modificar os widgets através de self.fields no init da classe
        self.fields['name'].widget.attrs.update({
           'class': 'classe-a classe-b',
            'placeholder': 'Escreva aqui seu nome',
    })

Também é possível modificar os campos dessa forma
    name = forms.CharField(
       widget = forms.TextInput(
            attrs = {
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva aqui seu nome',
                    
            }
        ),
     
"""

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True,
    )
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('este email ja existe', code='invalid')
            )
        return email

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length = 2,
        max_length = 30,
        required = True,
        help_text = 'Required',
        error_messages = {
            'min_lenght': 'Please, add more than 2 letters'
        }
    )
    last_name = forms.CharField(
        min_length = 2,
        max_length = 30,
        required = True,
        help_text = 'Required',
        error_messages = {
            'min_lenght': 'Please, add more than 2 letters'
        }
    )
    password1 = forms.CharField(
        label = 'Password',
        strip = False,
        widget = forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required = False,
    )
    password2 = forms.CharField(
        label = 'Password',
        strip = False,
        widget = forms.PasswordInput(attrs={'autocomplete': "new-password"}),
        help_text='Use the same passwprd as before.',
        required = False,
    )
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem', code='invalid')
                )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('este email ja existe', code='invalid')
                )
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try: 
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )
        
        return password1