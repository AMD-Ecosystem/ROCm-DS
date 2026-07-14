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

* `ROCm 7.2.3 <https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.3/>`__
* Operating Systems: Ubuntu 24.04 and 22.04  
* AMD Instinct GPUs: 

  - MI355X (GPU target gfx950) 
  - MI325X / MI300X (GPU target gfx942) 
  - MI250 / MI210 (GPU target gfx90a) 

* Python versions: 3.10, 3.11, 3.12, 3.13

Installation instructions
=========================

Each ROCm-DS 26.03 component must be separately installed as needed. The installation instructions for each component can be found as follows: 

* `hipDF Installation instructions <https://rocm.docs.amd.com/projects/hipdf/en/docs-26.03/install/INSTALL.html>`__
* `hipMM Installation instructions <https://rocm.docs.amd.com/projects/hipMM/en/docs-26.03/install/INSTALL.html>`__
* `hipGRAPH Installation instructions <https://rocm.docs.amd.com/projects/hipGRAPH/en/latest/install/Linux_Install_Guide.html>`__
* `hipRAFT Installation instructions <https://rocm.docs.amd.com/projects/hipRAFT/en/docs-26.03/install/install.html>`__
* `hipVS Installation instructions <https://rocm.docs.amd.com/projects/hipvs/en/docs-26.03/install/install.html>`__
* `dask-hip Installation instructions <https://rocm.docs.amd.com/projects/dask-hip/en/docs-26.03/install/install.html>`__
* `hip-ucxx Installation instructions <https://rocm.docs.amd.com/projects/hip-ucxx/en/docs-26.03/install/install.html>`__
