# Class Project

You will be buliding a distributed key-value datastore using ZeroMQ as transport protocol.

[ Node-0 ] 
[ Node-1 ]
[ Node-2 ]
[ Node-3 ]

### Cluster Adjustment

- Add Node-4


- Remove Node-0 


_How to launch server cluster_

> Format: python server_consumer.py {num_node}

```
pipenv run python server_consumer.py 4
```

_How to run client_

> Format: python client_producer.py {num_node}

```
pipenv run python client_producer.py 4
```
## Phase 1

### Consistent hashing

#### Test Case 1

R = 0

Adding and removing one node.


#### Test Case 2

R = 2

Adding and removing one node.




### HRW hashing

#### Test Case 1

- Adding and removing one node.


#### Test Case 2

- Adding and removing one node.
