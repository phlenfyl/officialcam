from django import forms

from .models import Contact



class StudioForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname','email','number','message']
        widgets ={
            'fullname': forms.TextInput(attrs={'class':'text-[#1b1a1a] bg-transparent border p-5.5 outline-0 text-sm/[15px] font-normal', 'placeholder':'first name                   last name'}),
            'email': forms.EmailInput(attrs={'class':'text-[#1b1a1a] bg-transparent border p-5.5 outline-0 text-sm/[15px] font-normal', 'placeholder':'Email'}),
            'number': forms.TextInput(attrs={'class':'text-[#1b1a1a] bg-transparent border p-5.5 outline-0 text-sm/[15px] font-normal', 'placeholder':'Enter your phone number'}),
            'message': forms.Textarea(attrs={'class':'text-[#1b1a1a] bg-transparent border p-5.5 outline-0 text-sm/[15px] font-normal', 'placeholder':'Message'}),
        }
