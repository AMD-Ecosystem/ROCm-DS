.. meta::
    :description: AMD Data Science installation
    :keywords: Data-analytics, RAPIDS, cuDF, cuGraph, RMM, hipDF, hipGraph, hipMM, Pandas, NetworkX, High-Performance Computing, GPU Acceleration, GPU Computing, Parallel Computing, Scalable Data Science, Python

.. _linux-install:

**************************************************************************************
Installing AMD Data Science
**************************************************************************************

This topic provides brief guidance and recommendations on setting up your environment and installing AMD Data Science components.

System requirements
===================

The following are the AMD Data Science release compatibilities and system requirements: 

* `ROCm 7.2.3 <https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.3/>`__

  .. note::
      
     ROCm version compatibility: The 26.07 release builds rocOpt against ROCm 7.1.1, but runs it on ROCm 7.2.3.

* Operating Systems: Ubuntu 24.04  
* AMD Instinct GPUs: 

  - MI355X (GPU target gfx950) 
  - MI300X (GPU target gfx942) 

* Python versions: 3.13

Installation instructions
=========================

Each AMD Data Science component must be separately installed as needed. You can find the installation instructions for each component as follows: 

* `rocOpt Installation instructions <https://rocm.docs.amd.com/projects/rocopt/en/latest/install/install_rocopt.html>`__
* `hipDF Installation instructions <https://rocm.docs.amd.com/projects/hipDF/en/docs-26.03/install/INSTALL.html>`__
* `hipMM Installation instructions <https://rocm.docs.amd.com/projects/hipMM/en/docs-26.03/install/INSTALL.html>`__
* `hipGRAPH Installation instructions <https://rocm.docs.amd.com/projects/hipGRAPH/en/latest/install/Linux_Install_Guide.html>`__
* `hipRAFT Installation instructions <https://rocm.docs.amd.com/projects/hipRaft/en/docs-26.03/install/install.html>`__
* `hipVS Installation instructions <https://rocm.docs.amd.com/projects/hipVS/en/docs-26.03/install/install.html>`__
* `dask-hip Installation instructions <https://rocm.docs.amd.com/projects/dask-hip/en/docs-26.03/install/install.html>`__
* `hip-ucxx Installation instructions <https://rocm.docs.amd.com/projects/hip-ucxx/en/docs-26.03/install/install.html>`__
