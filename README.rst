==========
TripleO UI
==========

This application serves the TripleO UI Frontend App for production use.

Development of the frontend app is done here:

https://github.com/rdo-management/rdo-director-ui


Installation
============

::

    $ sudo pip install tox
    $ cp app.conf.sample app.conf


The app will run on port 8888 if not otherwise defined in the `service`
section.

You can change the URLs of the Openstack API services in the `app`
section, if they're running on a different host.


Running the API server
======================

::

    $ tox -e venv tripleo-ui -- --config-file app.conf
