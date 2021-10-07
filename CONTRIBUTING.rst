CONTRIBUTING
************

Introduction
============

To assure code quality and maintainability as well as tidiness of the repository, a few rules to be followed by contributors are in place.
This is especially important, since the goal of this project is to learn about, and gain experience in *collaborative* software development.
Contributors are thus asked to read and follow the instructions laid out in this document. 

Git Workflow
============

The MDCode project uses a `Shared Repository Model <https://docs.github.com/en/github/collaborating-with-pull-requests/getting-started/about-collaborative-development-models>`_.
Contributors can open different branches (e.g. feature, bugfix, experimental) of this repository and commit on, push to, pull from them. Once their work on said branch is done, a `Pull Request <https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>`_ is submitted to merge into the development (`dev <https://github.com/JFxMachina/MDCode/dev>`_) branch.
Pull requests for the `dev <https://github.com/JFxMachina/MDCode/dev>`_ branch require at least two reviews to be accepted. Pull requests into the `main <https://github.com/JFxMachina/MDCode/main>`_ are only allowd from the `dev <https://github.com/JFxMachina/MDCode/dev>`_ branch and require at least three reviews to be accepeted. 

Branching
---------

While pushing to the main and dev branches is prohibited, contributors are free to create branches for feature development, testing, bug fixing etc.
For opening new branches, the following naming convention shall be used:

<TYPE>/<description-of-the-branch>

Where <TYPE> describes the nature of the branch and can be one of the following:

* BUG - For bug fixing
* WIP - For feature development
* EXP - For testing and experimental development

..
  # FIXEME : We should probably all agree on what to actually use.

The <description-of-the-branch> can be made up of multiple words separated by hyphens (`-`), however it should be kept as short as possible while still adequately describing what the branch is used for.

Commits
-------

Commits should cover individual but complete changes to the code base. E.g. when adding a module, commits should encompass the creation of for example a function, a class, or functionality. I.e. commit once your work on a code unit is done, and not mid way through editing. A good rule of thumb is, that you should be able to describe the changes in a simple sentence without having to go into too much details.

Commit messages should be as short as possible while still adequately describing the changes made and can either be made up of only a subject (brief description) or a subject and a body (detailed description). The subject should be written in the imperative form with the first letter capitalized and no punctuation at the end of the message. For reference, the reader is encouraged to take a look at `this blog post<https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide>`_.

Pull Requests
-------------

Pull requests into the `dev <https://github.com/JFxMachina/MDCode/tree/dev>`_ branch should (generally) only be issued once work on one or more issues is complete. They will generally only be granted once all tests are passed and the changes have been reviewd by two individual contributors (Exceptions can be made).
Pull requests into the `main <https://github.com/JFxMachina/MDCode/tree/main`_ branch are only accepted from the dev branch and require reviews by three individual contributors.

If the pull request closes some issue, it should be marked in the message.

Coding Standard
================

Style Guide
-----------

Contributions should (within reason!) adhere to the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide for python code.
For this purpose using the `pycodestyle <https://pypi.org/project/pycodestyle/>`_ is recommended.
Contributors are encouraged to skim over the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ and to refer to it in case of uncertantiy.

Naming conventions
^^^^^^^^^^^^^^^^^^

The PEP8 naming conventions are summarized bellow:

+----------------------------+--------------------+---------------------+
| Type                       | Public             | Internal            |
+============================+====================+=====================+
| Packages                   | lower              |                     |
+----------------------------+--------------------+---------------------+
| Modules                    | lower[#f1]         | _lower[#f1]         |
+----------------------------+--------------------+---------------------+
| Classes                    | CapWords           | _CapWords           |
+----------------------------+--------------------+---------------------+
| Exceptions                 | CapWords           |                     |
+----------------------------+--------------------+---------------------+
| Functions                  | lower_with_under() | _lower_with_under() |
+----------------------------+--------------------+---------------------+
| Global/Class Constants     | CAPS_WITH_UNDER    | _CAPS_WITH_UNDER    |
+----------------------------+--------------------+---------------------+
| Global/Class Variables     | lower_with_under   | _lower_with_under   |
+----------------------------+--------------------+---------------------+
| Instance Variables         | lower_with_under   | _lower_with_under   |
+----------------------------+--------------------+---------------------+
| Method Names               | lower_with_under() | _lower_with_under() |
+----------------------------+--------------------+---------------------+
| Function/Method Parameters | lower_with_under   |                     |
+----------------------------+--------------------+---------------------+
| Local Variables            | lower_with_under   |                     |
+----------------------------+--------------------+---------------------+

Module imports
^^^^^^^^^^^^^^

Star imports eg.
::

	from <somepackage>.<some_module> import *

are not to be used, as this pollutes the namespace, interferes with linting and generally makes the code harder to understand and less maintainable.

Testing
-------

Unit test for new code units should be written in parallel to the code units themselves.
Reviewers should check, whether code submitted in pull requests has sufficient test coverage.

Test modules (files containing tests) can contain tests for multiple different code units. They must be named and placed in the tests folder or one of its subfolders according to the following scheme:

If the test module contains (amongst others) a test testing the entire module 'some_module' in package 'somepackage' it is placed at
::

	'tests/<somepackage>/<some_module>_test.py'

If, on the other hand, the test module only contains tests for a specific part of the module (e.g. a class 'SomeClass' or a function 'some_function') it is placed at
::

	'tests/<somepackage>/<some_module>_<SomeClass>_test.py'

or
::

	'tests/<somepackage>/<some_module>_<some_function>_test.py'

respectively.

To run the tests, call pytest from the project root directory.

Documentation
-------------

Inline documentation for new code units should be written in parallel to the code units themselves.
While docstrings for small code units (functions, classes etc.) that are only used within the module can be omitted,
all code units that are accessed from other modules or scripts should at least have a basic docstring.

For functions the docstring should contain a brief and an extended description, a list of the expected arguments as well as a list of the return values.
If arguments are modified by the function, it should be noted as well.

For classes the docstring should contain a brief and an extended description. Eventual class and instance attributes should be documented as well.

For more information on how to proprely document python code, contributors are encouraged to skim overthe section on comments in `PEP 8 <https://www.python.org/dev/peps/pep-0008/#comments>`_, `PEP 257 - Docstring Conventrions <https://www.python.org/dev/peps/pep-0257/>`_, and the section on Abstract Syntax Mining in `PEP 258 <https://www.python.org/dev/peps/pep-0258/#ast-mining>`_ in which the types of docstrings that are included in automatic documentation generation are explained.
For a quick guide on writing reStructuredText, please refer to the `Sphinx and RST syntax guide <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_.

Reviewers should check, whether code submitted in pull requests has sufficient documentation coverage.

To build the documentation locally, go to the doc directory and run
::

	source run_sphinx.sh

.. rubic:: Footnotes
.. [#f1] If it improves readability lower_with_under can be used for modules as well.
