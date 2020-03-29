import json, time, requests, sys, os
from config import Config


def get_value(lineSplit, index, name):
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

def read_config():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    configFile = open(f"{dir_path}/config.json", "r")
    config = json.loads(configFile.read())
    
    inputPath = config.get('inputPath')
    outputPath = config.get('outputPath')
    user = config.get('user')
    
    configFile.close()
    return Config(inputPath, outputPath, user)


def main():
    config = read_config()

    file = open(config.inputPath, "r")
    lineList = file.readlines()

    project = ""

    for line in lineList:
        lineSplit = line.split(" ")

        project = get_value(lineSplit, 6,'project')
        run = get_value(lineSplit, 7,'run')
        clone = get_value(lineSplit, 8,'clone')
        gen = get_value(lineSplit,9,'gen')
        unit = get_value(lineSplit, 11,'unit').rstrip()

        wu = get_apiInfo(project, run, clone, gen, config.user)
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

    file.close()

if __name__ == "__main__":
    main()
