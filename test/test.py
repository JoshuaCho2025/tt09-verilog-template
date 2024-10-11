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

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.a.value = 13
    dut.b.value = 10

    a_vals = [i for i in range(16)]
    b_vals = [i for i in range(16)]
    
    for i in range(len(a_vals)):
        for i in range(len(b_vals)):
            dut.a_value = a_vals[i]
            dut.b_value = b_vals[i]

            dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
            assert dut.sum.value == ((int(dut.a_value) + int(dut.b_value)) % 16) and dut.carry_out.value == (1 if ((int(dut.a_value) + int(dut.b_value)) >= 16) else 0)
            await ClockCycles(dut.clk, 10)
            
        
    # Wait for one clock cycle to see the output values

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
    

