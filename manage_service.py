import os
import subprocess
import shutil

# Funciton to restart a service
def restart_service(hamdani_gandi):
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', hamdani_gandi], check=True)
        print(f"Service '{hamdani_gandi}' restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting service '{hamdani_gandi}': {e}")

# Funciton to clear the temp folder
def clear_temp_folder(cron_temp):
    try:
        shutil.rmtree(cron_temp)
        os.makedirs(cron_tem)
        print(f"Temporary folder '{cron_temp}' cleared successfully")
    except Exception as e:
        print(f"Error clearing temporary folder '{cron_temp}': {e}")


if __name__ == "__main__":
    SERVICE_NAME = "hamdani_gandi"
    TEMP_FOLDER = "/tmp/cron_temp"


    restart_service(SERVICE_NAME)
    clear_temp_folder(TEMP_FOLDER)
