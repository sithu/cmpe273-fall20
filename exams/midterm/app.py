import zmq_master
import time
from flask import Flask


app = Flask(__name__)

@app.route('/')
def root():
    return 'Election 2020'

@app.route('/result')
def calculate_result():
    # FIXME: 
    #zmq_master.send_to_voting_workers()
    #time.sleep(5)
    #result = zmq_master.receive_result()
    return {
        'x_votes': 15000,
        'y_votes': 20000 
    }
    