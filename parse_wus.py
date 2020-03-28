import json, time, requests, sys, os

def get_value(index, name):
    try:
        if name in lineSplit[index]:
            return lineSplit[index].split(':')[1]
    except:
        print("ERROR finding name: ", name, " at index: ", index)

def get_apiInfo(project, run, clone, gen, user):
    try:
        uri = f"https://api.foldingathome.org/project/{project}/run/{run}/clone/{clone}/gen/{gen}"
        response = requests.get(uri)
        wus = json.loads(response.content)
        
        for wu in wus:
            if wu.get('user') == user:
                return wu
        
        return ""
    except:
        print("ERROR: cannot get info from API")


dir_path = os.path.dirname(os.path.realpath(__file__))
configFile = open(f"{dir_path}/config.json", "r")
config = json.loads(configFile.read())

path = config.get('path')
user = config.get('user')

file = open(path, "r")
lineList = file.readlines()

project = ""

for line in lineList:
    lineSplit = line.split(" ")

    project = get_value(6,'project')
    run = get_value(7,'run')
    clone = get_value(8,'clone')
    gen = get_value(9,'gen')
    unit = get_value(11,'unit').rstrip()

    wu = get_apiInfo(project, run, clone, gen, user)
    if wu != "":
        code = wu.get('code')
        credit = wu.get('credit')
        credit_time = wu.get('credit_time')
        days = wu.get('days')
        cpuid = wu.get('cpuid')
    else:
        code = ""
        credit = ""
        credit_time = ""
        days = ""
        cpuid = ""


    print(f"{project},{run},{clone},{gen},{unit},{code},{credit},{credit_time},{days},{cpuid}")

##print("")


file.close()