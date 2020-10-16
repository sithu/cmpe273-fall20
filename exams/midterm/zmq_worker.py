import zmq
from  multiprocessing import Process

def voting_station_worker():
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://127.0.0.1:4000")
    
    result_sender = context.socket(zmq.PUSH)
    result_sender.connect("tcp://127.0.0.1:5000")
    
    msg = receiver.recv_json()
    region = msg['region']
    print(f'region={region} to count votes')
    result = {}
    # scan file and count votes
    if region == 'east':
        # FIXME
        # Count votes from east.cvs
        print(f'Counting {region}...')
        # FIXME
        result = {
            'region': region,
            'x': 0,
            'y': 0
        }
    else:
        # FIXME
        # Count votes from west.cvs
        print(f'Counting {region}...')
        # FIXME
        result = {
            'region': region,
            'x': 0,
            'y': 0
        }
    
    print(f'result={result}')
    result_sender.send_json(result)
    print('Finished the worker')
    
    
if __name__ == "__main__":
    voting_station_worker()