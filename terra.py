import subprocess

def terraform_run(command):
    process=subprocess.run(command ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.stdout.decode()

directory = "/mnt/c/Users/Krishna/OneDrive/Desktop/s3-python/terra-automate/Wanderlust-Mega-Project/terraform"

command = f"terraform -chdir={directory} init"
terraform_run(command)