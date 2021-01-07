# BLUESTACK

Below are the Various API used  in the APP
=====================================================================================
Note The app is also hosted on heroku 

 https://stark-eyrie-09414.herokuapp.com/bluestackApp/user-signup-view/ 
=======================================================================================
User sign up View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/user-signup-view/
--------------------------------------------------------
Method : POST

Param= {
   "email": "rr@gmail.com",
   "user_type" : "EM"
   "mobileNumber": "9922339090",
    "password": "rahul@123",
    "username": "user",
    "firstName": "demofirst",
    "lastName": "demolasr",
    "team": "qa",
    "position": "eerr"
}


User Login In View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/user-signup-view/
--------------------------------------------------------
Method : POST

 Login: URL: http://127.0.0.1:8000/bluestackApp/user-login-view/
 
 Param ={
    "email": "user@gmail.com", "password":"user"
   }


Create Employee View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/create-employee/
--------------------------------------------------------
Method : POST
Param = 
  {"email":"user4@gmail.com", 
    "mobileNumber":7858288481, 
    "username":"usr22", 
    "password":"user",
    "user_type":"OM",
    "firstName":"rajput",
    "lastName":"rarara",
    "team":"rajra",
    "position":"enfin"
}


Employee Detail View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/employee-detail/
--------------------------------------------------------
Method : GET




Update EMployee View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/employee-update/
--------------------------------------------------------
Method : PUT/ PATCH
For Patch please provide some value so it would be partial update
Param = 
  {"email":"user4@gmail.com", 
    "mobileNumber":7858288481, 
    "username":"usr22", 
    "password":"user",
    "user_type":"OM",
    "firstName":"rajput",
    "lastName":"rarara",
    "team":"rajra",
    "position":"enfin"
}



Delete Employee View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/employee-delete/1
--------------------------------------------------------
Method : DELETE
Over here lookup field is by default is pk





Create-room View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/create-room/
--------------------------------------------------------
Method : POST
Params = {"bookingMail": "abc@gmail.com",
          "name": "conf1",
          "sitting": "22",
          "currentStatus": "AV",
          }



Detail room View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/room-detail/
--------------------------------------------------------
Method : GET
Response :==>
[
    {
        "id": 2,
        "name": "kaka",
        "bookingMail": "ma@gmail.com",
        "sitting": "100",
        "currentStatus": "BO"
    },
    {
        "id": 3,
        "name": "conf3",
        "bookingMail": "me@gmail4.com",
        "sitting": "23",
        "currentStatus": "AV"
    },
    {
        "id": 4,
        "name": "rara",
        "bookingMail": "abc@gmail.com",
        "sitting": "34",
        "currentStatus": "AV"
    },
    {
        "id": 5,
        "name": "raraw",
        "bookingMail": "abec@gmail.com",
        "sitting": "34",
        "currentStatus": "AV"
    }
]



Delete room View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/room-delete/1
--------------------------------------------------------
Method: Delete 


Update room View
--------------------------------------------------------
http://127.0.0.1:8000/bluestackApp/room-detail-update/
--------------------------------------------------------
Method : PUT/ PATCH
