from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Topic

class ScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        topic_count = 0
        for form in self.forms:
            if form in self.cleaned_data.get('main'):
                topic_count += 1
            else:
                continue
        if topic_count == 0:
           raise ValidationError('Select main section')
        elif topic_count > 1:
            raise ValidationError('Main section already selected')
        
        return super().clean()
    

class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInLineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

