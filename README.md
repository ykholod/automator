# automator
Unified Project managing interface. Automator unifies various Project modules control procedures under single user-friendly inteface.
With automator tool you can build all Project parts, run multiple test scenarius and load files from PC to ESP8266 board.

# Usage
Automator communicates with ESP8266 board via COM port. 
Note: In case you are using USB interface, please emulate serial connection behavior with some application, like CoolTerm.

Genaral usage rule for automator is:
python automator.py <Action> <Target>
,where
	Action: build, validate, load
	Target: micropython, boiler, etc

Automator commands are available with --help option:
    python automator.py --help