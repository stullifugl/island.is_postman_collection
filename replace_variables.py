import os
import shutil

COLLECTION_FOLDER = "collections_created"
FILEENDING = "_auth_postman_collection.json"

DICTLIST = [
    {
        "key": "--collection_name_here--",
        "reference": "collection_name"
    },
    {
        "key": "--ids_url_here--",
        "reference": "url"
    },
    {
        "key": "--ids_redirect_url_here--",
        "reference": "redirect_url"
    },
    {
        "key": "--ids_client_id_here--",
        "reference": "client_id"
    },
    {
        "key": "--ids_client_secret_here--",
        "reference": "client_secret"
    }
]

def getLineList(path = "island.is_auth_system.postman_collection.json"):
    lineList = []
    f = open(path, "r")
    for line in f:
        lineList.append(line)

    return lineList

def getReferenceValue(reference):
    f = open("variables.txt", "r")
    for line in f:
        if (reference in line):
            wordList = line.split(": ")
            if len(wordList) == 2:
                return wordList[1].strip()
            break

    return "__value-not-found__"

def setupFolder():
    if os.path.exists(COLLECTION_FOLDER):
        shutil.rmtree(COLLECTION_FOLDER)
    os.mkdir(COLLECTION_FOLDER)

def replaceWordInLineList(lineList, dict):
    for x in range(0, len(lineList)):
        if dict["key"] in lineList[x]:
            lineList[x] = lineList[x].replace(dict["key"], getReferenceValue(dict["reference"]))

    return lineList

def createCollectionFromSettings():
    lineList = getLineList()

    for dict in DICTLIST:
        lineList = replaceWordInLineList(lineList, dict)

    fileName = getReferenceValue("client_name") + "_auth_postman_collection.json"

    f = open(COLLECTION_FOLDER + "/" + fileName, "w+")
    for line in lineList:
        f.write(line)


def main():
    setupFolder()
    createCollectionFromSettings()

main()