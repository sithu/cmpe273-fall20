# Class Project

You will be buliding a distributed key-value datastore using ZeroMQ as transport protocol.

[ Node-0 ] 
[ Node-1 ]
[ Node-2 ]
[ Node-3 ]

### Cluster Adjustment

- Add Node-4


- Remove Node-0 

## APIs

POST /api/entries

```
{
    "key": "foo",
    "value": "bar"
}
```


GET /api/entries

```
[
    {
        "key": "foo",
        "value": "bar"
    },
    {
        "key": "foo2",
        "value": "bar2"
    }
]
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
