from flask import Flask, request
from typing import Dict, List

import common4
from common4 import run_standard_text_flow

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def prompt_values():
    if request.method == 'POST':
        entered_values_raw = request.form['entered_values_raw']
        entered_values_as_int_list_unfiltered = [int(x) for x in entered_values_raw.split(',')]
        entered_values = [x for x in entered_values_as_int_list_unfiltered if x > 0 and x < 7]
        print('-------')
        print(entered_values)
        print(type(entered_values))
        print(type(entered_values[0]))
        print('-----')
        binary_order = request.form['binary_order']
        show_binary = request.form['show_binary'] == 'True'
        initial_pitch = request.form['initial_pitch']
        run_standard_text_flow(entered_values, binary_order, show_binary, initial_pitch)
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

