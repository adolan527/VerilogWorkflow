Verilog workflow tools

## Notepad++
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

## Testbench

The testbench program can be compiled using the included CMakeLists.txt file.
There is also further information on the API of said program in its own README.

## Git 

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

# Git Ignore

There is also a .gitignore which gets rid of everything besides source files, testbench, and ip cores.
