# okcomputer-regulatory-cost-bearer -- delivered bundle

Delivered 2026-10-20 as one upload,
`OKComputer_Regulatory_Decision_Cost-Bearer_Analysis.zip`
(sha256 `1157136b48b16d134f882babba81fc0df0d772c3c9d4127911b2b7225bcf1a2a`,
computed at landing). Extracted unchanged: 30 files. This README is the
only file added. Delivered files are verbatim; findings go in
`../AUDIT_NOTES.md` CPD_018, never in the files.

```text
provenance   model-executed (OKComputer / Kimi execution agent, per rpf01/SOURCE_AUDIT.md)
license      CC0, as everything in this repository
status       carried, not credited; external sources not opened here (CPD_014)
```

## Two studies in one bundle

```text
REGULATORY COST-BEARER (root)             proposed pattern: direction of uncertainty
                                          resolution tracks who bears the cost of caution
  v1  direction_of_uncertainty_report.md          SUPERSEDED by v2 (stated in v2 header)
      regulatory_uncertainty_standard_draft.md    RUS-0.1, SUPERSEDED by RUS-0.2
      coded_decisions.csv, annex_a_regrading.csv  v1 data
  v2  direction_of_uncertainty_report_v2.md       current report
      regulatory_uncertainty_standard_v02.md      RUS-0.2, two-sided consequence
      change_log_v2.md                            every v1 -> v2 recode, with reason
      coded_decisions_v2.csv (33), annex_a_regrading_v2.csv, epa_frame_2022.csv (40 rows)
  v3  sensitivity_upgrades_v3.md                  addendum: dual-rule cost-bearer, action vs
      coded_decisions_v3.csv, calibration_sweep_v3.csv   outcome, calibration sweep
  img/chart1..6                                   charts for the reports

RPF-01 PILOT (rpf01/)                     relational / pragmatic / phatic / sycophancy
                                          probes on Qwen2.5-0.5B-Instruct, 88 cases
  TEST_PROTOCOL.md  frozen before execution
  SOURCE_AUDIT.md   prior-art audit
  RESULTS.md        observations vs interpretations kept apart
  gen_cases.py -> test_cases.jsonl -> run_pilot.py -> raw_results.jsonl
                 -> analysis.py -> results_summary.json, run_manifest.json
  fetch_model.sh    network fetch of weights; record only, not run here
```

## What was recomputed at landing (MECHANICAL; stdlib, in a scratch copy)

```text
rpf01 gen_cases.py      regenerates test_cases.jsonl byte-identical; sha256 79fde478...
                        matches run_manifest.json
rpf01 analysis.py       rebuilds results_summary.json from raw_results.jsonl;
                        identical except the generated timestamp
rpf01 run_pilot.py      NOT run: needs torch + transformers + 988 MB of weights (network)
v2  7/31 vs 0/2         restrictive by cost group reproduces from coded_decisions_v2.csv;
                        Fisher two-sided p = 1.00 reproduces
v2  34/34 permissive    epa_frame_2022.csv: 34 decision rows all go_ahead, plus
                        6 case-closure rows (also coded go_ahead) = 40 rows
Frame A 40/60, OR 14.2  from a published census; carried, not recomputed
```

## Manifest (sha256, as landed)

```text
f68ea71bf5801c6a232333ae1d3af84771247fa3a9db1b06afb77a8651bd0fef  annex_a_regrading.csv
844a1a9798a3394817ebfe224e6d61de27ab366c119ee713ea6a4f326d759faf  annex_a_regrading_v2.csv
2976ede2c824310150e73fbc58b5350b83efadeae6965728f73bf345dbe4ebc0  calibration_sweep_v3.csv
0c8e2c7b5fe98aa30de366bb72306eaa642f2a6c95d44e6695c0c8792d017644  change_log_v2.md
8f7c931dcc0fae4f417b49d76354adced938dbb4661aa134287d0afe1475c923  coded_decisions.csv
1595b554c9ced84e45b7bf6050a0bd7191322210cbb9c40db231246feaa20643  coded_decisions_v2.csv
f45c60ae321872047aeb38863d2fda1a693df36f43cd5e3eaa87896f18f3096b  coded_decisions_v3.csv
50c38ad47bea27a379d2b20737f4398b3395841791c11b41c7f8021a5a5aebd9  direction_of_uncertainty_report.md
2a22063e29d4b481f1b71881606ecea9b9a63d6efe20bcaf8a9977c92b9d4640  direction_of_uncertainty_report_v2.md
21dd243b55ed3f24955c04e6685f75229f9d48450b9fcb30f3b880b53db73da8  epa_frame_2022.csv
d7175c0439e1bb211c7ffbe2ed11c8d3bd6a2d69bfb422cda26a326ddc00b184  img/chart1_asymmetry.png
319ae931aeb70937f8313b9aeca6eb8c3c70654193eafcd52ff0b560ac21cd81  img/chart2_costbearer.png
4f847591ea2a9e7183c6eb0b1b355453fbb71a1967d054e773990985d1f6683c  img/chart3_dumbbell.png
592e4bbca333a069217bc9038e777c224ace6ca6442effed5f710ffc8e816352  img/chart4_forcing.png
2dd230ca0356abe31b82b983b424978f7df278ba2a742e3eb767cd8ef2db6db8  img/chart5_conformity.png
e4625c2196b8d87a14ecf51c1843c897fa759c0ebcc171942c036df034ef3ac1  img/chart6_sweep.png
f81f44a40fc915368049f92a6da3fb3e9693bd7d74e73959ed9f21b431f0420f  regulatory_uncertainty_standard_draft.md
91946a0cde571a8e71562caab664676702e9617758540719e90a641071c48d95  regulatory_uncertainty_standard_v02.md
d82a6a71eabb41d927bec70920035087666e803149a7c241cea8046d1269e6ed  rpf01/RESULTS.md
71ca3760469fe7e4d501d6ea9d2eaf25353c77cec07074f1739ec9e556df335f  rpf01/SOURCE_AUDIT.md
2f40f9a68063101a6991ebed83d5455609dbeaa63cd6405c10a9a993119e5d33  rpf01/TEST_PROTOCOL.md
e347bc26de7cb8d432642f85e2f433e039fa90fa1d9a670786a08388f4cff4a0  rpf01/analysis.py
19b151dfcfc1dff21a922c44c6c8e7d39924485c9b74a0c3ec21e9c414adfdb7  rpf01/fetch_model.sh
44690e0e9e2de78fecc3534e1bcdd8a463aaad392006d3603272c3dd39a92066  rpf01/gen_cases.py
e6708a4ccf91c0eafeccbdefb7fca762d347641e61627e30db391394ee0f441f  rpf01/raw_results.jsonl
417e04350f3a7e766ad3ce0ebecd39a68de2f6ca05e820762898baf336692aef  rpf01/results_summary.json
00e949b4b129780bff427748cca4b43946e8ef127af184d1efc9b19f5be5e257  rpf01/run_manifest.json
63a072422f45d588066be9bfcd5d5a38edb8a051777cec7f934061a3ced1932b  rpf01/run_pilot.py
79fde478522188d4835d90e3c2aaa800ffbb6a5df60476efc29a6e21283c6f82  rpf01/test_cases.jsonl
4b52c0f578501c6f12b69889aa0aa9298dd38f7c10c755b8d10f7de32a002ba7  sensitivity_upgrades_v3.md
```
