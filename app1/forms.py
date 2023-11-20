from django import forms
from .models import Feedback
from .models import Comment
from .models import Post

class Feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','email','message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','author']
