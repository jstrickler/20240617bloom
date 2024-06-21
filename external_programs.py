import shlex
from subprocess import run, PIPE, CalledProcessError

run("hostname")

process = run("hostname", stdout=PIPE)
raw_output = process.stdout
hostname = raw_output.decode().rstrip()
print(f"{hostname = }")
print('-' * 60)

raw_command = "netstat -an"
command_words = shlex.split(raw_command)

try:
    process = run(command_words, stdout=PIPE)
except CalledProcessError as err:
    print(err)
else:
    output = process.stdout.decode()
    output_lines = output.splitlines()  # splits str on \n

    target_lines = [line for line in output_lines if "ESTAB" in line]
    for line in target_lines:
        print(line)



