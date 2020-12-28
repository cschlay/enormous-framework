"""
Many frameworks allow any urls to be used, however I prioritise integrity here and enforce strict url conventions.

So every url is supposed to have the pattern of:
    /v1/<resourceName>
    or
    /v1/<resourceName>/<resourceId>

The versioning is enforced and an error occurs if not specified. No other urls are allowed.
Also integer resourceId are not allowed either.
"""
from api.views import tasks


def construct_url_table(*args) -> dict:
    """
    Constructs a table of URLs. The arguments are supposed to be given as

    {
        "resourceName": endpointHandler
    }

    :param args: any argument of dictionary of urls
    :return: a dictionary of urls
    """
    url_table: dict = {}
    for url_set in args:
        url_table = {**url_table, **url_set}
    return url_table


urls = construct_url_table(
    {
        "tasks": tasks.TaskView
    }
)
