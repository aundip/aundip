<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://www.gitskins.com/api/section/hero?username=aundip&theme=matrix&mode=light" />
    <img src="https://www.gitskins.com/api/section/hero?username=aundip&theme=matrix&mode=dark" width="100%" alt="Profile banner for @aundip" />
  </picture>
</p>

<p align="center">
  <img src="https://www.gitskins.com/api/section/wordmark?username=aundip&theme=matrix&label=Koundinya" width="100%" alt="Koundinya" />
</p>

<p align="center">
  <b>Analog &amp; mixed-signal IC design</b> · Sky130 · ngspice · RISC-V<br/>
  <sub>EEE undergrad, University at Buffalo</sub>
</p>

<p align="center">
  <a href="https://aundip.github.io">Portfolio</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/aundip?tab=repositories">Repositories</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Sky130-130nm%20open%20PDK-0b7285?style=flat-square" alt="Sky130" />
  <img src="https://img.shields.io/badge/ngspice-46-1864ab?style=flat-square" alt="ngspice" />
  <img src="https://img.shields.io/badge/Python-NumPy%20%2F%20matplotlib-306998?style=flat-square" alt="Python" />
  <img src="https://img.shields.io/badge/RISC--V-CVA6%20%2F%20Verilator-283593?style=flat-square" alt="RISC-V" />
</p>

---

## General description

I design and characterize analog and mixed-signal blocks on the open Sky130
PDK, and measure the things I build instead of estimating them. Bandgap
references, OTAs, delta-sigma modulators on the analog side; RTL microarchitecture
experiments and device-level energy models on the digital side.

**One house rule, on every project:** no number is claimed until a real
simulation produced it. Unmeasured specs stay `—`. Every table below is a
testbench output, reproducible from the repo it links to.

## Selected work

| Project | Function | Measured |
| --- | --- | --- |
| [bandgap-sky130](https://github.com/aundip/bandgap-sky130) | Kuijk bandgap reference, folded-cascode error amp, real pass device | 1.220 V · **24 ppm/°C** · **0.009 %/V** line reg · 0.75 µs start-up · 47 µW |
| [delta-sigma-modulator](https://github.com/aundip/delta-sigma-modulator) | 3rd-order 1-bit ΔΣ modulator, behavioral NumPy model | **81.5 dB** SNDR · **13.2** ENOB · OSR 64 · 60 dB/dec · H∞ 1.49 |
| [sky130-miller-ota](https://github.com/aundip/sky130-miller-ota) | Two-stage Miller OTA: gm/ID sizing + 45-corner ngspice characterization harness | Harness validated on a 2-pole reference; DUT numbers pending |
| [cva6-ras-experiment](https://github.com/aundip/cva6-ras-experiment) | RAS depth vs IPC on CVA6 (Verilator), counted in hardware | Depth 4 is the knee · **+1.58%** dhrystone IPC · RAS misses −71% |
| [race-to-idle](https://github.com/aundip/race-to-idle) | When racing beats DVFS: α-power device physics + closed thermal loop | Crossover at slack ≈ 0.79 for 300 mW uncore |
| [secom-rca](https://github.com/aundip/secom-rca) | Root-cause attribution for SECOM lot failures | 590 signals → **1** surviving every test (S59) |

## Bench

```
PDK ......... sky130A (volare)          Sim ......... ngspice 46, Verilator 5
Analysis .... AC / tran / noise / MC    Corners ..... 5 process x 3 T x 3 VDD
Post ........ Python, NumPy, matplotlib RTL ......... SystemVerilog, CVA6
```

## Signal

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=aundip&show_icons=true&hide_border=true&hide_title=true&theme=transparent" alt="GitHub stats for aundip" />
</p>

## Duty cycle

The contribution graph, played back as a shooter. Regenerated nightly from this
repository's own activity.

<p align="center">
  <img src="https://raw.githubusercontent.com/aundip/aundip/output/space-shooter.gif" width="100%" alt="Animated contribution graph for aundip" />
</p>

## Current focus

- **Analog design** — closing the loop on the Miller OTA: real devices into the corner harness.
- **Mixed-signal** — taking the ΔΣ modulator from behavioral model to switched-capacitor schematic.
- **Open silicon** — everything above runs on free tools, so anyone can re-run the tables.

<p align="center">
  <sub>Measured, not estimated.</sub>
</p>
