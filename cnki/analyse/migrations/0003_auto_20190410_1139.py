# Generated by Django 2.0.5 on 2019-04-10 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0002_auto_20190401_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='local_url',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='authortokeyword',
            name='keyword_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyse.Keyword'),
        ),
        migrations.AlterField(
            model_name='fundtokeyword',
            name='keyword_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyse.Keyword'),
        ),
        migrations.AlterField(
            model_name='schooltokeyword',
            name='keyword_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyse.Keyword'),
        ),
        migrations.AlterField(
            model_name='yeartokeyword',
            name='keyword_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyse.Keyword'),
        ),
    ]
