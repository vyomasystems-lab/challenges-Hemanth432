# Capture the BUG Hackathon
# Multiplexer[31:1]

## Abstract
Multiplexer is a combinational circuit that has maximum of 2^n data inputs, ‘n’ selection lines and single output line. One of these data inputs will be connected to the output based on the values of selection lines.Since there are ‘n’ selection lines, there will be 2^n possible combinations of zeros and ones. So, each combination will select only one data input. Multiplexer is also called as Mux.Here we are using the 31 input lines mux and 5 select lines.


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

## Circuit Diagram of Multiplexer
The following is the schematic in eSim:
![image](https://user-images.githubusercontent.com/93421069/181905789-395ceff8-4878-4c91-ade7-44e8af2237bd.jpg)
## Verilog Code
```
// See LICENSE.vyoma for details

module mux(sel,inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, 
           inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17,
           inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,
           inp27, inp28, inp29, inp30, out);

  input [4:0] sel;
  input [1:0] inp0, inp1, inp2, inp3, inp4, inp5, inp6,
            inp7, inp8, inp9, inp10, inp11, inp12, inp13, 
            inp14, inp15, inp16, inp17, inp18, inp19, inp20,
            inp21, inp22, inp23, inp24, inp25, inp26,
            inp27, inp28, inp29, inp30;

  output [1:0] out;
  reg [1:0] out;

  // Based on sel signal value, one of the inp0-inp30 gets assigned to the 
  // output signal
  always @(sel or inp0  or inp1 or  inp2 or inp3 or inp4 or inp5 or inp6 or
            inp7 or inp8 or inp9 or inp10 or inp11 or inp12 or inp13 or 
            inp14 or inp15 or inp16 or inp17 or inp18 or inp19 or inp20 or
            inp21 or inp22 or inp23 or inp24 or inp25 or inp26 or inp27 or 
            inp28 or inp29 or inp30 )

  begin
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      default: out = 0;
    endcase
  end

endmodule 
```

## Python test file:
```# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer
@cocotb.test()
async def test_mux_inp0(dut):
    for inputValue in range(4):
        dut.inp0.value = inputValue
        dut.sel.value = 0
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 0  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
@cocotb.test()
async def test_mux_inp1(dut):
    for inputValue in range(4):
        dut.inp1.value = inputValue
        dut.sel.value = 1
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 1  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp2(dut):
    for inputValue in range(4):
        dut.inp2.value = inputValue
        dut.sel.value = 2
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 2  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp3(dut):
    for inputValue in range(4):
        dut.inp3.value = inputValue
        dut.sel.value = 3
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 3  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp4(dut):
    for inputValue in range(4):
        dut.inp4.value = inputValue
        dut.sel.value = 4
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 4  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp5(dut):
    for inputValue in range(4):
        dut.inp5.value = inputValue
        dut.sel.value = 5
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 5  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp6(dut):
    for inputValue in range(4):
        dut.inp6.value = inputValue
        dut.sel.value = 6
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 6  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp7(dut):
    for inputValue in range(4):
        dut.inp7.value = inputValue
        dut.sel.value = 7
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 7  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp8(dut):
    for inputValue in range(4):
        dut.inp8.value = inputValue
        dut.sel.value = 8
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 8  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp9(dut):
    for inputValue in range(4):
        dut.inp9.value = inputValue
        dut.sel.value = 9
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 9  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp10(dut):
    for inputValue in range(4):
        dut.inp10.value = inputValue
        dut.sel.value = 10
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 10  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp11(dut):
    for inputValue in range(4):
        dut.inp11.value = inputValue
        dut.sel.value = 11
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 11  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp12(dut):
    for inputValue in range(4):
        dut.inp12.value = inputValue
        dut.sel.value = 12
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 12  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp13(dut):
    for inputValue in range(4):
        dut.inp13.value = inputValue
        dut.sel.value = 13
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 13  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp14(dut):
    for inputValue in range(4):
        dut.inp14.value = inputValue
        dut.sel.value = 14
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 14  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp15(dut):
    for inputValue in range(4):
        dut.inp15.value = inputValue
        dut.sel.value = 15
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 15  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp16(dut):
    for inputValue in range(4):
        dut.inp16.value = inputValue
        dut.sel.value = 16
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 16  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp17(dut):
    for inputValue in range(4):
        dut.inp17.value = inputValue
        dut.sel.value = 17
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 17  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp18(dut):
    for inputValue in range(4):
        dut.inp18.value = inputValue
        dut.sel.value = 18
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 18  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp19(dut):
    for inputValue in range(4):
        dut.inp19.value = inputValue
        dut.sel.value = 19
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 19  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp20(dut):
    for inputValue in range(4):
        dut.inp20.value = inputValue
        dut.sel.value = 20
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 20  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp21(dut):
    for inputValue in range(4):
        dut.inp21.value = inputValue
        dut.sel.value = 21
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 21  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp22(dut):
    for inputValue in range(4):
        dut.inp22.value = inputValue
        dut.sel.value = 22
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 22  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp23(dut):
    for inputValue in range(4):
        dut.inp23.value = inputValue
        dut.sel.value = 23
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 23  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp24(dut):
    for inputValue in range(4):
        dut.inp24.value = inputValue
        dut.sel.value = 24
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 24  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp25(dut):
    for inputValue in range(4):
        dut.inp25.value = inputValue
        dut.sel.value = 25
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 25  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp26(dut):
    for inputValue in range(4):
        dut.inp26.value = inputValue
        dut.sel.value = 26
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 26  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp27(dut):
    for inputValue in range(4):
        dut.inp27.value = inputValue
        dut.sel.value = 27
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 27  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp28(dut):
    for inputValue in range(4):
        dut.inp28.value = inputValue
        dut.sel.value = 28
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 28  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp29(dut):
    for inputValue in range(4):
        dut.inp29.value = inputValue
        dut.sel.value = 29
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 29  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
        
@cocotb.test()
async def test_mux_inp30(dut):
    for inputValue in range(4):
        dut.inp30.value = inputValue
        dut.sel.value = 30
        await Timer(2, units='ns')
        dut._log.info(f'For Input={inputValue:02} Select= 30  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
 ```
## results.xml file
```
<testsuites name="results">
  <testsuite name="all" package="all">
    <property name="random_seed" value="1659170648" />
    <testcase name="test_mux_inp0" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="4" time="0.00103759765625" sim_time_ns="8.001" ratio_time="7711.081411764705" />
    <testcase name="test_mux_inp1" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="12" time="0.0008103847503662109" sim_time_ns="8.001" ratio_time="9873.088056487202" />
    <testcase name="test_mux_inp2" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="21" time="0.0008184909820556641" sim_time_ns="8.001000000000001" ratio_time="9775.306234780077" />
    <testcase name="test_mux_inp3" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="30" time="0.0008084774017333984" sim_time_ns="8.000999999999998" ratio_time="9896.380508404598" />
    <testcase name="test_mux_inp4" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="39" time="0.0007631778717041016" sim_time_ns="8.001000000000005" ratio_time="10483.794534208066" />
    <testcase name="test_mux_inp5" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="48" time="0.0007810592651367188" sim_time_ns="8.000999999999998" ratio_time="10243.78092307692" />
    <testcase name="test_mux_inp6" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="57" time="0.0007593631744384766" sim_time_ns="8.000999999999998" ratio_time="10536.460378021975" />
    <testcase name="test_mux_inp7" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="66" time="0.0008213520050048828" sim_time_ns="8.000999999999998" ratio_time="9741.255821190127" />
    <testcase name="test_mux_inp8" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="75" time="0.0008172988891601562" sim_time_ns="8.001000000000005" ratio_time="9789.564266044346" />
    <testcase name="test_mux_inp9" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="84" time="0.0007524490356445312" sim_time_ns="8.001000000000005" ratio_time="10633.278296577953" />
    <testcase name="test_mux_inp10" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="93" time="0.0007541179656982422" sim_time_ns="8.00099999999999" ratio_time="10609.745907050255" />
    <testcase name="test_mux_inp11" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="102" time="0.0007832050323486328" sim_time_ns="8.001000000000005" ratio_time="10215.71576986302" />
    <testcase name="test_mux_inp12" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="111" time="0.00047707557678222656" sim_time_ns="4.001000000000005" ratio_time="8386.511896051985">
      <failure />
    </testcase>
    <testcase name="test_mux_inp13" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="120" time="0.00032019615173339844" sim_time_ns="2.0009999999999906" ratio_time="6249.294344005927">
      <failure />
    </testcase>
    <testcase name="test_mux_inp14" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="129" time="0.0008459091186523438" sim_time_ns="8.001000000000005" ratio_time="9458.462881623456" />
    <testcase name="test_mux_inp15" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="138" time="0.0007908344268798828" sim_time_ns="8.001000000000005" ratio_time="10117.161984926144" />
    <testcase name="test_mux_inp16" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="147" time="0.0008676052093505859" sim_time_ns="8.00099999999999" ratio_time="9221.936329760912" />
    <testcase name="test_mux_inp17" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="156" time="0.0007953643798828125" sim_time_ns="8.001000000000005" ratio_time="10059.540258992813" />
    <testcase name="test_mux_inp18" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="165" time="0.0008137226104736328" sim_time_ns="8.001000000000005" ratio_time="9832.589013770881" />
    <testcase name="test_mux_inp19" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="174" time="0.000850677490234375" sim_time_ns="8.001000000000005" ratio_time="9405.444591928257" />
    <testcase name="test_mux_inp20" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="183" time="0.0007824897766113281" sim_time_ns="8.000999999999976" ratio_time="10225.05371846432" />
    <testcase name="test_mux_inp21" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="192" time="0.0008299350738525391" sim_time_ns="8.001000000000005" ratio_time="9640.513158287855" />
    <testcase name="test_mux_inp22" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="201" time="0.0007941722869873047" sim_time_ns="8.001000000000005" ratio_time="10074.640139297515" />
    <testcase name="test_mux_inp23" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="210" time="0.0008051395416259766" sim_time_ns="8.001000000000005" ratio_time="9937.407848386147" />
    <testcase name="test_mux_inp24" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="219" time="0.0009069442749023438" sim_time_ns="8.001000000000005" ratio_time="8821.931205047324" />
    <testcase name="test_mux_inp25" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="228" time="0.0007841587066650391" sim_time_ns="8.001000000000005" ratio_time="10203.291670416545" />
    <testcase name="test_mux_inp26" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="237" time="0.0008561611175537109" sim_time_ns="8.000999999999976" ratio_time="9345.20364912278" />
    <testcase name="test_mux_inp27" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="246" time="0.0007724761962890625" sim_time_ns="8.001000000000005" ratio_time="10357.600711111118" />
    <testcase name="test_mux_inp28" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="255" time="0.0008051395416259766" sim_time_ns="8.001000000000005" ratio_time="9937.407848386147" />
    <testcase name="test_mux_inp29" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="264" time="0.0008363723754882812" sim_time_ns="8.001000000000005" ratio_time="9566.31308551882" />
    <testcase name="test_mux_inp30" classname="test_mux" file="/workspace/challenges-Hemanth432/level1_design1/test_mux.py" lineno="273" time="0.0005011558532714844" sim_time_ns="4.001000000000005" ratio_time="7983.5443882017225">
      <failure />
    </testcase>
  </testsuite>
</testsuites>
```
## Test cases
![Screenshot (405)](https://user-images.githubusercontent.com/93421069/181906319-2a0fbb72-e3e6-4b22-96cc-c982f68a1b7a.png)

## GAW Plots
![image](https://user-images.githubusercontent.com/93421069/157199313-04d774cc-8efb-47e7-a59b-ddc357910b30.jpg)
## Steps to run generate NgVeri Model
1. Open eSim
2. Run NgVeri-Makerchip 
3. Add top level verilog file in Makerchip Tab
4. Click on NgVeri tab
5. Add dependency files
6. Click on Run Verilog to NgSpice Converter
7. Debug if any errors
8. Model created successfully
## Steps to run this project
1. Open a new terminal
2. Clone this project using the following command:</br>
```git clone https://github.com/Hemanth432?tab=repositories ```</br>
3. Change directory:</br>
```cd https://github.com/Hemanth432/Mixed-Signal-simulation-Hackathon ```</br>
4. Run ngspice:</br>
```ngspice johnson_amv_hemanth.cir.out```</br>
5. To run the project in eSim:

  - Run eSim</br>
  - Load the project</br>
  - Open eeSchema</br>
## Acknowlegdements
1. FOSSEE, IIT Bombay
2. Steve Hoover, Founder, Redwood EDA
3. Kunal Ghosh, Co-founder, VSD Corp. Pvt. Ltd. - kunalpghosh@gmail.com
4. Sumanto Kar, eSim Team, FOSSEE

## References
1. Website: "https://www.reddit.com/r/AskElectronics/comments/f7ubt4/astable_multivibrator_schmitt_trigger_johnson/" 


