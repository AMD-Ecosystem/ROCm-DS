.. meta::
    :description: ROCm-DS release compatibility
    :keywords: Data-analytics, RAPIDS, cuDF, cuGraph, RMM, hipDF, hipGRAPH, hipMM, Pandas, NetworkX, High-Performance Computing, GPU Acceleration, GPU Computing, Parallel Computing, Scalable Data Science, Python

.. _contributing-to-rocm-ds:

*************************
Contributing to ROCm-DS
*************************

AMD appreciates and values your interest in contributing to the ROCm Data Sciences (ROCm-DS) stack. This collection of libraries — hipDF, hipGRAPH,
hipMM, hipRAFT, and hipVS — is a fork of the RAPIDS® open-source project from NVIDIA and brings high-performance, GPU-accelerated data science,
graph analytics, mathematical computation, and vector search to the ROCm ecosystem. 
 
You can contribute in several ways: reporting bugs or requesting new features, improving documentation, performance optimizations,
porting functionality from equivalent CUDA-based libraries, writing or improving tests.  If you want to contribute to our ROCm-DS
repositories, review the guidance below to help ensure your contributions are accepted. 

Development workflow
====================

The ROCm-DS project uses GitHub to host the code, collaborate within the community, and manage version control. The project relies on pull requests
for all changes within the repositories, ensuring that contributions are reviewed and discussed before being merged into the main codebase. This
helps maintain code quality and consistency. The ROCm-DS project uses GitHub issues to track bugs, feature requests, and other-project related tasks,
providing a transparent and organized way to monitor progress and prioritize work. 

Issue tracking
--------------

* Use the GitHub Issues tab for each project — hipDF, hipGRAPH, hipMM, hipRAFT, and hipVS.                   
* Before opening a new issue, search for existing issues to avoid duplicates. If the issue exists, upvote it and add details or a minimal reproducer.
* If you’re unsure whether your issue matches an existing one, file your issue and reference the similar issue number. If it is a duplicate,
  it will be closed and tracked through the original issue.
* When filing a new issue, use the repository issue template.
* Include as much context as possible:

  - ROCm version, GPU model(s), architecture(s), OS and version, kernel/driver versions
  - Compiler/CMake/Python versions, branch or tag, commit SHA
  - Exact commands run, logs, stack traces, and a minimal reproducer
  - Expected vs. actual behavior

* Monitor your issue for follow-up as additional information may be needed.
* You can also open an issue to ask whether a proposed change meets the acceptance criteria or to discuss an idea about the library.

Coding style
------------

In general, follow the style of the surrounding code. HIP, C and C++ code is formatted using clang-format.  

Also, githooks can be installed to format the code pre-commit: 
 
.. code:: bash

    pip install pre-commit # Install pre-commit into your python environement
    cd <REPO_ROOT>
    pre-commit install # Install the githooks using pre-commit

Pull Request Guidelines
=======================

* Identify the issue you want to fix
* When you create a pull request, you should target the default branch. Our repositories typically use the develop branch as the default integration branch.
* For each new file in the repository, include the following licensing header and adjust the date to the current year. When simply modifying a file, the date should automatically be updated when using the pre-commit script.

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

* Ensure your code builds successfully
* Each component has a suite of test cases to run; include the log of the successful test run in your PR
* Do not break existing test cases
* New functionality is only merged with new unit tests
* If your PR includes a new feature, you must provide an application or test to ensure that the feature works and continues to be valid in the future
* Submit your PR and work with a reviewer or maintainer to get your PR approved
* Once approved, the PR is brought onto internal CI systems and may be merged into the component during the release cycle, as coordinated by the maintainer
* After your change is committed you will receive notification

Thank you for contributing
==========================

AMD and the ROCm-DS community appreciate your time, effort, and expertise. Every contribution, whether big or small, plays a vital role in making the project
better and more impactful to the entire community. Your involvement helps drive innovation, enhance the quality of the software, and ensures
the continued success of ROCm-DS. We look forward to collaborating with you and are excited to see the positive changes you'll bring to the project!
