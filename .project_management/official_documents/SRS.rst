===================================
Software Requirements Specification
===================================
--------------------------------------------------------------------------------
Collaborative Software Engineering in Computational Physics 2021 Group 1 Project
--------------------------------------------------------------------------------

Disclaimer
==========

Some parts of this document have been reproduced from *Collaborative
Software Engineering Project in Computational Physic – Project
directive* by Rickard Armiento without explicit permission.

Involved Parties
================

**Costumer and expert**: Rickard Armiento

**Supervisor**: Abhijith S Parackal

**Project team**:

Chi Xiao Project leader, Developer

Utkarsh Singh Scrum master, Developer

Joel Fischer Product owner, Developer

Mehdi Nourazar Testing responsible, Developer

Daniel Shafizadeh Documentation keeper, Developer

Gabriel Persson Developer

Introduction
============

Background
----------

The design of new materials with desired properties is a crucial step in
making innovative technologies viable. A typical challenge in materials
design is to find materials that fulfil specific requirements on
efficiency, cost, environmental impact, length of life, safety, and
other properties. Theoretical investigation of hypothetical material
candidates and system configurations by computational materials
simulations have become a standard tool in this field. These simulations
help us understand the physics of materials and systems of molecules and
can be used to predict many different materials properties. The
continued progression of computational power, storage capability, and
improved methodology, has led to the application of these methods in
high throughput to produce large, openly available, databases of
theoretically predicted materials properties that are a major asset for
addressing materials design challenges

Aims and goals
--------------

The purpose of the project is to use modern software engineering
practices for conceiving, designing, and implementing computational
physics software and to operate this software in a study aligned with
present trends in database-driven materials design. The project is meant
to keep a high scientific and technical standard, providing
documentation in the form of relevant reports and a final presentation.

The goals of the project can be summarized as follows:

-  Design, implement and operate a Molecular Dynamics (MD) program.

-  Develop the software with modern collaborative software engineering
   practices.

-  Extract an extensive set of hypothetical materials using one of the
   large online materials databases available.

-  Apply high-throughput methodology to run the MD code on
   supercomputers to build a database of relevant materials properties
   for the materials in the extracted dataset.

-  Analyse, data mine, and visualize the results, e.g., using property
   scatterplots to look at interesting general correlations and
   outliers.

-  Make the results available via the OPTIMADE network of materials
   property databases.

-  Advance currently available data for, and understanding of, materials
   via custom-made materials simulations based on molecular dynamics,
   making the resulting data available as open data.

Overall description
===================

The main product is a molecular dynamics (MD) program for simulating a
set of hypothetical materials. Said MD program should include
functionalities for:

-  Creating/extracting and pre-processing a large dataset of
   hypothetical materials

-  Simulating a hypothetical material to retrieve material properties

-  Running the simulation on high-throughput supercomputers

-  Post-processing, analysing and visualising simulation results

-  Making simulation results available as part of the OPTIMATE network
   of materials property databases

Secondary products include:

-  A large dataset of hypothetical materials for which to apply the MD
   program to

-  A corresponding result dataset

-  Documentation for the main deliverable in the form of technical
   documentation and a user’s guide

-  A final report and presentation

Description of the overall design and system parts
--------------------------------------------------

*Disclaimer*: *The design detailed here is not to be understood as a
strict imposition but as a conceptional guideline that can also be
subject to change.*

The MD core program should accept a material described by the atom types
and positions in a unit cell perform a molecular dynamics simulation to
resolve relevant properties. The ASE python library will be used to
create a representation of the material and run/control the simulation.
The actual MD simulation will be performed using the
`ASAP <https://wiki.fysik.dtu.dk/asap>`__ python library, the interface
to which is already provided in the
`ASE <https://wiki.fysik.dtu.dk/ase/>`__ library. This part is integral
to the whole project and should be able to work standalone. It should
either take input in form of a simple text file or alternatively in form
of a more sophisticated structure such as a Pandas DataFrame (or
similar). The materials thus supplied will be simulated in a sequential
manner. Scaling is achieved by independently running the program on
different batches of materials in parallel as well as parallelizing the
individual material simulation to take advantage of a high performance
multi core computer architecture. The output should again be in the form
of a simple text file or a DataFrame (or similar) binary. Possible file
formats include CSV for ease of use, Feather for speed, or hdf5 as a
platform independent compromise between speed and ease of use. OPTIMADE
conventions and its API should be taken into consideration when
designing the program output.

The creation, pre-processing, post-processing and analysis will be
performed in either separate python scripts or separate full-fletched
python modules.

Depending on the chosen input method and the source of the hypothetical
materials the input data need a full list of parameters for the active
interaction potential, complete structure information, periodic boundary
directions, total time of simulation, temperature, pressure, and atomic
species data for the hypothetical material in question.

Requirements on the complete system
-----------------------------------

The requirements on the complete system are covered by the requirements
on the system parts and are thus not explicitly specified here.

System Parts
============

MD simulation / Core System

+---+----------+----------------------------------------+-----------+
|   | Original | The MD program can successfully        | Very High |
|   |          | simulate a single material when        |           |
|   |          | provided with input of the specified   |           |
|   |          | form                                   |           |
+===+==========+========================================+===========+
|   | Original | The MD program can sequentially        | Very High |
|   |          | simulate batches of materials          |           |
+---+----------+----------------------------------------+-----------+
|   | Original | The MD program is parallelized to take | Medium    |
|   |          | advantage of HPC hardware              |           |
+---+----------+----------------------------------------+-----------+
|   | Original | The MD program can reproduce           | High      |
|   |          | properties of a known material         |           |
+---+----------+----------------------------------------+-----------+
|   | Original | The MD program generates a summary     | Low       |
|   |          | report                                 |           |
+---+----------+----------------------------------------+-----------+

Pre-processing / Database scraper

+---+----------------+--------------------------+--------+
|   | Original       | The pre-processing       | High   |
|   |                | module can generate or   |        |
|   |                | extract a large (more    |        |
|   |                | than can be handled      |        |
|   |                | manually) set of         |        |
|   |                | hypothetical materials   |        |
+===+================+==========================+========+
|   | Initial Review | Have an interface to at  | High   |
|   |                | least one of the         |        |
|   |                | following                |        |
+---+----------------+--------------------------+--------+
|   | Sub            | Have an interface which  | Medium |
|   |                | uses the                 |        |
|   |                | materialsproject.org API |        |
+---+----------------+--------------------------+--------+
|   | Sub            | Have an interface which  | Medium |
|   |                | uses the aflow.org API   |        |
+---+----------------+--------------------------+--------+
|   | Sub            | Have an interface which  | Medium |
|   |                | uses the oqmd.org API    |        |
+---+----------------+--------------------------+--------+
|   | Original       | The pre-processing       | High   |
|   |                | module can generate      |        |
|   |                | input of the form        |        |
|   |                | required by the MD       |        |
|   |                | program from             |        |
|   |                | aforementioned set of    |        |
|   |                | hypothetical materials   |        |
+---+----------------+--------------------------+--------+

Post-processing / Analysis

+---+----------+----------------------------------------+-----------+
|   | Original | The post-processing module can extract | Very High |
|   |          | and visualize interesting information  |           |
|   |          | about the simulated materials from the |           |
|   |          | MD program output                      |           |
+===+==========+========================================+===========+
|   | Original | The post-processing module can find    | High      |
|   |          | and visualize correlations in a large  |           |
|   |          | set of simulated materials             |           |
+---+----------+----------------------------------------+-----------+
|   | Original | The post processing module enables     | Very High |
|   |          | calculation and visualisation of time  |           |
|   |          | averaged properties for inorganic      |           |
|   |          | solid materials including but not      |           |
|   |          | limited to...                          |           |
+---+----------+----------------------------------------+-----------+
|   | Sub      | … the thermal expansion                | High      |
+---+----------+----------------------------------------+-----------+
|   | Sub      | … specific heat                        | High      |
+---+----------+----------------------------------------+-----------+
|   | Sub      | … compressibility                      | High      |
+---+----------+----------------------------------------+-----------+
|   | Sub      | … speed of sound                       | High      |
+---+----------+----------------------------------------+-----------+
|   | Original | The post-processing module generates a | Low       |
|   |          | summary report                         |           |
+---+----------+----------------------------------------+-----------+

OPTIMADE interface

+---+----------+---------------------------------------------+------+
|   | Original | The software enables to upload the produced | High |
|   |          | data using the OPTIMADE API                 |      |
+---+----------+---------------------------------------------+------+

HPC dispatch script

+---+----------+---------------------------------------------+------+
|   | Original | A script is available that launches         | High |
|   |          | multiple simulations on a HPC cluster       |      |
+---+----------+---------------------------------------------+------+

Other Deliverables

Input dataset

+---+----------+-------------------------------------------+--------+
|   | Original | The input dataset consists of at least    | Medium |
|   |          | 100 hypothetical materials                |        |
+===+==========+===========================================+========+
|   | Original | The input dataset is chosen               | Medium |
|   |          | systematically (promising or interesting  |        |
|   |          | and previously unexplored materials)      |        |
+---+----------+-------------------------------------------+--------+
|   | Original | The input dataset includes at least 3     | High   |
|   |          | materials with known properties which     |        |
|   |          | will serve as benchmark                   |        |
+---+----------+-------------------------------------------+--------+

Result dataset

+---+----------+-------------------------------------------+--------+
|   | Original | The result dataset covers the input       | Medium |
|   |          | dataset except for documented failures    |        |
+---+----------+-------------------------------------------+--------+

Documentation

C.f. the Documentation section below.

Final Report and Presentation

+---+----------+-------------------------------------------+--------+
|   | Original | The final report covers the code (design  | High   |
|   |          | and implementation specifics)             |        |
+===+==========+===========================================+========+
|   | Original | The final report covers the choice of     | Medium |
|   |          | materials                                 |        |
+---+----------+-------------------------------------------+--------+
|   | Original | The final report covers the results of    | High   |
|   |          | the simulations                           |        |
+---+----------+-------------------------------------------+--------+
|   | Original | The final presentation covers the code    | High   |
|   |          | (design and implementation specifics)     |        |
+---+----------+-------------------------------------------+--------+
|   | Original | The final presentation covers the choice  | Medium |
|   |          | of materials                              |        |
+---+----------+-------------------------------------------+--------+
|   | Original | The final presentation covers the results | High   |
|   |          | of the simulations                        |        |
+---+----------+-------------------------------------------+--------+
|   | Original | The final presentation covers details     | Low    |
|   |          | about the collaborative workflow and      |        |
|   |          | project management                        |        |
+---+----------+-------------------------------------------+--------+
|   | Original | The final presentation covers experiences | Low    |
|   |          | gained from the collaboration             |        |
+---+----------+-------------------------------------------+--------+

Performance requirements
========================

The software should preform to the level of simulating a basic crystal
structure i.e. standard cubic, body centred cubic or face centred cubic
for a period that is in the order of magnitude of Femto-seconds under a
reasonable computational time.

+---+----------------+--------------------------+--------+
|   | Original       | Cubic, bcc and fcc       | High   |
|   |                | materials can be         |        |
|   |                | simulated with           |        |
|   |                | reasonable performance   |        |
|   |                | compared to other        |        |
|   |                | similar software         |        |
+===+================+==========================+========+
|   | Original       | The code has been        | Medium |
|   |                | profiled and major       |        |
|   |                | unnecessary bottlenecks  |        |
|   |                | are avoided              |        |
+---+----------------+--------------------------+--------+
|   | Initial Review | A profiler report is     | Low    |
|   |                | delivered together with  |        |
|   |                | the other deliverables   |        |
+---+----------------+--------------------------+--------+

Testing
=======

The development process will be supported by an automated test module
that ensures that all previously implemented functionality is working as
intended with every addition and expansion of the software. Unit tests
are written in parallel to forementioned additions and expansions.

+---+----------+----------------------------------------+-----------+
|   | Original | CI test framework is in place for unit | Very High |
|   |          | and integration tests                  |           |
+===+==========+========================================+===========+
|   | Original | System test is in place (script for    | High      |
|   |          | benchmark run with known materials or  |           |
|   |          | manual test protocol)                  |           |
+---+----------+----------------------------------------+-----------+
|   | Original | Unit tests for all code units of       | Medium    |
|   |          | reasonable size are in place           |           |
+---+----------+----------------------------------------+-----------+
|   | Original | System test passes at the delivery     | Medium    |
+---+----------+----------------------------------------+-----------+
|   | Original | All automated tests pass at the end of | Medium    |
|   |          | each sprint                            |           |
+---+----------+----------------------------------------+-----------+

Stability
=========

+---+----------+-----------------------------------------------------------+--------+
|   | Original | Unit tests cover edge-cases where reasonable              | High   |
+===+==========+===========================================================+========+
|   | Original | Code has been run on a large dataset without major issues | Medium |
+---+----------+-----------------------------------------------------------+--------+

Delivery
========

== ======== ================================== ====
\  Original All products are delivered on time High
== ======== ================================== ====

Documentation
=============

Inline Documentation

+---+----------+----------------------------------------------------------+--------+
|   | Original | Reasoning and design choices are explained with comments | Medium |
+---+----------+----------------------------------------------------------+--------+

Technical Documentation

+---+----------------+--------------------------+--------+
|   | Original       | Sphinx documentation     | High   |
|   |                | generated                |        |
+===+================+==========================+========+
|   | Original       | Documentation hosted on  | Medium |
|   |                | read-the-docs in         |        |
|   |                | conjunction with GitHub  |        |
+---+----------------+--------------------------+--------+
|   | Original       | All classes, modules,    | High   |
|   |                | scripts and functions    |        |
|   |                | are documented with a    |        |
|   |                | basic docstring          |        |
|   |                | describing their         |        |
|   |                | function and purpose     |        |
+---+----------------+--------------------------+--------+
|   | Original       | Functions and classes    | Medium |
|   |                | that are directly used   |        |
|   |                | by the user have usage   |        |
|   |                | examples included in the |        |
|   |                | docstring                |        |
+---+----------------+--------------------------+--------+
|   | Original       | Class member attributes  | High   |
|   |                | are documented in the    |        |
|   |                | \__init_\_ method        |        |
+---+----------------+--------------------------+--------+
|   | Original       | Functions have a list of | High   |
|   |                | expected arguments and   |        |
|   |                | return values            |        |
+---+----------------+--------------------------+--------+
|   | Initial Review | The technical            | High   |
|   |                | documentation includes a |        |
|   |                | review of the inner      |        |
|   |                | workings of the          |        |
|   |                | simulation from a        |        |
|   |                | physics point of view    |        |
+---+----------------+--------------------------+--------+
|   | Initial Review | The technical            | High   |
|   |                | documentation includes a |        |
|   |                | review of the validation |        |
|   |                | of the implemented       |        |
|   |                | physics                  |        |
+---+----------------+--------------------------+--------+

User’s Guide

+---+----------+-----------------------------------------+----------+
|   | Original | The user’s guide includes an            | High     |
|   |          | Installation Guide                      |          |
+===+==========+=========================================+==========+
|   | Original | The user’s guide includes a short       | Medium   |
|   |          | overview                                |          |
+---+----------+-----------------------------------------+----------+
|   | Original | The user’s guide includes a tutorial    | High     |
|   |          | with example data (e.g. reproduce       |          |
|   |          | benchmark runs)                         |          |
+---+----------+-----------------------------------------+----------+
|   | Original | The user’s guide includes a tutorial on | Low      |
|   |          | how to run the program a on computing   |          |
|   |          | cluster                                 |          |
+---+----------+-----------------------------------------+----------+
|   | Original | The user’s guide includes a section     | Very Low |
|   |          | about further reading and references    |          |
+---+----------+-----------------------------------------+----------+

Repository Documentation

+---+----------+-----------------------------------------+----------+
|   | Original | A README which guides user to other     | High     |
|   |          | useful documents is available in the    |          |
|   |          | repository                              |          |
+===+==========+=========================================+==========+
|   | Original | A LICENSE has been chosen and is        | High     |
|   |          | available in the repository             |          |
+---+----------+-----------------------------------------+----------+
|   | Original | A CONTRIBUTING file which explains      | Low      |
|   |          | basic rules for contributing is         |          |
|   |          | available in the repository             |          |
+---+----------+-----------------------------------------+----------+
|   | Original | Further typical files are present in    | Very Low |
|   |          | the repository                          |          |
+---+----------+-----------------------------------------+----------+

Quality & Maintainability
=========================

The quality of the code will be kept high by the requirement of
independent project members verification on every merge from the
development branch to the main branch to guarantee code style,
functionality, and proper documentation.

Maintainability is ensured by proper Technical and inline documentation,
the use of few and mostly widespread libraries and a clean git history
and workflow. External and internal dependencies are kept to a minimum.
If necessary, implementation independent interfaces are provided in the
form of abstract base classes to allow for different subsystems to be
exchanged or modified.

No long-term maintenance after the delivery is currently foreseen.
However, this does not mean than maintainability should be disregarded.

+---+----------------+-------------------------+-----------+
|   | Original       | The source code is      | Very High |
|   |                | hosted on a git         |           |
|   |                | repository              |           |
+===+================+=========================+===========+
|   | Original       | A CONTRIBUTING file is  | High      |
|   |                | available in the        |           |
|   |                | repository and explains |           |
|   |                | the rules to be         |           |
|   |                | followed (coding        |           |
|   |                | standard, git workflow) |           |
+---+----------------+-------------------------+-----------+
|   | Original       | Appropriate review      | High      |
|   |                | rules for pull requests |           |
|   |                | on different branches   |           |
|   |                | are in place            |           |
+---+----------------+-------------------------+-----------+
|   | Original       | The CONTRIBUTING file   | High      |
|   |                | has clear instructions  |           |
|   |                | regarding commits and   |           |
|   |                | pull requests           |           |
+---+----------------+-------------------------+-----------+
|   | Initial Review | The delivered source    | High      |
|   |                | code follows a modern   |           |
|   |                | coding standard         |           |
+---+----------------+-------------------------+-----------+
