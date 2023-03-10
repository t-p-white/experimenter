"""
This type stub file was generated by pyright.
"""

from django.test import TestCase

"""Use django's Test client to run file based graphql test."""
DEFAULT_GRAPHQL_URL = ...

def file_graphql_query(
    query,
    op_name=...,
    input_data=...,
    variables=...,
    headers=...,
    files=...,
    client=...,
    graphql_url=...,
):  # -> HttpResponse:
    """
    Based on: https://www.sam.today/blog/testing-graphql-with-graphene-django/

    Perform file based mutation.

    :param str query: GraphQL query to run
    :param str op_name: If the query is a mutation or named query, you must
        supply the op_name. For annon queries ("{ ... }"), should be None (default).
    :param dict input_data: If provided, the $input variable in GraphQL will be set
        to this value. If both ``input_data`` and ``variables``,
        are provided, the ``input`` field in the ``variables``
        dict will be overwritten with this value. Defaults to None.
    :param dict variables: If provided, the "variables" field in GraphQL will be
        set to this value. Defaults to None.
    :param dict headers: If provided, the headers in POST request to GRAPHQL_URL
        will be set to this value. Defaults to None
    :param dict files: Files to be sent via request.FILES. Defaults to None.
    :param django.test.Client client: Test client. Defaults to django.test.Client.
    :param str graphql_url: URL to graphql endpoint. Defaults to "/graphql"
    :return: Response object from client
    """
    ...

class GraphQLFileUploadTestMixin:
    """GraphQL file upload test mixin."""

    GRAPHQL_URL = ...
    def file_query(
        self, query, op_name=..., input_data=..., files=..., variables=..., headers=...
    ):  # -> HttpResponse:
        """
        Perform file based mutation.

        :param str query: GraphQL query to run
        :param str op_name: If the query is a mutation or named query, you must
            supply the op_name. For annon queries ("{ ... }"), should be None (default).
        :param dict input_data: If provided, the $input variable in GraphQL will be set
            to this value. If both ``input_data`` and ``variables``,
            are provided, the ``input`` field in the ``variables``
            dict will be overwritten with this value. Defaults to None.
        :param dict variables: If provided, the "variables" field in GraphQL will be
            set to this value. Defaults to None.
        :param dict headers: If provided, the headers in POST request to GRAPHQL_URL
            will be set to this value. Defaults to None
        :param dict files: Files to be sent via request.FILES. Defaults to None.
        :param django.test.Client client: Test client. Defaults to django.test.Client.
        :param str graphql_url: URL to graphql endpoint. Defaults to "/graphql"
        :return: Response object from client
        """
        ...
    def assertResponseNoErrors(self, resp, msg=...):  # -> None:
        """
        Assert that the call went through correctly. 200 means the syntax is ok,
        if there are no `errors`, the call was fine.
        :param Response resp: HttpResponse
        :param str msg: Error message.
        """
        ...
    def assertResponseHasErrors(self, resp, msg=...):  # -> None:
        """
        Assert that the call was failing. Take care: Even with errors,
        GraphQL returns status 200!
        :param Response resp: HttpResponse
        :param str msg: Error message.
        """
        ...

class GraphQLFileUploadTestCase(GraphQLFileUploadTestMixin, TestCase): ...