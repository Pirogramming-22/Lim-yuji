from django.db import models
from apps.devtool.models import DevTool # DevTool과 연결

class Idea(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey('devtool.DevTool', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')

    def __str__(self):
        return self.title
    
class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='ideastar')
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Starred: {self.idea.title}"