from django.db import models

class Topic(models.Model) :
    """A topic the user is learning about"""
    text = models.CharField(max_length=200) 
    # CharField, stores small amout of text (don't want huge Topics)
    date_added = models.DateTimeField(auto_now_add=True) 
    # auto_now_add, automatically add current date when create a new topic

    def __str__(self): # similar to java's toString()
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # foreign key : reference to another record in database
    # kind of like having a Topic field for each Entry
    # must have on_delete argument
    text = models.TextField()
    # TextField doesn't have size limit
    # don't want to limit content of an entry
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta: # Meta holds extra information for managing a model
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."