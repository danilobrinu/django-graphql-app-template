# Project Overview

This project is a project template to scaffold or create the initial structure of your app.

**PROJECT STRUCTURE**

| File Name         | Description                                                                       |
| ----------------- | --------------------------------------------------------------------------------- |
| `├── domain/`     | _This folder should contains the domain apps._                                    |
| `└── migrations/` | _This folder contains the migration or changes to your database._                 |
| `__init__.py`     | This tells Python that your app is a package                                      |
| `admin.py`        | This file is where you can register your app’s models to the Django's admin site. |
| `apps.py`         | This is a configuration file common to all Django apps                            |
| `models.py`       | This file contains the models for your app.                                       |
| `README.md`       | This file contains the documentation of this project.                             |
| `schema.py`       | This file contains the schema that you want to expose to your graphql endpoint.   |

# Scaffoling an app

```sh
django-admin startapp --template https://github.com/danilobrinu/django-graphql-app-template/archive/master.zip <awesome-app>
```

**Example:** `django-admin startapp --template https://github.com/danilobrinu/django-graphql-app-template/archive/master.zip api_v1`

# Adding models to the app

The models are not automatically available to the app, so you need to add it manually.
To add it, go to your `models.py` in the root level of your app and import it.

**File: api_v1/domain/post/models.py**

```python
class Post(models.Model):
    pass
```

**File: api_v1/models.py**

```python
from .domain.post.models import Post # noqa
```

# Adding models to the admin site

To add the models to the admin site, just go to your `admin.py` in the root level of your app and
import it.

**File: api_v1/domain/post/models.py**

```python
class Post(models.Model):
    pass
```

**File: api_v1/admin.py**

```python
@admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
```

# Adding queries and mutations to the app

The queries and mutations are not automatically available to that app, so you need to add it manually.
To add it, go to your ``schema.py` in the root level of your app and import it.

**File: api_v1/domain/post/schema.py**

```python
class Query(graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    pass
```

**File: api_v1/schema.py**

```python
from .domain.post.schema import Query as PostQuery, Mutation as PostMutation

class Query(
    PostQuery,
    # The ObjectType class should be the last one always
    graphene.ObjectType,
):
    pass

class Mutation(
    PostMutation,
    # The ObjectType class should be the last one always
    graphene.ObjectType,
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
```
