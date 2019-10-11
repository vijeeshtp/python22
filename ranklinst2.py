
class student :

    def __init__(self, r, n, m1, m2, m3 , m4):
        self.rollno=r
        self.name= n
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3
        self.mark4 = m4


    def calcTotal (self):
        self.total= self.mark1 + self.mark2 + self.mark3 + self.mark4



def readfile (filename) :

        with open (filename) as data:
            lines= data.readlines()

        return lines

def processdata (lines):
    l= []
    for x in lines :
        vals= x.split(",")
        s = student(vals[0], vals[1], int (vals[2]), int (vals[3]), int(vals[4]), int (vals[5]))
        s.calcTotal()
        l.append( s )
    return l

def writetofile_old(filename, data):

    with open(filename, mode="w") as f:
        for x in data:
            s = x.rollno + "," + x.name +  "," + str (x.total) + "\n"
            f.write(s)

def writetofile(filename, data):
    l= []
    for x in data:
        s = x.rollno + "," + x.name + "," + str(x.total) + "\n"
        l.append(s)

    with open(filename, mode="w") as f:
            f.writelines(l)


def main ():

    try :
        lines =readfile("students.csv")

        records= processdata(lines)
        print (records)
        records.sort(key=lambda a : a.name)
        writetofile("namelist.csv", records)

        records.sort(key=lambda x: x.rollno)
        writetofile("rollno_list.csv", records)

        records.sort(key=lambda x: x.total, reverse=True)
        writetofile("mark_list.csv", records)

    except FileNotFoundError:
        print ("File name is incorrect")

main()
