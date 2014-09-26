from django import forms
from django.conf import settings
import os

class ImageForm(forms.Form):
    name = forms.FileField(
        label='Select image(s)',
    )

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.FileInput(attrs={'multiple': True})

    def clean_name(self):
        files = self.cleaned_data['name']
        file_type = files.content_type.split('/')[0]
        if len(file_type) == 1:
            raise forms.ValidationError("File type is not supported")
        if file_type in settings.TASK_UPLOAD_FILE_TYPES:
            if files.size > settings.TASK_UPLOAD_FILE_MAX_SIZE:
                raise forms.ValidationError("Please keep file size under our settings.")
        else:
            raise forms.ValidationError("File type is not supported")

        return files
