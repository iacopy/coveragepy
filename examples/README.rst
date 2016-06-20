Examples
========

This directory contains (mainly) some examples of python code and aims to be used for manual testing during coverage development.

Also contains some useful bash script as example for the usage.


* Setup

.. code:: bash

    # Setup virtualenv
    $ [sudo] pip install virtualenv
    $ cd go/to/coverage/root/directory
    $ virtualenv -p python3.5 ENV

    # Activate virtualenv
    $ source ENV/bin/activate

    # Build coverage
    $ python setup.py install


* Workflow


.. code:: bash

    # Update the code...
    # Update the build:
    $ python setup.py install

    # Run and see coverage results
    $ rm -rf htmlcov/
    $ coverage erase
    $ coverage run [--timid] [--branch] test_zero.py  # for example
    $ coverage html
    $ open htmlcov/index.html


* Teardown

.. code:: bash

    # Deactivate the virtualenv
    $ deactivate
