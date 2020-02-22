from django.db import models

class Topic(models.Model) :
    """A topic the user is learning about"""
    text = models.CharField(max_length=200) 
    # CharField, stores small amout of text
    date_added = models.DateTimeField(auto_now_add=True) 
    # auto_now_add, automatically add current date when create a new topic

    def __str__(self): # similar to java's toString()
        """Return a string representation of the model."""
        return self.text