from os import system

WORK_DIR = input("Enter Work Dir(/root/work/): ")

PNAME = input("Enter Python File Name: ")

SERVICE_NAME = input("Enter Service Name: ")

with open(f"{WORK_DIR}pyrunner.sh","a+") as f:
  f.write(f"""
#!/bin/bash

echo "Script executed at $(date)" >> {WORK_DIR}log.log
cd {WORK_DIR}

# Terminate existing instances of {PNAME}
echo "Terminating existing instances of {PNAME}" >>log.log
pids=$(pgrep -f {PNAME})
if [ -n "$pids" ]; then
    echo "Existing process IDs: $pids" >>log.log
    for pid in $pids; do
        echo "Killing process $pid" >>log.log
        kill -9 "$pid"
    done
    sleep 5
    pids=$(pgrep -f {PNAME})
    echo "Remaining process IDs: $pids" >>log.log
fi

# Start {PNAME}
echo "Starting {PNAME}" >>log.log
python3 {PNAME} 
""")
  f.close()

with open(f"/etc/systemd/system/{SERVICE_NAME}.service","a+") as f:
  f.write(f"""
[Unit]
Description={PNAME} Runner Service

[Service]
User=root
WorkingDirectory={WORK_DIR}
ExecStart=/bin/bash {WORK_DIR}pyrunner.sh
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
""")
  f.close()


system(f"chmod +x {WORK_DIR}/pyrunner.sh {WORK_DIR}{PNAME}")

system("sudo systemctl daemon-reload")

system(f"sudo systemctl start {SERVICE_NAME}")

system(f"sudo systemctl status {SERVICE_NAME}")
