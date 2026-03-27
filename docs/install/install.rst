.. meta::
    :description: ROCm-DS release compatibility
    :keywords: Data-analytics, RAPIDS, cuDF, cuGraph, RMM, hipDF, hipGraph, hipMM, Pandas, NetworkX, High-Performance Computing, GPU Acceleration, GPU Computing, Parallel Computing, Scalable Data Science, Python

.. _linux-install:

**************************************************************************************
Installing ROCm-DS
**************************************************************************************

This topic provides brief guidance and recommendations on setting up your environment and installing ROCm-DS components.

System requirements
===================

The following are the ROCm-DS release compatibilities and system requirements: 

* ROCm version: `7.2.0 <https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/>`__ and `7.2.1 <https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.1/>`__
* Operating Systems: Ubuntu 24.04 and 22.04  
* AMD Instinct GPUs: 

  - MI350X / MI355X (GPU target gfx950) 
  - MI300A / MI300X (GPU target gfx942) 
  - MI250X / MI250 / MI210 (GPU target gfx90a) 

* Python versions: 3.10, 3.11, 3.12, 3.13

Installation instructions
=========================

Each ROCm-DS 26.03 component must be separately installed as needed. The installation instructions for each component can be found as follows: 

* `hipDF Installation instructions <https://rocm.docs.amd.com/projects/hipdf-internal/en/docs-rocmds-26.03/install/INSTALL.html>`__
* `hipMM Installation instructions <https://rocm.docs.amd.com/projects/hipMM-internal/en/docs-rocmds-26.03/install/INSTALL.html>`__
* `hipGRAPH Installation instructions <https://rocm.docs.amd.com/projects/hipGRAPH/en/latest/install/Linux_Install_Guide.html>`__
* `hipRAFT Installation instructions <https://rocm.docs.amd.com/projects/hipRAFT-internal/en/amd-integration/install/install.html>`__
* `hipVS Installation instructions <https://rocm.docs.amd.com/projects/hipvs-internal/en/amd-integration/install/install.html>`__
* `dask-hip Installation instructions <https://rocm.docs.amd.com/projects/dask-hip-internal/en/dev-suphilip-add_amd_documentation/install/install.html>`__
* `hip-ucxx Installation instructions <https://rocm.docs.amd.com/projects/hip-ucxx-internal/en/dev-suphilip-add-amd-docs/install/install.html>`__
