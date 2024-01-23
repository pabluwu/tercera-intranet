from datetime import timezone
from django.core.exceptions import ValidationError

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Fecha no puede ser anterior a hoy.")
    
def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Archivo demasiado grande, no debe exceder los 2MB.')
    
    
def validate_file_extension(value):
    if value.file.content_type != 'application/pdf':
        raise ValidationError('Solo puedes subir archivos PDF')