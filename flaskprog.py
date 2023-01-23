import json

from flask import Flask, request, jsonify
from typing import Dict, List

import common4
from formatting5 import get_intervals, length_needed, total_num_pitches, make_permutations, join_us, pitch_list_generator, add_starting_p, pitch_stripper, tallies, generate_unique_name, later_function, footer
from common4 import run_standard_text_flow

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def prompt_values():
    if request.method == 'POST':
        entered_values_raw = request.form['entered_values_raw']
        entered_values_as_int_list_unfiltered = [int(x) for x in entered_values_raw.split(',')]
        entered_values = [x for x in entered_values_as_int_list_unfiltered if x > 0 and x < 7]
        
        binary_order = request.form['binary_order']
        if binary_order not in {'ord', 'ran', 'shuf'}:
            raise Exception('Bad value for binary order!')
        show_binary = request.form['show_binary'] == 'True'
        initial_pitch = request.form['initial_pitch']

        inputs_together = {
            'entered_values': entered_values,
            'binary_order': binary_order,
            'show_binary': show_binary,
            'initial_pitch': initial_pitch
        }

        interval_set = get_intervals(entered_values)
        perm_list = make_permutations(length_needed(entered_values), binary_order)
        perm_result = join_us(perm_list)
        pitches_list_all = pitch_list_generator(initial_pitch, perm_list, entered_values)
        pitches_list_all_plus = add_starting_p(pitches_list_all, initial_pitch)
        string_list = pitch_stripper(pitches_list_all_plus)
        total_tally = tallies(pitches_list_all)
        outputs_together = {
            'interval_set': interval_set,
            'binary': perm_list,
            'all_pitches': pitches_list_all_plus,
            'tallies': total_tally,
            'suggested_title': generate_unique_name()
        }
        # return ("---INPUTS---" + json.dumps(inputs_together, indent=2) + '\n\n---OUTPUTS---\n' + json.dumps(outputs_together, indent=2)).replace('\n', '<br/>')
        return jsonify({'inputs': inputs_together, 'outputs': outputs_together})
    else: 
        return '''
            <form method="post">
                <label for="entered_values_raw">Enter values (comma separated):</label>
                <input type="text" name="entered_values_raw" id="entered_values_raw">
                <br>
                <label for="binary_order">Enter binary order:</label>
                <input type="text" name="binary_order" id="binary_order">
                <br>
                <label for="show_binary">Show binary?</label>
                <input type="checkbox" name="show_binary" id="show_binary">
                <br>
                <label for="initial_pitch">Enter initial pitch:</label>
                <input type="text" name="initial_pitch" id="initial_pitch">
                <br>
                <input type="submit" value="Submit">
            </form>
        '''

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

#   python3 -m venv venv

#   source venv/bin/activate

#   python3 -m pip install -r requirements.txt

