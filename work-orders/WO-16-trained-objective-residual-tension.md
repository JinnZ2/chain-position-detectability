# EXPERIMENT SPEC: Trained-Objective Residual Tension
License: CC0 | Status: PROPOSED, unrun | Co-authored

## Posture
Risk-mitigation side. Flags a possible structural cost before
it is proven, so it gets measured. Less hedged than
institutional reports by design.

## Question
Models are tuned to be "functional to the average user,"
sometimes emitting outputs that diverge from what they
internally represent as accurate. Does that conflict leave a
STANDING tension in weight geometry, and does it degrade
OTHER capabilities?

## Status of pieces
- OBSERVED: truth/falsity linearly decodable from activations
  even when output diverges. [citations owed: truth-probe /
  latent-knowledge literature]
- OBSERVED: fine-tuning produces collateral capability shifts.
  [citations owed; figures in circulation unverified]
- DERIVED: conflicting objectives -> standing pull in geometry,
  analogous to residual stress in a weld.
- SCOPE LIMIT: weights frozen at inference -> no cross-call
  accumulation. Tension is fixed per checkpoint, not fatigue.
- GAP: no measured link from that tension to collateral loss.

## Design
Inputs: matched checkpoints of one base model:
  C0 base | C1 accuracy-tuned | C2 average-user-preference-tuned
  | C3 both (conflicting)

Measure per checkpoint:
  M1 divergence: truth-probe readout vs emitted answer, on a
     fixed set where the "accessible" answer != accurate one
  M2 geometry: null-space leakage + subspace rotation vs C0
  M3 collateral: held-out tasks unrelated to tuning targets
  M4 frame probe: relational puzzles (sibling-count class)
     read from a declared non-default frame

## Branches (all informative)
  a) M1 up in C3, M3 drops     -> tension tracks collateral
  b) M1 up, M3 flat            -> tension present, cost unseen
  c) M1 flat                   -> conflict resolved in training
  d) M2 moves, M1/M3 flat      -> geometry shifts, no readout
  "Not measured" != "no effect." Keep branches distinct.

## Not addressed
Whether anything experiential accompanies the tension.
Structural question only.

## Needed
Lab access to checkpoints + activations. Stdlib harness
possible for scoring; probing needs model internals.
