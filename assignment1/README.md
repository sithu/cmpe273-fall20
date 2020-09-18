# Assignment 1

You will be building a simple bookmarking application using [Python Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). All the bookmark data will be stored into a local [sqlitedict](https://pypi.org/project/sqlitedict/) datastore.

## Install Dependencies

```
pipenv install Flask==1.1.1
pipenv install pillow qrcode
pipenv install flask_monitoringdashboard
```

## API

### POST /api/bookmarks

_Request_

```
{
    "name": "Pinterest",
    "url": "https://www.pinterest.com/pin/27373510214883341/",
    "description": "Innovation Engine"
}
```

_Response_

201 Created

```
{
    "id": "abc123"
}
```

If the POST url is already existed in the database, the POST API should return HTTP 400 error.

_Response_

400 Bad Request

```
{
    "reason": "The given URL already existed in the system."
}
```



### GET /api/bookmarks/abc123

```
{
    "id": "abc123",
    "name": "Pinterest",
    "url": "https://www.pinterest.com/pin/27373510214883341/",
    "description": "Innovation Engine"
}
```

If the request bookmark id does not exist in the system, the API should return 


_Response_

```
404 Not Found
```

### GET /api/bookmarks/abc123/qrcode

200 OK

Return QR Code PNG image.


### DELETE /api/bookmarks/abc123

204 No Content



### GET /api/bookmarks/{id}/stats

The endpoint should return the number of GET request made to each bookmark and it should support conditional GET.

|Sequence | Request | DB | Response Header | Response Body
|-----|---------|----|----------|-----------|
| 1 | No ETag header | 10 | 200 OK, ETag: 10 | 10
| 2 | ETag: 10      | 10 | 304 Not Modified, ETag: 10 | |
| 3 | ETag: 10      | 10 | 304 Not Modified, ETag: 10 | |
| 4 | ETag: 10      | 11 | 200 OK, ETag: 11 | 11 |
| 5 | ETag: 11      | 11 | 304 Not Modified, ETag: 11 | |




_Response Header_

```
200 OK
ETag: version_num
```

_Response Body_

```
3
```

OR when the conditional GET applied in the subsequent calls, the response will not have a body.

_Request Header_

```
ETag: version_num
```

_Response Header_

```
304 Not Modified
ETag: version_num
```
