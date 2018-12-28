from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField
class Custom_Table(UserCreationForm):
    昵称 = forms.CharField(max_length=50,required=False)
    生日 = forms.DateTimeField(required=False)
    验证码 = CaptchaField()
    class Meta:
        model = User
        fields = ('username','password1','password2','email','昵称','生日')



class Custom_Table2(UserChangeForm):
    昵称 = forms.CharField(max_length=50,required=False)
    生日 = forms.DateTimeField(required=False)

    class Meta:
        model = User
        fields = ('username','password','email','昵称','生日')

class Custom_Table3(AuthenticationForm):
    验证码 = CaptchaField()
