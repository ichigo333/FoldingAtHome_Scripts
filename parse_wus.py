import json, time, requests, sys, os
from config import Config
from wu import Wu

def get_value(lineSplit, index, name):
    try:
        if name in lineSplit[index]:
            return lineSplit[index].split(':')[1]
    except:
        print("ERROR finding name: ", name, " at index: ", index)

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

    with open(config.inputPath, "r") as inputFile:
        lineList = inputFile.readlines()

    with open(config.outputPath, "w") as outputFile:
        for line in lineList:
            lineSplit = line.split(" ")

            wu = Wu()
            wu.project = get_value(lineSplit, 6,'project')
            wu.run = get_value(lineSplit, 7,'run')
            wu.clone = get_value(lineSplit, 8,'clone')
            wu.gen = get_value(lineSplit,9,'gen')
            wu.unit = get_value(lineSplit, 11,'unit').rstrip()
            wu.get_apiInfo(config.user)

            print(wu)
            outputFile.write(str(wu) + '\n')


if __name__ == "__main__":
    main()
