# Built-in package


# Third-party packages
from django.apps import AppConfig


# Local packages


class {{ app_name | title }}Config(AppConfig):
    name = "{{ app_name }}"
    verbose_name = "{{ app_name | title }}"
