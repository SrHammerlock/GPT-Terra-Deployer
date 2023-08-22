import subprocess
def init():
    path = "in/out"
    #command2 = ["terraform", "apply"]
    result = subprocess.run(["cd", path, "&&", "terraform", "init"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = subprocess.run(["cd", path, "&&", "terraform", "apply","-auto-approve"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("done")

