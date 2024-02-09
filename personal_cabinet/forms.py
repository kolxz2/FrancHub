from django import forms

class CurrentUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CurrentUserForm, self).__init__(*args, **kwargs)
        if self.request and self.request.user.is_authenticated:
            self.fields['current_user'] = forms.CharField(label='Текущий пользователь', initial=self.request.user.username, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        else:
            self.fields['current_user'] = forms.CharField(label='Текущий пользователь', widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Не авторизован'}))