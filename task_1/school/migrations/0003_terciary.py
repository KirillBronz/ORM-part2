from django.db import migrations , models 

class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_secondary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name = 'student',
            name = 'teacher',
        ),
        migrations.AddField(
            model_name = 'student',
            name = 'teacher',
            field = models.ManyToManyField(related_name='student', to='school.Teacher') 
        )
    ]