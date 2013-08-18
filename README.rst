A test project to verify bugs `#20934 <https://code.djangoproject.com/ticket/20934>`_ and `#20640 <https://code.djangoproject.com/ticket/20640>`_


Tests can be found in test_app/tests.py and run with ./manage.py test

Manual testing:

`#20934 <https://code.djangoproject.com/ticket/20934>`_

::

    $ ./manage.py syncdb
    $ ./manage.py loaddata test_fixture.json
    $ ./manage.py runserver
    login to admin
    go to /admin/test_app/unchangeablemodel/

`#20640 <https://code.djangoproject.com/ticket/20640>`_

::

    $ ./manage.py syncdb
    $ ./manage.py loaddata test_fixture.json
    $ ./manage.py runserver
    login to admin
    go to /admin/test_app/unchangeablemodeldependency/
    select the UnchangeableModelDependency object
    action: "Delete selected unchangeable model dependencys"
    Go
