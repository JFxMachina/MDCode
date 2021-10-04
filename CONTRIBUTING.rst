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

WIP

..
  # FIXME : Add some commit rules.

Pull Requests
-------------

WIP

..
  # FIXME : Add some Pull request rules.

Coding Standard
================

Style Guide
-----------

Contributions should (within reason!) adhere to the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide for python code.
For this purpose using the `pycodestyle <https://pypi.org/project/pycodestyle/>`_ is recommended.
Contributors are encouraged to skim over the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ and to refer to it in case of uncertantiy.

Testing
-------

Unit test for new code units should be written in parallel to the code units themselves.
Reviewers should check, whether code submitted in pull requests has sufficient test coverage.

..
  # FIXME : Add further instructions on how to write tests using pytest.

Documentation
-------------

Inline documentation for new code units should be written in parallel to the code units themselves.
While docstrings for small code units (functions, classes etc.) that are only used within the module can be omitted,
all code units that are accessed from other modules or scripts should at least have a basic docstring.

For functions the docstring should contain a brief and an extended description, a list of the expected arguments as well as a list of the return values.
If arguments are modified by the function, it should be noted as well.

For classes the docstring should contain a brief and an extended description. Eventual class and instance attributes should be documented as well.

For more information on how to proprely document python code, contributors are encouraged to skim overthe section on comments in `PEP 8 <https://www.python.org/dev/peps/pep-0008/#comments>`_, `PEP 257 - Docstring Conventrions <https://www.python.org/dev/peps/pep-0257/>`_, and the section on Abstract Syntax Mining in `PEP 258 <https://www.python.org/dev/peps/pep-0258/#ast-mining>`_ in which the types of docstrings that are included in automatic documentation generation are explained.

Reviewers should check, whether code submitted in pull requests has sufficient documentation coverage.
