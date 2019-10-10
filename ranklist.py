def  readfile (filename) :
    data = open (filename)
    lines= data.readlines()
    return lines

def processdata (lines):
    l= []
    for x in lines :
        vals= x.split(",")
        total = int (vals[2])+ int (vals[3])+ int (vals[4])+ int (vals[5])
        l.append( (vals[0], vals[1], total ) )
    return l

def writetofile(filename, data):
    f = open(filename, mode="w")
    for x in data:
        s = x[0] + "," + x[1] +  "," + str (x[2]) + "\n"
        f.write(s)

def main ():
    lines =readfile("students.csv")
    records= processdata(lines)
    print (records)
    records.sort(key=lambda a : a[1])
    writetofile("namelist.csv", records)

    records.sort(key=lambda x: x[0])
    writetofile("rollno_list.csv", records)

    records.sort(key=lambda x: x[2], reverse=True)
    writetofile("mark_list.csv", records)

main()
