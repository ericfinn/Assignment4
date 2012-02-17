import csv

g_attributes = []

def indexOfAttribute(attr):
    index = 0
    for a in g_attributes:
        if a[0] == attr[0]:
            return index
        index = index + 1
    return -1

def getName(attr):
    return attr[0]

def getDomainType(attr):
    return attr[1]

def getDomain(attr):
    return attr[2]


#get names and domains of attributes from names file
#create mapping from domains in data file to discrete values
#get data from data file

# a : classification
# d : discrete
# i : ignore
# c : continuous

#returns a tuple of (examples, attributes)
def parseFile(dataFile, namesFile):
    namesreader = csv.reader(open(namesFile, 'rb'), skipinitialspace=True)
    datareader = csv.reader(open(dataFile, 'rb'), delimiter=',')
    
    examples = []
    attributes = []
    
    for row in namesreader:
        attributes.append([row[0].strip(), row[1].strip(), set()])
        
        for row in datareader:
            examples.append(row)
            i = 0
            for data in row:
                attributes[i][2].add(row[i])
                i = i + 1
                
    data = (examples, attributes)
    return data
