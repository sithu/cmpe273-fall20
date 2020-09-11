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

### GET /api/bookmarks/abc123

```
{
    "id": "abc123",
    "name": "Pinterest",
    "url": "https://www.pinterest.com/pin/27373510214883341/",
    "description": "Innovation Engine"
}
```

### GET /api/bookmarks/abc123/qrcode

200 OK

Return QR Code PNG image.


### DELETE /api/bookmarks/abc123

204 No Content



### GET /api/bookmarks/stats

The endpoint should return the number of request made to each bookmark and it should support conditional GET.

200 OK

_Respond_

```
{
    [
        "abc123": 3
    ]
}
```
