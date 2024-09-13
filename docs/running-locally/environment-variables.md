# Set Up `.env` File

- Clone a new `.env` file from the `.env.template` to store local configuration options:

```bash
$ cd env && cp .env.template .env.test
```

# Trello Set Up

The project uses a web service called Trello to store to-do items. 

Before running the app locally, you will need to set up some Trello configuration as follows.

* [Create a Trello account](https://trello.com/signup)
* [Generate an API key](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#managing-your-api-key) and use it to populate the `TRELLO_API_KEY` variable in the `.env` file
* Create an API token by clicking the link on the page where your API key is displayed, and use it to populate the `TRELLO_API_TOKEN` variable in the `.env` file
* Create a new board in your Trello account
* Follow [these instructions](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#your-first-api-call) to get the board ID, and use it to populate the `TRELLO_BOARD_ID` variable in the `.env` file
* Use [this endpoint](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-lists-get) to get the list IDs for the board, and use them to populate the `TRELLO_<list name>_LIST_ID` variables in the `.env` file
