## Problem

HTTP doesn't store data about you. That's why we call him **stateless**.

But just imagine…
you're logged on Amazon :luc_arrow_right_circle: request #1

 now, you want to store some item in cart.
 so server should know who's sending this request

the request itself doesn't store that auth data (token for example)
you should store that in browser

so, after first request you should get a token and then use that alongside with next requests

Now you have here 3 options:
1. cookies :luc_cookie:
2. local storage
3. session storage

---

### JWT

You send request to login :luc_arrow_right_circle:
Server responds with JWT token :luc_arrow_left_circle:

Then you <mark style="background: #ABF7F7A6;">manually store it in Local Storage</mark> in the frontend:

```js
localStorage.setItem('token', 'eyJhbGc...')
```

When you want to send your next requests,
you <mark style="background: #ABF7F7A6;">manually add that token to the header</mark>:

```
Authorization: Bearer eyJhbGc...
```

Server that extracts that token, verifies signature, knows who are you from JWT subject and claims.

---

### Cookies

You send request to login :luc_arrow_right_circle:
Server generates `sessionId` and stores in server memory, along with `userId` and other user data.
After that, responds with this response header:

```
Set-Cookie: sessionId=abc123; HttpOnly
```

The <mark style="background: #ABF7F7A6;">browser automatically stores these cookies</mark>.

When sending your next requests, the <mark style="background: #ABF7F7A6;">browser automatically includes those cookies in the request</mark>.

```
Cookie: sessionId=abc123
```

The server will take that `sessionId` and look up in its storage.
Then maps it to `userId`.
