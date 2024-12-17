# dist-unit-test-p4

This repository contains the artifact for the CS 7457 Advanced Networks Fall '24 paper 

# Notes

The artifact is provided in a Zenodo link in a VM. From here onwars, all experiments will be run in the VM to ease running the experiments

# Starting the VM

Run the VM using virtualbox. When you reached the home screen, choose the P4 profile (not the "vagrant") and type in the password: "p4"

# Code Organization

In the /home/p4 folder, here are the folders you need to pay attention to

1. hadoop: this is the Hadoop software system, cloned and already built from [https://github.com/apache/hadoop](https://github.com/apache/hadoop). This folder contains the software system and the unit tests we will run on the hadoop-hdfs project
2. tutorials: this is from the [https://github.com/p4lang/tutorials](https://github.com/p4lang/tutorials) repository. All experiments will be run in this folder since this repository gives a general extensible guideline on creating new modules with P4.

# Experiments

## Single device unit test
## Distributed unit test
## P4 Distributed unit test
