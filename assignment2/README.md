# Assignment 2

## Dependency

- [Requests](https://requests.readthedocs.io/en/master/)

## Requirements

You will be building low-code/no-code HTTP client application that supports these features:

* Outbound HTTP GET calls
* Handle logic based on the response as INPUT.
* Trigger OUTPUT event based on the logic.


### Scheduler 'when' Format

| Field name    | Mandatory? | Allowed values  | Special characters |
| ------------- | ---------- | --------------- | ------------------ |
| Seconds       | No*        | 0-59            | * / , -            |
| Minutes       | Yes        | 0-59            | * / , -            |
| Hours         | Yes        | 0-23            | * / , -            |
| Day of month  | Yes        | 1-31            | * / , - L W        |
| Month         | Yes        | 1-12 or JAN-DEC | * / , -            |
| Day of week   | Yes        | 0-6 or SUN-SAT  | * / , - L #        |
| Year          | No*        | 1970–2099       | * / , -            |


_Flow Syntax_

```yaml
Step:
 id: 1
 method: GET
 outbound_url: http://requestbin.com/
 condition:
  if: 
    equal:
    left: http.response.code
    right: 200
  then:
    action: print
    data: http.response.body
  else:
    action: print
    data: "Error"
    
Scheduler:
  when: "0/1 * 0 ? * * *"
  step_id_to_execute: [ 1 ]
```

Save the flow in _input.yaml_

## How to execute Flow Http Client

```
python3 httpflow.py input.yaml
```

### Expected Output

```
Response body

OR

Error
```
