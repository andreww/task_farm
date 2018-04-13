#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to run tasks in paralle on an MPI cluster

Tasks are shell commands, which get distributed over
processes running on nodes. Run with:

    mpirun -n 3 run_tasks.py

NB: this needs python 3 for it's "subprocess" module
"""
import sys
import subprocess
import schwimmbad

tasks = ['echo "I am one" > one.txt', 
         'echo "I am two" > two.txt',
         'echo "I am 3" > three.txt']

def task_runner(task):
    cpi = subprocess.run(task, shell=True)
    return cpi.returncode

pool = schwimmbad.MPIPool()
# If we are not on master process wait
if not pool.is_master():
    pool.wait()
    sys.exit(0)

results = list(pool.map(task_runner, tasks))
print(results)
pool.close()





