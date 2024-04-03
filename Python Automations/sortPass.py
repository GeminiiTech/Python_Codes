import json

def save_details(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f)

def load_details(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# Define file path and load existing data
file_path = 'pass.json'
data = load_details(file_path)

# Define input text
text = 'Year : 2010|kenny@gmail.com|hshdbhsdjkjdjvj|otherStuff'
text2 = 'Year : 2011|taiwo@gmail.com|hshdbhsdjkjdjvj|herStuff'
text3 = 'Year : 2012|emma@gmail.com|hshdbhsdjkjdjvj|othStuff'

# Store input text in a list
items = [text, text2, text3]

# Split text and create a list of lists
totalText = [item.split('|') for item in items]

# Create a dictionary to store data
dictionary = {
    'year': [item[0].split(':')[1].strip() for item in totalText],
    'email': [item[1] for item in totalText],
    'auth': [item[2] for item in totalText],
    'stuff': [item[3] for item in totalText]
}

# Save the dictionary to a JSON file
save_details(file_path, dictionary)




# import json

# def save_details(filePath,data):
#     with open(filePath,"w") as f:
#         json.dump(data,f)

# def load_details(filePath):
#     try:
#         with open(filePath,"r") as f:
#             data = json.load(f)
#             return data
#     except:
#         return {}

# # VARIABLES
# # STORES THE JSON FILE
# file_path = 'pass.json'
# # STORES THE CURRENT CONTENT OF THE JSON FILE
# data  = load_details(file_path)        

# text = 'Year : 2010|kenny@gmail.com|hshdbhsdjkjdjvj|otherStuff'
# text2 = 'Year : 2011|taiwo@gmail.com|hshdbhsdjkjdjvj|herStuff'
# text3 = 'Year : 2012|emma@gmail.com|hshdbhsdjkjdjvj|othStuff'

# items = [text,text2,text3]
# totalText = []
# def splitText(list,totalText):
#     for i in list:
#         eachText = i.split('|')
#         totalText.append(eachText)
#     return totalText

# stuff = splitText(items,totalText)

# dictionary = {}
# eachYear = []
# eachEmail = []
# eachAuth = []
# otherStuff = []

# for i,items in enumerate(totalText):
#     year = items[0].split(":")
#     eachYear.append(year[1])
#     eachEmail.append(items[1])
#     eachAuth.append(items[2])
#     otherStuff.append(items[3])

# dictionary['year'] = list(eachYear)
# dictionary['email'] = list(eachEmail)
# dictionary['auth'] = list(eachAuth)
# dictionary['stuff'] = list(otherStuff)

# save_details(file_path,dictionary)
# print(dictionary)    
    