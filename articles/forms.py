from django import forms


class SearchForm(forms.Form):
    """
    Formular für die Suche in der Knowledge Base.

    Attributes:
        query (str): Die Suchanfrage des Benutzers.
    """
    query = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Knowledge Base durchsuchen', 'class': 'search-input'}))
