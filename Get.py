import requests

hostURL = "https://jsonplaceholder.cypress.io/posts/";

response_code = requests.get(hostURL);

rownum = 1
for resp in response_code.json():
    assert isinstance(resp['userId'], int), "UserId datatype of row-"+rownum+" is invalid"
    assert isinstance(resp['id'], int), "Id datatype of row-"+rownum+" is invalid"
    assert isinstance(resp['title'], str), "title datatype of row-"+rownum+" is invalid"
    assert isinstance(resp['body'], str), "body datatype of row-"+rownum+" is invalid"
    print("Test Datatypes row-"+ str(rownum) +" : Pass")
    rownum+=1;