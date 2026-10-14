# AMD Data Science 26.07 release notes

AMD is pleased to announce the AMD Data Science toolkit 26.07 release with the
introduction of **rocOpt** for decision optimization on AMD Instinct GPUs. rocOpt
is the AMD ROCm port of the open-source GPU-accelerated optimization engine
(based on cuOpt `26.02.00`, `branch-26.02`). rocOpt solves mixed integer
linear programming (MILP), linear programming (LP), quadratic programming (QP),
and vehicle routing problems (VRP) on AMD GPUs.

- [AMD Data Science release highlights](#amd-data-science-release-highlights)
- [System requirements](#system-requirements)
- [AMD Data Science components](#amd-data-science-components)
- [Detailed component changelog](#detailed-component-changelog)

## AMD Data Science release highlights

The 26.07 release introduces rocOpt for decision optimization:

- Initial ROCm/HIP port of the cuOpt engine running natively on AMD Instinct GPUs.
- Multi-architecture fat binary built by default for **gfx942 (MI300X / CDNA3)**
and **gfx950 (MI355X)**. HIP selects the correct code object at load
time, so a single image runs on either part.
- Full C, C++, Python, and Server API surface carried over from cuOpt.
- The container image builds on ROCm 7.1.1 and runs on the ROCm 7.2.3 runtime, avoiding
a known code generation issue on gfx942 while providing the updated runtime to enable
use with other AMD Data Science components.

## System requirements

For the 26.07 release, the AMD Data Science components support the ROCm 7.2.3 release. Refer to the {doc}`Compatibility matrix <compatibility-matrix>` to verify supported AMD Instinct GPUs, operating systems, and ROCm versions.

## AMD Data Science components

rocOpt is the only AMD Data Science component in the 26.07 release. Click {fab}`github` to go to the component's source code on GitHub.

<div class="pst-scrollable-table-container">
    <table id="rocm-rn-components" class="table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Version</th>
                <th>GitHub</th>
            </tr>
        </thead>
        <colgroup>
            <col span="1">
            <col span="1">
        </colgroup>
        <tbody class="rocm-ds-components">
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocopt/en/latest/">rocOpt</a></td>
                <td><a href="#rocOpt-1-0-0">1.0.0</a></td>
                <td><a href="https://github.com/AMD-Ecosystem/rocOpt"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

## Detailed component changelog

The following sections describe key changes to AMD Data Science components.

### rocOpt (1.0.0)

#### Supported APIs

- **C++ API** — native API, supporting all features
- **C API** — LP, MILP, QP
- **Python API** — Routing (TSP, VRP, PDP); LP, MILP, and QP via the algebraic
  modeling interface
- **Server API** — LP, MILP, Routing (TSP, VRP, PDP)

#### Build & packaging

- Ported the RAPIDS/cuOpt build onto AMD Data Science: `rapids-cmake`, `rmm`/`hipmm`,
  `libraft`/`hipRaft`, `rocthrust`, `libhipcxx`, and the ROCm-DS logger are
  sourced from the open-source AMD-Ecosystem forks and the `rocm-7.2.3` PyPI index.
- Two-stage container build (`dockerfile.rocm`): compile on ROCm 7.1.1, run on ROCm 7.2.3.
- MPS parser dependency repinned to `rocopt-mps-parser` (`1.0.0`).
- Benchmark tooling: multi-GPU dispatcher, an image benchmark build option, and
  short LP/MILP pre-flight scripts with idempotent dataset download.
- rocOpt version set to `1.0.0`, `CUOPT_VERSION` (`26.02.00`) and `CUOPT_BRANCH`
  (`branch-26.02`) track the upstream base.


#### Example notebooks

Jupyter notebooks under [`examples_notebook/`](https://github.com/AMD-Ecosystem/rocOpt/tree/release/rocopt-26.07/examples_notebook) show
end-to-end rocOpt workflows on AMD GPUs and are ready to run in the rocOpt
container:

- **Diet optimization (LP)** —
  `diet_optimization/diet_optimization_lp.ipynb`: the classic diet problem solved as a linear program with the Python modeling
  API, minimizing cost subject to nutritional requirements.
- **Diet optimization (MILP)** —
  `diet_optimization/diet_optimization_milp.ipynb`: the same problem with integer decisions, demonstrating mixed integer linear
  programming.
- **Last-mile delivery (CVRPTW)** —
  `last_mile_delivery/cvrptw_benchmark_rocopt.ipynb`: a capacitated vehicle routing problem with time windows on the Gehring &
  Homberger benchmark, focused on time-to-solution and routing performance.

The docker image does not include the example notebooks, so fetch them from the repo into `/rocopt-release/examples_notebook`. Each notebook includes an environment-setup step for installing prerequisites so it can be run directly from the prebuilt image.

#### Known limitations

The Barrier (interior-point) LP solver depends on the  **cuDSS** sparse direct solver, and has no ROCm equivalent in this release. Use PDLP for large LPs and dual simplex for smaller problems.
