import argparse

from typing import List, Tuple

import text_flow

# invoke like this:
# python cli_with_arguments.py 5,2,5,1 ord y G
# and expect output like
#
# Received: [1, 2, 3]  ord, True, G
# Output written to: Epic_Nightmare_Tollboth_XVI.txt

def main():
	entered_values, binary_order, show_binary, initial_pitch = parse_all_commandline_args()
	print(f"Received: {entered_values}  {binary_order}, {show_binary}, {initial_pitch}")
	text_flow.run_standard_text_flow(entered_values, binary_order, show_binary, initial_pitch)


def parse_all_commandline_args() -> Tuple[List[int], str, bool, str]:
	parser = argparse.ArgumentParser()
	parser.add_argument("entered_values", help="intervals comma separated")
	parser.add_argument("binary_order", help="ordering: ord,ran,more,super")
	parser.add_argument("show_binary", help="show binary: y or n")
	parser.add_argument("initial_pitch", help="initial pitch")
	# TODO: greg to validate arguments, make help messages nicer or whatever
	# see https://docs.python.org/3/howto/argparse.html
	args = parser.parse_args()
	return (list(map(int, args.entered_values.split(','))), args.binary_order, args.show_binary == 'y', args.initial_pitch)



if __name__ == '__main__':
	main()
