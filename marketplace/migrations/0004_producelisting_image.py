# Generated migration for image field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_alter_producelisting_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producelisting',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload a photo of your produce', null=True, upload_to='listings/'),
        ),
    ]
