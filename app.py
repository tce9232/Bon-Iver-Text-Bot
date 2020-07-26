import flask
import pickle
import lyric_prefix as lp
from textgenrnn import textgenrnn
import pandas as pd
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        lp.print_something
        Prefix = flask.request.form['Prefix']
        textgen_2 = textgenrnn(weights_path='model/Bon_Iver_model2_weights.hdf5',
                       vocab_path='model/Bon_Iver_model2_vocab.json',
                       config_path='model/Bon_Iver_model2_config.json')
        output = lp.lyrics_generator(textgen_2, Prefix, prefix_mode=2, temperatures=[1])
        return flask.render_template('main.html',
                                     original_input={'Prefix':Prefix},
                                     result=output,
                                     )
if __name__ == '__main__':
    app.run(debug=True)