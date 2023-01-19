import random

from typing import Dict, List

import itertools

import formatting5

from formatting5 import get_intervals, length_needed, total_num_pitches, make_permutations, pitch_list_generator, pitch_stripper, tallies, generate_unique_name, later_function, footer
#interval_set, seq_length, total, perm_list, pitches_list_all, string_list, total_tally, filename, decision, footer

def run_standard_text_flow(entered_values, binary_order, show_binary, initial_pitch):
    interval_set = get_intervals(entered_values)
    seq_length = length_needed(entered_values)
    total = total_num_pitches(seq_length)
    perm_list = make_permutations(seq_length, binary_order)
    pitches_list_all = pitch_list_generator(initial_pitch, perm_list, entered_values)
    string_list = pitch_stripper(pitches_list_all)
    total_tally = tallies(pitches_list_all)
    filename = generate_unique_name()
    decision = later_function(binary_order)
    foot = footer(filename)

    with open(filename, 'a') as file:
        file.write("\nPossible pitch outcomes using {} for the {} entered intervals: {}\n\n".format(decision, seq_length, interval_set))
        file.write(str(string_list))
        file.write("\n\n")
        if decision.lower() == 'y' or decision.lower() == 'yes':
            file.write("\nbinary sequence\n[0=up, 1=down]\n")
            file.write(str(perm_list))
            file.write("\n\n")
        file.write("\nPitch tally:\n")
        file.write(str(total_tally))
        file.write("\nTotal # of piches: {}\n".format(total))
        file.write(str(footer))
    print("Output written to: {}".format(filename))







