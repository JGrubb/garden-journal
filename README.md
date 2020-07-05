# Garden Journal

This will be an app to record our harvest from the garden and our chickens.

## API

The main data storage will be to CSV for now.  Maybe this will change later.

A Flask app will read and write CSV.  The app should display a table view of
previous days' harvest, ordered by date descending.  The topmost row of the 
table will be a webform with fields for each produce item as well as an extra
column for adding a new key/column to the CSV.

- App should handle updates gracefully, ie what if we pick another cucumber
later in the day?

## Future?

- Create a iPhone shortcut to enable "hey Siri, garden report 4 eggs".
- Add support for general weather recording so we can correlate weather with
yields
- Create IDs for garden beds maybe?
