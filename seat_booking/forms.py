from django import forms
from .models import User

class BookingForm(forms.ModelForm):
    """
    A form for creating and updating Booking instances.

    This form is based on the User model and includes all fields from the model.

    Attributes:
        Meta (class): A class that holds the metadata for the form.
            model (User): The model that the form is based on.
            fields (str): Specifies that all fields from the model should be included in the form.
    """
    class Meta:
        model=User
        fields='__all__'
