.. meta::
    :description: ROCm-DS release compatibility
    :keywords: Data-analytics, RAPIDS, cuDF, cuGraph, RMM, hipDF, hipGraph, hipMM, Pandas, NetworkX, High-Performance Computing, GPU Acceleration, GPU Computing, Parallel Computing, Scalable Data Science, Python

.. _contributing-to-rocm-ds:

*************************
Contributing to ROCm-DS
*************************

AMD welcomes contributions from the community to ROCm-DS and its components. Whether those contributions are bug reports, bug fixes,
documentation additions, performance notes, or other improvements, we value collaboration with our users. We can build
better solutions together. Please follow these details to help ensure your contributions will be successfully accepted.

Our code contribution guidelines closely follow the model of `GitHub pull-requests <https://help.github.com/articles/using-pull-requests/>`_. 
Pull requests should be made against the ``develop`` branch in the ROCm-DS components.

Issue Discussion
================

Use the GitHub Issues tab for issue notification. 

* Use your best judgment for issue creation. If your issue is already listed, upvote the issue and
  comment or post to provide additional details, such as how you reproduced this issue.
* If you're not sure if your issue is the same, err on the side of caution and file your issue.
  You can add a comment to include the issue number (and link) for the similar issue. If we evaluate
  your issue as being the same as the existing issue, we'll close the duplicate.
* If your issue doesn't exist, use the issue template to file a new issue.

  - When filing an issue, be sure to provide as much information as possible, including script output so we can collect
    information about your configuration. This helps reduce the time required to reproduce your issue.
  - Check your issue regularly, as we may require additional information to successfully reproduce the issue.

* You can also open an issue to ask the maintainers whether a proposed change meets the acceptance criteria or to discuss an idea about the library.

Acceptance Criteria
===================

With ROCm-DS we are interested in contributions that:

* Fix bugs, improve documentation, enhance testing, and reduce complexity.
* Improve the performance of existing routines.
* Add missing functionality found in one of the categories above.
* Add additional formats or allow an existing format to be used with an existing routine.

An opportunity exists here for contributors to add different algorithms that optimize for important user requirements and
performance considerations. We encourage contributors to leverage the GitHub "Issues" tab to discuss possible additions they would like to add.

Exceptions
----------

ROCm-DS places a heavy emphasis on being high performance. Because of this, contributions that add new routines (or that modify existing routines)
must do so from the perspective that they offer high performance in relation to the hardware they are run on.

Additionally, when adding new routines, these routines must offer enough value to enough users to be deemed worth including. Because compile times,
binary sizes, and general library complexity are important considerations, we reserve the right to decide whether a proposed routine is
too niche or specialized to be worth including.

Code Structure
==============

The following is the structure of ROCm-DS library in the GitHub repository.

* The ``library/include/`` directory contains the header files (which itself includes headers
  defining the public API). The ``library/include/`` directory also contains the headers for all public types.
* The ``library/src/`` directory contains the implementations of routines. These implementations
  are broken up into directories describing the category the routine belongs to. These directories
  contain both the C++ and HIP kernel code.
* The ``clients/`` directory contains the testing and benchmarking code as well as all the samples demonstrating usage.
* The ``docs/`` directory contains all of the documentation files.
* The ``scripts/`` directory contains potentially useful Python and shell scripts for downloading
  test matrices (see ``scripts/performance/matrices/``) as well as plotting tools.

Coding Style
============

In general, follow the style of the surrounding code. C and C++ code is formatted using ``clang-format``. Use the clang-format version installed with
ROCm (found in the ``/opt/rocm/llvm/bin`` directory). Please do not use your system's built-in ``clang-format``, as this is a different version that may result in incorrect results.

To format a file, use:

.. code:: bash

  /opt/rocm/hcc/bin/clang-format -style=file -i <path-to-source-file>


Also, githooks can be installed to format the code per-commit:

.. code:: bash

  ./.githooks/install

Pull Request Guidelines
=======================

When you create a pull request, you should target the default branch. Our current default branch is the **develop** branch, which serves as our integration branch.

Deliverables
------------

When raising a PR in ROCm-DS, here are some important things to include:

1. For each new file in the repository, include the following licensing header
and adjust the date to the current year. When simply modifying a file, the date should
automatically be updated when using the pre-commit script.


.. code-block:: cpp

    /* ************************************************************************
    * Copyright (C) 20xx Advanced Micro Devices, Inc. All rights Reserved.
    *
    * Permission is hereby granted, free of charge, to any person obtaining a copy
    * of this software and associated documentation files (the "Software"), to deal
    * in the Software without restriction, including without limitation the rights
    * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    * copies of the Software, and to permit persons to whom the Software is
    * furnished to do so, subject to the following conditions:
    *
    * The above copyright notice and this permission notice shall be included in
    * all copies or substantial portions of the Software.
    *
    * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    * THE SOFTWARE.
    *
    * ************************************************************************ */

2. When adding a new routine, please make sure you are also adding appropriate testing code. These new unit tests should
integrate within the existing `googletest framework <https://github.com/google/googletest/blob/main/docs/primer.md>`_.
This typically involves adding the following files:

  * ``testing_<routine_name>.cpp`` file in the directory ``clients/testing/``
  * ``test_<routine_name>.cpp`` file in directory ``clients/tests/``
  * ``test_<routine_name>.yaml`` file in directory ``clients/tests/``

  See existing tests for guidance when adding your own.

3. When modifying an existing routine, add appropriate testing to ``test_<routine_name>.yaml`` file in directory ``clients/tests/``.

4. Tests must have good code coverage. 

5. Ensure code builds successfully. This includes making sure that the code can compile, that the code is properly formatted, and that all tests pass.

6. Don't break existing tests.

Process
-------

When a PR is raised targeting the develop branch in ROCm-DS, CI will be automatically triggered. This will:

* Test that the PR passes static analysis (that is, ensure clang formatting rules have been followed).
* Test that the documentation can be properly built
* Ensure that the PR compiles on different OS and GPU device architecture combinations.
* Ensure that all tests pass on different OS and GPU device architecture combinations

Feel free to ask questions on your PR regarding any CI failures you encounter.

* Reviewers are listed in the CODEOWNERS file
