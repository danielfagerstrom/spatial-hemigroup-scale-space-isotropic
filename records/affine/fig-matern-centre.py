# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "scipy", "matplotlib"]
# ///
"""Q-0313, PROCESS.md section 8 pass 1 (readability): a figure for the threshold theorem
(thm:origin-boundedness-d), paper-iso/fig-matern-centre.png.

The object drawn is the radial density of the Matern kernel mu_{0,1} of prop:isotropic-bridge(2),
the law on R^d with transform (1 + |xi|^2/2)^{-gamma}, at gamma = 3/4, in dimensions d = 1, 2, 3.
Its density is the symmetric case of the multivariate variance-gamma (generalized Laplace) density
of Fischer, Gaunt and Sarantsev (2.24), p. 10 (records/affine/READING-fischer2025variance.md), with
mu = theta = 0, s = gamma, Sigma = I, so Q = |x| and C = sqrt 2:

    p_d(r) = 2 / ((2 pi)^{d/2} Gamma(gamma)) * (r / sqrt 2)^{gamma - d/2} * K_{gamma - d/2}(sqrt 2 r).

The kernel's profile at the origin is c = 2 gamma = 3/2 in every dimension (clause (3) of the
theorem: k_I(0+) = gamma for F_I(sigma) = gamma log(1 + sigma)), so the theorem puts the density
bounded near the centre for d = 1 (3/2 > 1) and unbounded for d = 2, 3 (3/2 <= d).

The script checks, and prints: (i) that each p_d integrates to 1 over R^d, |S^{d-1}| int r^{d-1}
p_d(r) dr; (ii) the d = 1, gamma = 1 case against the Laplace density e^{-sqrt 2 |x|}/sqrt 2;
(iii) the value of p_1 at the centre, 2^{nu-1} Gamma(nu) times the prefactor with nu = 1/4; and
(iv) the local slope of log p_d against log r at small r, which is 2 gamma - d for d > 2 gamma
(K_nu(z) ~ Gamma(|nu|)/2 (z/2)^{-|nu|} as z -> 0). Nothing in the paper reads these numbers.

Run from the repository root:
    uv run records/affine/fig-matern-centre.py > records/affine/fig-matern-centre-output.txt
"""
from math import gamma as Gamma, pi, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.special import kv

ROOT = Path(__file__).resolve().parents[2]
# Q-0451: in the verification export of a release the paper's directory is paper/, and the
# script is at this same path, so it runs there too.
PAPER = ROOT / "paper-iso" if (ROOT / "paper-iso").is_dir() else ROOT / "paper"
OUT = PAPER / "fig-matern-centre.png"
GAMMA = 0.75


def density(r, d, g=GAMMA):
    """The radial density of the Matern kernel mu_{0,1} of index g on R^d (Fischer (2.24))."""
    nu = g - d / 2
    return 2 / ((2 * pi) ** (d / 2) * Gamma(g)) * (r / sqrt(2)) ** nu * kv(nu, sqrt(2) * r)


def sphere_area(d):
    return 2 * pi ** (d / 2) / Gamma(d / 2)


def main():
    print(f"Matern kernel mu_(0,1) of index gamma = {GAMMA}; profile at the origin c = 2 gamma = "
          f"{2 * GAMMA}")
    print()
    print("(i) total mass |S^(d-1)| int_0^inf r^(d-1) p_d(r) dr")
    for d in (1, 2, 3):
        f = lambda r: sphere_area(d) * r ** (d - 1) * density(r, d)
        mass = quad(f, 0, 1, limit=200)[0] + quad(f, 1, np.inf, limit=200)[0]
        print(f"  d = {d}: {mass:.10f}")
        assert abs(mass - 1) < 1e-7
    print()
    lap = [density(x, 1, 1.0) / (np.exp(-sqrt(2) * x) / sqrt(2)) for x in (0.1, 0.5, 1.0, 2.0)]
    print("(ii) d = 1, gamma = 1 against the Laplace density e^(-sqrt2 |x|)/sqrt2, ratios:",
          ", ".join(f"{v:.12f}" for v in lap))
    assert all(abs(v - 1) < 1e-12 for v in lap)
    print()
    nu = GAMMA - 0.5
    # With z = sqrt2 r, (r/sqrt2)^nu = z^nu / 2^nu and z^nu K_nu(z) -> 2^{nu-1} Gamma(nu) as z -> 0.
    p1_0 = 2 / ((2 * pi) ** 0.5 * Gamma(GAMMA)) * 2 ** (nu - 1) * Gamma(nu) / 2 ** nu
    print(f"(iii) d = 1: p_1(0+) = {p1_0:.10f}; p_1(1e-8) = {density(1e-8, 1):.10f}")
    print()
    print("(iv) local slope d log p_d / d log r at small r (2 gamma - d where d > 2 gamma)")
    for d in (1, 2, 3):
        r1, r2 = 1e-6, 1e-5
        slope = (np.log(density(r2, d)) - np.log(density(r1, d))) / (np.log(r2) - np.log(r1))
        expect = 2 * GAMMA - d if d > 2 * GAMMA else 0.0
        print(f"  d = {d}: slope {slope:+.4f}, expected {expect:+.4f}")
    print()

    # Q-0428 (the presentation review of round 1, item 17; records/affine/reviews/
    # VERIFY-round1-presentation.md): the figure is drawn at the size at which it is printed,
    # 0.45 of the text width of 159.2 mm, that is 2.82 in, so that the 8 pt lettering set here
    # prints at 8 pt (it printed at 4.4 pt: a 6.4 in drawing with 10 pt lettering, reduced). The
    # curves are labelled on the plot and not in a legend, the bounded one as bounded, the axis
    # says that |x| is the distance from the centre, and the left end is marked. The three line
    # styles, in black, stay distinct in greyscale.
    plt.rcParams.update({"font.size": 8, "axes.labelsize": 8, "xtick.labelsize": 8,
                         "ytick.labelsize": 8, "axes.linewidth": 0.6,
                         "mathtext.fontset": "cm"})
    r = np.logspace(-3, np.log10(3), 400)
    fig, ax = plt.subplots(figsize=(2.82, 1.75))
    styles = {1: "-", 2: "--", 3: ":"}
    for d in (1, 2, 3):
        ax.loglog(r, density(r, d), styles[d], color="black", lw=1.0)
    # the labels, each in an empty part of the plot with a thin line to its curve
    lead = {"arrowstyle": "-", "lw": 0.5, "shrinkA": 1.5, "shrinkB": 0}
    ax.annotate("$d = 3$, unbounded", xy=(1.2e-2, density(1.2e-2, 3)), xytext=(4e-2, 9e2),
                ha="left", va="center", arrowprops=lead)
    ax.annotate("$d = 2$, unbounded", xy=(2.5e-2, density(2.5e-2, 2)), xytext=(8e-2, 6e1),
                ha="left", va="center", arrowprops=lead)
    ax.annotate("$d = 1$, bounded", xy=(1.2e-2, density(1.2e-2, 1)), xytext=(4e-3, 6e-2),
                ha="left", va="center", arrowprops=lead)
    ax.set_xlabel("distance $|x|$ from the centre")
    ax.set_ylabel("density of $\\mu_{0,1}$")
    ax.annotate("centre", xy=(1e-3, 3e-3), xytext=(3.2e-3, 3e-3), va="center", ha="left",
                arrowprops={"arrowstyle": "->", "lw": 0.6})
    ax.set_xlim(1e-3, 3)
    ax.set_ylim(3e-4, 8e3)
    ax.tick_params(width=0.6, length=3)
    ax.tick_params(which="minor", width=0.4, length=1.5)
    fig.tight_layout(pad=0.3)
    fig.savefig(OUT, dpi=600)
    print(f"wrote {OUT.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
