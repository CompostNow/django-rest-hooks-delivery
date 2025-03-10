Django REST Hooks Delivery
==========================

Various deliverers for `django rest hooks
<https://github.com/zapier/django-rest-hooks>`_ and `django rest hooks ng
<https://github.com/PressLabs/django-rest-hooks-ng>`_.

Forked from `presslabs/django-rest-hooks-delivery
<https://github.com/presslabs/django-rest-hooks-delivery>`_ to add backoff algorithm,
emails on final attempt, and to allow multiple failed instances per hook (by tying it 
to the model instance, not the hook).

Installation
------------

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/CompostNow/django-rest-hooks-delivery.git#egg=django-rest-hooks-delivery

Add ``rest_hooks_delivery`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'rest_hooks_delivery',
    )


Usage
-----

Make sure you have added :code:`rest_hooks_delivery` to the list of
:code:`INSTALLED_APPS` before :code:`django.contrib.admin` and that you have
set :code:`HOOK_DELIVERER` to one of the available deliverers. Currently only
:code:`rest_hooks_delivery.deliverers.retry` is available.

.. code-block:: python

    ### settings.py ###

    INSTALLED_APPS = [
    ...
    'rest_hooks_delivery',
    'django.contrib.admin',
    ]

    HOOK_DELIVERER = 'rest_hooks_delivery.deliverers.retry'

It also provides a management command useful for retrying failed hooks.

.. code-block:: bash

    ./manage.py retry_failed_hooks

