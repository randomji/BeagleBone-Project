import csv
import re
import os


x = 0
num = 1
MAClist = []
scan = []
allscan = []
allpower = []
scanlist = []


def csv2blob(filename):
	with open(filename,'rb') as f:
		z = f.read()

	# Split into two parts: stations (APs) and clients

	parts = z.split('\r\n\r\n')
    	stations = parts[0]
	clients = parts[1]
	import sys
	if sys.version_info[0] < 3:
		from StringIO import StringIO
	else:
		from io import StringIO

	stations_str = StringIO(stations)
	clients_str  = StringIO(clients)

	r = csv.reader(stations_str)
	i = list(r)
	z = [k for k in i if k <> []]

	stations_list = z

	r = csv.reader(clients_str)
	i = list(r)
	z = [k for k in i if k <> []]

	clients_list = z
    
	return stations_list, clients_list


while True:
	fout=open("parsed.csv","at")
	if num < 10:
		csvfile = "/root/aircrack-captures/MonitorMode-0"+str(num)+".csv"
		if os.path.exists(csvfile) == True:
			if os.path.getsize(csvfile) > 0:            
				stations_list, clients_list = csv2blob(csvfile)
				nclients = len(clients_list)
				clhead = clients_list[0]
				clients_head = [j.strip() for j in clhead]
				clients_data = [clients_list[i] for i in range(1,nclients)]
			
				#print "Scan"+" "+str(x)+"/"+"File"+" "+str(num)+":"

				for i,row in enumerate(clients_data):
					c_mac_ix = clients_head.index('Station MAC')
					c_pow_ix = clients_head.index('Power')
					c_mac = row[c_mac_ix].strip()
					c_pow = row[c_pow_ix].strip()
					if c_mac=='(not associated)':
						continue
					mac_prefix = c_mac[0:8]
				
					if c_mac in MAClist:
						pass
					else:
						MAClist.append(c_mac)

					tuple = (c_mac, c_pow)
					#print tuple
					scan.append(tuple)
			
				#print '\n'
				allscan.append(scan)
				scan = []
				num+=1
				x+=1
			else:
				scan = []
				allscan.append(scan)
				scan = []
				num+=1
		else:
			break

	elif num > 9:
		csvfile = "/root/aircrack-captures/MonitorMode-"+str(num)+".csv"
		if os.path.exists(csvfile) == True:
			if os.path.getsize(csvfile) > 0:            
				stations_list, clients_list = csv2blob(csvfile)
				nclients = len(clients_list)
				clhead = clients_list[0]
				clients_head = [j.strip() for j in clhead]
				clients_data = [clients_list[i] for i in range(1,nclients)]

				#print "Scan"+" "+str(x)+"/"+"File"+" "+str(num)+":"

				for i,row in enumerate(clients_data):
					c_mac_ix = clients_head.index('Station MAC')
					c_pow_ix = clients_head.index('Power')
					c_mac = row[c_mac_ix].strip()
					c_pow = row[c_pow_ix].strip()
					if c_mac=='(not associated)':
						continue
					mac_prefix = c_mac[0:8]
	
                			if c_mac in MAClist:
						pass						
					else:
						MAClist.append(c_mac)

					tuple = (c_mac, c_pow)
					#print tuple
					scan.append(tuple)
			
				#print '\n'
				allscan.append(scan)
				scan = []
				num+=1
				x+=1

			else:
				scan = []
				allscan.append(scan)
				scan = []
				num+=1	
		else:
			break


numscan = len(allscan)
numMAC = len(MAClist)
powerlist = []
i = 0


for i in range(0,numscan):
	#print "Scan"+str(i)+":"
	#print "\n"
	j = 0
	scanpower = [0] * numMAC
	for mac in MAClist:
		#print "Checking :", mac
		#print "\n"
		for tuple in allscan[i]:	
			#print tuple
			if mac == tuple[0]:
				scanpower[j] = tuple[1]
				#print scanpower
		j+=1
		#print "\n"
	powerlist.append(scanpower)


with open('output.csv' , 'w') as csvoutput:
	writer = csv.writer(csvoutput, delimiter=',')
	header = []
	header.append("Station MAC")
	for i in range(0, numscan):
		i+=1
		length = "Scan"+str(i)
		#print length
		header.append(length)
	writer.writerow(header)
	
	for j in range(0,numMAC):
		data = []
		MAC = str(MAClist[j])
		data.append(MAC)
		for i in range(0,numscan):
			PWR = str(powerlist[i][j])
			data.append(PWR)
		writer.writerow(data)
		


		
		
		
