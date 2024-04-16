# ELO Rest API

## General

openapi.json can be downloaded from the ELO Server directly

* http://eloServer.com:6056/ix-Archive/resources/openapi.json

Also notice that other resources are available at http://eloServer.com:6056/ix-Archive/resources.html

In addition, there is a small example from elo directly:
* https://eloServer.com/ix-Archive/js-api-examples/rest/index.html

### Client generation

based on the openapi.json we can generate a client to make our life easier

Tool used https://github.com/openapi-generators/openapi-python-client

```
pip install openapi-python-client
cd eloclient
openapi-python-client generate --path ../eloRestAPI/openapi_v23.json 
```


## Authentication

The authentication is done via
~~a ticket, which is returned by the login function ("/IXServicePortIF/login").
The ticket is valid for a certain amount of time, which is returned by the login function as well.~~ I could not get the ticketed based authentication to work. Therefore, I used **HTTP Basic Auth**.

### Notes on the Ticket based authentication

Entities

"LoginResult"

**Calls**

__"/IXServicePortIF/login":__
-> returns a Ticket

Desc:
"\u003cp\u003e\n If the function succeeds, the return value is an object containing a ticket that allows access to all
the other\n interface functions.\n \u003c/p\u003e\n \u003cp\u003e\n This ticket has a limited lifetime as returned in
\u003ccode\u003eLoginResult.ticketDuration\u003c/code\u003e. The life time can be\n extended by calling
\u003ccode\u003ealive\u003c/code\u003e.\n \u003c/p\u003e\n \u003cp\u003e\n The
\u003ccode\u003erunAsUser\u003c/code\u003e parameter is used in Single-Sign-On environments. The login is performed for
every user\n with the same SSO account specific to the application and the \u003crunAsUser\u003e parameter specifies the
security context\n for the Indexserver connection. The SSO account must have administrator privileges.\n
\u003c/p\u003e",

```
curl -X 'POST' \
'http://eloServer:6056/ix-Archive/rest/IXServicePortIF/login' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"ci": {
"callId": "string",
"country": "string",
"language": "string",
"ticket": "string",
"timeZone": "string",
"options": 0
},
"userName": "Administrator",
"userPwd": "secret",
"clientComputer": "",
"runAsUser": ""
}'
```

**It is important to also send the dummy `"ci": {...}` in the request body. Otherwise, the result from the server
will just be `"ticket":"de.elo.ix.client.ticket_from_cookie"`**

returns

```
{
    "result": {
        "clientInfo": {
            "callId": "string",
            "country": "STRING",
            "language": "string",
            "ticket": "E9F16B2C8E7595D55A818AABB18CDC3F",
            "timeZone": "string",
            "options": 0
        },
        "ticketLifetime": 486,
        "user": {
            "desc": "",
            "flags": 2013265919,
            "groupList": [
                9100,
                9999
            ],
            "id": 0,
            "keylist": [
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63,
                63
            ],
            "name": "Administrator",
            "parent": 0,
            "pwd": "",
            "sessions": [],
            "type": 1,
            "userProps": [
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ],
            "ldapProperties": {},
            "guid": "(E10E1000-E100-E100-E100-E10E10E10E40)",
            "tStamp": "1970.01.01.00.00.00",
            "lastLoginIso": "20230927",
            "superiorId": 0,
            "flags2": 49015,
            "orgUnitIds": [],
            "availableRoles": [],
            "packageName": ""
        },
        "activeSubstitutions": []
    }
}
```
/IXServicePortIF/getSessionFromTicket
-> returns a LoginResult
