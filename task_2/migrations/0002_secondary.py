from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False , verbose_name=id)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name="Scope",
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(default=False, verbose_name='main')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.topic', verbose_name="Section")),

            ],
            options={
                'verbose_name':'article theme',
                'verbose_name_plural': 'article theme',
                'ordering': ['-main', 'tag_name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(through='articles.Scoping', to='articles.Topic'),
        ),
    ]