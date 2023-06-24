from .schema import schema
from .views import *
from django.urls import path
from graphene_django.views import GraphQLView

app_name = 'quiz'

urlpatterns = [
    # Only a single URL to access GraphQL
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]