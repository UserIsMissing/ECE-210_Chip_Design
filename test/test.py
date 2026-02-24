# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Resetting circuit")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    # Charging neuron to trigger a spike
    # for state >> 1 leak, input of 150 hits threshold of 200 quicker
    dut._log.info("Testing charged neuron:")
    dut.ui_in.value = 150

    # wait to see a spike on bit 7 (out)
    for i in range (20):
        await ClockCycles(dut.clk, 1)
        if dut.uio_out.value & 0x80: # see if bit 7 is HIGH
            dut._log.info(f"Spike detected at cycle #{i}")
            break
    else:
        raise AssertionError("Neuron never spiked!!!")
    
    # Verifying correct refractory period
    # After a spike, state should remain 0 for 10 cycles
    dut._log.info("Testing Refractory Period (ignoring inputs)...")
    for i in range(1, 11):
        await ClockCycles(dut.clk, 1)
        current_state = int(dut.uo_out.value)
        current_spike = int(dut.uio_out.value) & 0x80
        
        dut._log.info(f"Refractory Cycle {i}: State = {current_state}, Spike = {current_spike}")

        assert current_state == 0, f"Error: State should be 0 durring refractory period (Cycle {i})"
        assert current_spike == 0, f"Error: Shouldn't spike durring refractory period (Cycle {i})"

    # Verifying recovery
    # Refractory period ended
    # Needed to wait 2 cycles. First the counter sets to 0, then the state updates
    # At cycle 11, refrac period ends, neuron should start charging again
    await ClockCycles(dut.clk, 2)

    current_state = int(dut.uo_out.value)
    dut._log.info(f"Recovery Cycle: State = {current_state}")

    assert int(current_state) > 0, "Error: Neuron failed to charge after refractory period"
    dut._log.info("PASSED")
