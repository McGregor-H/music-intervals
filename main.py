from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        entered_values = request.form['entered_values']
        binary_order = request.form['binary_order']
        show_binary = request.form['show_binary']
        initial_pitch = request.form['initial_pitch']
        # Do something with the entered values
        return 'Values received: {} {} {} {}'.format(entered_values, binary_order, show_binary, initial_pitch)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

