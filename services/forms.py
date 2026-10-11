from django import forms
from .models import ServiceRequest


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ["room_number", "request_type", "details"]
        widgets = {
            "details": forms.Textarea(attrs={"rows": 4}),
        }