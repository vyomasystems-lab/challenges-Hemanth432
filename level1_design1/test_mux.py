# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
   
    await Timer(2, units='ns')
    for i in range(5):

    
        sel= random.randint(0,30)
        inp0=random.randint(0,3)
        inp1=random.randint(0,3)
        inp2=random.randint(0,3)
        inp3=random.randint(0,3)
        inp4=random.randint(0,3)
        inp5=random.randint(0,3)
        inp6=random.randint(0,3)
        inp7=random.randint(0,3)
        inp8=random.randint(0,3)
        inp9=random.randint(0,3)
        inp10=random.randint(0,3)
        inp11=random.randint(0,3)
        inp12=random.randint(0,3)
        inp13=random.randint(0,3)
        inp14=random.randint(0,3)
        inp15=random.randint(0,3)
        inp16=random.randint(0,3)
        inp17=random.randint(0,3)
        inp18=random.randint(0,3)
        inp19=random.randint(0,3)
        inp20=random.randint(0,3)
        inp21=random.randint(0,3)
        inp22=random.randint(0,3)
        inp23=random.randint(0,3)
        inp24=random.randint(0,3)
        inp25=random.randint(0,3)
        inp26=random.randint(0,3)
        inp27=random.randint(0,3)
        inp28=random.randint(0,3)
        inp29=random.randint(0,3)
        inp30=random.randint(0,3)

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
        
        dut._log.info(f'sel={sel:05} inp0={inp0:02} inp1={inp1:02} inp2={inp2:02} inp3={inp3:02} inp4={inp4:02} inp5={inp5:02} inp6={inp6:02} inp7={inp7:02} inp8={inp8:02} inp9={inp9:02} inp10={inp10:02} inp11={inp11:02} inp12={inp12:02} inp13={inp13:02} inp14={inp14:02} inp15={inp15:02} inp16={inp16:02} inp17={inp17:02} inp18={inp18:02} inp19={inp19:02} inp20={inp20:02} inp21={inp21:02} inp22={inp22:02} inp23={inp23:02} inp24={inp24:02} inp25={inp25:02} inp26={inp26:02} inp27={inp27:02} inp28={inp28:02} inp29={inp29:02} inp30={inp30:02} model={A+B:02} DUT={int(dut.out.value):02}')
        assert dut.out.value == A+B, "Randomised test failed with: {A} + {B} = {OUT}".format(
            A=dut.a.value, B=dut.b.value, SUM=dut.out.value)