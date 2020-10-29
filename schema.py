# Built-in packages

# Third-party packages
from graphene import ObjectType, Schema

# Local packages


class Query(
    # The ObjectType class should be the last one always
    ObjectType,
):
    pass


class Mutation(
    # The ObjectType class should be the last one always
    ObjectType,
):
    pass


schema = Schema(query=Query, mutation=Mutation)
