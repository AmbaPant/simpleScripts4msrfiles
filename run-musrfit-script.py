#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from os.path import exists
from sys import argv
import subprocess
from datetime import date
import numpy as np

today = date.today()

strsample = "yoursample" 

temptmsrfile ="tempt-msrfile.msr"
fitmodel = "tf20G-" + strsample + "-myModel" #you can whatever u like

myT =     [270,   240,    220,    200,    180,    160,    140]
mytf20 =  [154887,154918, 154915, 154913, 154909, 154907, 154902]
myalpha =  ["0.87",154918, 154915, 154913, 154909, 154907, 154902]# a u like

txtmsrfile = "msrfitfiles.txt"
datfitfile = "datfitfiles.txt"

with open(txtmsrfile, "a") as f: #to collect files name in a text file for copy 
    f.write(f"{today}\n")
with open(datfitfile, "a") as f:
    f.write(f"{today}\n")

i = 0
while i < len(myT):
    sed_command = "sed -e 's/myTF20run/"+str(mytf20[i]) +"/g;" 
    sed_command +=  "s/myalphaval/"+str(myalpha[i]) +"/g' "
    sed_command += temptmsrfile + " > myTempIntermediate.msr"
    print(sed_command)

    result = subprocess.run(sed_command, shell=True, capture_output=True, text=True)

    newfilename = str(myT[i]) + "K_" + str(mytf20[i])+ "_"+ fitmodel
    print("file:",newfilename)
    
    cp_command = "cp myTempIntermediate.msr " + newfilename + ".msr"
    print(cp_command)
    result = subprocess.run(cp_command, shell=True, capture_output=True, text=True)

    run_command = "musrfit -p --timeout 0 %s" %(newfilename+".msr") #if ur musrfit run takes longer than 1 hr, --timeout 0
    print(run_command)
    result = subprocess.run(run_command, shell=True, capture_output=True, text=True)
    #run_command = "test run done"
    sleep(1)
    run_command = "musrview %s --ascii" %(newfilename+".msr") 
    print("data save ok ? --- ", run_command)
    result = subprocess.run(run_command, shell=True, capture_output=True, text=True)
    
    with open(txtmsrfile, "a") as f:
        f.write(f'"{newfilename}.msr",\n')
    with open(datfitfile, "a") as f:
        f.write(f'"{newfilename}.dat",\n')

    print(i,"==>Done.......",run_command)

    i = i + 1
print("*****All done !!*****")
