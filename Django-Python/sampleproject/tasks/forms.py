from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

class EditTaskForm(forms.Form):
    taskNum = forms.CharField(label="Task Count")
    updateTask = forms.CharField(label="Update Task")