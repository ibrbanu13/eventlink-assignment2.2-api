# EventLink API Documentation
 
EventLink helps university students discover campus and club events, and lets organizers publish and manage them. This document describes the Assignment 2 prototype: a REST API with **mocked in-memory data**, token authentication and role-based access.
 
- Base URL: `http://127.0.0.1:8000/api/v1`
- Interactive docs (Swagger UI): `http://127.0.0.1:8000/docs`
- Mock data lives in memory and **resets every time the server restarts**.

## Authentication
 
There is no login in this prototype. Three fixed tokens are used instead. Send one in every events request:
 
```http
Authorization: Bearer user-a-token
```
 
| Role | Token | Permissions |
|---|---|---|
| Organizer A (regular user) | `user-a-token` | Reads, updates and deletes only their own events |
| Organizer B (regular user) | `user-b-token` | Reads, updates and deletes only their own events |
| Administrator | `admin-token` | Reads, updates and deletes any event |
 
- Missing or unknown token: `401 Unauthorized`.
- Valid token, but the event belongs to someone else: `403 Forbidden` (see [Design decisions](#design-decisions)).
- `GET /greeting` is public and needs no token.

## Response format
 
Every JSON response uses an envelope. The HTTP status always matches it: `2xx` means `success: true`, `4xx` and `5xx` mean `success: false`.
 
**Success**
 
```json
{
  "success": true,
  "message": "Event retrieved successfully.",
  "data": { "id": "evt_101", "title": "Introduction to Education Program of Faculty of International Resource Sciences Akita University, Japan" }
}
```
 
- `data` holds the resource, an array of resources, or `null` (after a delete).
- List responses add `meta`: `{ "total": 2, "page": 1, "perPage": 10 }`.
**Error**
 
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request contains invalid or missing fields.",
    "details": [
      { "field": "title", "message": "String should have at least 3 characters" }
    ]
  }
}
```
 
- `error.code` is one of the fixed values below; clients use it to decide what to show.
- `details` appears only for validation errors.
- Messages never include stack traces, file paths or internal details.

## Error codes
 
| HTTP status | `error.code` | When it happens | How to fix it |
|---:|---|---|---|
| 400 | `VALIDATION_ERROR` | A field is missing, has the wrong type or length, or an unknown field was sent. Also invalid query parameters. | Read `error.details` and correct each listed field. |
| 401 | `UNAUTHORIZED` | The `Authorization` header is missing or the token is unknown. | Send `Authorization: Bearer <token>` with one of the three mock tokens. |
| 403 | `FORBIDDEN` | The event belongs to another user. | Use the owner's token, or `admin-token`. |
| 404 | `NOT_FOUND` | No event has this id, or the URL does not exist. | Check the id (list events first) and the URL. |
| 405 | `METHOD_NOT_ALLOWED` | The HTTP method is not supported on this URL. | Use one of the methods listed for the endpoint below. |
| 409 | `CONFLICT` | You already have an event with the same title, start time and location. | Change one of those fields, or edit the existing event. |
| 500 | `INTERNAL_ERROR` | Unexpected server error. | Retry; if it persists, report it. |