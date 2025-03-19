from django import forms
from .models import *

class DataBerita(forms.ModelForm):
    class Meta:
        model = Data_Berita
        exclude = ()
        fields = '__all__'
        error_messages = {
            'judul' :{
                'required' : 'Judul harus diisi'
            }
        }

class DataPengguna(forms.ModelForm):
    class Meta:
        model = Data_Pengguna
        exclude = ()
        fields = '__all__'  # Memperbaiki typo dari 'fileds' menjadi 'fields'
        error_messages = {
            'email' : {
                'required' : 'Email harus diisi',
            },
        }

# class UserRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

    
#      def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirm = cleaned_data.get('password_confirm')

#         if password and password_confirm and password != password_confirm:
#             self.add_error('password_confirm', 'Password tidak cocok')

#         return cleaned_data

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user


class UserRegistrationForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput, label="Password")
    # password_confirm = forms.CharField(widget=forms.PasswordInput, label="Konfirmasi Password")

    class Meta:
        model = User
        fields = '__all__'

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     password_confirm = cleaned_data.get('password_confirm')

    #     if password and password_confirm and password != password_confirm:
    #         self.add_error('password_confirm', 'Password tidak cocok')

    #     return cleaned_data

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #     return user