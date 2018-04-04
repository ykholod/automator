###
#   April 3, 2018
#   Copyright Yaroslav Kholod
#   Author Yaroslav Kholod
 
#   Description:
#   Automate The Project building, testing and loading procedures

#   Run:
#     python automator.py build micropython
#     python automator.py validate micropython
#     python automator.py load micropython


#usr/bin/python

import argparse
import os


parser = argparse.ArgumentParser(description='The Project build, test and launch point')
subparsers = parser.add_subparsers(help='List of commands')

# A build command
list_parser = subparsers.add_parser('build', help='Build some target')
list_parser.add_argument('build', type=str, help='Build MicroPython image',
	                     choices=['micropython'])

# A validate command
validate_parser = subparsers.add_parser('validate', help='Validate available script')
validate_parser.add_argument('validate', type=str, help='Validate your code',
	                         choices=['micropython','weatherStation','boiler','column'])

# A load command
create_parser = subparsers.add_parser('load', help='Board the system')
create_parser.add_argument('load', type=str, help='Upload MicroPython image',
	                        choices=['micropython','weatherStation','boiler','column'])

# Parser default values
parser.set_defaults(build=None)
parser.set_defaults(validate=None)
parser.set_defaults(load=None)

args = parser.parse_args()

if args.build != None:
	if args.build == 'micropython': os.system('python micropython_build.py')

if args.validate != None:
	if args.validate == 'micropython': print 'Validate MicroPython'
	elif args.validate == 'weatherStation': print 'Validate weatherStation'
	elif args.validate == 'boiler': print 'Validate boiler'
	elif args.validate == 'column': print 'Validate column'
	else: print 'Unclear requirement'

if args.load != None:
	if args.load == 'micropython': os.system('python micropython_load.py')
	elif args.load == 'weatherStation': print 'Load weatherStation'
	elif args.load == 'boiler': print 'Load boiler'
	elif args.load == 'column': print 'Load column'
	else: print 'Unclear requirement'


