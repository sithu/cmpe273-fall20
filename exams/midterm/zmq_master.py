import zmq
import sys
import time

def send_to_voting_workers():
    context = zmq.Context()
    sock = context.socket(zmq.PUSH)
    sock.bind("tcp://127.0.0.1:4000")
    
    time.sleep(1)
    
    # send worker to count East states' votes
    sock.send_json({ 'region': 'east' })
    
    # send worker to count East states' votes
    sock.send_json({ 'region': 'west' })
    
    time.sleep(1)
    
 
def receive_result():
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://127.0.0.1:3000")
    
    result_1 = receiver.recv_json()
    result_2 = receiver.recv_json()
    
    # FIXME 
    # Calculate total votes from result 1 and 2.
    return {
        'x_votes': 15000,
        'y_votes': 20000 
    }
     