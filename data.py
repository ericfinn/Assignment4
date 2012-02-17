import csv

namesFile = "restaurant.names"
dataFile = "restaurant.data"

#domain: tuple(number, set or {'min':number, 'max':number})
#               0 if set
#               1 if min-max
#rawAttribute: tuple (string, domain)
#attribute: tuple(string, set(int))

g_attributes = []

def indexOfAttribute(attr):
    index = 0
    for a in g_attributes:
        if a[0] == attr[0]:
            return index
        index = index + 1
    return -1


#get names and domains of attributes from names file
#create mapping from domains in data file to discrete values
#get data from data file

# a : classification
# d : discrete
# i : ignore
# c : continuous

namesreader = csv.reader(open(namesFile, 'rb'), delimiter=',')
datareader = csv.reader(open(dataFile, 'rb'), delimiter=',')

examples = []


for row in namesreader:
    examples.append((row[0].strip(), row[1].strip()))


print examples
