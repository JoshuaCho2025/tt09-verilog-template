<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works
Kogge-Stone vs Ripple
In contrast to the Ripple Carry Adder where we need to wait for the Cout from the previous bit to use as the Cin for the next bit calculation, the Kogge-Stone will calculate all of the bit additions together and then after all of the carry outs are calculated, then all at the same time calculate the final addition using the cin. Don't need to wait for each stage to complete. We can just split up into 3 different stages basically. Load, Calculate the Cout, Calculate using the Cout again.

## How to test

Testing using python file and using different inputs generated from 0-15 for each input. 256 total combinations and used a python for loop to go through all of the different options. Because we covered all of the possibilities are covered, we also then cover the corner cases.

## External hardware

No hardware
