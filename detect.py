import csv
import os
import subprocess
import time
import pmc_modify

total_elements = []

#Procmon logic
##### 
#create PML file
create_pml = subprocess.Popen(["Procmon.exe", "/Quiet", "/LoadConfig", "2.pmc", "/BackingFile", "adobeup.pml"], stdout=subprocess.PIPE, shell=True)
(out4, err4) = create_pml.communicate()

####
#terminate process
terminate_procmon = subprocess.Popen(["Procmon.exe", "/Terminate"], stdout=subprocess.PIPE, shell=True)
(out4, err4) = terminate_procmon.communicate()

####
#create csv
createcsv = subprocess.Popen('Procmon.exe /Quiet /OpenLog adobeup.pml /SaveApplyFilter /SaveAs adobeup.csv', stdout=subprocess.PIPE, shell=True)
(out3, err3) = createcsv.communicate()


# Read CSV file
with open('adobeup.csv') as csv_file:
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

out =  b'desktop-epvoj7k\\test_sym'
out =  out.lower()
#print(out)

#Check access at captured file
for i in total_elements:
  return_value = subprocess.Popen(["accesschk64.exe", "/AcceptEula", "-nobanner", i], stdout=subprocess.PIPE, shell=True)
  (out2, err2) = return_value.communicate()
  out2 = out2.lower()
  result = out2.find(out)
  if result != -1:
    print("Issue found for", i)
