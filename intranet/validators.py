from datetime import timezone
from django.core.exceptions import ValidationError

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Fecha no puede ser anterior a hoy.")