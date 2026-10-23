# T11: HTTP and REST Concepts

## 1. What is HTTP?

HTTP stands for HyperText Transfer Protocol. It is used for communication between a client and a server over the Web. It helps us access web pages, images, videos, and other information.

For example, when we open a website in a browser, the browser sends a request to the server. The server processes the request and sends back a response.

## 2. Client and Server

HTTP works using a client-server model.

- **Client:** The application that sends a request. Examples include a web browser and a Python program.
- **Server:** The system that receives the request and sends back the required information.
- **Proxy:** A middle system that passes requests between the client and server. It can also help with caching and security.

For example, when we check the weather on our phone, the application requests weather information from a server and displays the result.

## 3. How HTTP Works

HTTP communication usually follows these steps:

1. The client sends a request to the server.
2. The server receives and processes the request.
3. The server prepares a response.
4. The response is sent back with a status code, headers, and sometimes a body.
5. The client reads the response and shows the result to the user.

In simple terms, the client asks for something, and the server responds to that request.

## 4. URL Anatomy

A URL is the address used to locate a resource on the Web.

Example:

`https://api.example.com/items/10?category=books`

The main parts are:

- **https:** The protocol used to access the resource securely.
- **api.example.com:** The domain name of the server.
- **/items/10:** The path that identifies the requested resource.
- **?category=books:** A query parameter that provides extra information.

These parts help the client send a request to the correct location.

## 5. HTTP Methods

HTTP methods tell the server what action the client wants to perform.

- **GET:** Used to retrieve information.
- **POST:** Used to send data, often to create a new resource.
- **PUT:** Used to replace or update an existing resource.
- **DELETE:** Used to remove a resource.

For example, in a student management application, GET can be used to view student details, while POST can be used to add a new student.

## 6. HTTP Status Codes

A status code tells us whether a request was successful or if something went wrong.

### 2xx – Success

- **200 OK:** The request was successful.
- **201 Created:** A new resource was created successfully.

### 4xx – Client Errors

- **400 Bad Request:** The request contains incorrect or invalid information.
- **401 Unauthorized:** Valid authentication is missing or invalid.
- **403 Forbidden:** The client is not allowed to access the resource.
- **404 Not Found:** The requested resource does not exist.
- **429 Too Many Requests:** Too many requests were sent within a certain period.

### 5xx – Server Errors

- **500 Internal Server Error:** Something unexpected went wrong on the server.
- **503 Service Unavailable:** The server is temporarily unable to handle the request.

These status codes make it easier to understand the result of an API request.

## 7. HTTP Headers and Message Bodies

HTTP headers provide additional details about a request or response. They help the client and server understand how the data should be handled.

Some common examples are:

- `Content-Type: application/json` – Indicates that the message body contains JSON data.
- `Accept: application/json` – Tells the server that the client can accept JSON responses.
- `Authorization: Bearer <token>` – Can be used to send an authentication token.

The message body contains the actual data being sent.

For example:

`{"name": "Arun", "marks": 85}`

This is JSON data containing a student's name and marks. JSON is commonly used when exchanging data between applications.

## 8. Important Features of HTTP

HTTP has several useful features:

- **Simple:** Its request-and-response structure is easy to understand.
- **Extensible:** Headers allow developers to add extra information to requests and responses.
- **Stateless:** Each request is independent by default. The server does not automatically remember previous requests.
- **Sessions:** Cookies can help a website remember information about a user between requests.
- **Caching:** Some responses can be stored and reused, which helps reduce repeated requests and improve performance.

Modern versions of HTTP also include features that help transfer data more efficiently.

## 9. What is a REST API?

REST stands for Representational State Transfer. It is an architectural style used to design APIs around resources.

For example, consider an API for managing items:

- `/items` refers to a collection of items.
- `/items/10` refers to a particular item.
- GET `/items/10` retrieves the item.
- PUT `/items/10` updates the item.
- DELETE `/items/10` deletes the item.

REST APIs commonly use HTTP methods to perform actions on resources. They often exchange data in JSON format, making it easier for different applications to communicate.

## 10. API Keys and Rate Limits

An **API key** is a credential used by some APIs to identify an application or control access to a service. It should be kept private and should not be uploaded to a public GitHub repository.

A **rate limit** controls how many requests a client can make within a specific period. It helps prevent excessive usage and protects the server from being overloaded.

For example, if an application sends too many requests, the server may respond with `429 Too Many Requests`.

## Conclusion

HTTP is an important part of web communication because it allows clients and servers to exchange information. Understanding HTTP methods, status codes, headers, and JSON helps us work with APIs more easily. REST provides a common way to organize APIs and manage resources using HTTP.


