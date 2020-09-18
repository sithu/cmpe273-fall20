# Assignment 2

## Dependency

- [Requests](https://requests.readthedocs.io/en/master/)

## Requirements

You will be building low-code/no-code HTTP client application that supports these features:

* Outbound HTTP GET calls
* Handle logic based on the response as INPUT.
* Trigger OUTPUT event based on the logic.


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
