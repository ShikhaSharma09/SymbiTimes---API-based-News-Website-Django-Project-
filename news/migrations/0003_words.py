# Generated by Django 4.2.3 on 2024-04-05 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_index_quiz_qna_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.IntegerField()),
                ('word', models.CharField(max_length=300)),
            ],
        ),
    ]
