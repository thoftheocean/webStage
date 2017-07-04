from django.db import models
from django.core.validators import ValidationError

# Create your models here.

def validate_pre(value):
    print(value)
#     print('作者必须以a开头')
    # if not value.startswith('a'):
    #     raise ValidationError('u must start with a', code='invalid')
class Poem(models.Model):
    author = models.CharField(max_length=10, validators=[validate_pre])
    title = models.CharField(max_length=10)
