Authentication
==========================

Users login by doing the following request:

.. code-block::

    POST /v1/login
    {
        "username": "string"
        "password": "string"
    }

On success 200 is returned:

.. code-block:: json

    {
        "token": "string"
    }

The 400 response is always returned for incorrect credentials and no hint for username already existing is given.

Token Authentication
--------------------

When using a token authentication, the user information is stored as a copy in-memory because these are supposed to
be accessed frequently.

.. automodule:: app.authentication.token_authentication
   :members:
   :undoc-members:
   :show-inheritance:
