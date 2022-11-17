import virtualbox;

import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
vbox = virtualbox.VirtualBox()

if( sys.argv[1] == "list"):
  print([m.name for m in vbox.machines])
elif sys.argv[1] == "create":
  m = vbox.create_machine("",sys.argv[2],['/test'],"Linux",'forceOverwrite=0')
  vbox.register_machine(m)
elif sys.argv[1] == "delete":
  vm = vbox.find_machine(sys.argv[2])
  vm.remove(delete=True)
elif sys.argv[1] == "standUp":
  session = virtualbox.Session()
  machine = vbox.find_machine(sys.argv[2])
  progress = machine.launch_vm_process(session, "gui", [])
  progress.wait_for_completion()
  print("session status: " +str(session.state))
  print("machine status: " +str(machine.state))


print("end");
"""session = virtualbox.Session()
session = virtualbox.Session()
machine = vbox.find_machine("UBUNTU2004_default_1668471086686_97993")
#progress = machine.launch_vm_process(session, "gui", "")
#>>> # For virtualbox API 6_1 and above (VirtualBox 6.1.2+), use the following:
progress = machine.launch_vm_process(session, "gui", [])
progress.wait_for_completion()

filename = vbox.compose_machine_filename('addmachine','/test','','E:\virtualbox')

m = vbox.create_machine(filename,"testCreate",['/test'],"Linux",'forceOverwrite=0')
vbox.registerMachine(m)
E:\virtualbox

m = vbox.createMachine(_arg_settingsFile='',
                                   _arg_name="testCreate",
                                   _arg_groups=['/test'],
                                   _arg_osTypeId="Linux",
                                   _arg_flags='forceOverwrite=0')
vbox.registerMachine(m)"""