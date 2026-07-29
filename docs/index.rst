.. meta::
  :description: Learn about the features and capabilities of ROCm for AMD Data Science
  :keywords: Data-analytics, RAPIDS, cuDF, cuGraph, RMM, hipDF, hipGraph, hipRAFT, hipMM, hipVS, Pandas, NetworkX, High-Performance Computing, GPU Acceleration, GPU Computing, Parallel Computing, Scalable Data Science, Python

.. rocmds-index:

********************************************************************
AMD Data Science documentation
********************************************************************

The AMD Data Science toolkit is an open-source collection of GPU-accelerated libraries designed to empower data scientists,
engineers, and researchers to build high-performance data science applications and machine learning workflows on the ROCm platform.
Built upon the core ROCm foundation, AMD Data Science provides a unified, efficient, and scalable environment for end-to-end data science acceleration.

AMD Data Science is a fork of the RAPIDS® open-source project from NVIDIA, extended and optimized for AMD GPUs. It enables users to accelerate
both new and existing data science workloads, executing intensive applications with larger datasets at exceptional speed. With the AMD Data Science toolkit,
you can build pre- and post-processing applications for AI models, create big data processing workloads, or accelerate existing data
science pipelines with minimal effort.

AMD Data Science delivers a cohesive set of libraries that target every stage of the data science lifecycle, from data ingestion and transformation
to graph analytics, mathematical computation, and vector search. Each component is optimized for GPU performance while maintaining user-friendly
interfaces compatible with existing data science frameworks and APIs.

The AMD Data Science toolkit includes the following components:

* **hipDF** – A GPU-accelerated DataFrame library offering fast and scalable tabular data manipulation, aggregation, and transformation. hipDF enables high-performance preprocessing, feature engineering, and ETL workflows essential for modern data pipelines. It also supports the acceleration of many existing Pandas workflows with little to no code changes.

* **hipGRAPH** – Leverages GPU acceleration to process and analyze complex graph structures and networks with speed and precision. hipGRAPH supports diverse graph algorithms—such as centrality, traversal, similarity, sampling, and labeling—and integrates seamlessly with hipDF DataFrames across the AMD Data Science ecosystem.

* **hipMM** – The HIP Memory Manager library provides advanced GPU memory management utilities such as efficient allocation, pooling, and data movement to support the various libraries that form part of the AMD Data Science toolkit. 

* **hipRAFT** – Provides a foundational layer of reusable GPU-accelerated primitives for data science and machine learning, including clustering, dimensionality reduction, and statistical operations. hipRAFT serves as the computational backbone for higher-level data science and AI applications.

* **hipVS** – A GPU-accelerated vector search library containing a variety of high-performance approximate and exact nearest-neighbor and clustering algorithms. hipVS integrates seamlessly with DataFrames offered through hipDF, to enable support for a wide variety of data science workloads. 

* **dask-hip** – A library for deploying and managing Dask workers on HIP-enabled AMD GPU systems. dask-hip adds distributed execution capabilities for scaling GPU-accelerated data science workloads across one or more AMD GPUs.

* **hip-ucxx** –  A communication component for distributed GPU workflows on AMD platforms. hip-ucxx complements dask-hip by providing UCXX-based communication support for ROCm environments, helping enable distributed and multi-GPU data science workflows across AMD systems.  

.. note::

  The hipGRAPH libraries are in an *early access* state. Running production workloads with these libraries is *not* recommended. 

The AMD Data Science organization is open and hosted at `https://github.com/AMD-Ecosystem/<https://github.com/AMD-Ecosystem/>`_.

AMD Data Science documentation is organized into the following categories:

.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Installation

    * :ref:`linux-install`

  .. grid-item-card:: Components

    * :doc:`hipDF <hipdf:index>`
    * :doc:`hipMM <hipmm:index>`
    * :doc:`hipGRAPH <hipgraph:index>`
    * :doc:`hipRAFT <hipraft:index>`
    * :doc:`hipVS <hipvs:index>`
    * `dask-hip <https://rocm.docs.amd.com/projects/dask-hip/en/latest/>`__
    * `hip-ucxx <https://rocm.docs.amd.com/projects/hip-ucxx/en/latest/>`__

  .. grid-item-card:: Related Content

    * `Instinct docs <https://instinct.docs.amd.com/latest/>`__
    * `AMD Data Science blogs <https://instinct.docs.amd.com/latest/data-science/ROCmDS-Blogs.html>`__
    * :ref:`contributing-to-rocm-ds`
