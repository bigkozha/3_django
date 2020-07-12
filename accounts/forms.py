from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'data-test': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'data-test':'password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('The user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('The password is wrong')
            if not user.is_active:
                raise forms.ValidationError('The user is not active')

        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=[
            'username',
            'password'
        ]
