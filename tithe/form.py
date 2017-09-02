from django import forms
from models import Offering
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.utils.translation import ugettext_lazy as _

class OfferingForm(forms.ModelForm):
    member_code=forms.CharField()
    member=forms.CharField(max_length=45)
    receipt_code=forms.CharField(max_length=45)
    combinedoffering=forms.IntegerField()
    campmeetingoffering=forms.IntegerField()
    churchbuilding=forms.IntegerField()
    conference=forms.IntegerField()
    localchurch=forms.IntegerField()
    funds=forms.IntegerField()
    total=forms.IntegerField()



    class Meta:
        model = Offering
        fields = (
                  'member_code', 'member', 'receipt_code', 'tithes', 'combinedoffering',
                  'campmeetingoffering', 'churchbuilding', 'conference', 'localchurch', 'funds', 'total',
                 )


class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
        