# Coding Question

You will be implemention a voting system which consists of API to fetch the result and two worker prcesses to count the votes from east and west regions.

The API will return the election result as:

```json
{
    'x_votes': 6,
    'y_votes': 5 
}
```

The communication between the app and worker processes will be via ZeroMQ.

To run worker process 1:

```
python3 zmq_worker.py
```

To run worker process 2 (in another terminal):
```
python3 zmq_worker.py
```

Implement the solution and add any necessary code to get it working.