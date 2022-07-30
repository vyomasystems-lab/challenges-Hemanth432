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

## Circuit Diagram in eSim
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


