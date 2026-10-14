# Spatial scale space from hemigroup axioms: rotation-invariant self-decomposable kernels in dimension d — release iso-v0.1

This repository is the verification artifact of the article of the same name (the PDF is at the
root, with its supplement). It is an export of the development repository at revision `fba251f`, restricted to
what the article's statements rest on; the development repository also holds the material of
other modules of the same theory and stays private until they are released.

## What is here

- `Formalization/` — the Lean 4 development: the transitive import closure of every module that a
  numbered statement of the article names (79 modules), with the toolchain pinned
  in-tree (`lean-toolchain`, `lake-manifest.json`).
- `Formalization/CIAxiomGuard.lean` — prints the axiom usage of every named declaration.
- `blueprint/trust-boundary.txt`, `blueprint/AXIOMS.md` — the 12 interface names of
  the full development, each with the page-verified citation it rests on and the step it carries
  beyond its source; `blueprint/AXIOMS-verbatim.md`, where it is present, sets the sources' own
  wording beside each entry. The headline theorem, `AffineHemigroup.isotropic_classification`, rests on 2 of them, and section 1.1 of the paper says what the other results rest on.
- `blueprint/src/parts/` — the statements and proofs of record of the article's sections 2–3 (the
  blueprint's chapters of the same numbers), with the `\lean{}` tag naming the declaration
  behind each statement; a chapter of another module is included where the article transcribes a
  statement from it.
- `paper/` — the article's sources.
- `notes/` — the process account, the external reviews verbatim, and the response plan.
- `records/affine/fig-matern-centre.py`, `records/affine/fig-thresholds.py`, `records/affine/check-q0448-matern-table.py`, `records/affine/axioms-iso-all-declarations.py`, `records/affine/axioms-iso-all-declarations-output.txt`, `records/affine/gen-verification-table.py`, `blueprint/trust-boundary-iso.txt`, `records/affine/ai-figures-2026-10-11`, `records/affine/ai-figures-2026-10-13.md` — the files that the article names by these paths.

## Verifying

    cd Formalization
    lake exe cache get        # Mathlib's prebuilt oleans
    lake build
    lake env lean CIAxiomGuard.lean

The last command prints, for `AffineHemigroup.isotropic_classification`, Lean's three logical axioms and
`AffineHemigroup.levy_khintchine_converse`, `AffineHemigroup.levy_khintchine_unique`, and nothing else (the block that the paper prints).

## Statements and declarations

| blueprint node (chapter) | declarations |
|---|---|
| `thm:cited-A1 (02)` | `AffineHemigroup.density_of_integrable_charFun` |
| `thm:cited-A2 (02)` | `AffineHemigroup.sato_polar_criterion` |
| `thm:cited-A3 (02)` | `AffineHemigroup.levy_khintchine_exists`, `AffineHemigroup.levy_khintchine_unique`, `AffineHemigroup.levy_khintchine_converse` |
| `thm:cited-A4 (02)` | `AffineHemigroup.selfDecomposable_infinitelyDivisible` |
| `thm:cited-A5 (02)` | `AffineHemigroup.operatorSelfDecomposable_infinitelyDivisible` |
| `thm:cited-A6 (02)` | `AffineHemigroup.khintchine_null_array` |
| `thm:cited-A8 (02)` | `AffineHemigroup.wolfe_symmetric_unimodal` |
| `thm:cited-A9 (02)` | `AffineHemigroup.gelfand_naimark_logMajorized` |
| `thm:cited-A10 (02)` | `AffineHemigroup.schoenberg_radial_bernstein` |
| `thm:cited-A11 (02)` | `AffineHemigroup.karamata_tauberian_zero` |
| `prop:line-levy-unique (02)` | `AffineHemigroup.line_levy_unique` |
| `def:isotropic-origin-datum (03)` | `AffineHemigroup.OriginDatum`, `AffineHemigroup.OriginDatum.levyMeasure`, `AffineHemigroup.OriginDatum.exponentL`, `AffineHemigroup.OriginDatum.exponent`, `AffineHemigroup.OriginDatum.profileAtOrigin`, `AffineHemigroup.IsLawOf`, `AffineHemigroup.sphereArea`, `AffineHemigroup.polarProfileOf`, `AffineHemigroup.sphereArea_eq_toSphere`, `AffineHemigroup.OriginDatum.tendsto_profileAtOrigin`, `AffineHemigroup.OriginDatum.polar_decomposition` |
| `lem:positive-transform-origin (03)` | `AffineHemigroup.positive_transform_heat`, `AffineHemigroup.positive_transform_bound`, `AffineHemigroup.density_bound_ball`, `AffineHemigroup.heatKernel` |
| `lem:isotropic-exponent-log (03)` | `AffineHemigroup.isotropic_exponent_log_bound`, `AffineHemigroup.isotropic_exponent_log_limit`, `AffineHemigroup.OriginDatum.tailConst` |
| `thm:origin-boundedness-d (03)` | `AffineHemigroup.origin_decay_exponent`, `AffineHemigroup.origin_density_smooth`, `AffineHemigroup.origin_density_bounded_smooth`, `AffineHemigroup.subordinated_profileAtOrigin`, `AffineHemigroup.subordinated_law`, `AffineHemigroup.delayLaw_zero`, `AffineHemigroup.subordinated_density_limit`, `AffineHemigroup.subordinated_unbounded`, `AffineHemigroup.origin_unbounded`, `AffineHemigroup.origin_unbounded_rate`, `AffineHemigroup.origin_dichotomy`, `AffineHemigroup.measurable_gaussVar` |
| `lem:origin-decay-exponent (03)` | `AffineHemigroup.OriginDatum.exponent_decay` |
| `prop:origin-boundedness-subordinated (03)` | `AffineHemigroup.gaussVar`, `AffineHemigroup.mixtureDensity` |
| `cor:origin-profile-exponent (03)` | `AffineHemigroup.exponent_gaussian_limit`, `AffineHemigroup.exponent_profile_limit`, `AffineHemigroup.transform_profile_limit`, `AffineHemigroup.origin_profile_dimension_free` |
| `prop:origin-lower-bound-d (03)` | `AffineHemigroup.origin_lower_bound`, `AffineHemigroup.origin_lower_bound_density`, `AffineHemigroup.origin_lower_bound_ball`, `AffineHemigroup.lowerBoundConst`, `AffineHemigroup.lowerBoundTau`, `AffineHemigroup.lowerBoundKappa` |
| `prop:isotropic-radial-monotone (03)` | `AffineHemigroup.radial_monotone_family`, `AffineHemigroup.radial_monotone_law` |
| `prop:origin-upper-bound-d (03)` | `AffineHemigroup.origin_upper_bound`, `AffineHemigroup.origin_upper_bound_of_heat`, `AffineHemigroup.origin_density_upper`, `AffineHemigroup.origin_density_lower`, `AffineHemigroup.origin_density_log_order`, `AffineHemigroup.origin_ball_log_order`, `AffineHemigroup.origin_density_order` |
| `prop:origin-rate-d (03)` | `AffineHemigroup.origin_ball_rate`, `AffineHemigroup.origin_density_rate`, `AffineHemigroup.origin_ball_rate_critical`, `AffineHemigroup.origin_density_rate_critical`, `AffineHemigroup.origin_transform_ball_log`, `AffineHemigroup.origin_density_log_lower`, `AffineHemigroup.origin_rate`, `AffineHemigroup.origin_rate_critical` |
| `prop:isotropic-exponent-profile (03)` | `AffineHemigroup.slowFactor_basic`, `AffineHemigroup.slowFactor_ratio`, `AffineHemigroup.slowFactor_tendsto_of_integrable`, `AffineHemigroup.slowFactor_tendsto_atTop`, `AffineHemigroup.cin_sub_log_limit`, `AffineHemigroup.sphere_log_mean`, `AffineHemigroup.sphereLogMean_one`, `AffineHemigroup.exponent_profile_asymptotic`, `AffineHemigroup.exponent_profile_bounds`, `AffineHemigroup.transform_power_comparison`, `AffineHemigroup.transform_power_bounded_iff`, `AffineHemigroup.transform_power_limit`, `AffineHemigroup.OriginDatum.slowFactor`, `AffineHemigroup.OriginDatum.slowFactorZero`, `AffineHemigroup.sphereLogMean`, `AffineHemigroup.exponentConst` |
| `prop:origin-rate-profile-d (03)` | `AffineHemigroup.origin_rate_profile`, `AffineHemigroup.origin_rate_profile_critical`, `AffineHemigroup.origin_density_rate_profile`, `AffineHemigroup.origin_ball_rate_profile`, `AffineHemigroup.origin_density_power_of_integrable`, `AffineHemigroup.origin_density_power_of_not_integrable`, `AffineHemigroup.origin_density_rate_profile_critical`, `AffineHemigroup.origin_ball_rate_profile_critical`, `AffineHemigroup.slowLog_bounds`, `AffineHemigroup.slowLog_div_log`, `AffineHemigroup.origin_density_log_of_integrable`, `AffineHemigroup.origin_density_log_of_not_integrable`, `AffineHemigroup.OriginDatum.profileConst`, `AffineHemigroup.OriginDatum.slowLog` |
| `def:filtration-thresholds (03)` | `AffineHemigroup.classS`, `AffineHemigroup.classA`, `AffineHemigroup.classAInf`, `AffineHemigroup.DelayDatum`, `AffineHemigroup.delayExponentL`, `AffineHemigroup.witnessProfile`, `AffineHemigroup.witnessExponent`, `AffineHemigroup.witnessF`, `AffineHemigroup.thresholdFun`, `AffineHemigroup.thresholdSup`, `AffineHemigroup.threshold`, `AffineHemigroup.witness_isDelayDatum` |
| `lem:threshold-monotone (03)` | `AffineHemigroup.thresholdSup_spec`, `AffineHemigroup.threshold_pos`, `AffineHemigroup.thresholdSup_succ`, `AffineHemigroup.threshold_strictAnti`, `AffineHemigroup.witness_polar_closed_form`, `AffineHemigroup.witness_threshold_criterion`, `AffineHemigroup.witness_antitone_iff` |
| `lem:threshold-criterion (03)` | `AffineHemigroup.regIncGamma` |
| `lem:threshold-limit (03)` | `AffineHemigroup.threshold_limit_bounds`, `AffineHemigroup.threshold_limit`, `AffineHemigroup.thresholdEps`, `AffineHemigroup.stirlingK` |
| `lem:threshold-asymptotic (03)` | `AffineHemigroup.tendsto_stirlingRatio`, `AffineHemigroup.threshold_asymptotic_bounds`, `AffineHemigroup.threshold_asymptotic`, `AffineHemigroup.stirlingRatio` |
| `lem:delay-polar-profile (03)` | `AffineHemigroup.delay_polar_profile`, `AffineHemigroup.delay_polar_profile_datum` |
| `thm:filtration-strict (03)` | `AffineHemigroup.filtration_witness`, `AffineHemigroup.filtration_witness_exists`, `AffineHemigroup.filtration_strict`, `AffineHemigroup.filtration_top` |
| `lem:lk-negative-definite (03)` | `AffineHemigroup.lkForm_sub_negDef`, `AffineHemigroup.lkForm_negDef` |
| `lem:bernstein-triplet-unique (03)` | `AffineHemigroup.bernstein_triplet_unique` |
| `lem:filtration-top (03)` | `AffineHemigroup.classAInf_of_classS`, `AffineHemigroup.classS_of_classAInf` |
| `thm:no-cin-ray-in-the-plane (03)` | `AffineHemigroup.no_cin_ray_in_the_plane`, `AffineHemigroup.cin_ray_scaled` |
| `lem:shadow-polar-profile (03)` | `AffineHemigroup.shadow_profile_mean`, `AffineHemigroup.shadow_profile_regular`, `AffineHemigroup.shadow_datum`, `AffineHemigroup.lintegral_shadow`, `AffineHemigroup.OriginDatum.shadow`, `AffineHemigroup.shadowProfile` |
| `prop:profile-one-dimension-down (03)` | `AffineHemigroup.profile_one_dimension_down`, `AffineHemigroup.profile_one_dimension_down_of_classA`, `AffineHemigroup.not_classA_succ_of_profile_discontinuous`, `AffineHemigroup.step_datum_separates`, `AffineHemigroup.cin_ray_not_classA`, `AffineHemigroup.stepOriginDatum` |
| `thm:separating-family-critical-values (03)` | `AffineHemigroup.separating_family_critical_values`, `AffineHemigroup.witness_classA_iff`, `AffineHemigroup.criticalValues_strictAnti`, `AffineHemigroup.criticalValues_tendsto`, `AffineHemigroup.witness_classA_iff_le`, `AffineHemigroup.witness_not_classA_of_gt`, `AffineHemigroup.criticalValues_existsUnique_window`, `AffineHemigroup.separating_family_strict` |
| `def:isotropic-operator-family (03)` | `AffineHemigroup.IsIsotropicOperatorFamily`, `AffineHemigroup.IsSingleOperator` |
| `def:isotropic-kernel-family (03)` | `AffineHemigroup.IsIsotropicCascadeFamily`, `AffineHemigroup.IsIncreasingBijection`, `AffineHemigroup.IsGauge`, `AffineHemigroup.push`, `AffineHemigroup.charFun_push`, `AffineHemigroup.isGauge_iff_isIncreasingBijection` |
| `lem:radial-marginal (03)` | `AffineHemigroup.radial_marginal`, `AffineHemigroup.radial_marginal_eq_dirac`, `AffineHemigroup.radial_marginal_ops`, `AffineHemigroup.marginal` |
| `lem:isotropic-marginal-family (03)` | `AffineHemigroup.isotropic_marginal_family`, `AffineHemigroup.isotropic_marginal_cascadeData` |
| `thm:isotropic-classification (03)` | `AffineHemigroup.isotropic_classification`, `AffineHemigroup.isotropic_classification_origin`, `AffineHemigroup.isotropic_classification_unique` |
| `cor:isotropic-classification-operators (03)` | `AffineHemigroup.isotropic_classification_operators`, `AffineHemigroup.isotropic_classification_operators_unique` |
| `lem:isotropic-realisation (03)` | `AffineHemigroup.isotropic_realisation` |
| `cor:isotropic-scale-zero-kernels (03)` | `AffineHemigroup.scale_zero_kernels`, `AffineHemigroup.scale_zero_operators`, `AffineHemigroup.scale_zero_families`, `AffineHemigroup.scale_zero_relabelling` |
| `prop:isotropic-polar-reading (03)` | `AffineHemigroup.polar_reading`, `AffineHemigroup.polar_reading_unique`, `AffineHemigroup.polar_reading_admissible`, `AffineHemigroup.classA_iff_originDatum`, `AffineHemigroup.polar_classification` |
| `lem:isotropic-stage-levy-measure (03)` | `AffineHemigroup.OriginDatum.stageProfile`, `AffineHemigroup.OriginDatum.stageMeasure`, `AffineHemigroup.OriginDatum.stageProfile_nonneg`, `AffineHemigroup.OriginDatum.stageMeasure_zero`, `AffineHemigroup.OriginDatum.stageMeasure_absolutelyContinuous`, `AffineHemigroup.OriginDatum.stageMeasure_rotation`, `AffineHemigroup.OriginDatum.stageMeasure_integrable`, `AffineHemigroup.OriginDatum.exponent_smul_sub_smul`, `AffineHemigroup.OriginDatum.stageMeasure_univ`, `AffineHemigroup.OriginDatum.stageMeasure_univ_ne_top_iff`, `AffineHemigroup.isotropic_stage_transform`, `AffineHemigroup.isotropic_stage_mass` |
| `prop:isotropic-stage-atom (03)` | `AffineHemigroup.isotropic_stage_compoundPoisson`, `AffineHemigroup.isotropic_stage_exp_neg_mass`, `AffineHemigroup.profileAtOrigin_pos`, `AffineHemigroup.isotropic_stage_atom`, `AffineHemigroup.isotropic_stage_operator`, `AffineHemigroup.isotropic_stage_not_selfDecomposable` |
| `prop:isotropic-stage-density (03)` | `AffineHemigroup.isotropic_stage_triplet`, `AffineHemigroup.isotropic_stage_absolutelyContinuous`, `AffineHemigroup.isotropic_stage_no_point_mass`, `AffineHemigroup.isotropic_stage_smooth_density`, `AffineHemigroup.isotropic_stage_dichotomy` |
| `prop:isotropic-bridge (03)` | `AffineHemigroup.isotropic_bridge_family`, `AffineHemigroup.isotropic_bridge_matern`, `AffineHemigroup.isotropic_bridge_stable`, `AffineHemigroup.isotropic_bridge_student_transform`, `AffineHemigroup.isotropic_bridge_student_family`, `AffineHemigroup.IsCausalKernels`, `AffineHemigroup.bridgeFamily` |
| `lem:operators-to-kernels (04)` | `AffineHemigroup.operators_to_kernels_repr`, `AffineHemigroup.operators_to_kernels_unique`, `AffineHemigroup.operators_to_kernels_converse`, `AffineHemigroup.operators_to_kernels_transport`, `AffineHemigroup.operators_to_kernels_transport_iff`, `AffineHemigroup.operators_to_kernels_continuity`, `AffineHemigroup.operators_to_kernels_gw`, `AffineHemigroup.operators_to_kernels_affine`, `AffineHemigroup.operators_to_kernels_isotropic`, `AffineHemigroup.gaussDensity`, `AffineHemigroup.gaussL1` |
| `lem:kernels-to-operators (04)` | `AffineHemigroup.kernels_to_operators_continuity`, `AffineHemigroup.kernels_to_operators_gw`, `AffineHemigroup.kernels_operators_correspondence`, `AffineHemigroup.kernels_to_operators_isotropic` |

## Licence

Lean sources under Apache 2.0, text under CC BY 4.0 (`LICENSES/`).
