import os
import subprocess

# commands to run simultaneously
command1 = ['python3', 'Bill_example.py']
command2 = ['python3', 'DJ_example.py']
command3 = ['python3', 'proximity_sensor_example.py']


# Execute script
process1 = subprocess.Popen(command1, preexec_fn=os.setpgrp)


# Execute script 2
process2 = subprocess.Popen(command2, preexec_fn=os.setpgrp)

# Execute script 3
process2 = subprocess.Popen(command3, preexec_fn=os.setpgrp)

# Wait for both processess to complete
process1.wait()
process2.wait()
process3.wait()


print("All scripts executed successfully")
