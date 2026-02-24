# This project is for ECE-210 at UC Santa Cruz
## Leaky Integrate-and-Fire (LIF) with Refractory Period - By Cole Schreiner
## Overview:
This project aims implements a bio-inspired Leaky Integrate-and-Fire (LIF) neuron.
In order to imporove the base design, I implemented a **Refractory Period** which prevents
the neuron from firing for 10 clock cycles after a spiked event. This mimics the recovery time
of biological neurons and provides a natural low-pass filtering effect for high-frequency noise.

## Features:
- **Leaky Integration**: The exponential decay of the membrane potential over time uses a 
hardware efficient bit shift operation (`state >> 1`) to simulate membrane leakage.
- **Refactory Period**: After firing, the neuron enters a refractory state for 10 clock cycles, disabling it durring that period.

## Design:
1. **Integration**: The membrane potential (`state`) integrates incoming spikes and decays over time.
2. **Firing**: When the membrane potential exceeds a threshold >= 200, the neuron fires, outputting a spike and resetting the potential.
3. **Refractory Period**: After firing, the neuron is disabled for 10 clock cycles, ignoring all inputs and preventing it from firing again immediately.


<!-- ![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# Tiny Tapeout Verilog Project Template

- [Read the documentation for project](docs/info.md)

## What is Tiny Tapeout?

Tiny Tapeout is an educational project that aims to make it easier and cheaper than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## Set up your Verilog project

1. Add your Verilog files to the `src` folder.
2. Edit the [info.yaml](info.yaml) and update information about your project, paying special attention to the `source_files` and `top_module` properties. If you are upgrading an existing Tiny Tapeout project, check out our [online info.yaml migration tool](https://tinytapeout.github.io/tt-yaml-upgrade-tool/).
3. Edit [docs/info.md](docs/info.md) and add a description of your project.
4. Adapt the testbench to your design. See [test/README.md](test/README.md) for more information.

The GitHub action will automatically build the ASIC files using [LibreLane](https://www.zerotoasiccourse.com/terminology/librelane/).

## Enable GitHub actions to build the results page

- [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## Resources

- [FAQ](https://tinytapeout.com/faq/)
- [Digital design lessons](https://tinytapeout.com/digital_design/)
- [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
- [Join the community](https://tinytapeout.com/discord)
- [Build your design locally](https://www.tinytapeout.com/guides/local-hardening/)

## What next?

- [Submit your design to the next shuttle](https://app.tinytapeout.com/).
- Edit [this README](README.md) and explain your design, how it works, and how to test it.
- Share your project on your social network of choice:
  - LinkedIn [#tinytapeout](https://www.linkedin.com/search/results/content/?keywords=%23tinytapeout) [@TinyTapeout](https://www.linkedin.com/company/100708654/)
  - Mastodon [#tinytapeout](https://chaos.social/tags/tinytapeout) [@matthewvenn](https://chaos.social/@matthewvenn)
  - X (formerly Twitter) [#tinytapeout](https://twitter.com/hashtag/tinytapeout) [@tinytapeout](https://twitter.com/tinytapeout)
  - Bluesky [@tinytapeout.com](https://bsky.app/profile/tinytapeout.com)
 -->