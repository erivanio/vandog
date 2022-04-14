import datetime
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('planos', '0005_auto_20220414_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='entrada',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='saida',
        ),
    ]
