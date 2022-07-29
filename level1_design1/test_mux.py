# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    sel=25
    inp0=0
    inp1=1
    inp2=2
    inp3=3
    inp4=0
    inp5=1
    inp6=2
    inp7=3
    inp8=0
    inp9=1
    inp10=2
    inp11=3
    inp12=0
    inp13=1
    inp14=2
    inp15=3
    inp16=0
    inp17=1
    inp18=2
    inp19=3
    inp20=0
    inp21=1
    inp22=2
    inp23=3
    inp24=0
    inp25=1
    inp26=2
    inp27=3
    inp28=0
    inp29=1
    inp30=2
    
    # input driving
    dut.sel.value=sel
    dut.inp0.value=inp0
    dut.inp1.value=inp1
    dut.inp2.value=inp2
    dut.inp3.value=inp3
    dut.inp4.value=inp4
    dut.inp5.value=inp5
    dut.inp6.value=inp6
    dut.inp7.value=inp7
    dut.inp8.value=inp8
    dut.inp9.value=inp9
    dut.inp10.value=inp10
    dut.inp11.value=inp11
    dut.inp12.value=inp12
    dut.inp13.value=inp13
    dut.inp14.value=inp14
    dut.inp15.value=inp15
    dut.inp16.value=inp16
    dut.inp17.value=inp17
    dut.inp18.value=inp18
    dut.inp19.value=inp19
    dut.inp20.value=inp20
    dut.inp21.value=inp21
    dut.inp22.value=inp22
    dut.inp23.value=inp23
    dut.inp24.value=inp24
    dut.inp25.value=inp25
    dut.inp26.value=inp26
    dut.inp27.value=inp27
    dut.inp28.value=inp28
    dut.inp29.value=inp29
    dut.inp30.value=inp30

    await Timer(2, units='ns')
    
    assert dut.out.value == inp7, "multiplexer result is incorrect: {inp7} != {OUT}, expected value={3}".format(
        sel=int(dut.sel.value), inp0=int(dut.inp0.value), inp1=int(dut.inp1.value),inp2=int(dut.inp2.value),inp3=int(dut.inp3.value),
                inp4=int(dut.inp4.value),
                inp5=int(dut.inp5.value),
                inp6=int(dut.inp6.value),
                inp7=int(dut.inp7.value),
                inp8=int(dut.inp8.value),
                inp9=int(dut.inp9.value),
                inp10=int(dut.inp10.value),
                inp11=int(dut.inp11.value),
                inp12=int(dut.inp12.value),
                inp13=int(dut.inp13.value),
                inp14=int(dut.inp14.value),
                inp15=int(dut.inp15.value),
                inp16=int(dut.inp16.value),
                inp17=int(dut.inp17.value),
                inp18=int(dut.inp18.value),
                inp19=int(dut.inp19.value),
                inp20=int(dut.inp20.value),
                inp21=int(dut.inp21.value),
                inp22=int(dut.inp22.value),
                inp23=int(dut.inp23.value),
                inp24=int(dut.inp24.value),
                inp25=int(dut.inp25.value),
                inp26=int(dut.inp26.value),
                inp27=int(dut.inp27.value),
                inp28=int(dut.inp28.value),
                inp29=int(dut.inp29.value),
                inp30=int(dut.inp30.value),
             OUT=int(dut.out.value), EXP=1)



