import requests

hostURL = "https://jsonplaceholder.cypress.io/posts/";
body = {
    "title" : "recommendation",
    "body" : "motorcycle",
    "userID" : 12
}
response_code = requests.post(hostURL,body);
assert response_code.json()["title"]==body["title"], "Title data : invalid"
print("title data : correct")
assert response_code.json()["body"]==body["body"], "Body data : invalid"
print("body data : correct")
assert response_code.json()["userID"]==str(body["userID"]), "UserId data : invalid"
print("userID data : correct")
