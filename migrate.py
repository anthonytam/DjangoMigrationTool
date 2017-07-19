# Some would call this hacky...
import sys
import inspect
from fields import models

# A little more SO
# https://stackoverflow.com/q/5903720
def modelCompare(current, required):
    modelToRemove = []
    for currentModel in current:
        if currentModel not in required:
            print("DROP TABLE " + currentModel + ";")
            modelToRemove.append(currentModel)
    for model in modelToRemove:
        current.pop(model)
    modelToRemove = []
    for requiredModel in required:
        if requiredModel not in current:
            query = "CREATE TABLE " + requiredModel + "(\n"
            for requiredModelAttribute in required[requiredModel]:
                query += requiredModelAttribute + " "
                for requiredModelAtrributeProperty in required[requiredModel][requiredModelAttribute]:
                    query += getSQLForAttributeProperty(requiredModelAtrributeProperty, required[requiredModel][requiredModelAttribute][requiredModelAtrributeProperty])
                query += ",\n"
            query += ");"
            print(query)
        elif current[requiredModel] != required[requiredModel]:
            for currentModelAttribute in current[requiredModel]:
                if currentModelAttribute not in required[requiredModel]:
                    print("\t" + requiredModel + "." + currentModelAttribute + " is not longer needed (ALTER TABLE TO RM ATT?)")
                    modelToRemove.append(currentModelAttribute)
            for model in modelToRemove:
                current[requiredModel].pop(model)
            modelToRemove = []
            for requiredModelAttribute in required[requiredModel]:
                if requiredModelAttribute not in current[requiredModel]:
                    print("\t" + requiredModel + "." + requiredModelAttribute + " is needed (ALTER TABLE TO ADD ATT?)")
                    for requiredModelAtrributeProperty in required[requiredModel][requiredModelAttribute]:
                        print("\t\t" + requiredModel + "." + requiredModelAttribute + "." + requiredModelAtrributeProperty + " needs to be " + str(required[requiredModel][requiredModelAttribute][requiredModelAtrributeProperty]) + " (ADD TO ALTER TABLE)")
                elif current[requiredModel][requiredModelAttribute] != required[requiredModel][requiredModelAttribute]:
                    for currentModelAttributeProperty in current[requiredModel][requiredModelAttribute]:
                        if currentModelAttributeProperty not in required[requiredModel][requiredModelAttribute]:
                            print("\t" + requiredModel + "." + requiredModelAttribute + "." + currentModelAttributeProperty + " is no longer needed (ALTER TABLE TO RM PROPERTY?)")
                            modelToRemove.append(currentModelAttributeProperty)
                    for model in modelToRemove:
                        current[requiredModel][requiredModelAttribute].pop(model)
                    modelToRemove = []
                    for requiredModelAttributePropery in required[requiredModel][requiredModelAttribute]:
                        if requiredModelAttributePropery not in current[requiredModel][requiredModelAttribute]:
                            print("\t" + requiredModel + "." + requiredModelAttribute + "." + requiredModelAttributePropery + " is needed (ALTER TABLE TO ADD PROPERTY?)")
                        elif current[requiredModel][requiredModelAttribute][requiredModelAttributePropery] != required[requiredModel][requiredModelAttribute][requiredModelAttributePropery]:
                            print("\t" + requiredModel + "." + requiredModelAttribute + "." + requiredModelAttributePropery + " needs to become " + str(required[requiredModel][requiredModelAttribute][requiredModelAttributePropery]) + " (ALTER TABLE TO CHANGE VALUE?)")

def getSQLForAttributeProperty(key, value):
    if key is "type":
        return value + " "
    elif key is "null":
        return "" if value else "NOT NULL "
    elif key is "unique":
        return "UNIQUE " if value else ""
    elif key is "blank":
        return ""
    elif key is "max_length":
        raise Exception("HOW THE FUCK? " + key)
    else:
        raise NotImplementedError(key)

currModels = ""
currClasses = {}
reqClasses = {}

with open(sys.argv[1], 'r') as f:
    for line in f:
        if "from django.db import models" not in line:
            if "class" in line and "Meta" not in line:
                currClasses[(line.split(" ")[1].split("(")[0].strip())] = {}
            currModels += line
exec(currModels)

for theClass in currClasses:
    # A little logic from SO,
    # https://stackoverflow.com/a/9058322
    attributes = inspect.getmembers(globals()[theClass], lambda a:not(inspect.isroutine(a)))
    for a in attributes:
        if not (a[0].startswith('__') and a[0].endswith('__')) and a[0] is not "Meta":
            currClasses[theClass][a[0]] = {}
            if len(a[1].classAttrs) > 0:
                for key in a[1].classAttrs:
                    currClasses[theClass][a[0]][key] = a[1].classAttrs[key]
    del globals()[theClass]
currModels = ""

with open(sys.argv[2], 'r') as f:
    for line in f:
        if "from django.db import models" not in line:
            if "class" in line and "Meta" not in line:
                reqClasses[(line.split(" ")[1].split("(")[0].strip())] = {}
            currModels += line
exec(currModels)

for theClass in reqClasses:
    # A little logic from SO,
    # https://stackoverflow.com/a/9058322
    attributes = inspect.getmembers(globals()[theClass], lambda a:not(inspect.isroutine(a)))
    for a in attributes:
        if not (a[0].startswith('__') and a[0].endswith('__')) and a[0] is not "Meta":
            reqClasses[theClass][a[0]] = {}
            if len(a[1].classAttrs) > 0:
                for key in a[1].classAttrs:
                    reqClasses[theClass][a[0]][key] = a[1].classAttrs[key]
    del globals()[theClass]

modelCompare(currClasses, reqClasses)

# ...It is
