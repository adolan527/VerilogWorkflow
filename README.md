Verilog workflow tools

# Notepad++
Assuming you have Notepad++ installed, install ```Pork To Sausage```

1. Open Notepad++
2. Select `Plugins`
3. Select `Plugins Admin`
4. Select `Available`
5. Search for "Pork To Sausage".
6. Check the box next to the plugin.
7. Press "Install" and allow Notepad++ to restart.

If you have any trouble with this step, consult https://github.com/npp-plugins/pork2sausage.

Next, you need to configure the plugin.

1. Open Notepad++
2. Select `Plugins`
3. Select `Pork To Sausage`
4. Select `Edit User Commands`
5. A file will open. Copy the contents of this repository's pork2Sausage.ini file into this file.
6. There are some path names which you will have to fill in for yourself. Do absolute names.

To assign the plugin commands to hotkeys do the following.

1. Open Notepad++
2. Select `Macros`
3. Select `Modify Shortcut/Delete Macro
4. Select `Plugin Commands`
5. Locate the commands titled `Verilog Find Definition` and `Verilog Create TB`.
6. Edit the macro field.

## Testbench

The testbench program can be compiled using the included CMakeLists.txt file.
There is also further information on the API of said program in its own README.

## Using the commands

### Find Definition 
Highlight the name of a module, then run the command. Notepad++ will then open the definition at its exact line number.

### Create TB

1. Copy the entirety of module's port definitions. 
2. Paste in the location you want the testbench.
3. Highlight the port definitions, then run the command.

Example highlighted text:

	module regFile(
		input[15:0] data, //databus input
		input[2:0] DR, //destination register. Address of the register to write to
		input LDREG, //active high write enable bit. 
		input[2:0] SR1, SR2, //source registers 1 and 2. Address of register to read from
		input clk, //clk
		input reset_n, //active low async reset.
		output reg[15:0] SR1out, SR2out //data from source registers 1 and 2
		);
		
Example output:

	reg  LDREG, clk, reset_n;
	reg[2:0]  DR, SR1, SR2;
	reg[15:0]  data;
	wire[15:0] SR1out SR2out t;

	regFile regFile_inst(
	 .data(data),.DR(DR),.LDREG(LDREG),.SR1(SR1),.SR2(SR2),.clk(clk),.reset_n(reset_n),.SR1out(SR1out),.SR2out(SR2out),.t(t));

	always #5 clk = ~clk;

	initial begin
	clk = 0;
	end

Note: the format of the port definition must be formatted as such:
	"module NAME(" - is on its own line.
	");" - is on its own line
	No empty lines between ports
	PORTNAME, - no whitespace between a port name and the following comma.
	
These limitations could be fixed, but the aforementioned formatting is a good guideline regardless.

# Git 

There is a pre-commit hook which will do the following.

1. Iterate through every .v file in the repository
2. Search for the phrase "TODO" included in any files.
3. Compile all TODOs into a file name "TODO" in the root of the repository.

File paths, line numbers, and the full line where TODO was discovered is included.

Example output:
	TODO list:

	LC3.srcs/sources_1/new/Controller/controller.v

		35 		//TODO Implement control logic, add states.

	LC3.srcs/sources_1/new/Datapath/address.v

		68 		//TODO Test address module

	LC3.srcs/sources_1/new/Memory/addressControlLogic.v

		50 	// TODO: Write a tb for this module.
		51 	// TODO: Current implementation performance to ROM implementation.

### Git Ignore

There is also a .gitignore which gets rid of everything besides source files, testbench, and ip cores. Verify that your directory names do not conflict with this if you choose to use it.
