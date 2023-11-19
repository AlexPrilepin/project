import subprocess
from subprocess import Popen, PIPE, STDOUT
def get_output(filename, info_in_test):
    cmd = f"python3 {filename}"
    namespace = {"a" : 1}
    info_in_test = list(map(str, info_in_test))
    proc = Popen(cmd.split(' '), stdout=PIPE, stderr=PIPE, stdin=PIPE, text=True)
    (output, error)  = proc.communicate(input="\n".join(info_in_test))
    result = str(output).strip("'") 
    if "\\n" in result:
        result = str(result).split("\\n")
    else:
        result = str(result).split("\n")
    if not error:
        return result[:-1]
    else:
        return str(error)


def into_file(name, text):
    with open(name, "w") as d:
        d.write(text)


def tests_operator(filename1, filename2, all_tests):
    good = True
    for i in all_tests:
        if get_output(filename1, i) != get_output(filename2, i):
            good = False
            break
    return good

