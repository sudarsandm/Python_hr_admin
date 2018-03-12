Human Resources Module
======================

hr module implemented for employees

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@github.com:hr/CommandlineUtility:``
3. Fetch development dependencies: ``make install``

Usage
=====

Pass in the employee inventory file in json format

::

    $ hr path/to/inventory.json

Pass in along with option ``--export`` and the file in json format

::

    $ hr --export path/to/inventory.json

Running Tests
-------------

Run tests locally using make if virtualenv is present

::

    $ make

Run tests using pipenv if virtualenv is not present

::

    $ pipenv run make
