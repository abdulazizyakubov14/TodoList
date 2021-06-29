from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class TodoList(models.Model):
	COLORS = (
		('bg-danger','danger'),
		('bg-warning','warning'),
		('bg-info','info'),
		('bg-success','success'),
		)
	title = models.CharField('Title',max_length=250)
	body = RichTextField()
	date = models.DateTimeField('Date', auto_now_add=True)
	prioroty = models.CharField('Prioroty',max_length=50, choices=COLORS)
	star = models.BooleanField('Star/Unstar', default=False)
	image = models.ImageField( 'Rasim qo\'shish', upload_to='todo_poster/',)

	def __str__(self):
		return self.title
