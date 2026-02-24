<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

**Integration & Leak:** The circuit takes in an 8-bit input (`ui_in`) which represents incoming spikes. The membrane potential (`state`) integrates these inputs by adding them to the current state. 
**Spiking Mechanism:** 
**Refactory Period**: After firing, the neuron enters a refractory state for 10 clock cycles, disabling it durring that period.

## How to test

**Reset:** Bring rst_n low for at least 10 clock cycles to initialize the (`state`) and (`ref_count`) to zero
**Charge:** Provide a steady 8-bit input value
**See Spike:** Monitor (`uio_out[7]`) for a high pulse, which indicates the threshold has been met
**Refractory:** After a spike, observe that (`uo_out[7]`) remains low for 10 clock cycles, regardless of the input.
**Recovery:** After the refractory period, the neuron should be able to spike again if the input is sufficient.

## External hardware

N/A