# RTCG API

The RTCG API allows you interact with the card index and card data. Anyone can get card data, but updating or adding cards is a whitelisted feature only. We currently are not accepting applications for whitelisting. Below you can find the docs for each route and its return data.

## Requests

The base URL for the API is `api.rtcg.repl.co`. Each listed route can be added to the end of that URL. All requests require the `Content-Type: application/json` header to be set. If you have an API token, add a header to your requests like so: `X-API-TOKEN: token-name`

## Routes 

+ **`/cards`**
  + `GET`: Returns list of all cards in the index.
+ **`/card/{id}`**
  + `GET`: Return an individual card by ID. `404` if card does exist.
  + `PUT`: Update an existing card in the index. Returns updated card on success, `404` if card does not exist.
  + `DELETE`: Deletes an existing card in the index. Returns `204` empty response on success, `404` if card does not exist.
+ **`/card/add`**
  + `POST`: Create and a new card to the index. Returns `201` on success, `400-403` or `500` on fail.

## Objects

The standard card object looks like this:

```json
{
  "color":"#808080",
  "description":"A ReplTalk moderator and anime fanatic.",
  "id":2,
  "image":"https://storage.googleapis.com/replit/images/1612721588723_7d2dd8f20ea4fe3f5a7f770825f40eca.jpeg",
  "name":"frissyn",
  "rarity":"Very Rare",
  "shiny":true,
  "title":"God of Anime"
}
```
