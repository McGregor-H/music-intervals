from typing import List, Tuple

import common4
#from common4 import run_standard_text_flow

#run_text = run_standard_text_flow(get_intervals, length_needed, total_num_pitches, make_permutations, pitch_list_generator, pitch_stripper, tallies, generate_unique_name, later_function, footer)

#entered_values = [5,2,1,5]
#ord, shuf, ran
#binary_order = "ord"
#initial_pitch = 'C'
#start_pitch = initial_pitch
#show_binary = "y"

# this one is intended to work much like what you have now
# python cli_interactive.py
# and then user gets instructions, has to make the inputs, etc


#([1,4,3], 'ord', True, 'C')
def main():
	entered_values, binary_order, show_binary, initial_pitch = prompt_for_all_arguments()
	common4.run_standard_text_flow(entered_values, binary_order, show_binary, initial_pitch)
#(interval_set, seq_length, total, perm_list, pitches_list_all, string_list, total_tally, filename, decision, footer)


def prompt_for_all_arguments():# -> Tuple[List[int], str, bool, str]:
    print("Enter sequence of intervals as number of half steps \n1=minor 2nd, 2=Major 2nd, 3=minor 3rd, \n4=Major 3rd, 5=Perfect 4th, 6=Tri-tone")
    entered_values_raw = input("Enter a sequence of intervals separated by a comma: \nonly valid intervals: 1 - 6\n >")
    entered_values = [int(x.strip()) for x in entered_values_raw.split(',')]
    if (any(x > 6 or x < 1 for x in entered_values)):
        raise Exception("All entered values must be integer between 1 and 6 inclusive")

    print("\nChoose a method of permutation:\n[ord] ORDERED - using all combinations of up/down once in order")
    print("[shuf] REGULAR SHUFFLE - using all combinations of up/down once in random order")
    print("[ran] ACTUAL RANDOM - using completely random patterns of up/down for the interval set\n")
    binary_order = input("Enter: [ord], [shuf], or [ran] \n>")
    print("Would you like the binary code sequence pattern \nprinted on the generated text file? ")
    show_binary = input("Enter [y or n] >")
    print("Enter the starting pitch: \nenter choice as: C, C#, D, D#, E, F, F#, G, G#, A, A#, B\n ")
    initial_pitch = input(">")

    return entered_values, binary_order, show_binary, initial_pitch

#prompt_for_all_arguments()

if __name__ == '__main__':
	main()
