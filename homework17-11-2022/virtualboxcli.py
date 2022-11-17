import virtualbox;
import sys 
 
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
