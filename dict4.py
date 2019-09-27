data = {

    "123" : {
        "name" : "anand",
        "marks" : {
            "sem1" : {
                "sub1" :1,
                "sub2" :2,
                "sub3" :3
            },
            "sem2" : {
                "sub1" :1,
                "sub2" :2,
                "sub3" :3
            },
            "sem3" : {
                "sub1" :1,
                "sub2" :2,
                "sub3" :3
            }

        }
    },

    "456": {
        "name": "seetha",
        "marks": {
            "sem1": {
                "sub1": 2,
                "sub2": 2,
                "sub3": 2
            },
            "sem2": {
                "sub1": 3,
                "sub2": 3,
                "sub3": 3
            },
            "sem3": {
                "sub1": 4,
                "sub2": 4,
                "sub3": 4
            }

        }
    }
}

print (data)

for rollno, details in data.items ():

    marks = details ["marks"]

    totalMark = 0
    for sem, subjects in marks.items () :

        semTotal =0
        for  sub, mark in subjects.items():
            semTotal = semTotal+ mark
        totalMark = totalMark + semTotal

    print (rollno, details["name"], totalMark)


