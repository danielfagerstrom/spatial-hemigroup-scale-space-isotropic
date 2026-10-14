/-
Copyright (c) 2026 Daniel Fagerström. All rights reserved.
Released under the Apache 2.0 license as described in the file LICENSES/Apache-2.0.txt.
Authors: Daniel Fagerström
-/
import AffineHemigroup.IsotropicLibrary

/-!
# The axiom guard of the isotropic paper

**Generated** by `records/affine/axioms-iso-all-declarations.py gen`; do not edit by hand. The
script's `check` step fails when this file differs from what it generates.

`Formalization/CIAxiomGuard.lean` checks the whole module against `blueprint/trust-boundary.txt`,
twelve axioms, three of which are cited facts of the affine paper. The isotropic paper claims
nine: its seven cited facts, C3 being three (`blueprint/trust-boundary-iso.txt`). This file makes
that claim a build error when it fails. For each statement that Appendix B of the paper lists
(and for a statement whose Lean exists and which the paper does not print yet, when there is
one), one command

  `#iso_axioms <the declarations of the statement> expects <cited facts>`

fails unless (a) every declaration depends only on Lean's three logical axioms and on the nine,
and (b) the cited facts that the declarations reach, taken together, are exactly the listed ones,
which are those of the statement's row in the paper's table of the cited facts per statement, in
its Appendix B (none, when the statement has no row). The declarations are the `\lean` tags of
the blueprint nodes, read by `records/affine/gen-verification-table.py`, which also writes the
appendix's list.

The file is part of the library (nothing imports it), so `lake build`, and with it the Lean CI
job, runs the check. It prints nothing; the report of Lean's `#print axioms` for the same
declarations is `records/affine/axioms-iso-all-declarations-output.txt`. It imports the library
of the isotropic paper, `AffineHemigroup.IsotropicLibrary`, and no other file.
-/

open Lean Elab Command

namespace AffineHemigroup.IsoAxiomGuard

/-- Lean's three logical axioms. -/
def logicalAxioms : List Name := [``propext, ``Classical.choice, ``Quot.sound]

/-- The nine axioms of the isotropic paper: its cited facts C1 to C7, C3 being three. -/
def citedFacts : List Name := [
  ``AffineHemigroup.density_of_integrable_charFun,
  ``AffineHemigroup.sato_polar_criterion,
  ``AffineHemigroup.levy_khintchine_exists,
  ``AffineHemigroup.levy_khintchine_unique,
  ``AffineHemigroup.levy_khintchine_converse,
  ``AffineHemigroup.selfDecomposable_infinitelyDivisible,
  ``AffineHemigroup.wolfe_symmetric_unimodal,
  ``AffineHemigroup.schoenberg_radial_bernstein,
  ``AffineHemigroup.karamata_tauberian_zero]

/-- `#iso_axioms d₁ d₂ … expects a₁ a₂ …`: every declaration `dᵢ` depends only on the logical
axioms and on `citedFacts`, and the cited facts reached by the `dᵢ` together are exactly the
`aⱼ`. -/
syntax (name := isoAxioms) "#iso_axioms " ident* " expects " ident* : command

@[command_elab isoAxioms] def elabIsoAxioms : CommandElab := fun stx => do
  let want := stx[3].getArgs.toList.map (·.getId)
  let mut reached : List Name := []
  for d in stx[1].getArgs do
    let n ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo d
    let axs ← liftCoreM <| collectAxioms n
    for a in axs do
      unless logicalAxioms.contains a do
        unless citedFacts.contains a do
          throwErrorAt d "{n} depends on the axiom {a}, not one of the isotropic paper's nine"
        unless reached.contains a do
          reached := a :: reached
  for a in reached do
    unless want.contains a do
      throwError "the declarations of this statement reach {a}, which its row does not list"
  for a in want do
    unless reached.contains a do
      throwError "the row lists {a}, which no declaration of this statement reaches"

-- the commands below are the content of this file, not leftovers of a proof session
set_option linter.hashCommand false

-- Def. `def:isotropic-operator-family`: no cited fact
#iso_axioms
  AffineHemigroup.IsIsotropicOperatorFamily
  AffineHemigroup.IsSingleOperator
  expects

-- Def. `def:isotropic-kernel-family`: no cited fact
#iso_axioms
  AffineHemigroup.IsIsotropicCascadeFamily
  AffineHemigroup.IsIncreasingBijection
  AffineHemigroup.IsGauge
  ScaleSpace.IsSelfDecomposable
  ScaleSpace.isSelfDecomposable_iff_charFun
  AffineHemigroup.push
  AffineHemigroup.charFun_push
  AffineHemigroup.isGauge_iff_isIncreasingBijection
  expects

-- Lemma `lem:operators-to-kernels`: no cited fact
#iso_axioms
  AffineHemigroup.operators_to_kernels_repr
  AffineHemigroup.operators_to_kernels_unique
  AffineHemigroup.operators_to_kernels_converse
  AffineHemigroup.operators_to_kernels_transport
  AffineHemigroup.operators_to_kernels_transport_iff
  AffineHemigroup.operators_to_kernels_continuity
  AffineHemigroup.operators_to_kernels_gw
  AffineHemigroup.operators_to_kernels_affine
  AffineHemigroup.operators_to_kernels_isotropic
  AffineHemigroup.gaussDensity
  AffineHemigroup.gaussL1
  AffineHemigroup.kernels_to_operators_continuity
  AffineHemigroup.kernels_to_operators_gw
  AffineHemigroup.kernels_operators_correspondence
  AffineHemigroup.kernels_to_operators_isotropic
  expects

-- Lemma `lem:radial-marginal`: no cited fact
#iso_axioms
  AffineHemigroup.radial_marginal
  AffineHemigroup.radial_marginal_eq_dirac
  AffineHemigroup.radial_marginal_ops
  AffineHemigroup.marginal
  expects

-- Lemma `lem:isotropic-marginal-family`: no cited fact
#iso_axioms
  AffineHemigroup.isotropic_marginal_family
  AffineHemigroup.isotropic_marginal_cascadeData
  ScaleSpace.CascadeFamily
  ScaleSpace.CascadeData
  expects

-- Thm. `thm:isotropic-classification`: C3(ii), C3(iii)
#iso_axioms
  AffineHemigroup.isotropic_classification
  AffineHemigroup.isotropic_classification_origin
  AffineHemigroup.isotropic_classification_unique
  expects
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse

-- Cor. `cor:isotropic-classification-operators`: C3(ii), C3(iii)
#iso_axioms
  AffineHemigroup.isotropic_classification_operators
  AffineHemigroup.isotropic_classification_operators_unique
  expects
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse

-- Lemma `lem:isotropic-realisation`: no cited fact
#iso_axioms
  AffineHemigroup.isotropic_realisation
  expects

-- Cor. `cor:isotropic-scale-zero-kernels`: C2, C3(i), C3(ii), C3(iii), C4
#iso_axioms
  AffineHemigroup.scale_zero_kernels
  AffineHemigroup.scale_zero_operators
  AffineHemigroup.scale_zero_families
  AffineHemigroup.scale_zero_relabelling
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_exists
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.selfDecomposable_infinitelyDivisible

-- Def. `def:isotropic-origin-datum`: no cited fact
#iso_axioms
  AffineHemigroup.OriginDatum
  AffineHemigroup.OriginDatum.levyMeasure
  AffineHemigroup.OriginDatum.exponentL
  AffineHemigroup.OriginDatum.exponent
  AffineHemigroup.OriginDatum.profileAtOrigin
  AffineHemigroup.OriginDatum.IsSubordinated
  AffineHemigroup.IsLawOf
  AffineHemigroup.sphereArea
  AffineHemigroup.polarProfileOf
  AffineHemigroup.sphereArea_eq_toSphere
  AffineHemigroup.OriginDatum.tendsto_profileAtOrigin
  AffineHemigroup.OriginDatum.polar_decomposition
  expects

-- Prop. `prop:isotropic-polar-reading`: C2, C3(i), C3(ii), C3(iii), C4
#iso_axioms
  AffineHemigroup.polar_reading
  AffineHemigroup.polar_reading_unique
  AffineHemigroup.polar_reading_admissible
  AffineHemigroup.classA_iff_originDatum
  AffineHemigroup.polar_classification
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_exists
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.selfDecomposable_infinitelyDivisible

-- Prop. `prop:isotropic-bridge`: no cited fact
#iso_axioms
  AffineHemigroup.isotropic_bridge_family
  AffineHemigroup.isotropic_bridge_matern
  AffineHemigroup.isotropic_bridge_stable
  AffineHemigroup.isotropic_bridge_student_transform
  AffineHemigroup.isotropic_bridge_student_family
  AffineHemigroup.IsCausalKernels
  AffineHemigroup.bridgeFamily
  AffineHemigroup.gaussVar
  AffineHemigroup.measurable_gaussVar
  expects

-- Thm. `thm:origin-boundedness-d`: C1
#iso_axioms
  AffineHemigroup.origin_decay_exponent
  AffineHemigroup.origin_density_smooth
  AffineHemigroup.origin_density_bounded_smooth
  AffineHemigroup.subordinated_profileAtOrigin
  AffineHemigroup.subordinated_law
  AffineHemigroup.delayLaw_zero
  AffineHemigroup.subordinated_density_limit
  AffineHemigroup.subordinated_unbounded
  AffineHemigroup.origin_unbounded
  AffineHemigroup.origin_unbounded_rate
  AffineHemigroup.origin_dichotomy
  AffineHemigroup.measurable_gaussVar
  expects
  AffineHemigroup.density_of_integrable_charFun

-- Cor. `cor:origin-profile-exponent`: no cited fact
#iso_axioms
  AffineHemigroup.exponent_gaussian_limit
  AffineHemigroup.exponent_profile_limit
  AffineHemigroup.transform_profile_limit
  AffineHemigroup.origin_profile_dimension_free
  expects

-- Prop. `prop:isotropic-radial-monotone`: C2, C3(ii), C3(iii), C5
#iso_axioms
  AffineHemigroup.radial_monotone_family
  AffineHemigroup.radial_monotone_law
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.wolfe_symmetric_unimodal

-- Prop. `prop:isotropic-exponent-profile`: no cited fact
#iso_axioms
  AffineHemigroup.slowFactor_basic
  AffineHemigroup.slowFactor_ratio
  AffineHemigroup.slowFactor_tendsto_of_integrable
  AffineHemigroup.slowFactor_tendsto_atTop
  AffineHemigroup.cin_sub_log_limit
  AffineHemigroup.sphere_log_mean
  AffineHemigroup.sphereLogMean_one
  AffineHemigroup.exponent_profile_asymptotic
  AffineHemigroup.exponent_profile_bounds
  AffineHemigroup.transform_power_comparison
  AffineHemigroup.transform_power_bounded_iff
  AffineHemigroup.transform_power_limit
  AffineHemigroup.OriginDatum.slowFactor
  AffineHemigroup.OriginDatum.slowFactorZero
  AffineHemigroup.sphereLogMean
  AffineHemigroup.exponentConst
  expects

-- Prop. `prop:origin-rate-profile-d`: C2, C3(iii), C5, C7
#iso_axioms
  AffineHemigroup.origin_rate_profile
  AffineHemigroup.origin_rate_profile_critical
  AffineHemigroup.origin_density_rate_profile
  AffineHemigroup.origin_ball_rate_profile
  AffineHemigroup.origin_density_power_of_integrable
  AffineHemigroup.origin_density_power_of_not_integrable
  AffineHemigroup.origin_density_rate_profile_critical
  AffineHemigroup.origin_ball_rate_profile_critical
  AffineHemigroup.slowLog_bounds
  AffineHemigroup.slowLog_div_log
  AffineHemigroup.origin_density_log_of_integrable
  AffineHemigroup.origin_density_log_of_not_integrable
  AffineHemigroup.OriginDatum.profileConst
  AffineHemigroup.OriginDatum.slowLog
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.wolfe_symmetric_unimodal
  AffineHemigroup.karamata_tauberian_zero

-- Prop. `prop:isotropic-stages`: C1, C3(iii)
#iso_axioms
  AffineHemigroup.OriginDatum.stageProfile
  AffineHemigroup.OriginDatum.stageMeasure
  AffineHemigroup.OriginDatum.stageProfile_nonneg
  AffineHemigroup.OriginDatum.stageMeasure_zero
  AffineHemigroup.OriginDatum.stageMeasure_absolutelyContinuous
  AffineHemigroup.OriginDatum.stageMeasure_rotation
  AffineHemigroup.OriginDatum.stageMeasure_integrable
  AffineHemigroup.OriginDatum.exponent_smul_sub_smul
  AffineHemigroup.OriginDatum.stageMeasure_univ
  AffineHemigroup.OriginDatum.stageMeasure_univ_ne_top_iff
  AffineHemigroup.isotropic_stage_transform
  AffineHemigroup.isotropic_stage_mass
  AffineHemigroup.isotropic_stage_compoundPoisson
  AffineHemigroup.isotropic_stage_exp_neg_mass
  AffineHemigroup.profileAtOrigin_pos
  AffineHemigroup.isotropic_stage_atom
  AffineHemigroup.isotropic_stage_operator
  AffineHemigroup.isotropic_stage_not_selfDecomposable
  AffineHemigroup.isotropic_stage_triplet
  AffineHemigroup.isotropic_stage_absolutelyContinuous
  AffineHemigroup.isotropic_stage_no_point_mass
  AffineHemigroup.isotropic_stage_smooth_density
  AffineHemigroup.isotropic_stage_dichotomy
  expects
  AffineHemigroup.density_of_integrable_charFun
  AffineHemigroup.levy_khintchine_converse

-- Prop. `prop:profile-one-dimension-down`: C2, C3(i), C3(ii), C3(iii), C4
#iso_axioms
  AffineHemigroup.profile_one_dimension_down
  AffineHemigroup.profile_one_dimension_down_of_classA
  AffineHemigroup.not_classA_succ_of_profile_discontinuous
  AffineHemigroup.step_datum_separates
  AffineHemigroup.cin_ray_not_classA
  AffineHemigroup.stepOriginDatum
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_exists
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.selfDecomposable_infinitelyDivisible

-- Def. `def:filtration-thresholds`: no cited fact
#iso_axioms
  AffineHemigroup.classS
  AffineHemigroup.classA
  AffineHemigroup.classAInf
  AffineHemigroup.DelayDatum
  AffineHemigroup.delayExponentL
  AffineHemigroup.witnessProfile
  AffineHemigroup.witnessExponent
  AffineHemigroup.witnessF
  AffineHemigroup.polarProfileOf
  AffineHemigroup.thresholdFun
  AffineHemigroup.thresholdSup
  AffineHemigroup.threshold
  AffineHemigroup.witness_isDelayDatum
  expects

-- Thm. `thm:separating-family-critical-values`: C2, C3(i), C3(ii), C3(iii), C4
#iso_axioms
  AffineHemigroup.separating_family_critical_values
  AffineHemigroup.witness_classA_iff
  AffineHemigroup.criticalValues_strictAnti
  AffineHemigroup.criticalValues_tendsto
  AffineHemigroup.witness_classA_iff_le
  AffineHemigroup.witness_not_classA_of_gt
  AffineHemigroup.criticalValues_existsUnique_window
  AffineHemigroup.separating_family_strict
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_exists
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.selfDecomposable_infinitelyDivisible

-- Lemma `lem:polar-decomposition`: no cited fact
#iso_axioms
  AffineHemigroup.OriginDatum.polar_decomposition
  expects

-- Lemma `lem:isotropic-exponent-log`: no cited fact
#iso_axioms
  AffineHemigroup.isotropic_exponent_log_bound
  AffineHemigroup.isotropic_exponent_log_limit
  AffineHemigroup.OriginDatum.tailConst
  expects

-- Prop. `prop:origin-lower-bound-d`: C3(iii)
#iso_axioms
  AffineHemigroup.origin_lower_bound
  AffineHemigroup.origin_lower_bound_density
  AffineHemigroup.origin_lower_bound_ball
  AffineHemigroup.lowerBoundConst
  AffineHemigroup.lowerBoundTau
  AffineHemigroup.lowerBoundKappa
  expects
  AffineHemigroup.levy_khintchine_converse

-- Prop. `prop:origin-upper-bound-d`: C2, C3(iii), C5
#iso_axioms
  AffineHemigroup.origin_upper_bound
  AffineHemigroup.origin_upper_bound_of_heat
  AffineHemigroup.origin_density_upper
  AffineHemigroup.origin_density_lower
  AffineHemigroup.origin_density_log_order
  AffineHemigroup.origin_ball_log_order
  AffineHemigroup.origin_density_order
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.wolfe_symmetric_unimodal

-- Lemma `lem:shadow-polar-profile`: no cited fact
#iso_axioms
  AffineHemigroup.shadow_profile_mean
  AffineHemigroup.shadow_profile_regular
  AffineHemigroup.shadow_datum
  AffineHemigroup.lintegral_shadow
  AffineHemigroup.OriginDatum.shadow
  AffineHemigroup.shadowProfile
  expects

-- Lemma `lem:delay-polar-profile`: no cited fact
#iso_axioms
  AffineHemigroup.delay_polar_profile
  AffineHemigroup.delay_polar_profile_datum
  expects

-- Lemma `lem:positive-transform-origin`: no cited fact
#iso_axioms
  AffineHemigroup.positive_transform_heat
  AffineHemigroup.positive_transform_bound
  AffineHemigroup.density_bound_ball
  AffineHemigroup.heatKernel
  expects

-- Lemma `prop:origin-rate-d`: C2, C3(iii), C5, C7
#iso_axioms
  AffineHemigroup.origin_ball_rate
  AffineHemigroup.origin_density_rate
  AffineHemigroup.origin_ball_rate_critical
  AffineHemigroup.origin_density_rate_critical
  AffineHemigroup.origin_transform_ball_log
  AffineHemigroup.origin_density_log_lower
  AffineHemigroup.origin_rate
  AffineHemigroup.origin_rate_critical
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.wolfe_symmetric_unimodal
  AffineHemigroup.karamata_tauberian_zero

-- Lemma `lem:threshold-monotone`: no cited fact
#iso_axioms
  AffineHemigroup.thresholdSup_spec
  AffineHemigroup.threshold_pos
  AffineHemigroup.thresholdSup_succ
  AffineHemigroup.threshold_strictAnti
  AffineHemigroup.witness_polar_closed_form
  AffineHemigroup.witness_threshold_criterion
  AffineHemigroup.witness_antitone_iff
  expects

-- Lemma `lem:threshold-limit`: no cited fact
#iso_axioms
  AffineHemigroup.threshold_limit_bounds
  AffineHemigroup.threshold_limit
  AffineHemigroup.thresholdEps
  AffineHemigroup.stirlingK
  expects

-- Lemma `lem:threshold-asymptotic`: no cited fact
#iso_axioms
  AffineHemigroup.tendsto_stirlingRatio
  AffineHemigroup.threshold_asymptotic_bounds
  AffineHemigroup.threshold_asymptotic
  AffineHemigroup.stirlingRatio
  expects

-- Lemma `lem:filtration-top`: C2, C3(i), C3(ii), C3(iii), C4, C6
#iso_axioms
  AffineHemigroup.classAInf_of_classS
  AffineHemigroup.classS_of_classAInf
  AffineHemigroup.filtration_top
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_exists
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.selfDecomposable_infinitelyDivisible
  AffineHemigroup.schoenberg_radial_bernstein

/-! ## Statements with Lean that the paper does not print -/

-- Thm. `thm:filtration-strict`: C2, C3(i), C3(ii), C3(iii), C4, C6
#iso_axioms
  AffineHemigroup.filtration_witness
  AffineHemigroup.filtration_witness_exists
  AffineHemigroup.filtration_strict
  AffineHemigroup.filtration_top
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_exists
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.selfDecomposable_infinitelyDivisible
  AffineHemigroup.schoenberg_radial_bernstein

-- Thm. `thm:no-cin-ray-in-the-plane`: C2, C3(i), C3(ii), C3(iii), C4
#iso_axioms
  AffineHemigroup.no_cin_ray_in_the_plane
  AffineHemigroup.cin_ray_scaled
  expects
  AffineHemigroup.sato_polar_criterion
  AffineHemigroup.levy_khintchine_exists
  AffineHemigroup.levy_khintchine_unique
  AffineHemigroup.levy_khintchine_converse
  AffineHemigroup.selfDecomposable_infinitelyDivisible

end AffineHemigroup.IsoAxiomGuard
