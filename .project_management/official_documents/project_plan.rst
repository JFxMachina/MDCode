============
Project Plan
============
--------------------------------------------------------------------------------
Collaborative Software Engineering in Computational Physics 2021 Group 1 Project
--------------------------------------------------------------------------------

Involved parties
================

The stakeholders are Project-Group 1 and the customer, Rickard Armiento.

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
can be used to predict many varied materials properties. The continued
progression of computational power, storage capability, and improved
methodology has led to the application of these methods in high
throughput to produce large, openly available, databases of
theoretically predicted materials properties that are a major asset for
addressing materials design challenges.

Overview
--------

The project team will participate in the development of materials design
via high-throughput materials simulations and materials databases by
creating software for molecular dynamics simulations, operate this
software to determine materials properties on a large-scale materials
database, analyse and visualize the results to uncover any interesting
conclusions, make these results available online by participating in a
network of materials property databases, and deliver the outcome to the
customer.

The purpose of the project is to use modern software engineering
practices for conceiving, designing, and implementing computational
physics software and to operate this software in a study aligned with
present trends in database-driven materials design. The project is meant
to keep a high scientific and technical standard, providing
documentation in the form of relevant reports and a final presentation.

Aims and Goals
--------------

-  Design, implement, and operate a Molecular Dynamics (MD) program.
   This will require the team members to get insight into the inner
   workings of an MD code, how to interpret results obtained with the
   program, and assert the quality of these results. The work includes
   the correct selection and writing of code subroutines, debugging,
   testing, and operation of the program.

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

Project Phases
==============

Initiation phase
----------------

-  Lay out the aim, scope and goals of the project, as described above.

-  Create a team and assigning project roles.

-  Create and signing a group contract

Planning/Preparation phase
--------------------------

-  Create SRS and Project plan and have them approved by the customer.

-  Set up GitHub repository and project organization.

Execution phase
---------------

Divided into development phases and separated by milestones. Milestones
are defined with the help of epics to clearly signify when a phase is
done. A list of epics follows, grouped up to the development phase they
belong to.

Development Phase 1
-------------------

-  Create a uniform software development environment for all team
   members.

-  Create a working MD code compatible with OpenKIM potentials.

-  Create a working interface with one (or more) of high-throughput
   database APIs.

-  Create an elementary visualization and data analysis suite.

-  Set up the initial structure for documentation.

Development Phase 2
-------------------

-  Write a validation module and validate the MD code for accuracy with
   respect to literature.

-  Add High-throughput functionality to the code:

-  Given a dataset, write code to execute the MD code for batch
   simulations on a supercomputer.

-  Write code to create a user curated dataset to be used as input for
   the MD code.

-  Create an interface between the MD code and data analysis suite.

Development Phase 3
-------------------

-  Write a module which formats data to be used by utility libraries for
   OPTIMADE.

-  Perform the High throughput Molecular dynamics run, analyse results,
   and upload to the OPTIMADE network of databases via the API.

Development Phase 4
-------------------

-  Finalise documentation for all feature sets worked upon in previous
   development phases.

-  Create an interactive presentation for the customer exhibiting the
   features of the code.

End phase
---------

1. Deliver product (this includes the code and documentation) and final
   reports.

2. Present the product to the customer.

Organization Plan
=================

The structure of the team/organization is as follows:

**Costumer and expert**: Rickard Armiento

**Supervisor**: Abhijith S Parackal

**Project team**:

==================== ================================
Chi Xiao             Project leader, Developer
Utkarsh Singh        Scrum master, Developer
Joel Fischer         Product owner, Developer
Mehdi Nourazar       Testing responsible, Developer
Danial Shafizadeh    Documentation keeper, Developer
Gabriel Persson      Developer
==================== ================================

Document Plan
=============

As also specified in the Project directive and SRS, structured and
standardized documentation will be generated in parallel to the
development of each feature set (defined by an epic). Mainly, the
deliverables would be the SRS, Project plan, User Guide and a technical
manual (mostly auto-generated documentation) which details how the
software works internally.

Training Plan
=============

Project group 1 will be trained in aspects of modern collaborative
software engineering practices through hands-on sessions as part of the
course. The group may also schedule independent work sessions to better
understand certain practical aspects of Software development.

Report plan
===========

The customer will be informed of the progress in execution phase after
each sprint review meeting. After fulfilment of project closure
conditions (meeting delivery targets), a final presentation is held for
the customer, as specified in the Project directive and SRS. The final
project report will be delivered to the customer individually as the
final part of the project.

Meeting plan
============

The meeting plan is dictated by the project phases.

Before the execution phase:
---------------------------

-  Project group 1 meet for discussion and approval (internal) of the
   SRS.

-  A meeting with the customer is scheduled for the approval of SRS.
   After suggestions are implemented, approval is sought from the
   customer again.

-  Project group 1 meet for discussion and approval (internal) of the
   project plan.

-  A meeting with the customer is scheduled for the approval of Project
   Plan. After suggestions are implemented, approval is sought from the
   customer again.

During the execution phase:
---------------------------

-  A sprint planning meeting is scheduled to create a product backlog
   and breakdown epics into stories to assign tasks.

-  Three to four stand-up meetings are held during each sprint.

-  A final sprint review meeting at the end of each sprint, with the
   meeting notes communicated to the customer.

After the execution phase:
--------------------------

-  Internal review meeting to discuss if all of project deliverables are
   met and the closing condition is achieved.

-  A meeting with the customer is scheduled to demonstrate the working
   software.

Resource Plan
=============

Scientific software
-------------------

-  The MD program will be built using the ASAP and ASE software
   libraries, which should be helpful for this implementation. It is
   also suggested that the OpenKIM support in these libraries can be
   used to access interesting interatomic potentials.

-  Python, ASAP, and ASE are free software that can be downloaded and
   installed on most computers.

-  For information about the OPTIMADE open API, see
   https://www.optimade.org/

-  Helper software is available at
   https://github.com/Materials-Consortia/optimade-python-tools

Development tools
-----------------

-  PyTest, git and GitHub’s CI/CD (Actions) functionality will be used
   to automate testing and the development workflow.

-  Sphinx will be used for automated technical documentation generation.

-  GitHub Actions are available through GitHub Pro which is free for
   students.

-  Sphinx, pyTest and git are free and open-source, and can be
   downloaded and installed on most computers.

Time and computational resources
--------------------------------

The team is expected to do most of the development in the university
computer labs or on their own personal computers.

Milestones
==========

The milestones mark the end between the development phases and is listed
below in categories grouping them to the phase that they signify the end
of. They also have a global number for ease of reference.

Development phase 1
-------------------
1. Performed the first MD run using an input file.

2. Visualizing one property for one calculation.

Development phase 2
-------------------

3. Validation runs have good agreement with literature.

4. The MD code can run on the supercomputer.

5. The code can run a batch calculation of at least 10 materials and
automatically plot data using the results.

Development phase 3
-------------------

6. A large dataset of input materials has been simulated and the
respective results are available.

7. The results from the high-throughput run have been analysed and are
available via our OPTIMADE implementation.

Development phase 4
-------------------

8. Final iterations of User’s guide, Technical Documentation and Project
reports are ready.

9. Interactive presentation of completed project for the customer is
ready.

Risk analysis
=============

The identified risks are analysed, and their impact is minimized as
detailed in the ‘\ `Procedure for risk
analysis <https://teams.microsoft.com/l/file/76B9D9E9-AA20-4C2F-8FDF-E148DF7D5FB9?tenantId=913f18ec-7f26-4c5f-a816-784fe9a58edd&fileType=docx&objectUrl=https%3A%2F%2Fliuonline.sharepoint.com%2Fsites%2FCollaborativeSoftwareEngineeringProjectinComputationalPhysic-Projectgroup1%2FDelade%20dokument%2FProject%20group%201%2FOfficial%20Documents%2FProcedure%20for%20Risk%20Analysis.docx&baseUrl=https%3A%2F%2Fliuonline.sharepoint.com%2Fsites%2FCollaborativeSoftwareEngineeringProjectinComputationalPhysic-Projectgroup1&serviceName=teams&threadId=19:0fb2cf8412ff4e5b86a843f96f038d50@thread.tacv2&groupId=a831df63-c0c4-4c6e-a6c0-650c42f99daf>`__\ ’
(shared on Teams). The major risks to this project are identified and
analysed here.

Identified Risks
----------------

Technical risks:
^^^^^^^^^^^^^^^^

-  Poor testing, validation and documentation quality

-  The probability of risk occurrence is minimized by employing a good
   training plan for the team members, ensuring competency in each of
   these areas.

-  The impact of this risk is minimized by de-coupling parts of the
   feature set to decreasing the workload on task owners.

-  Loss of progress due to data loss (failure of computer resources or
   human error), repository breaking version control operations or
   feature breaking changes

-  The probability of risk occurrence is minimized by review of pull
   requests by multiple team members before the feature set is released
   to the main branch.

-  The impact of this risk is minimized by employing good version
   control practices.

-  Time-consuming feature integration

-  The probability of risk occurrence is minimized by ensuring
   compatibility between different feature sets.

-  The impact of this risk is minimized updating the product backlog for
   next sprint to accommodate this event and, if needed, re-negotiating
   the scope of the feature set.

Financial risks:
^^^^^^^^^^^^^^^^

-  Improper allocation of project budget

-  This probability of risk occurrence is minimized by, firstly,
   allocation of budget agreed upon by all team members, and review of
   budget allocation in previous sprints to reduce the error in further
   allocations.

-  The impact of this risk is minimized by assigning more team members
   to the task for which resources are lacking.

-  Improper refinement of product backlog

-  The probability of risk occurrence is minimized by review of product
   backlog in sprint planning.

-  The risk impact is minimized by tracking and updating the backlog
   through the sprint if needed.

Resource risks:
^^^^^^^^^^^^^^^

-  Loss of software resources (e.g., version conflicts in project
   dependencies)

-  The probability of risk occurrence is minimized by solely employing
   well-maintained external libraries to the code and reducing the
   overall number of dependencies.

-  The impact of this risk is minimized by developing the feature sets
   as standalone codes so that the failure of one feature set due to
   loss of software resources has minimal impact on the other parts.

-  Loss of human resources (e.g., team member leaving the project)

-  The probability of risk occurrence is minimized by signing a group
   contract.

-  The impact of this risk is minimized by assigning an owner and
   co-owner to the same task which ensures the reduction of knowledge
   loss if this event occurs.

Priorities
==========

The priorities for this project are as listed in the SRS. Overall, the
priority among the deliverables is set as follows. Note that at the
end of a sprint, negotiating with the customer to re-prioritize the
list is a possibility.

+--------------------------------------------+----------+------------+
| Deliverables                               | Priority | Negotiable |
+============================================+==========+============+
| An MD program capable of simulating the    | 5        | No         |
| materials that will be considered.         |          |            |
+--------------------------------------------+----------+------------+
| Tests that assure the quality of the MD    | 3        | No         |
| simulations.                               |          |            |
+--------------------------------------------+----------+------------+
| A large dataset of materials for which to  | 5        | No         |
| apply the MD code.                         |          |            |
+--------------------------------------------+----------+------------+
| Helper software / scripts for running MD   | 4        | No         |
| simulations in high throughput for the     |          |            |
| large dataset on supercomputers.           |          |            |
+--------------------------------------------+----------+------------+
| A results dataset created from the         | 5        | No         |
| high-throughput MD simulations for the     |          |            |
| large input dataset of materials.          |          |            |
+--------------------------------------------+----------+------------+
| Helper software / scripts for analysis,    | 3        | Yes        |
| data mining, and visualization of the      |          |            |
| results of the high-throughput MD          |          |            |
| simulations.                               |          |            |
+--------------------------------------------+----------+------------+
| Software for making the results dataset    | 2        | Yes        |
| available via the OPTIMADE open API and as |          |            |
| part of the OPTIMADE network of materials  |          |            |
| property databases.                        |          |            |
+--------------------------------------------+----------+------------+
| Main Reports / Documentation:              | 5        | No         |
|                                            |          |            |
| -  Specification of requirements           |          |            |
|                                            |          |            |
| -  Project plan                            |          |            |
|                                            |          |            |
| -  User’s guide                            |          |            |
|                                            |          |            |
| -  Technical documentation                 |          |            |
|                                            |          |            |
| -  Final report                            |          |            |
+--------------------------------------------+----------+------------+

Project Closing
===============

Closing condition: The project deliverables are met, and the end-product
is presented with a live demonstration.

