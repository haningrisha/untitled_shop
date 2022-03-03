from django.core.validators import RegexValidator, FileExtensionValidator
from untitled_shop.settings import MODEL_EXTENSIONS


class PhoneNumberValidator(RegexValidator):
    def __init__(self):
        super().__init__(regex=r'^\+?1?\d{9,15}$', message="Wrong phone number format")


def validate_model_file_extensions(value):
    return FileExtensionValidator(allowed_extensions=[MODEL_EXTENSIONS])(value)
