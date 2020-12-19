from django import forms


from .models import ToDoList, Items


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ["name"]
