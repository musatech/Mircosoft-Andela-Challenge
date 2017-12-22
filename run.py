import os,sys, subprocess
import platform

# Is Docker Installed
is_docker_installed = False
try:
    res = subprocess.check_output(["docker"])
    is_docker_installed = True
except subprocess.CalledProcessError:
    sys.exit("Something went wrong trying to run Docker")
except OSError :
    sys.exit("Docker may not be installed")


if not is_docker_installed :
    print("Docker or Docker Compose not Installed \n")
    print("Ensure both packages are installed to Continue \n")


host_os = platform.system()

# to Start
if is_docker_installed:
    if (host_os == "Linux"):
        os.system("sudo docker-compose up")
    else:
        os.system("docker-compose up")
