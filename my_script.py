from datetime import datetime

with open("jenkins_output.log", "a") as log_file:
    log_file.write(f"[{datetime.now()}] Jenkins ran this script!\n")
