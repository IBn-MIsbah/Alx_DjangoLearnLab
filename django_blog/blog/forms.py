from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag
from taggit.forms import TagWidget

class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
        ]

class PostForm(forms.ModelForm):
    # tags = forms.CharField(required=False, help_text='Comma-separated tags')

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            # 'tags'
        ]
        widgets = {
            'tags': TagWidget()
        }
    # def save(self, commit = True):
    #     instance = super().save(commit=False)
    #     if commit:
    #         instance.save()
        
    #     tag_names = self.cleaned_data['tags'].split(',')
    #     tag_objs = []

    #     for name in tag_names:
    #         name = name.strip()
    #         if name:
    #             tag_objs, created = Tag.objects.get_or_create(name=name)
    #             tag_objs.append(tag_objs)
    #     instance.tags.set(tag_objs)
    #     return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'})
        }