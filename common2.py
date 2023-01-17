import random

from typing import Dict, List

import itertools

import formatting3

from formatting3 import string_list, total_num_pitches, seq_length, interval_sequence, perm_list, total_tally, filename, decision, footer, unique_name, show_binary


def run_standard_text_flow(string_list, total_num_pitches, seq_length, interval_sequence, perm_list, total_tally, filename, decision, footer, unique_name, show_binary):

    with open(filename, 'a') as file:
		# TODO greg - write any instructions and stuff i didnt, fix newlines and spacing and evertything
        file.write("\nPossible pitch outcomes using {} for the {} entered intervals: {}\n\n".format(decision, seq_length, interval_sequence))
        file.write(str(formatting3.string_list))
        file.write("\n\n")
        if show_binary == 'y' or 'yes':
            file.write("\nbinary sequence\n[0=up, 1=down]\n")
            file.write(str(formatting3.perm_list))
            file.write("\n\n")
        file.write("\nPitch tally:\n")
        file.write(str(formatting3.total_tally))
        file.write("\nTotal # of piches: {}\n".format(total_num_pitches))
        file.write(formatting3.footer(unique_name))
    print(f"Output written to: {filename}")


run_standard_text_flow(string_list, total_num_pitches, seq_length, interval_sequence, perm_list, total_tally, filename, decision, footer, unique_name, show_binary)

