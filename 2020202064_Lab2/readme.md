#Assignment 2 of SNS - Data Link Layer Security


step1- Entered message is converted into matrix(M) form , in which each word are i range between 1-27
step2- Matrix converted in the Translated matrix using dot product with A {which is initially given}=>Encdata
step3- computed crc for the messge -> first converted into binary form after that apply crc algo (using python lib for computation of crc)
step4- translated matrix converted into string(Encdata_str) and then concatenate crc(E)=> Encdata_str+'$'+ E_str
step5- output of step 4 is seded to the receiver

At receiver end same operation are done in reverse manner ...
step6 - extract Encdata_str and E_str=E1
step7 - Encdata_str->Encdata(matrix format)
step8 - M = A^-1.Encdata 
step9 - crc(M) = E2
step10 - compare both E2 and E1 
	if both are equal then receive message are correct otherwise wrong message received.
	
How to run code::
step1: python3 Alice.py(one terminal)

step2: python3 Bob.py(In separate terminal)

step3:................
