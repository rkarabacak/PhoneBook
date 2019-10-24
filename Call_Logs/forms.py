from crispy_forms.bootstrap import FormActions
from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from Call_Logs.models import call_logs


class CallLogsForm(forms.ModelForm):

   class Meta:
        model = call_logs
        fields = [
            # 'callTime',
            'fromNumber',
            'toUser',            
            'note',
            'id_contacts',            
        ]