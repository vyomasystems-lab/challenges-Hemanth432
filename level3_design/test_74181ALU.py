# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer
@cocotb.test()
async def test_alu_s0(dut):
    for a in range(16):
        for b in range(16):
            dut.a.value = a
            dut.b.value = b
            dut.ci.value = 1
            dut.M.value = 0
            dut.s.value = 0            
            await Timer(2, units='ns')
            dut._log.info(f'For Input={a:04} For Input2={b:04} For civalue={ci:01} For Mvalue={M:01} Select= 0  OUT={int(dut.y.value):04}')
            assert dut.y.value == ~a, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(input=a,input2=b, civalue=ci, Mvalue=M, s=dut.s.value, y = dut.y.value)