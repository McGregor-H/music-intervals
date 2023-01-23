from flask import Flask, request
from typing import Dict, List

import common4
from common4 import run_standard_text_flow

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def prompt_values():
    if request.method == 'POST':
        #entered_values_raw = request.form.getlist('entered_values_raw')
        #entered_values = [int(val) for val in entered_values_raw.split(',') if int(val) in range(1, 7)]
        entered_values_raw = request.form['entered_values_raw']
        print(entered_values_raw)
        #temp_raw = entered_values_raw[0].split(', ')
        temp_raw = entered_values_raw.split(', ')
        print(temp_raw)
        entered_values = []
        for interval in temp_raw:
            if int(interval) in range(1, 7):
                entered_values.append(interval)
        print(entered_values)
        binary_order = request.form['binary_order']
        show_binary = request.form['show_binary'] == 'True'
        initial_pitch = request.form['initial_pitch']
        # Pass the values to main
        #print(entered_values)
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

