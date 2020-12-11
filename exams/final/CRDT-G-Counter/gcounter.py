class GCounter(object):
    def __init__(self, i, n, zmq_port):
        self.i = i # server id
        self.n = n # number of servers
        self.xs = [0] * n
        self.zmq_port = zmq_port
        # TODO
        # You can assume all servers are running at host tcp://127.0.0.1:xxxx
        # Start a new ZMQ server instance or process.

    def query(self):
        return sum(self.xs)

    def add(self, x):
        assert x >= 0
        self.xs[self.i] += x

    def merge(self, c):
        zipped = zip(self.xs, c.xs)
        self.xs = [max(x, y) for (x, y) in zipped]
    
    def to_dict(self):
        return {
            'i': self.i,
            'n': self.n,
            'xs': self.xs
        }
        
    def _listen_merge_request_from_peer(self):
        # receive merge request from peer.
        # TODO
        #
        # self.merge(xxx)
        pass        


    def sync_to_peer(self, zmq_peer_port):
        peer = f"tcp://127.0.0.1:{zmq_peer_port}"
        print(f"Syncing to peer:{peer}")
        # send merge request to peer.
        # TODO
        #
        pass