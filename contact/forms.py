from django import forms 
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):

#Também é possível modificar os campos dessa forma
    name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva aqui seu nome',
            }
        ),
        help_text='Ajuda aqui'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    class Meta:
        model = models.Contact
        fields = (
            'name',
            'lastname',
            'phone',
            'email',
            'description',
            'category',

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
# na variável widgets é possível editar os widgets do formulário
# na variável attrs é possível aplicar atributos html aos widgets

        # widgets = {
        #     'name': forms.TextInput(
        #         attrs = {
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui seu nome',
        #         }
        #     )
        # }
#É possível modificar os widgets através de self.fields no init da classe
        # self.fields['name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Escreva aqui seu nome',
        # })