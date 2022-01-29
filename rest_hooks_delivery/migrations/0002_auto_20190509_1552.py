from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_hooks_delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failedhook',
            name='event',
            field=models.CharField(choices=[], db_index=True, editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='failedhook',
            name='target',
            field=models.URLField(db_index=True, editable=False, max_length=255, verbose_name='original target URL'),
        ),
        migrations.AlterUniqueTogether(
            name='failedhook',
            unique_together=set([]),
        ),
    ]
