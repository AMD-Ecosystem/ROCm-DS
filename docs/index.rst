.. meta::
  :description: Learn about the features and capabilities of ROCm for Data Science (ROCm-DS)
  :keywords: Data-analytics, RAPIDS, cuDF, cuGraph, RMM, hipDF, hipGraph, hipRAFT, hipMM, hipVS, Pandas, NetworkX, High-Performance Computing, GPU Acceleration, GPU Computing, Parallel Computing, Scalable Data Science, Python

.. rocmds-index:

********************************************************************
AMD ROCm-DS
********************************************************************

The ROCm Data Science Toolkit (ROCm-DS) is an open-source collection of GPU-accelerated libraries designed to empower data scientists,
engineers, and researchers to build high-performance data science applications and machine learning workflows on the ROCm platform.
Built upon the core ROCm foundation, ROCm-DS provides a unified, efficient, and scalable environment for end-to-end data science acceleration.

ROCm-DS is a fork of the RAPIDS® open-source project from NVIDIA, extended and optimized for AMD GPUs. It enables users to accelerate
both new and existing data science workloads, executing intensive applications with larger datasets at exceptional speed. With ROCm-DS,
you can build pre- and post-processing applications for AI models, create big data processing workloads, or accelerate existing data
science pipelines with minimal effort.

ROCm-DS delivers a cohesive set of libraries that target every stage of the data science lifecycle, from data ingestion and transformation
to graph analytics, mathematical computation, and vector search. Each component is optimized for GPU performance while maintaining user-friendly
interfaces compatible with existing data science frameworks and APIs.

The toolkit includes the following key components:

* hipDF – A GPU-accelerated DataFrame library offering fast and scalable tabular data manipulation, aggregation, and transformation. hipDF enables high-performance preprocessing, feature engineering, and ETL workflows essential for modern data pipelines. It also supports the acceleration of many existing Pandas workflows with little to no code changes.

* hipGRAPH – Leverages GPU acceleration to process and analyze complex graph structures and networks with speed and precision. hipGRAPH supports diverse graph algorithms—such as centrality, traversal, similarity, sampling, and labeling—and integrates seamlessly with hipDF DataFrames across the ROCm-DS ecosystem.

* hipRAFT – Provides a foundational layer of reusable GPU-accelerated primitives for data science and machine learning, including clustering, dimensionality reduction, and statistical operations. hipRAFT serves as the computational backbone for higher-level data science and AI applications.

ROCm-DS documentation is organized into the following categories:

.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Installation

    * :ref:`system-requirements`
    * :ref:`linux-install`

  .. grid-item-card:: Components

    * `hipDF <https://rocm.docs.amd.com/projects/hipDF/en/latest/>`_
    * `hipMM <https://rocm.docs.amd.com/projects/hipMM-internal/en/latest/>`_
    * `hipGRAPH <https://rocm.docs.amd.com/projects/hipGRAPH/en/latest/>`_
    * `hipRAFT <https://rocm.docs.amd.com/projects/hipRAFT-internal/en/release-rocmds-ga-25.10/>`_
    * `hipVS <https://rocm.docs.amd.com/projects/hipvs-internal/en/latest/>`_

  .. grid-item-card:: Related Content

    * `Instinct docs <https://instinct.docs.amd.com/latest/>`_
    * `ROCm-DS blogs <https://instinct.docs.amd.com/latest/data-science/ROCmDS-Blogs.html>`_
    * :ref:`contributing-to-rocm-ds`
