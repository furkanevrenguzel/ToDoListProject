from django import forms


from .models import ToDoList, Items

class ToDoItemForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ["todolist", "title", "content", "last_date", "durum"]

    
