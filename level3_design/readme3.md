# Capture the BUG Hackathon
# Level3-74181ALU Chip
- [Abstract](#abstract)
- [Reference Circuit Diagram](#reference-circuit-diagram)
- [Reference Truth Table](#reference-truthtable)
- [Circuit Details](#circuit-details)
- [Software Used](#software-used)
  * Vyoma's UpTickPro
  * Gitpod
  * Github
  * python
- [Verilog Code]
- [Python test file]
- [Test cases passed and failed]
- [Python file with bugs]
- [Python test file for buggy design]
- [Test cases passed and failed]
- [Acknowlegdements](#acknowlegdements)
- [References](#references)

## Abstract
The 74181 chip is important because of its key role in
minicomputer history. Before the microprocessor era,
minicomputers built their processors from boards of
individual chips. A key part of the processor was the
arithmetic/logic unit (ALU), which performed
arithmetic operations (addition, subtraction) and
logical operations (AND, OR, XOR).The 74181
implements a 4-bit ALU providing 16 logic functions
and 16 arithmetic functions.This circuit is
implemented using verilog.


## Reference Circuit Diagram
![image](https://user-images.githubusercontent.com/93421069/181905789-395ceff8-4878-4c91-ade7-44e8af2237bd.jpg)
## Reference Truth Table
![image](https://user-images.githubusercontent.com/93421069/181906870-49cab5ad-b8a5-4055-abc5-80aba594fdf2.jpg)
)
## Circuit Details
Texas Instruments introduced the 74181 Arithmetic /
Logic Unit (ALU) chip, which put a full 4-bit ALU on
one fast TTL chip. This chip provided 32 arithmetic
and logic functions, as well as carry lookahead for
high performance.The 74181 implements a 4-bit
ALU providing 16 logic functions and 16 arithmetic
functions. As well as the expected addition,
subtraction, and Boolean operations, there are
some bizarre functions such as "(A + B) PLUS
AB".So there are 2^4 = 16 possible functions.
Extend these to 4 bits, and these are exactly the 16
logic functions of the 74181, from trivial 0 and 1 to
expected logic like A AND B to contrived operations
like NOT A AND B. These 16 functions are selected
by the S0-S3 select inputs.The circuit diagram is
shown in Figure 1.The expected outputs or the truth
table is shown in Figure 2
</br>

## Software Used
### Vyoma's UpTickPro
It is an python based verification tool made by Vyoma Systems.
</br>
For more details refer:
</br>
https://vyomasystems.com/
### Gitpod
Gitpod provides a Theia IDE using VS Code as editor who’s contents it keeps track of. It provides a full operating system environment to run code developed there.
</br>
https://www.gitpod.io/
### Github
GitHub is a development platform inspired by the way you work. From open source to business, you can host and review code, manage projects, and build software alongside 36 million developers.
</br> https://github.com/
### python
Python is a programming language. Python can be used on a server to create web applications
https://www.python.org/

## Verilog Code
![image](https://user-images.githubusercontent.com/93421069/181907775-4d985e4f-eb0e-4632-b966-9e62417eaabe.jpg)

## Python test file 
```
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
async def test_alu_s2(dut):
        for a in range(16):
            for b in range(16):
                    dut.a.value = a
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 2         
                    await Timer(2, units='ns')
                    dut._log.info(f'a={a:04} b={b:04} ci=0 M=1 s=2 OUT={int(dut.y.value):04}')
                    assert dut.y.value == (~a)&b, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)
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
async def test_alu_s7(dut):
        for a in range(16):
            for b in range(16):
                    dut.a.value = a
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 7        
                    await Timer(2, units='ns')
                    dut._log.info(f'a={a:04} b={b:04} ci=0 M=1 s=7 OUT={int(dut.y.value):04}')
                    assert dut.y.value == a&(~b), "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)                    
@cocotb.test()
async def test_alu_s10(dut):
    for a in range(16):
        for b in range(16):
                    dut.a.value = a
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 10           
                    await Timer(2, units='ns')
                    dut._log.info(f'a={a:04} b={b:04} ci=0 M=1 s=10  OUT={int(dut.y.value):04}')
                    assert dut.y.value == b, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)                    
@cocotb.test()
async def test_alu_s11(dut):
    for a in range(16):
        for b in range(16):
                    dut.a.value = a
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 11           
                    await Timer(2, units='ns')
                    dut._log.info(f'a={a:04} b={b:04} ci=0 M=1 s=11  OUT={int(dut.y.value):04}')
                    assert dut.y.value == a&b, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value) 
@cocotb.test()
async def test_alu_s14(dut):
    for a in range(1):
        for b in range(16):
                    dut.a.value = a
                    dut.b.value = b
                    dut.ci.value =0
                    dut.M.value = 1
                    dut.s.value = 14            
                    await Timer(2, units='ns')
                    dut._log.info(f'a={a:04} b={b:04} ci=0 M=1 s=14  OUT={int(dut.y.value):04}')
                    assert dut.y.value == a+b, "Test failed with: {a} {b} {ci} {M} {s} = {y}".format(a=dut.a.value,b=dut.b.value,ci=dut.ci.value,M=dut.M.value, s=dut.s.value, y = dut.y.value)                    
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
                   
```
## Test cases passed and failed
![image](![Screenshot (401)](https://user-images.githubusercontent.com/93421069/181907942-dc56c998-4389-48ed-93b8-c01a0362b464.png)
)

## Buggy Verilog code
We can observe that in line 15 b[2] is replaced with b[3].

![image](![Screenshot (403)](https://user-images.githubusercontent.com/93421069/181907673-8172f490-6b22-4509-87be-54634c0551a7.png))
## Outputs of test cases passed and failed
![image](![Screenshot (404)](https://user-images.githubusercontent.com/93421069/181908010-b56ec4b2-3003-45b2-9a27-51e346e82e4b.png))

## Acknowlegdements
1. Vyoma SystemsFOSSEE, IIT Bombay
2. FOSSEE, IIT Bombay
3. IIT Madras
4. NIELIT
5. Kunal Ghosh, Co-founder, VSD Corp. Pvt. Ltd. - kunalpghosh@gmail.com
6. Sumanto Kar, eSim Team, FOSSEE

## References
1. Basics of Digital Electronics 



