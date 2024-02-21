from django import forms

from personal_account.models import Franchise, FranchisePhoto


class CurrentUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CurrentUserForm, self).__init__(*args, **kwargs)
        if self.request and self.request.user.is_authenticated:
            self.fields['current_user'] = forms.CharField(label='Текущий пользователь',
                                                          initial=self.request.user.username,
                                                          widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        else:
            self.fields['current_user'] = forms.CharField(label='Текущий пользователь', widget=forms.TextInput(
                attrs={'readonly': 'readonly', 'value': 'Не авторизован'}))


class AddFranchiseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddFranchiseForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AddFranchiseForm, self).save(commit=False)
        if self.request:
            instance.user_id = self.request.user.id
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Franchise
        fields = '__all__'
        exclude = ['user']


class FranchiseEditForm(forms.ModelForm):
    class Meta:
        model = Franchise
        exclude = ['user']
        fields = '__all__'


class FranchisePhotoForm(forms.ModelForm):
    class Meta:
        model = FranchisePhoto
        fields = ['franchise_photos']
