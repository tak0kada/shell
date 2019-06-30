from pathlib import Path
import subprocess

class ShellException(Exception):
    pass

def exec(cmd: str, timeout_s: float = 0, log: Path = None) -> None:
    cmd_org = cmd
    timeout_s = "" if timeout_s == 0 else "timeout {} ".format(timeout_s)
    cmd = "set -euxo pipefail\n" + timeout_s + cmd
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sh_msg = proc.stdout.decode('utf-8')
    print(sh_msg)

    if proc.returncode != 0:
        msg = "Execution of \"{}\" failed. \n\n {}"
        if log is None:
            raise ShellException(msg.format(timeout_s + cmd_org, sh_msg))
        else:
            with open(str(log.absolute()), "w") as f:
                f.write(msg.format(cmd_org, sh_msg))

def valueof(cmd: str, timeout_s: float = 0) -> str:
    cmd_org = cmd
    timeout_s = "" if timeout_s == 0 else "timeout {} ".format(timeout_s)
    cmd = "set -euo pipefail\n" + timeout_s + cmd
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if proc.returncode == 0:
        return proc.stdout.decode('utf-8')
    else:
        # return ""
        msg = "Execution of \"{}\" failed. \n\n {}"
        sh_msg = proc.stdout.decode('utf-8')
        raise ShellException(msg.format(timeout_s + cmd_org, sh_msg))

if __name__ == "__main__":
    exec("echo 'Hello World!'")
    val = shell_valueof("pwd")
    print(val)
