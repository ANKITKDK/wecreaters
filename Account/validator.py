from django.core.exceptions import ValidationError

def video_file_size(value):
    filesize=value.size
    if filesize>4000000:
        raise ValidationError('Maximum size is 4 mb')
