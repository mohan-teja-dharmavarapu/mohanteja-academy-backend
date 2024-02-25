from django.db import models
from django.core.validators import FileExtensionValidator
from wagtail.models import DraftStateMixin, RevisionMixin, LockableMixin, WorkflowMixin
from wagtail.fields import RichTextField


class Chapter(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, models.Model):
    chapter_number = models.IntegerField(unique=True, null=True, blank=True)
    chapter_name = models.CharField(null=True, blank=True)
    chapter_description = RichTextField(null=True, blank=True)
    noof_units = models.IntegerField(blank=True, null=True)
    chapter_video = models.FileField(upload_to='videos_uploaded',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    
    
class Unit(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    unit_number = models.IntegerField(null=True, blank=True)
    unit_name = models.CharField(null=True, blank=True)
    unit_description = RichTextField(null=True, blank=True)
    noof_topics = models.IntegerField(blank=True, null=True)
    unit_videos = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    
    
class Topic(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    topic_number = models.IntegerField(null=True, blank=True)
    topic_name = models.CharField(null=True, blank=True)
    topic_description = RichTextField(null=True, blank=True)
    topic_article = RichTextField(null=True, blank=True)
    topic_video = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    
    
class Problem(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    problem_number = models.IntegerField(null=True, blank=True)
    problem_name = models.CharField(null=True, blank=True)
    problem_question = RichTextField(null=True, blank=True)
    problem_answer = RichTextField(null=True, blank=True)
    problem_source = RichTextField(null=True, blank=True)
    problem_video = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    problem_article = RichTextField(null=True, blank=True)
    
