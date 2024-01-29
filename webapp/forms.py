from django.forms import ModelForm
from .models import Reservation, Feedback 

class reservation(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class feedback(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'