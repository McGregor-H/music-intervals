import random

from flask import Flask, redirect, request, url_for

from utils import get_intervals, length_needed, total_num_pitches, make_permutations, join_us, pitch_list_generator, add_starting_p, pitch_stripper, tallies, generate_unique_name, later_function, footer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root_form():
    if request.method == 'POST':
        return redirect(
            url_for('result_page', 
                entered_values_raw=request.form['entered_values_raw'], 
                binary_order=request.form['binary_order'], 
                initial_pitch=request.form['initial_pitch'], 
                random_seed=random.randrange(1000))
        )
    else:
        return '''<!DOCTYPE html>
        <html>
            <head>
                <title>Enter</title>
            </head>
            <body>

                <form method="post">
                    <p style="font-family: impact; font-size:40px;color:blue;">the interval program!<p>
                    <p style="font-family: dejavu sans">Enter a sequence of intervals</p>
                    <p style="font-family: dejavu sans">1=minor 2nd, 2=Major 2nd, 3=minor 3rd,</p>
                    <p style="font-family: dejavu sans"> 4=Major 3rd, 5=Perfect 4th, 6=Tri-tone</p>
                    <p style="color:red">for example: 2,5,3,1</p>
                    <body style="background-color:orange;">
                    <label style="font-family: dejavu sans" for="entered_values_raw">Enter values (comma separated):</label>
                    <input type="text" name="entered_values_raw" id="entered_values_raw">
                    <br>
                    <label style="font-family: dejavu sans" for="binary_order">Binary Order:</label>
                    <select id="binary_order" name="binary_order">
                        <option value="ord">Ordinary</option>
                        <option value="shuf">Shuffle</option>
                        <option value="ran">Random</option>
                    </select>
                    <br>
                    <label style="font-family: dejavu sans" for="initial_pitch">Enter initial pitch:</label>
                    <select id="initial_pitch" name="initial_pitch">
                        <option value="C">C</option>
                        <option value="C#">C#</option>
                        <option value="D">D</option>
                        <option value="D#">D#</option>
                        <option value="E">E</option>
                        <option value="F">F</option>
                        <option value="F#">F#</option>
                        <option value="G">G</option>
                        <option value="G#">G#</option>
                        <option value="A">A</option>
                        <option value="A#">A#</option>
                        <option value="B">B</option>
                    </select>
                    <input type="submit" value="Submit">
                    <br>
                </form>
                <html>
            '''


@app.route("/result")
def result_page():
    entered_values_raw = request.args['entered_values_raw']
    entered_values_as_int_list_unfiltered = [int(x) for x in entered_values_raw.split(',')]
    entered_values = [x for x in entered_values_as_int_list_unfiltered if x > 0 and x < 7]
    binary_order = request.args['binary_order']
    initial_pitch = request.args['initial_pitch']
    random_seed = int(request.args['random_seed'])

    interval_set = get_intervals(entered_values)
    perm_list = make_permutations(length_needed(entered_values), binary_order, random_seed=random_seed)
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

    return f'''<!DOCTYPE html>
<html>
<head>
    <title>Results</title>
</head>
<body>
    <h3>Here's the thing</h3>
    {string_list}
    {interval_set}
    {perm_list}
    {pitches_list_all_plus}
    {total_tally}
    {generate_unique_name}
</body>
</html>
'''


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

#   python3 -m venv venv

#   source venv/bin/activate

#   python3 -m pip install -r requirements.txt

