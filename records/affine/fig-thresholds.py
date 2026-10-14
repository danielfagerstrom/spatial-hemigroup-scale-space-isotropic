# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "scipy", "matplotlib"]
# ///
"""Q-0286, review flag 40: the figure of the paper's section 3.4 (paper-iso/fig-thresholds.png since
the split of Q-0307; paper/fig-thresholds.png before).

Panel (a): the thresholds w_d = Gamma(m) / (2 M_d), m = (d+1)/2, of def:filtration-thresholds
(eq:threshold-constant), M_d = sup_{z>0} z^m (e^{-z} - 2^{-d/2} e^{-z/2}), for d = 1..20, with the
two bounds of lem:threshold-limit: e^{-1/2}/(2 sqrt m) <= w_d for every d, and
w_d <= K/(2 (1 - eps_d) sqrt m) when eps_d = 2^{-d/2} e^{m/2} < 1, K = sqrt(pi/2) + sqrt(pi) + 4.

Panel (b): the witness profiles k^{(w)}_d of the closed form [B, (A.1)] (eq:witness-polar,
restated in the proof of lem:threshold-monotone),
    k^{(w)}_d(r) = 2^{3/2} Gamma(m)/Gamma(d/2) / r + 2 w [P(d/2, r^2/2) - P(d/2, r^2/4)],
at w = 4, which lies in (w_3, w_2]: nonincreasing for d = 1, 2 and increasing somewhere for d = 3,
as thm:filtration-strict(1) says (F^(4) in A_2 minus A_3).

Nothing in the paper reads these numbers: every statement about the w_d is proved
(lem:threshold-monotone, lem:threshold-limit, thm:filtration-strict(2)). The script checks the
computed values against those statements and against the numerical values [B, Rem. 4.10] reports
(c_1 ~ 12.61, c_2 ~ 5.24, c_3 ~ 3.21; [B] writes c for w), and prints a table.

Run from the repository root:
    uv run records/affine/fig-thresholds.py > records/affine/fig-thresholds-output.txt
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import gamma, gammainc

ROOT = Path(__file__).resolve().parents[2]
# paper/ until the split (Q-0307, adr/0001). Q-0451: in the verification export of a release
# the paper's directory is paper/, and the script is at this same path, so it runs there too.
PAPER = ROOT / "paper-iso" if (ROOT / "paper-iso").is_dir() else ROOT / "paper"
OUT = PAPER / "fig-thresholds.png"
K = np.sqrt(np.pi / 2) + np.sqrt(np.pi) + 4


def h(d, z):
    m = (d + 1) / 2
    return z**m * (np.exp(-z) - 2 ** (-d / 2) * np.exp(-z / 2))


def M(d):
    """The supremum of h_d, attained in (0, d log 2) (lem:threshold-monotone)."""
    res = minimize_scalar(lambda z: -h(d, z), bounds=(1e-12, d * np.log(2)), method="bounded",
                          options={"xatol": 1e-13})
    # refine on a grid as a guard against a local optimum
    zs = np.linspace(1e-9, d * np.log(2), 20001)
    zg = zs[np.argmax(h(d, zs))]
    z = res.x if h(d, res.x) >= h(d, zg) else zg
    return h(d, z), z


def w_thr(d):
    m = (d + 1) / 2
    Md, z = M(d)
    return gamma(m) / (2 * Md), Md, z


def k_witness(w, d, r):
    m = (d + 1) / 2
    return (2**1.5 * gamma(m) / gamma(d / 2)) / r + 2 * w * (gammainc(d / 2, r**2 / 2)
                                                             - gammainc(d / 2, r**2 / 4))


def main():
    ds = np.arange(1, 21)
    rows = []
    print("Thresholds w_d = Gamma(m)/(2 M_d) of def:filtration-thresholds ([B]'s c_d), d = 1..20")
    print(f"{'d':>3} {'m':>5} {'z*':>9} {'M_d':>12} {'w_d':>10} {'lower':>9} {'eps_d':>8} {'upper':>9}")
    for d in ds:
        m = (d + 1) / 2
        wd, Md, z = w_thr(d)
        lo = np.exp(-0.5) / (2 * np.sqrt(m))
        eps = 2 ** (-d / 2) * np.exp(m / 2)
        up = K / (2 * (1 - eps) * np.sqrt(m)) if eps < 1 else np.inf
        rows.append((d, m, z, Md, wd, lo, eps, up))
        ups = f"{up:9.4f}" if np.isfinite(up) else "      inf"
        print(f"{d:3d} {m:5.1f} {z:9.5f} {Md:12.8f} {wd:10.5f} {lo:9.5f} {eps:8.4f} {ups}")

    w = np.array([r[4] for r in rows])
    print()
    print("Checks against the statements (all must read True):")
    print(f"  strictly decreasing for d = 1..20 (lem:threshold-monotone): {bool(np.all(np.diff(w) < 0))}")
    print(f"  z* in (0, d log 2) for every d (lem:threshold-monotone): "
          f"{all(0 < r[2] < r[0] * np.log(2) for r in rows)}")
    print(f"  M_(d+1) > sqrt(m) M_d for d = 1..19 (lem:threshold-monotone): "
          f"{all(rows[i + 1][3] > np.sqrt(rows[i][1]) * rows[i][3] for i in range(len(rows) - 1))}")
    print(f"  lower bound e^(-1/2)/(2 sqrt m) <= w_d (lem:threshold-limit): "
          f"{all(r[5] <= r[4] for r in rows)}")
    print(f"  upper bound K/(2(1-eps_d) sqrt m) >= w_d where eps_d < 1 (lem:threshold-limit): "
          f"{all(r[4] <= r[7] for r in rows if np.isfinite(r[7]))}")
    print(f"  w_2 < 6.34 < 6 + 4 sqrt 2 = {6 + 4 * np.sqrt(2):.4f} (thm:filtration-strict(2)): "
          f"{w[1] < 6.34 < 6 + 4 * np.sqrt(2)}")
    print(f"  [B, Rem. 4.10] values 12.61, 5.24, 3.21 reproduced to two decimals: "
          f"{[round(x, 2) for x in w[:3]] == [12.61, 5.24, 3.21]}")
    print(f"  w = 4 lies in (w_3, w_2] = ({w[2]:.4f}, {w[1]:.4f}]: {w[2] < 4 <= w[1]}")

    r = np.linspace(0.05, 4.0, 4000)
    print()
    print("Witness profiles k^(4)_d on r in [0.05, 4] (eq:witness-polar):")
    for d in (1, 2, 3):
        k = k_witness(4.0, d, r)
        dk = np.diff(k)
        inc = r[1:][dk > 0]
        rng = f"increasing on about [{inc.min():.3f}, {inc.max():.3f}]" if inc.size else "nonincreasing"
        print(f"  d = {d}: {rng}; max increment {dk.max():+.3e}")

    # Q-0428 (the presentation review of round 1, item 18; records/affine/reviews/
    # VERIFY-round1-presentation.md): drawn at the size at which it is printed, 0.86 of the text
    # width of 159.2 mm, that is 5.39 in, so that the 8 pt lettering set here prints at 8 pt
    # (the legends printed at 4.3 pt). Everything is black or grey with distinct line styles, so
    # that the panels read in greyscale. The paper's term is "critical values", not
    # "thresholds". In panel (a) the two bounds of lem:threshold-limit are named as bounds, and
    # the asymptote sqrt(pi/d) of lem:threshold-asymptotic is added (Q-0425). In panel (b) the
    # interval on which k^(4)_3 increases is shaded and labelled: it is what the panel is for.
    plt.rcParams.update({"font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8,
                         "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 8,
                         "axes.linewidth": 0.6, "mathtext.fontset": "cm"})
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.39, 2.05))
    ax1.semilogy(ds, w, "o-", color="k", ms=2.5, lw=0.9, label=r"$w_d$")
    ax1.semilogy(ds, np.sqrt(np.pi / ds), "-.", color="k", lw=0.8, label=r"$\sqrt{\pi/d}$")
    ax1.semilogy(ds, [r_[5] for r_ in rows], "--", color="0.4", lw=0.9, label="lower bound")
    upd = [(r_[0], r_[7]) for r_ in rows if np.isfinite(r_[7])]
    ax1.semilogy([u[0] for u in upd], [u[1] for u in upd], ":", color="0.4", lw=1.1,
                 label="upper bound")
    ax1.axhline(4.0, color="k", lw=0.5, ls=(0, (1, 2)))
    ax1.text(16.2, 3.6, r"$w = 4$", va="top", ha="left")
    ax1.set_xlabel(r"dimension $d$")
    ax1.set_ylabel(r"critical value $w_d$")
    ax1.set_xticks([1, 5, 10, 15, 20])
    ax1.legend(frameon=False, loc="upper right", handlelength=2.6, borderaxespad=0.2,
               labelspacing=0.25)
    ax1.set_title(r"(a) the critical values $w_d$")

    rr = np.linspace(0.4, 3.5, 2000)
    k3 = k_witness(4.0, 3, r)
    inc3 = r[1:][np.diff(k3) > 0]
    lo3, hi3 = float(inc3.min()), float(inc3.max())
    print()
    print(f"panel (b): k^(4)_3 increases on about [{lo3:.2f}, {hi3:.2f}], shaded in the figure")
    ax2.axvspan(lo3, hi3, color="0.85", lw=0)
    styles = {1: "-", 2: "--", 3: "-."}
    for d in (1, 2, 3):
        ax2.plot(rr, k_witness(4.0, d, rr), styles[d], color="k", lw=0.9,
                 label=rf"$k^{{(4)}}_{d}$")
    ax2.annotate(r"$k^{(4)}_3$ increases", xy=((lo3 + hi3) / 2, k_witness(4.0, 3, np.array([(lo3 + hi3) / 2]))[0]),
                 xytext=(1.0, 6.4), ha="left", va="center",
                 arrowprops={"arrowstyle": "-", "lw": 0.5, "shrinkA": 1.5, "shrinkB": 1.5})
    ax2.set_xlabel(r"radius $r$")
    ax2.set_ylabel(r"polar profile")
    ax2.set_ylim(0, None)
    ax2.legend(frameon=False, loc="upper right", handlelength=2.6, borderaxespad=0.2,
               labelspacing=0.25)
    ax2.set_title(r"(b) the witness at $w = 4$")
    for ax in (ax1, ax2):
        ax.tick_params(width=0.6, length=3)
        ax.tick_params(which="minor", width=0.4, length=1.5)
    fig.tight_layout(pad=0.3, w_pad=1.2)
    fig.savefig(OUT, dpi=600)
    print()
    print(f"figure written: {OUT.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
