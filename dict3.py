
data = {
    "111" : {
        "name" : "kumar",
        "phone" : "1232323",
        "mark" : [33,44,55,66]
    },
    "222": {
        "name": "anil",
        "phone": "1232323",
        "mark": [10, 20, 30, 40]
    },
    "333": {
        "name": "tom",
        "phone": "1232323",
        "mark": [55, 33, 55, 66]
    }
}

for rollno, details in data.items() :

    marks = details ["mark"]
    total = 0
    for m in marks :
        total = total + m;

    print (rollno, details ["name"], total)