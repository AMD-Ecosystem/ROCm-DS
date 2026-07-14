# ROCm-DS 26.03 Release notes

AMD is pleased to announce the ROCm Data Science Toolkit (ROCm-DS) 26.03 release with major component upgrades, broader hardware enablement, and new distributed computing capabilities for AMD GPU environments. ROCm-DS is an open-source data science toolkit designed to improve the performance of data preparation, analytics, machine learning, and vector search workloads on AMD GPUs. 

With the 26.03 release, ROCm-DS continues to strengthen its software stack while improving portability for users bringing existing GPU data science workflows to AMD hardware. The 26.03 release introduces dask-hip and hip-ucxx as new components, adding foundational support for distributed and multi-GPU workflows on ROCm. In addition, core libraries, including hipDF, hipMM, hipRAFT, and hipVS, have been updated to incorporate newer upstream functionality and support for ROCm 7.2.3. 

```{note}
hipGRAPH remains early access (EA) in ROCm-DS 26.03. 
```

- [ROCm-DS Release highlights](#rocm-ds-release-highlights)
- [System requirements](#system-requirements)
- [ROCm-DS components](#rocm-ds-components)
- [Detailed component Changelogs](#detailed-component-changelogs)

## ROCm-DS release highlights

The 26.03 release includes the following major updates and highlights: 

* Updated core libraries, with key components aligned to newer upstream 25.10 APIs and functionality. 
* New distributed computing components: 

    - dask-hip, AMD’s port of dask-cuda, for deploying and managing Dask workers on HIP-enabled GPU systems. 
    - hip-ucxx, adding UCXX-based communication support for distributed GPU workflows on ROCm. 

* Major hipDF upgrade to 3.0.0, including API updates, a new `pylibhipdf` Python wrapper compatible with upstream `pylibcudf`, and expanded GPU architecture support. 
* Major hipMM upgrade to 4.0.0, introducing a precompiled shared library model (`librmm.so`), improved logging integration, enhanced diagnostics, and updated Python packaging. 
* hipRAFT 1.0.0 and hipVS 1.0.0 updated with new primitives, performance improvements, API changes, and expanded multi-GPU capabilities. 
* Expanded hardware support, including support for the gfx950 GPU architecture across major libraries, with additional experimental gfx11xx/gfx12xx RDNA support in hipDF. 
* ROCm 7.2.3 support across updated components. 
* Python 3.13 support added in selected components. 
* Continued support for Python and C++ APIs, helping developers integrate ROCm-DS into analytics, AI, and GPU-accelerated data science workflows. 

This release advances ROCm-DS toward a more complete platform for distributed, multi-GPU, and large-scale data science workloads on AMD GPUs. 

## System requirements

For the 26.03 release, the ROCm-DS components support the ROCm 7.2.3 release. Refer to the {doc}`Compatibility matrix <compatibility-matrix>` to verify supported AMD Instinct GPUs, operating systems, and ROCm versions.

## ROCm-DS components

The following table lists ROCm-DS components versions for the 26.03 release, including any version
changes. Click {fab}`github` to go to the component's source code on GitHub.

<div class="pst-scrollable-table-container">
    <table id="rocm-rn-components" class="table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Version</th>
                <th></th>
            </tr>
        </thead>
        <colgroup>
            <col span="1">
            <col span="1">
        </colgroup>
        <tbody class="rocm-ds-components">
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipdf-internal/en/docs-rocmds-26.03/">hipDF</a></td>
                <td>2.0.0&nbsp;&Rightarrow;&nbsp;<a href="#hipdf-3-0-0">3.0.0</a></td>
                <td><a href="https://github.com/ROCm-DS/hipDF"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipMM-internal/en/docs-rocmds-26.03/">hipMM</a></td>
                <td>3.0.0&nbsp;&Rightarrow;&nbsp;<a href="#hipmm-4-0-0">4.0.0</a></td>
                <td><a href="https://github.com/ROCm-DS/hipMM"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipGRAPH/en/docs-25.10/">hipGRAPH</a></td>
                <td>1.0.0b1</td>
                <td><a href="https://github.com/ROCm-DS/hipGRAPH"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipRAFT-internal/en/amd-integration/">hipRAFT</a></td>
                <td>0.1.0&nbsp;&Rightarrow;&nbsp;<a href="#hipraft-1-0-0">1.0.0</a></td>
                <td><a href="https://github.com/ROCm-DS/hipRaft"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipvs-internal/en/amd-integration/">hipVS</a></td>
                <td>0.1.0&nbsp;&Rightarrow;&nbsp;<a href="#hipvs-1-0-0">1.0.0</a></td>
                <td><a href="https://github.com/ROCm-DS/hipVS"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/dask-hip-internal/en/dev-suphilip-add_amd_documentation/">dask-hip</a></td>
                <td><a href="#dask-hip-1-0-0">1.0.0</a></td>
                <td><a href="https://github.com/AMD-AIOSS/dask-hip"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hip-ucxx-internal/en/dev-suphilip-add-amd-docs/">hip-ucxx</a></td>
                <td><a href="#hip-ucxx-0-1-0">0.1.0</a></td>
                <td><a href="https://github.com/AMD-AIOSS/hip-ucxx"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

## Detailed component Changelogs

The following sections describe key changes to ROCm-DS components.

### hipDF (3.0.0)

#### Added 

* API alignment with upstream 25.10 functionality 
* Support for ROCm 7.2.3 
* New `pylibhipdf` wrapper module with Python bindings compatible with upstream `pylibcudf` 
* Support for the gfx950 GPU architecture 
* Experimental support for gfx11xx and gfx12xx RDNA architectures: 

    - gfx1100 
    - gfx1101 
    - gfx1200 
    - gfx1201 

* Added hipcomp zstd GPU decompression support for ORC and Parquet 

#### Known limitations

* DEBUG builds with `-O0` are not currently supported. Use `-Og` or higher. 
* Some `cudf.pandas` acceleration layer configurations may show instability under heavy memory pressure, particularly with XNACK-related settings. 

### hipMM (4.0.0)

#### Added 

* Updated to newer upstream 25.10 functionality 
* Support for ROCm 7.2.3 
* Support for the gfx950 GPU architecture 
* Transition from a header-only library to a shared library model, with core implementations now delivered in librmm.so 
* Improved downstream build times through precompiled library delivery 
* New non-blocking HIP stream support via the cuda_stream class 
* Enhanced out-of-memory diagnostics with clearer failure reporting 
* Integration with ROCmDS-Logger 
* Python package support through the new amd-hipmm package and hipmm namespace 
* Python 3.13 support 

#### Changes 

* Downstream projects must now link against `librmm.so` using `find_package(rmm)` and `rmm::rmm` 
* The logging API has migrated from `spdlog` to `rocmds-logger` 

### hipRAFT (1.0.0)

#### Added

* Updated to newer upstream 25.10 functionality 
* ROCm 7.2.3 support 
* Support for gfx950 
* Added RAFT_CUDA_TRY error-checking support for HIP runtime API calls 
* Ported NN-Descent graph construction kernel with wavefront-size-64 compatibility 
* Improved hipBLASLt GEMM device pointer mode handling on AMD GPUs 

#### Changes

* OpenMP cleanup and HIP TLS exit behavior 
* Half-precision construction under HIP 
* GEMM test stability 
* MST correctness on 64-wide wavefronts 
* Synchronization and race conditions 
* RCCL header inclusion 
* Eigenvalue ordering and histogram initialization

#### Known limitations

* Multi-node / multi-GPU is experimental 
* `raft-dask` is experimental 

### hipVS (1.0.0)

#### Added

* Updated to newer upstream 25.10 functionality 
* ROCm 7.2.3 support 
* Support for gfx950 
* Enabled multi-GPU algorithms and RCCL configurations 
* New Composable Kernel (CK) pairwise distance support for: 

    - L2 
    - cosine 
    - inner-product distance kernels 

* Improved support for large datasets, including batch processing enhancements for NN-Descent 
* Added benchmark visualization tooling for interactive comparison of benchmark results 

#### Changes

* Wavefront-width compatibility (wf32 and wf64) 
* ANN algorithm correctness 
* HIP race conditions 
* Spectral clustering stability 
* Graph build robustness 

#### Known limitations 

* Multi-node / multi-GPU remains experimental 
* `wf32` support remains experimental 


### dask-hip (1.0.0)

#### Added 

* Initial release of dask-hip 
* ROCm 7.2.3 support 
* Based on upstream 25.10 functionality 
* Ships as the amd-dask-hip Python package on AMD PyPI 
* Introduces a `pynvml-to-amdsmi` translation layer so existing dask-cuda logic can operate on AMD GPUs with minimal changes 
* ROCm auto-detection at import time 
* Support for HIP_VISIBLE_DEVICES, automatically mapped to CUDA_VISIBLE_DEVICES when needed 
* Runtime dependencies for HIP interoperability, GPU telemetry, and numba-hip support 
* Optional UCXX-related dependencies for ROCm communication testing 

#### Known limitations

* Only AMD GPUs are supported 
* UCXX-based multi-node communication on ROCm is experimental 
* TCP transport is fully supported 
* GPUDirect Storage (GDS) is not available on AMD in this release 
* Proxy-based spilling behavior may differ from NVIDIA GPU platforms 

### hip-ucxx (0.1.0)

#### Added 

* hip-ucxx is introduced in ROCm-DS 26.03 as a new communication component for distributed GPU workflows on AMD platforms. 
* ROCm 7.2.3 support 

```{note}
UCXX-based multi-node communication is early access (EA) in ROCm-DS 26.03.
```
