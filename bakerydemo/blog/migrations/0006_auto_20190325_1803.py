# Generated by Django 2.1.7 on 2019-03-25 18:03

from django.db import migrations, models
import django.db.models.deletion
import uuid
import wagtail_i18n.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_i18n', '0003_initial_data'),
        ('blog', '0005_auto_20190325_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='region',
            field=models.ForeignKey(default=wagtail_i18n.models.Region.default_id, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Region'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='region',
            field=models.ForeignKey(default=wagtail_i18n.models.Region.default_id, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Region'),
        ),
        migrations.AddField(
            model_name='blogpeoplerelationship',
            name='region',
            field=models.ForeignKey(default=wagtail_i18n.models.Region.default_id, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_i18n.Region'),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='blogpeoplerelationship',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='blogindexpage',
            unique_together={('translation_key', 'region', 'language')},
        ),
        migrations.AlterUniqueTogether(
            name='blogpage',
            unique_together={('translation_key', 'region', 'language')},
        ),
    ]