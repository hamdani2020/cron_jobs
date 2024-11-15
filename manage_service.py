import os
import shutil
import subprocess


# Funciton to restart a service
def restart_service(docker):
    try:
        subprocess.run(["sudo", "systemctl", "restart", docker], check=True)
        print(f"Service '{docker}' restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting service '{docker}': {e}")


# Funciton to clear the temp folder
def clear_temp_folder(cron_temp):
    try:
        shutil.rmtree(cron_temp)
        os.makedirs(cron_temp)
        print(f"Temporary folder '{cron_temp}' cleared successfully")
    except Exception as e:
        print(f"Error clearing temporary folder '{cron_temp}': {e}")


if __name__ == "__main__":
    SERVICE_NAME = "docker"
    TEMP_FOLDER = "/tmp/cron_temp"

    restart_service(SERVICE_NAME)
    clear_temp_folder(TEMP_FOLDER)
