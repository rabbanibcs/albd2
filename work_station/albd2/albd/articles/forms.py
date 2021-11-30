import itertools
from django import forms
from django.utils.text import slugify

from .models import Article, ArticlePhoto, ArticleAttachment, ArticleVideo


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'snippet': forms.Textarea(attrs={'cols': 100, 'rows': 5}),
            'title': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
            'short_title': forms.Textarea(attrs={'cols': 100, 'rows': 1}),
            'core_issue': forms.Textarea(attrs={'cols': 100, 'rows': 1}),
            'courtesy': forms.Textarea(attrs={'cols': 80, 'rows': 1}),
            'meta_description': forms.Textarea(attrs={'cols': 80, 'rows': 1}),
        }
        fields = '__all__'

    def save(self, commit=False):

        instance = super(ArticleForm, self).save(commit=False)

        max_length = Article._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.title)[:max_length]

        for x in itertools.count(1):
            if not Article.objects.filter(slug=instance.slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.save()

        return instance


class ArticlePhotoForm(forms.ModelForm):
    class Meta:
        model = ArticlePhoto
        widgets = {
            'caption': forms.Textarea(attrs={'cols': 80, 'rows': 1}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }
        fields = '__all__'


class ArticleAttachmentForm(forms.ModelForm):
    class Meta:
        model = ArticleAttachment
        widgets = {
            'caption': forms.Textarea(attrs={'cols': 80, 'rows': 1}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }
        fields = '__all__'


class ArticleVideoForm(forms.ModelForm):
    class Meta:
        model = ArticleVideo
        widgets = {
            'caption': forms.Textarea(attrs={'cols': 80, 'rows': 1}),
        }
        fields = '__all__'
