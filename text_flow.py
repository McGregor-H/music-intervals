from typing import Dict, List

from utils import get_intervals, length_needed, total_num_pitches, make_permutations, join_us, pitch_list_generator, add_starting_p, pitch_stripper, tallies, generate_unique_name, later_function, footer

def run_standard_text_flow(entered_values, binary_order, show_binary, initial_pitch):
    interval_set = get_intervals(entered_values)
    seq_length = length_needed(entered_values)
    total = total_num_pitches(seq_length)
    perm_list = make_permutations(seq_length, binary_order)
    perm_result = join_us(perm_list)
    perm_output_str = '\n'.join([' '.join(map(str, item)) for item in perm_result])
    pitches_list_all = pitch_list_generator(initial_pitch, perm_list, entered_values)
    pitches_list_all_plus = add_starting_p(pitches_list_all, initial_pitch)
    pitches_output_str = '\n'.join([' '.join(map(str, item)) for item in pitches_list_all_plus])
    string_list = pitch_stripper(pitches_list_all_plus)
    total_tally = tallies(pitches_list_all)
    filename = generate_unique_name()
    decision = later_function(binary_order)
    foot = footer(filename)
    with open(filename, 'a') as file:
        file.write("\nPossible pitch outcomes using {} for the {} entered intervals:\n{}\n\n".format(decision, seq_length, interval_set))
        file.write(str(pitches_output_str))
        file.write("\n\n")
        #if decision.lower() == 'y' or decision.lower() == 'yes':
        if show_binary.lower().strip() in {'y', 'yes'}:
                file.write("\n\nSelected binary ordering was: {} which means {}\n".format(binary_order, decision))
                file.write("\nbinary sequence\n[0=up, 1=down]\n")
                file.write(str(perm_result))
                file.write("\n\n")
        file.write("\nPitch tally:\n")
        for key, value in total_tally.items():
            file.write("{}: {}\n".format(key, value))
        file.write("\nTotal # of piches: {}\n".format(total))
        file.write(str(foot))
    print("Output written to: {}".format(filename))







