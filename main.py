import random

from flask import Flask, g, redirect, render_template, request, url_for

from utils import get_intervals, length_needed, total_num_pitches, make_permutations, join_us, pitch_list_generator, add_starting_p, pitch_stripper, tallies, generate_unique_name_no_suffix, later_function, footer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root_form():
    if request.method == 'POST':
        entered_values_raw = request.form['entered_values_raw']
        if not all(char.isdigit() and int(char) in range(1, 7) for char in entered_values_raw.split(',')):
            return render_template('./form.html')
        return redirect(
            url_for('result_page',
                entered_values_raw=entered_values_raw,
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
    entered_values = entered_values[:9]
    binary_order = request.args['binary_order']
    initial_pitch = request.args['initial_pitch']
    random_seed = int(request.args['random_seed'])
    seq_length = len(entered_values)

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
        total_tally=tallies(pitches_list_all),
        total_length =total_num_pitches(seq_length)
    )

@app.before_request
def set_quote():
    g.quote = random.choice([
        "It's all pipes!  -G. Costanza",
        "The central message of Buddhism is not every man for himself!  -Wanda",
        "What we observe is not nature itself, but nature exposed to our method of questioning.  -Werner Heisenberg",
        "If I was an imitation, a perfect imitation, how would you know if it was really me?  -Childs",
        "I can't lie to you about your chances. But you have my sympathies.  -Ash",
        "Moods are for cattle and love play.  -Gurney Halleck",
        "Oh, I'm afraid the deflector shield will be quite operational when your friends arrive.  -Emperor Palpatine",
        "Who run Bartertown?  -Master",
        "Ever see a hot shot hit kid?  I saw the gimp catch one in Philly.  -William S. Burroughs",
        "One word sums up probably the responsibility of any vice president,and that one word is 'to be prepared.' -Dan Quayle",
        "A man goes to the doctor for a check, and the doctor exams him and says I’ve got bad news, you’ve got cancer and alzheimers.  The man goes Thank god I don’t have cancer.   -Gilbert Gottfried",
        "When I was born the doctor came out to the waiting room and said to my father, I'm very sorry. We did everything we could…  but he pulled through.  -Rodney Dangerfield",
        "And soon I shall have understanding of video cassette recorders and car telephones. And when I have understanding of them, I shall have understanding of computers.And when I have understanding of computers, I shall be the Supreme Being!  -Evil",
        "South to drop off, north to pick up. Okay, that's a good system! - Jack Butler",
        "Huge blocks of ice, weighing many tons, were lifted into the air and tossed aside as other masses rose beneath them. We were helpless intruders in a strange world, our lives dependent upon the play of grim elementary forces that made a mock of our puny efforts.  -Sir Ernest Shackleton",
        "The desert is an ocean in which no oar is dipped.  -T.E. Lawrence",
        "24 hours is like 3 weeks!  -Amity Island Town Hall Meeting.",
        "No sir. I'm just a big Finkle fan... This is my Graceland.  -Ace Ventura",
        "No. I cannot. For I am sorely needed... here, at the ashram.  -Ace Ventura",
        "I'll go speak with this Lord Humongus. He seems like a reasonable man.  -Curmudgeon",
        "The Duke: Describe what the last man who passed a $20 bill looked like.   Bartender: Thirty,Tall.   The Duke: About six feet tall?   Bartender: Six-five., The Duke: Dark-Brown Hair?   Bartender: Light Colored.   The Duke: Sounds like our man.  -Midnight Run",
        "Now, in order to prevent the enemy from issuing fake or confusing orders the CRM 114 is designed not to receive at all unless the message is preceded by the correct three-letter code group prefix.  -Gen. Turgidson",
        "They were a party of settlers in covered-wagon times...  -Jack Torrence",
        "El que hace trofeos de los hombres.  -Ana",
        "Y'know, one day, Tito Puente will be dead, and you'll say, 'Oh, yes, I've been listening to his work for years, and I think he's fabulous.  -John Winger",
        "See you on deck, Senator.  -Judge Smails",
        "Spaulding: I want a hamburger, no a cheeseburger. I want a hotdog, I want a milkshake, I want potato chips...   Judge Smails: You'll get nothing and like it!",
        "Never heard of him... that's not exactly true. We were like brothers. We flew together during the war.   -Buck Murdock",
        "My mind seems to have become a kind of machine for grinding general laws out of large collections of facts.   -Charles Darwin",
        "...it's like I'm sittin' here playing cards with my brother's kids or somethin'  -Johnny Tyler",
        "I may not be a first-rate composer, but I am a first-class second-rate composer.  -Richard Strauss",
        "There was this sailor who was so fat... (Suddenly threatened by fat sailor at the bar) ...Uh, he was so fat that everybody liked him and there was nothing funny about him at all.   -Fozzie Bear",
        "Our doubts are traitors and make us lose the good we oft might win by fearing to attempt.  -Shakespere",
        "The new model is something like two thousand cubic inches, developing two hundred brake - horsepower at four thousand revolutions per minute on a magnesium frame with two styrofoam seatsand a total curb weight of exactly two hundred pounds.   -Raoul Duke",
        "We could have brought anyone into this show: Janet Jackson, Paula Abdul. Nomi Malone is what Las Vegas is all about!   -Mr.Karlman",
        "Well, we've never done this before. But seeing as it's special circumstances and all, he says I can knock a hundred dollars off that Trucoat.  - Jerry Lundegaard",
        "That was a bit of a nastiness last night, yes? Some very extreme nastiness, yes? A few of a certain Billy Boy's friends were ambulanced off late, yes. Your name was mentioned. The words got through to me by the usual channels. Certain friends of yours were named also. Oh, nobody can prove anything about anybody, as usual. But I'm warning you, little Alex, being a good friend to you, as always, the one man in this sore and sick community who wants to save you from yourself!  -Mr.Deltoid",
        "You'll have it, but let Heinrich plant the detonators and Theo prepare the vault. After we call the police you can tear the building apart looking for this man but, until then, do not alter the plan!  -Hans Gruber",
        "By Grabthar's Hammer -- what a savings.   -Alan Rickman playing Sir Alexander Dane portraying Dr. Lazarus",
        "Mr. Joshua, your left arm, please.  -General Peter McAllister",
        "Okay Victor, I'll give the taxpayers a break. But I have something I want to confess. And I don't think you're gonna like it. I AM CASTOR TROY.",
        "See you at the party Richter!  -Doug Quaid",
        "Utah, get me two!  -Pappas",
        "Pay him. Pay that man his money.  -Teddy KGB",
        "But always – do not forget this, Winston – always there will be the intoxication of power, constantly increasing and constantly growing subtler. Always, at every moment, there will be the thrill of victory, the sensation of trampling on an enemy who is helpless. If you want a picture of the future, imagine a boot stamping on a human face–for ever.  -O'Brian",
        "Fine! I don't need you. I'll get myself a new best friend, too! So, go ahead. Go back to your fancy cars, and your big bank accounts, and your celebrity friends, and your beautiful women, and Victoria Silvstedt, Playmate of the Year...  -Coop Cooper",
    ])


if __name__ == "__main__":
    # intended for local dev invoked via `python main.py`
    # google cloud's app engine will not use this, it uses only the `app` object defined above
    app.run(host="127.0.0.1", port=8080, debug=True)

#   python3 -m venv venv

#   source venv/bin/activate

#   python3 -m pip install -r requirements.txt

