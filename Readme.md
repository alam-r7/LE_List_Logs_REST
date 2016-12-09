# LE_List_Logs_REST

You need to have a Read/Write API key for your LE account, modify the 'apiKey' variable with your R/W key.
When the script completes, two JSON Objects will be returned. One with your log keys and the other will have your log set keys.

Example Response:

```
Log Keys: 
{
	"Log Set A": {
		"Log 1": "LOG_KEY_1"
		"Log 2": "LOG_KEY_2"
	}
	"Log Set B": {
		"Log 3": "LOG_KEY_3"
		"Log 4": "LOG_KEY_4"
	}
}

Log Set Keys:
{
	"Log Set A": "LOG_SET_KEY_A"
	"Log Set B": "LOG_SET_KEY_B"
}
```
