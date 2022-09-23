import os.path
import json


def quitRequest(quit):
    output = {}
    if(quit):
        output["output"] = "Quit the Game"
    else:
        output["output"] = "You cannot quit the Game"
    return json.dumps(output)


def outputFile(result):
    directory = './results/'
    filename = "output.py"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)

    file = open(file_path, "w")
    file.write(quitRequest(result))
    file.close()


outputFile(result=False)
