# Some would call this hacky...
import sys
import inspect
import re
from fields import models

# A little more SO
# https://stackoverflow.com/q/5903720
def modelCompare(current, required):
    modelToRemove = []
    for currentModel in current:
        if currentModel not in required:
            print("DROP TABLE " + models.modelToTableName(currentModel) + ";")
            modelToRemove.append(currentModel)
    for model in modelToRemove:
        current.pop(model)
    modelToRemove = []
    for requiredModel in required:
        if requiredModel not in current:
            query = "CREATE TABLE " + models.modelToTableName(requiredModel) + " ("
            query += "\n id SERIAL NOT NULL PRIMARY KEY,"
            for requiredModelAttribute in required[requiredModel]:
                query += "\n " + requiredModelAttribute
                for requiredModelAtrributeProperty in required[requiredModel][requiredModelAttribute]:
                    query += getSQLForAttributeProperty(requiredModelAtrributeProperty, required[requiredModel][requiredModelAttribute][requiredModelAtrributeProperty])
                query += ","
            query = list(query)
            query = query[:-1]
            query = "".join(query)
            query += "\n);"
            print(query)
        elif current[requiredModel] != required[requiredModel]:
            isAlterNeeded = False
            query = "ALTER TABLE " + models.modelToTableName(requiredModel)
            for currentModelAttribute in current[requiredModel]:
                if currentModelAttribute not in required[requiredModel]:
                    query += "\n DROP COLUMN " + currentModelAttribute + ","
                    isAlterNeeded = True
                    modelToRemove.append(currentModelAttribute)
            for model in modelToRemove:
                current[requiredModel].pop(model)
            modelToRemove = []
            for requiredModelAttribute in required[requiredModel]:
                if requiredModelAttribute not in current[requiredModel]:
                    isAlterNeeded = True
                    query += "\n ADD COLUMN " + requiredModelAttribute
                    for requiredModelAtrributeProperty in required[requiredModel][requiredModelAttribute]:
                        query += getSQLForAttributeProperty(requiredModelAtrributeProperty, required[requiredModel][requiredModelAttribute][requiredModelAtrributeProperty])
                    query += ","
                elif current[requiredModel][requiredModelAttribute] != required[requiredModel][requiredModelAttribute]:
                    for currentModelAttributeProperty in current[requiredModel][requiredModelAttribute]:
                        if currentModelAttributeProperty not in required[requiredModel][requiredModelAttribute]:
                            #A bit of a special case because postgres handles this differently
                            getSQLToRemoveProperty(requiredModel, requiredModelAttribute, currentModelAttributeProperty)
                            modelToRemove.append(currentModelAttributeProperty)
                    for model in modelToRemove:
                        current[requiredModel][requiredModelAttribute].pop(model)
                    modelToRemove = []
                    for requiredModelAttributeProperty in required[requiredModel][requiredModelAttribute]:
                        if requiredModelAttributeProperty not in current[requiredModel][requiredModelAttribute]:
                            #A bit of a special case because postgres handles this differently
                            getSQLToAddProperty(requiredModel, requiredModelAttribute, requiredModelAttributeProperty, required[requiredModel][requiredModelAttribute][requiredModelAttributeProperty])
                        elif current[requiredModel][requiredModelAttribute][requiredModelAttributeProperty] != required[requiredModel][requiredModelAttribute][requiredModelAttributeProperty]:
                            #A bit of a special case because postgres handles this differently
                            getSQLToAddProperty(requiredModel, requiredModelAttribute, requiredModelAttributeProperty, required[requiredModel][requiredModelAttribute][requiredModelAttributeProperty])
            query = list(query)
            query[-1] = ';'
            query = "".join(query)
            if isAlterNeeded:
                print(query)

def getSQLToRemoveProperty(table, attribute, property):
    if property is "blank":
        pass
    elif property is "null":
        print("ALTER TABLE " + models.modelToTableName(table) + " ALTER COLUMN " + attribute + " SET NOT NULL;")
    elif property is "unique":
        print("ALTER TABLE " + models.modelToTableName(table) + " ADD UNIQUE (" + attribute + ");")
    else:
        raise NotImplementedError(table + " > " + attribute + " > " + property)

def getSQLToAddProperty(table, attribute, property, value):
    if property is "type":
        print("ALTER TABLE " + models.modelToTableName(table) + " ALTER COLUMN " + attribute + " TYPE " + value + ";")
    elif property is "unique":
        # We need to allow values to be null, in SQL we do nothing.
        pass
    elif property is "null":
        print("ALTER TABLE " + models.modelToTableName(table) + " ALTER COLUMN " + attribute + " " + ("DROP" if value else "SET") + " NOT NULL;")
    else:
        raise NotImplementedError(table + " > " + attribute + " > " + property)

def getSQLForAttributeProperty(key, value):
    if key is "type":
        return value
    elif key is "null":
        return "" if value else " NOT NULL"
    elif key is "unique":
        return " UNIQUE" if value else ""
    elif key is "blank":
        return ""
    elif key is "pk":
        return "PRIMARY KEY"
    elif key is "max_length":
        raise Exception("max_length should be utilized by the Field constructor. A constructor has not been implemented correctly.")
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
