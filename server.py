import random

from flask import Flask, g, redirect, render_template, request, url_for

from utils import get_intervals, length_needed, total_num_pitches, make_permutations, join_us, pitch_list_generator, add_starting_p, pitch_stripper, tallies, generate_unique_name_no_suffix, later_function, footer

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
        return render_template('./form.html')


@app.route("/result")
def result_page():
    # parse/process inputs
    entered_values_raw = request.args['entered_values_raw']
    entered_values_as_int_list_unfiltered = [int(x) for x in entered_values_raw.split(',')]
    entered_values = [x for x in entered_values_as_int_list_unfiltered if x > 0 and x < 7]
    binary_order = request.args['binary_order']
    initial_pitch = request.args['initial_pitch']
    random_seed = int(request.args['random_seed'])

    # generate outputs and pass to template
    perm_list = make_permutations(length_needed(entered_values), binary_order, random_seed=random_seed)
    pitches_list_all = pitch_list_generator(initial_pitch, perm_list, entered_values)
    return render_template('./result.html',
        decision=later_function(binary_order),
        interval_set=get_intervals(entered_values),
        initial_pitch = initial_pitch,
        binary_order=binary_order,
        binary=perm_list,
        all_pitches=pitch_list_generator(initial_pitch, perm_list, entered_values),
        suggested_title=generate_unique_name_no_suffix(),
        total_tally=tallies(pitches_list_all)
    )

@app.before_request
def set_quote():
    g.quote = random.choice([
        "-It's all pipes!-",
        "-The central message of Buddhism is not every man for himself!-",
        "-What we observe is not nature itself, but nature exposed to our method of questioning.-",
        "-If I was an imitation, a perfect imitation, how would you know if it was really me?-",
        "-I can't lie to you about your chances. But you have my sympathies.-",
        "-Moods are for cattle and love play.-",
        "-In the afterlife, we’ll sit around talking about the good old days, when we wished that we were dead.",
        "-Who run Bartertown?-",
        "-Ever see a hot shot hit kid?  I saw the gimp catch one in Philly.-",
        "-A man goes to the doctor for a check, and the doctor exams him and says I’ve got bad news, you’ve got cancer and alzheimers.  The man goes Thank god I don’t have cancer.-",
        "-When I was born the doctor came out to the waiting room and said to my father, I'm very sorry. We did everything we could…  but he pulled through.-",
        "-Digital watches. And soon I shall have understanding of video cassette recorders and car telephones. And when I have understanding of them, I shall have understanding of computers.And when I have understanding of computers, I shall be the Supreme Being!-"

    ])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

#   python3 -m venv venv

#   source venv/bin/activate

#   python3 -m pip install -r requirements.txt



