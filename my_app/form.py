# forms.py
from django import forms
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from .models import Staff, Position

class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'position']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name',
                'required': True
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'position': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            })
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
            'date_of_birth': 'Date of Birth',
            'position': 'Position'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate position choices
        self.fields['position'].queryset = Position.objects.all().order_by('position_name')
        
        # Make all fields required
        for field in self.fields.values():
            field.required = True

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        
        if date_of_birth:
            # Check if date is not in the future
            if date_of_birth > date.today():
                raise ValidationError("Date of birth cannot be in the future.")
            
            # Check minimum age (e.g., 16 years old)
            min_age_date = date.today() - timedelta(days=16*365)
            if date_of_birth > min_age_date:
                raise ValidationError("Staff member must be at least 16 years old.")
            
            # Check maximum age (e.g., 80 years old)
            max_age_date = date.today() - timedelta(days=80*365)
            if date_of_birth < max_age_date:
                raise ValidationError("Please verify the date of birth.")
        
        return date_of_birth

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name:
            # Remove extra spaces and capitalize
            first_name = ' '.join(first_name.split()).title()
            if len(first_name) < 2:
                raise ValidationError("First name must be at least 2 characters long.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name:
            # Remove extra spaces and capitalize
            last_name = ' '.join(last_name.split()).title()
            if len(last_name) < 2:
                raise ValidationError("Last name must be at least 2 characters long.")
        return last_name