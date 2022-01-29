from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest_hooks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FailedHook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_retry', models.DateTimeField(auto_now=True, db_index=True)),
                ('target', models.URLField(verbose_name='Original target URL', max_length=255, editable=False, db_index=True)),
                ('event', models.CharField(db_index=True, verbose_name='Event', max_length=64, editable=False, choices=[('customer.created', 'customer.created'), ('customer.deleted', 'customer.deleted'), ('customer.updated', 'customer.updated'), ('invoice.created', 'invoice.created'), ('invoice.deleted', 'invoice.deleted'), ('invoice.updated', 'invoice.updated'), ('plan.created', 'plan.created'), ('plan.deleted', 'plan.deleted'), ('plan.updated', 'plan.updated'), ('proforma.created', 'proforma.created'), ('proforma.deleted', 'proforma.deleted'), ('proforma.updated', 'proforma.updated'), ('provider.created', 'provider.created'), ('provider.deleted', 'provider.deleted'), ('provider.updated', 'provider.updated'), ('subscription.created', 'subscription.created'), ('subscription.deleted', 'subscription.deleted'), ('subscription.updated', 'subscription.updated')])),
                ('payload', models.TextField(editable=False)),
                ('response_headers', models.TextField(max_length=65535, editable=False)),
                ('response_body', models.TextField(max_length=65535, editable=False)),
                ('last_status', models.PositiveSmallIntegerField(editable=False, db_index=True)),
                ('retries', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('hook', models.ForeignKey(editable=False, to='rest_hooks.Hook', on_delete=models.PROTECT)),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),
            ],
            options={
                'ordering': ('-last_retry',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='failedhook',
            unique_together=set([('target', 'event', 'user', 'hook')]),
        ),
    ]
