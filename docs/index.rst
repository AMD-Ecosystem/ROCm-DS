.. meta::
  :description: Learn about the features and capabilities of ROCm for Data Science (ROCm-DS)
  :keywords: Data-analytics, RAPIDS, cuDF, cuGraph, RMM, hipDF, hipGraph, hipMM, Pandas, NetworkX, High-Performance Computing, GPU Acceleration, GPU Computing, Parallel Computing, Scalable Data Science, Python

.. rocmds-index:

********************************************************************
AMD ROCm-DS
********************************************************************

.. note::
   ROCm-DS is in an early access state. Running production workloads is not recommended.

The ROCm Data Science toolkit (or ROCm-DS) is an open-source software collection for high-performance data science applications built on the core ROCm platform. ROCm-DS is a fork of the RAPIDS® open-source project from NVIDIA and enables users to accelerate their data processing and analysis workloads on AMD GPUs. You can leverage ROCm-DS to accelerate both new and existing data science workloads, allowing you to execute intensive applications with larger datasets at lightning speed. ROCm-DS enables the creation of scalable solutions addressing the pressing needs of today's data-driven landscape. With ROCm-DS, you can build pre- and post-processing applications for your AI models, create new big data processing workloads, or accelerate your existing data science pipelines with minimal effort.

The available libraries in ROCm-DS provide the tools to build a complete workflow for data science acceleration on AMD GPUs. hipDF enables you to create DataFrames and execute GPU-accelerated operations on them. It also includes the ability to accelerate many existing Pandas workflows with minimal effort and no code changes. hipGraph can be used to create, analyze, and review complex networks. Both the hipDF and hipGraph libraries (currently in early access) provide these capabilities for acceleration on AMD Instinct GPUs, with hipMM providing supporting functions for the memory management of these high-performance GPU-based applications. For information about installing hipDF or hipGRAPH components, and required elements, see the Installation instructions for the components.

ROCm-DS documentation is organized into the following categories:

.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Installation

    * :ref:`system-requirements`
    * :ref:`linux-install`

  .. grid-item-card:: Components

    * `hipDF <https://rocm.docs.amd.com/projects/hipDF/en/docs-25.05/>`_
    * `hipMM <https://rocm.docs.amd.com/projects/hipMM/en/docs-25.05/>`_
    * `hipGRAPH <https://rocm.docs.amd.com/projects/hipGRAPH/en/docs-25.05/>`_
    Intersphinx links
    
    * :doc:`hipDF <hipdf:index>`
    * :doc:`hipMM <hipmm:index>`
    * :doc:`hipGRAPH <hipgraph:index>`

  .. grid-item-card:: Related Content

    * `Instinct docs <https://instinct.docs.amd.com/latest/>`_
    * `ROCm-DS blogs <https://instinct.docs.amd.com/latest/data-science/ROCmDS-Blogs.html>`_
    * :ref:`contributing-to-rocm-ds`
