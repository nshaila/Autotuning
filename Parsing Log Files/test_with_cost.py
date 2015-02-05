# The code for parsing the input file to create another file consisting all the parameter 
#value combinations and corresponding run times.


#from __future__ import print_function
import fileinput
from decimal import Decimal
import re


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def bool_to_int_str(s):
    if s == 'True':
    	return '1'
    elif s == 'False':
    	return '0'
    else:
    	return s

def parser(input_file):

    # Opening the input file
    f = open(input_file)
    l = file_len(input_file)
    #print "line no: ", l
    # Opening the output file
    #fo = open("results.txt", "w")

    # Retrieving start location from the first line of the file
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline().split(',')
    #print 'parameter names: ', n
    s = f.readline().split('],')
    final_list = []
    for x in range(0, len(s)):
    	temp = s[x].lstrip(' [').rstrip(']\n')
    	temp_list = temp.split(', ')
    	encoded_list = []
    	for element in temp_list:
    		encoded_list.append(bool_to_int_str(element))
    	#print encoded_list
    	encoded_list = map(int, encoded_list)
    	final_list.append(encoded_list)
    #print final_list[0]
    	
    #for element in s:
    #	element1 = element.split(',')
    #	print element1
    	
    	
    	#for something in element1:
    		#print something
    	#print '\n'
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    n = f.readline()
    #print n[2]
    searchObj = re.search(r'coordinate: ', n)
    s = searchObj.end()
    searchObj1 = re.search(r'perf_params:', n)
    e = searchObj1.start()
    #print s,e
    #x = 40
    print 1
    #print 'prameter indexes:', n[s+1:e-2] #gives the parameter indexes
    p =  n[s+1:e-2]
    #print p
    temp = p.lstrip(' [').rstrip(']\n')
    #print temp
    new = temp.split(',')
    list = map(int, new)
    param_list = []
    for x in range(0,len(list)):
    	param_list.append(final_list[x][list[x]])
    print param_list	
    
    #find the cost matrix
    searchObj2 = re.search(r'cost:', n)
    s = searchObj2.end()
    p = n[s+1:len(n)]
    #print n[s+1]
    #print 'costs:', p #gives the cost matrix
    
    #computation for getting the smallest run time
    temp = p.lstrip(' [').rstrip(']\n')
    #print temp
    new = temp.split(',')
    list = map(float, new)
    cost_list = []
    #print list
    #print 'minimum run time: ', min(list)
    cost_list.append(min(list))
    
    #find the line that has the values in it. and then extract the absolute values of the coordinates and minimum run time
    str = '(run'
    x = 1
    #l = fileinput.filelineno()
    #print l
    count = 1
    #for line in fileinput.input():
    #for x in range(0, l):
    for x in range(0, 10):
    	n = f.readline()
    	p = n.find(str);
    	if p == 0:
    		count = count + 1
    		print count
    		s = searchObj.end()
    		#print s
    		searchObj1 = re.search(r'perf_params:', n)
    		e = searchObj1.start()
    		#print "hi ", n[s+1:e-2]
    		temp = n[s+1:e-2].lstrip(' [').rstrip(']\n')
    		#print temp[0]
    		if temp[0] == ':' :
    			temp = n[s+2:e-2].lstrip(' [').rstrip(']\n')
    			#print temp
    		elif temp[0] == "e" :
    			temp = n[s+3:e-2].lstrip(' [').rstrip(']\n')
    			#print temp
    		elif temp[0] == 't' :
    			temp = n[s+4:e-2].lstrip(' [').rstrip(']\n')
    			#print temp
    		elif temp[0] == 'a' :
    			temp = n[s+5:e-2].lstrip(' [').rstrip(']\n')
    			#print temp
    		elif temp[0] == 'n' :
    			temp = n[s+6:e-2].lstrip(' [').rstrip(']\n')
    			#print temp
    		elif temp[0] == 'i' :
    			temp = n[s+7:e-2].lstrip(' [').rstrip(']\n')
    			#print temp
    		elif temp[0] == 'd' :
    			temp = n[s+8:e-2].lstrip(' [').rstrip(']\n')
    			#print temp
    		elif temp[0] == 'r' :
    			temp = n[s+9:e-2].lstrip(' [').rstrip(']\n')
    			#print temp
    		elif temp[0] == 'o' :
    			temp = n[s+11:e-2].lstrip(' [').rstrip(']\n')
    			#print temp
    		new_list = temp.split(',')
    		#print new_list
    		new_list = map(int, new_list)
    		param_list = []
    		for x in range(0,len(new_list)):
    			param_list.append(final_list[x][new_list[x]])
    		print param_list
    			
    		#print new_list
    		#print 'parameter indexes:', n[s+1:e-2] #gives the parameter indexes
    		searchObj2 = re.search(r'cost:', n)
    		s = searchObj2.end()
    		c = n[s+1:len(n)] #gives the cost matrix
    		#print c
    		temp = c.lstrip(' [').rstrip(']\n')
   			#print temp
    		new = temp.split(',')
    		list = map(float, new)
    		#print list
    		#print 'minimum run time: ', min(list)
    		cost_list.append(min(list))
    
    print '\n\n'
    cost_list.sort()
    print cost_list
    print '\n\ntotal run: ', len(cost_list)
    	

    
    '''
    x = 1
    for x in range(0, 19):
    
    	n = f.readline()
    	n = f.readline()
    	n = f.readline()
    	n = f.readline()
    	n = f.readline()
    	#searchObj3 = re.search(r'----- end random search -----',n)
    	print x+2
    	searchObj = re.search(r'coordinate:', n)
    	if searchObj is None:
    		n = f.readline()
    		searchObj = re.search(r'coordinate:', n)
    		s = searchObj.end()
    		searchObj1 = re.search(r'perf_params:', n)
    		e = searchObj1.start()
    		print 'prameter indexes:', n[s+1:e-2] #gives the parameter indexes
    		searchObj2 = re.search(r'cost:', n)
    		s = searchObj2.end()
    		#print 'costs:', n[s+1:len(n)] #gives the cost matrix
    	else:
    		s = searchObj.end()
    		searchObj1 = re.search(r'perf_params:', n)
    		e = searchObj1.start()
    		print 'prameter indexes:', n[s+1:e-2] #gives the parameter indexes
    		searchObj2 = re.search(r'cost:', n)
    		s = searchObj2.end()
    		#print 'costs:', n[s+1:len(n)] #gives the cost matrix
	'''
    
    
    ''' trying to create a list and put things inside that
    my_list = []
    #print my_list
    for x in range(s+1,e-2) :
    	my_list.append(n[x])
    #print my_list
    '''

    # Retrieving trial number from the second line of the file
    #s = f.readline().split()
    #trial = int(s[0])
    #print ('number of trial: ', trial, file = fo)
    #print ("\n", file = fo)
    #print trial
    f.close()
	
    #print '\n'
'''
    # Retrieving the first combination of params.
    n = f.readline()
    n_run = f.readline()
    print ('number of runs: ', n_run, file = fo)
    
    n_param = f.readline()
    print ('parameter values: ', n_param, file = fo)
    
    n = f.readline()
    s = f.readline().split(',')
    #print len(s)
    print ('minimum run time: ', float(min(s)), file = fo)
    print ("\n", file = fo)
 
 	# Retrieving all other combination of params from the rest of the file. 
    x = 1
    for x in range(0, trial-1):
    	v_line = f.readline()
    	#print v_line[0] 
    	if v_line[0] in  '=':
    		n_run = f.readline()
    		print ('number of runs: ', n_run, file = fo)

    		n_param = f.readline()
    		print ('parameter values: ', n_param, file = fo)
    
    		n = f.readline()
    		s = f.readline()
    		l = len(s) - 3
    		t = s[1:l]
    		#print 'length', l
    		p = t.split(',')
    		#p = float(min(s))
    		#print p
    		print ('minimum run time: ', float(min(p)), file = fo)
    		print ("\n", file = fo)
    
    # Retrieving the total number of combination extracted from the file.
    print ("Total number of parameter combination extracted : ", x+1+1, file = fo)
    print ("\n\n", file = fo)
		
'''
	#f.close()
    #fo.close()
   
        
'''     x = 1
    for x in range(0, trial-1):
    	v_line = f.readline()
    	#print v_line[0]
    	for v_line in '=':
    		print "We're on time %d" % (x+1)
'''    	 
    #print s[347]
    #x = s[347]
    #for x in ']':
    	#print "yey \n"
    
        	
    #goal = s.split()[0:1] #(s[1])+(s[2])+(s[3])+(s[4])+(s[5])+(s[6])+(s[7])
    #goal = (s[1])+(s[2])+(s[3])+(s[4])+(s[5])+(s[6])+(s[7])+(s[8])
    #float(goal)
    #print goal
    #print goal[0]
    
  
# This is the main function. It calls the parser function and prints the result
# in appropriate format as needed.
if __name__ == "__main__":

    # 'result' will store the output of the 'parser' function inside newfile.
    #result = parser('antdata.txt')
    result = parser('tuning2051.log')

