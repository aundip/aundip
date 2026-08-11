"""Fetch the gitskins hero once and swap its auto-detected language chips for
real skills. The API takes no custom-chip param, so the SVG is patched and
committed as a static asset.
"""
import re, sys, urllib.request

SKILLS = ["Analog IC Design", "Sky130 130nm", "ngspice", "ΔΣ Mixed-Signal", "RISC-V RTL"]
TAGLINE = "Analog &amp; mixed-signal IC design on open silicon."
CHIP_X0, CHIP_GAP, CHIP_MAX_X = 46, 14, 700

def chip_width(label):
    # ponytail: 6.9px/char estimate for 12px/750-weight sans; no font metrics lib
    return round(len(label) * 6.9) + 30

def patch(svg):
    chips = re.findall(r'<g class="aura-chip".*?</g>', svg, re.S)
    if not chips:
        sys.exit("no chips found — gitskins markup changed")
    template = chips[0]
    rect = re.search(r'<rect [^>]*/>', template).group(0)
    text = re.search(r'<text [^>]*>.*?</text>', template, re.S).group(0)

    out, x = [], CHIP_X0
    for i, label in enumerate(SKILLS):
        w = chip_width(label)
        if x + w > CHIP_MAX_X:
            print(f"dropped (no room): {label}")
            continue
        r = re.sub(r'x="\d+"', f'x="{x}"', rect, count=1)
        r = re.sub(r'width="\d+"', f'width="{w}"', r, count=1)
        t = re.sub(r'x="\d+"', f'x="{x + 15}"', text, count=1)
        t = re.sub(r'>[^<]*</text>', f'>{label}</text>', t, count=1)
        out.append(f'<g class="aura-chip" style="animation-delay:{i * 90}ms">\n      {r}\n      {t}\n    </g>')
        x += w + CHIP_GAP

    svg = svg.replace(chips[0], "\n    ".join(out), 1)
    for extra in chips[1:]:
        svg = svg.replace(extra, "", 1)
    svg = re.sub(r'>Building with [^<]*</text>', f'>{TAGLINE}</text>', svg, count=1)
    return svg

for mode in ("dark", "light"):
    url = f"https://www.gitskins.com/api/section/hero?username=aundip&theme=matrix&mode={mode}"
    svg = patch(urllib.request.urlopen(url).read().decode())
    assert TAGLINE in svg and all(s in svg for s in SKILLS[:3]), "patch did not apply"
    assert "SourcePawn" not in svg and ">Python<" not in svg, "old chips survived"
    open(f"/Users/koundinya/gh-profile/hero-{mode}.svg", "w").write(svg)
    print(f"wrote hero-{mode}.svg ({len(svg)} bytes)")
