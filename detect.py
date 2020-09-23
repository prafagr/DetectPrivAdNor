import csv
import os
import subprocess
import time
import pmc_modify

total_elements = []

#Procmon logic
##### 
#create PML file
create_pml = subprocess.Popen(["Procmon.exe", "/Quiet", "/LoadConfig", "2.pmc", "/BackingFile", "out_pml.pml"], stdout=subprocess.PIPE, shell=True)
(out4, err4) = create_pml.communicate()

####
#terminate process
terminate_procmon = subprocess.Popen(["Procmon.exe", "/Terminate"], stdout=subprocess.PIPE, shell=True)
(out4, err4) = terminate_procmon.communicate()

####
#create csv
createcsv = subprocess.Popen('Procmon.exe /Quiet /OpenLog out_pml.pml /SaveApplyFilter /SaveAs output.csv', stdout=subprocess.PIPE, shell=True)
(out3, err3) = createcsv.communicate()


# Read CSV file
with open('output.csv') as csv_file:
 csv_reader = csv.reader(csv_file, delimiter = ',')
 line_count=0
 
 for row in csv_reader:
  if line_count == 0:
   line_count +=1
  else:
   total_elements.append(row[4])
   line_count +=1
   
# Remove duplicates   
total_elements = list(dict.fromkeys(total_elements))

out =  b'RW #user 1'

admin = b'RW #user 2'

for i in total_elements:
  return_value = subprocess.Popen(["accesschk64.exe", "/AcceptEula", "-nobanner", i], stdout=subprocess.PIPE, shell=True)
  (out2, err2) = return_value.communicate()
  result = out2.find(admin)
  if result != -1:
    result2 = out2.find(out)
    if result2 != -1:
        print("Issue found for", i)
