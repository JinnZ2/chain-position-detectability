# WO-5 tested analysis environment

The analysis was tested on Ubuntu 24.04 with Python 3.12.3 and the exact package versions in [`requirements.txt`](requirements.txt). Matplotlib uses the noninteractive `Agg` backend and the `DejaVu Sans` font family. Numerical outputs were byte-identical across repeated runs in this environment. Figure bytes may vary across operating systems or rendering-library builds even when numerical outputs agree.

From the repository root, install the dependencies into an isolated environment and run:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r research/wo-5/analysis/requirements.txt
python research/wo-5/analysis/analyze_hop_distance.py
```

The script verifies the SHA-256 of [`hop-coded-effects.csv`](hop-coded-effects.csv) before fitting models. It writes all derived tables and figures deterministically using seed `20260919` for the count-preserving source-level permutation.
