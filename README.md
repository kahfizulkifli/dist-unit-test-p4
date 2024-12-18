# dist-unit-test-p4

This repository contains the artifact for the CS 7457 Advanced Networks Fall '24 paper 

# Notes

The artifact is provided in a [google drive link](https://drive.google.com/file/d/12VTOjS7Fdpz4fKeWhoABzrZEVqou6Xz3/view?usp=sharing) in a VM. From here onwards, all experiments will be run in the VM to ease running the experiments. Download the zip file and unzip it. You should get a zip file called dist-unit-test-p4.zip and it will unzip to a "Open Virtualization Format Archive" file type.

# Starting the VM

Run the VM using virtualbox. When you reached the home screen, choose the P4 profile (not the "vagrant") and type in the password: "p4"

# Code Organization

In the /home/p4 folder, here are the folders you need to pay attention to

1. hadoop: this is the Hadoop software system, cloned and already built from [https://github.com/apache/hadoop](https://github.com/apache/hadoop). This folder contains the software system and the unit tests we will run on the hadoop-hdfs project. We don't include it in the github repo because it is a huge repository.
2. tutorials: this is from the [https://github.com/p4lang/tutorials](https://github.com/p4lang/tutorials) repository. All experiments will be run in this folder since this repository gives a general extensible guideline on creating new modules with P4. In this repo, we attach the 3 experiments in each folder and the utils. This repository stores the essential scripts required.

# Experiments

## Single device unit test
```
cd /home/p4/tutorials/exercises/simple_unit_test_state
time python3 single_device_unit_test.py
```
## Distributed unit test
```
cd /home/p4/tutorials/exercises/simple_unit_test_state
make run
# Inside the mininet CLI
xterm h1 h2 h3 h4 h5
# There should be 5 terminals
# In Node: h5 xterm, run controller
python3 end_host_controller.py
# In the other nodes (h1, h2, h3, h4), run the unit test process
time python3 unit_test_process.py
```
## P4 Distributed unit test
```
cd /home/p4/tutorials/exercises/simple_unit_test_state_end_host
make run
# In the mininet CLI
xterm h1 h2 h3 h4
# There should be 4 terminals
# In each terminal, run the unit process
time python3 unit_test_process.py
```

# Acknowledgements
We appreciate the tutorials and documentation provided by the P4-lang team

# Contact

Please contact us if you have any questions:
* Dimas Parikesit (vqx2dc@virginia.edu)
* Kahfi Zulkifli (kwf3wv@virginia.edu)
