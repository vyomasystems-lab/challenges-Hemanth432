# Capture the BUG Hackathon
# Level3-74181ALU Chip
- [Abstract](#abstract)
- [Reference Circuit Diagram](#reference-circuit-diagram)
- [Reference Truth Table](#reference-truthtable)
- [Circuit Details](#circuit-details)
- [Software Used](#software-used)
  * Vyoma's UpTickPro(#Vyoma's UpTickPro)
  * Gitpod(#Gitpod)
  * Github(#Github)
  * python(#python)
- [Verilog Code](#verilog-code)
- [Python test file](#Vyoma's UpTickPro)
- [Test cases passed and failed](#Vyoma's UpTickPro)
- [Python file with bugs](#Vyoma's UpTickPro)
- [Python test file for buggy design](#Vyoma's UpTickPro)
- [Test cases passed and failed](#Vyoma's UpTickPro)
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
![image](![Screenshot (403)](https://user-images.githubusercontent.com/93421069/181907673-8172f490-6b22-4509-87be-54634c0551a7.png)
)

## Makerchip
```
\TLV_version 1d: tl-x.org
\SV
/* verilator lint_off UNUSED*/  /* verilator lint_off DECLFILENAME*/  /* verilator lint_off BLKSEQ*/  /* verilator lint_off WIDTH*/  /* verilator lint_off SELRANGE*/  /* verilator lint_off PINCONNECTEMPTY*/  /* verilator lint_off DEFPARAM*/  /* verilator lint_off IMPLICIT*/  /* verilator lint_off COMBDLY*/  /* verilator lint_off SYNCASYNCNET*/  /* verilator lint_off UNOPTFLAT */  /* verilator lint_off UNSIGNED*/  /* verilator lint_off CASEINCOMPLETE*/  /* verilator lint_off UNDRIVEN*/  /* verilator lint_off VARHIDDEN*/  /* verilator lint_off CASEX*/  /* verilator lint_off CASEOVERLAP*/  /* verilator lint_off PINMISSING*/  /* verilator lint_off BLKANDNBLK*/  /* verilator lint_off MULTIDRIVEN*/  /* verilator lint_off WIDTHCONCAT*/  /* verilator lint_off ASSIGNDLY*/  /* verilator lint_off MODDUP*/  /* verilator lint_off STMTDLY*/  /* verilator lint_off LITENDIAN*/  /* verilator lint_off INITIALDLY*/  

//Your Verilog/System Verilog Code Starts Here:
///////Verilog Code Johnson COunter //////
 
module johnson_counter( out,reset,clk);
input clk,reset;
output [3:0] out;
 
reg [3:0] q;
 
always @(posedge clk)
begin
 
if(reset)
 q=4'd0;
 else
 	begin 
 		q[3]<=q[2];
  		q[2]<=q[1];
  		q[1]<=q[0];
   		q[0]<=(~q[3]);
 	end
 end
 
assign out=q;  
endmodule
 
//////End////


//Top Module Code Starts here:
	module top(input logic clk, input logic reset, input logic [31:0] cyc_cnt, output logic passed, output logic failed);
		logic  [3:0] out;//output
//The $random() can be replaced if user wants to assign values
		johnson_counter johnson_counter(.clk(clk), .reset(reset), .out(out));
	
\TLV
//Add \TLV here if desired                                     
\SV
endmodule



```
## Makerchip Plots
![image](https://user-images.githubusercontent.com/93421069/157203919-81198120-0aa3-465b-b91a-b82deb184e08.jpg)
## Netlists
![image](https://user-images.githubusercontent.com/93421069/157199341-a6362b3e-6954-409c-83a6-121f35dd0b9f.jpg)
## NgSpice Plots
![image](https://user-images.githubusercontent.com/93421069/157198999-fd38420c-e9da-4a0c-8682-abe88fd31df5.jpg)
![image]((https://user-images.githubusercontent.com/93421069/157199201-5630b945-6a28-4d06-8750-4d1a734e535f.jpg)

![image](https://user-images.githubusercontent.com/93421069/157199144-28832168-615a-45fd-9411-6c148462b3f4.jpg)
![image](https://user-images.githubusercontent.com/93421069/157199217-e84fa852-a6b9-4cc5-a0c7-8879969ac06a.jpg)
![image](https://user-images.githubusercontent.com/93421069/157199231-b4149019-8bd9-4182-a643-45dc2c41fdf8.jpg)
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


