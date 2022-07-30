# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer
@cocotb.test()
async def test_alu_a0(dut):
    for a in range(1):
        for b in range(16):
                    dut.a.value = a
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 0            
                    await Timer(2, units='ns')
                    dut._log.info(f'a={a:04} b={b:04} ci=0 M=1 s=0  OUT={int(dut.y.value):04}')
                    assert dut.y.value == 15, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)
@cocotb.test()
async def test_alu_a1(dut):
        for b in range(16):
                    dut.a.value = 1
                    dut.b.value = b
                    dut.M.value = 1
                    dut.s.value = 0            
                    await Timer(2, units='ns')
                    dut._log.info(f'a=1 b={b:04} ci=0 M=1 s=0  OUT={int(dut.y.value):04}')
                    assert dut.y.value == 14, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)
@cocotb.test()
async def test_alu_a2(dut):
        for b in range(16):
                    dut.a.value = 2
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 0            
                    await Timer(2, units='ns')
                    dut._log.info(f'a=2 b={b:04} ci=0 M=1 s=0  OUT={int(dut.y.value):04}')
                    assert dut.y.value == 13, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)
@cocotb.test()
async def test_alu_a3(dut):
        for b in range(16):
                    dut.a.value = 3
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 0            
                    await Timer(2, units='ns')
                    dut._log.info(f'a=3 b={b:04} ci=0 M=1 s=0  OUT={int(dut.y.value):04}')
                    assert dut.y.value == 12, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)                    
@cocotb.test()
async def test_alu_s3(dut):
        for a in range(16):
            for b in range(16):
                    dut.a.value = a
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 3         
                    await Timer(2, units='ns')
                    dut._log.info(f'a={a:04} b={b:04} ci=0 M=1 s=3 OUT={int(dut.y.value):04}')
                    assert dut.y.value == 0, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)
@cocotb.test()
async def test_alu_s15(dut):
    for a in range(16):
        for b in range(16):
                    dut.a.value = a
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 15            
                    await Timer(2, units='ns')
                    dut._log.info(f'a={a:04} b={b:04} ci=0 M=1 s=15  OUT={int(dut.y.value):04}')
                    assert dut.y.value == a, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)                    
