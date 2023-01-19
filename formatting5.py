from typing import Dict, List
import random
import itertools
import textwrap

#B.S. values for now
#entered_values = [5,2,1,5]
#ord, shuf, ran
#binary_order = ("shuf")
#initial_pitch = ('C')
#show_binary = ('y')

#get_intervals, length_needed, total_num_pitches, make_permutations, pitch_list_generator, pitch_stripper, tallies, generate_unique_name, later_function, footer


#interval_set, seq_length, total, perm_list, pitches_list_all, string_list, total_tally, filename, decision, footer
#####################################################
#NUMBERS TO INTERVAL NAMES
def get_intervals(entered_values):
    intervals = {
        1: "m2",
        2: "M2",
        3: "m3",
        4: "M3",
        5: "P4",
        6: "Tt"
    }
    return [intervals[val] for val in entered_values]

#interval_set = get_intervals(entered_values)
#####################################################
#NUMBER OF INTERVALS ENTERED
def length_needed(entered_values):
    seq_length = len(entered_values)
    return seq_length

#seq_length = length_needed(entered_values)

########################################################
def total_num_pitches(seq_length):
    total = (2 ** seq_length) * seq_length + 1
    return total

#total = total_num_pitches(seq_length)





#seq_length = length_needed(entered_values)
#interval_sequence = get_intervals(entered_values)
#total_num_pitches = (2 ** seq_length) * seq_length + 1
#start_pitch = initial_pitch
#####################################################
#BINARY GENERATOR
def make_permutations(seq_length, binary_order):
    #generate list of all possible permutations of 0 and 1 with x length
    #permutations = list(itertools.product([0,1], repeat=length))

    if "shuf" in binary_order:
        permutations = list(itertools.product([0,1], repeat=seq_length))
        random.shuffle(permutations)
        perm_list = []
        #print each permutation in the list and append to perm_list
        for perm in permutations:
            #print(perm)
            perm_list.append(perm)
            #return perm_list and choice so it can be used in a later function
        return perm_list


    elif "ord" in binary_order:
        permutations = list(itertools.product([0,1], repeat=seq_length))
        perm_list = []
        #print each permutation in the list and append to perm_list
        for perm in permutations:
            #print(perm)
            perm_list.append(perm)
            #return perm_list and choice so it can be used in a later function
        return perm_list      
    

    elif "ran" in binary_order: 
        perm_list = []
        list_length = 2 ** seq_length
        for i in range(list_length):
            perm_lister = tuple(random.choice([0,1]) for _ in range(seq_length))
            perm_list.append(perm_lister)
        #for set in perm_list:
            #print(set)
        return perm_list


#perm_list = make_permutations(seq_length, binary_order)

#print(perm_list)

#####################################################
#PITCH LIST GENERATOR

def pitch_list_generator(initial_pitch, perm_list, entered_values):
    pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    pitches_list_all = []
    for bit in perm_list:
        pitches_list = []  # reset the pitches_list for each permutation
        start_pitch = initial_pitch
        for i in range(len(entered_values)):
            interval = entered_values[i]
            direction = bit[i]  # change here to use bit instead of perm_list
            if direction == 0:
                initial_pitch_index = pitches.index(initial_pitch)
                new_pitch_index = (initial_pitch_index + interval) % len(pitches)
                new_pitch = pitches[new_pitch_index]
                pitches_list.append(new_pitch)  
                initial_pitch = new_pitch
            else:
                initial_pitch_index = pitches.index(initial_pitch)
                new_pitch_index = (initial_pitch_index - interval) % len(pitches)
                new_pitch = pitches[new_pitch_index]
                pitches_list.append(new_pitch)  
                initial_pitch = new_pitch
        pitches_list_all.append(pitches_list)

    pitches_list_all.insert(0, start_pitch)
    return pitches_list_all

#pitches_list_all = pitch_list_generator(initial_pitch, perm_list, entered_values)
########################################################
def pitch_stripper(pitches_list_all):
    #flatten the list
    flatten_list = [elem for sublist in pitches_list_all for elem in sublist]
    #join the list 
    string_list = ' '.join(flatten_list)
    return string_list

#string_list = pitch_stripper(pitches_list_all)
    


#print(pitches_list_all)  

#####################################################
#PITCH TALLIES
def tallies(pitches_list_all):
    pitch_counts = {
        "C": 0,
        "C#": 0,
        "D": 0,
        "D#": 0,
        "E": 0,
        "F": 0,
        "F#": 0,
        "G": 0,
        "G#": 0,
        "A": 0,
        "A#": 0,
        "B": 0
    }
    for pitch in pitches_list_all:
        if type(pitch) == list:
            for note in pitch:
                if note in pitch_counts:
                    pitch_counts[note] += 1
        elif pitch in pitch_counts:
            pitch_counts[pitch] += 1
    return pitch_counts

#total_tally = tallies(pitches_list_all)
#####################################################
#FILE NAME MAKER

def generate_unique_name():
    word_1 = ['Inkwell', 'Ion', 'Trinity', 'Ceti', 'Echo', 'Kilo', 'Lightfoot', 'Nightwind', 'Panic', 'Sierra', 'Whiskey', 'X-ray', 'Zebra', 'Fallen', 'Hunter', 'Iceberg', 'Advantage', 'Blockade', 'Ricochet', 'Shakedown', 'Thunder', 'Switchblade', 'Cutlass', 'Sabre', 'Marduk', 'Enkidu', 'Omega']
    word_2 = ['Ridge', 'Canyon', 'Mountain', 'Creek', 'Hollow', 'Point', 'Bluff', 'Path', 'Tower', 'Cove', 'Plains', 'Valley', 'Bay', 'Channel', 'Gulf', 'Reef', 'Ravine', 'Deep', 'Quadrant', 'Triangle', 'Highway', 'Parkway']
    word_3 = ['part_I', 'part_II', 'part_III', 'part_IV', 'part_V', 'part_VI', 'part_VII', 'part_VIII', 'part_IX', 'part_X']
    choice_1 = random.choice(word_1)
    choice_2 = random.choice(word_2)
    choice_3 = random.choice(word_3)
    unique_name = choice_1 + '_' + choice_2 + '_' + choice_3
    filename = unique_name + '.txt'
    return filename



#filename = generate_unique_name()
#print(filename)
#####################################################
def later_function(binary_order):

    if binary_order == 'ord':
        decision = ("all of the possible permutations in order")
        return decision
    elif binary_order == 'shuf': 
        # do something with perm_output_str
        decision = ("all of the possible permutation in random order [like a shuffled deck]")
        return decision
    elif binary_order == 'ran':
        decision = ("random permutations")
        return decision 
    else:
        exit(0)

#decision = later_function(binary_order)
######################################################


def footer(filename):
	return f"""
--------------------------------
for more info visit:
https://www.gregpfeiffer.com

{filename}
generated with THE INTERVAL CODE

copyright G.C.Pfeiffer ©2022
"""






