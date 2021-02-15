import socket 
import numpy as np
import crcmod
from crcmod.predefined import * 

word_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,' ':27}


rev_word_dict = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',
14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',27:' '}

A = [[-3,-3,-4],[0,1,1],[4,3,4]]
np_A = np.array(A)
np_A_inv = np.linalg.inv(np_A)
crc32_func = crcmod.predefined.mkCrcFun('crc-32')


host = 'local host'
port = 1234
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect(('127.0.0.1', port)) 

def Encode(msg1):
    msg1 = msg1.upper()  
    l=len(msg1)
    l1 = 0
    if l%3!=0:
    	l1 = 3-l%3
    msg1 += ' ' *l1

    f_data = msg1.encode()
    E_str =str(crc32_func(f_data))

    T_msg = []
    for i in msg1.upper():
        if i in word_dict:
            T_msg.append(word_dict[i])

    T_msg_np = np.array(T_msg).reshape(3,-1)

    Encdata = np.dot(A,T_msg_np)
    Encdata = Encdata.flatten()

    Encdata_str = ""
    for i in range(len(Encdata)-1):
        Encdata_str = Encdata_str+str(Encdata[i])+","
    Encdata_str=Encdata_str+str(Encdata[-1])

    Data = Encdata_str + '$' + E_str
    return Data

def Decode(Data):
	# print(Data)
	Encdata_str = Data.split('$')[0]
	E1_str = Data.split('$')[1]
	# print(E1_str)

	EncD= Encdata_str.split(',')

	Encdata=[]
	for i in EncD:
		Encdata.append(int(i))

	Encdata = np.array(Encdata).reshape(3,-1)
	data = np.dot(np.linalg.inv(A),Encdata)
	act_data = ''
	T_data = data.flatten()

	for i in T_data:
		if i in rev_word_dict:
			act_data = act_data + rev_word_dict[i]

	f_data1 = act_data.encode()
	E2_str =str(crc32_func(f_data1))
	# print(E2_str)

	if E1_str == E2_str:
		print("Correct message recieved !")
	else:
		print("Wrong message recieved !")

	return act_data

while True:
	msg1 = s.recv(1024)
	msg1 = msg1.decode()
	msg1= Decode(msg1)

	
	print("Alice:>>",msg1)


	msg2 = input("Bob:>>")
	msg2 = Encode(msg2)
	msg2 = msg2.encode()
	s.send(msg2)

s.close() 
