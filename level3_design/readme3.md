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
![image](https://user-images.githubusercontent.com/93421069/181907775-4d985e4f-eb0e-4632-b966-9e62417eaabe.jpg)

## Netlists
![image]((https://user-images.githubusercontent.com/93421069/181907775-4d985e4f-eb0e-4632-b966-9e62417eaabe.jpg))
## NgSpice Plots
![image](![Screenshot (403)](https://user-images.githubusercontent.com/93421069/181907673-8172f490-6b22-4509-87be-54634c0551a7.png))
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


