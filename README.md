# Garden Journal

This will be an app to record our harvest from the garden and our chickens.

## API

This is an append only log of things gathered in the garden.  Sqlite used for the backend with a schema of (timestamp, key, value).  New entries are added by posting JSON to the `/new` endpoint with the following format:


```
{
    "key": "cucumbers",
    "value": 3
}
```

App adds a timestamp automatically.

## Future?

- Create a iPhone shortcut to enable "hey Siri, garden report 4 eggs".
- Add support for general weather recording so we can correlate weather with
yields
- Create IDs for garden beds maybe?
