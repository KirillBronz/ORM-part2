from django.db import  migrations, models 

class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name ='student',
            name = 'group',
            field = models.CharField(max_length=64, verbose_name='class_room'),
        ),
        migrations.AlterField(
            model_name ='student',
            name = 'name',
            field = models.CharField(max_length=64, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name ='teacher',
            name = 'name',
            field = models.CharField(max_length=64, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name ='teacher',
            name = 'subject',
            field = models.CharField(max_length=64, verbose_name='subject'),
        ),
    ]