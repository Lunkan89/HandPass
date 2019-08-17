import os
import csv


def dis(A,B):
	return pow(pow(A[0]-B[0],2)+pow(A[1]-B[1],2),0.5)






def disratio(A):
	a=max(A)
	b=[]
	for c in A:
		c=c/a
		b.append(c)
	return b



def save_password(A,distance_bw_point_tuple,fs):
	path=os.getcwd()
	f=open(path+os.sep+fs,'w')
	for i in distance_bw_point_tuple:
		f.write(str(i[0])+">"+str(i[1]) +",")
	f.write("\n")
	for j in A:
		len_tuple=len(distance_bw_point_tuple) -1
		for i in range(0,len_tuple):
			f.write(str(j[i])+",")
		f.write("\n")
	f.close()

def create_list_distance(A,fs):
	#this is the array of set of two points where we want to check the distance
	distance_bw_point_tuple=((0,1),(0,5),(0,9),(0,13),(0,17),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19),(19,20),(1,5),(5,9),(9,13),(13,17),(2,6),(6,10),(10,14),(14,18),(3,7),(7,11),(11,15),(15,19),(4,8),(8,12),(12,16),(16,20))

	#this is empty where i will store distance b/w pair of points in distance_bw_points_tupe
	list_dist=[]
	for j in A:
		dist=[]
		for i in distance_bw_point_tuple:
			if (j[i[0]] is not None) & (j[i[1]] is not None):
				dist.append(dis(j[i[0]],j[i[1]]))
			else:
				dist.append(0)
		dist=disratio(dist)
		list_dist.append(dist)
	save_password(list_dist,distance_bw_point_tuple,fs)

def compare_hand(csv1,csv2):
	system_password=[]
	entered_password=[]
	f=open(csv1,'r')
	r=csv.reader(f)
	flag=0
	for line in r:
		if(flag==0):
			flag=1
			continue
		system_password.append(line)
	f.close()
	flag=0
	f=open(csv2,'r')
	r=csv.reader(f)
	for line in r:
		if(flag==0):
			flag=1
			continue
		entered_password.append(line)
	f.close()
	entered_password_length=len(entered_password)
	system_password_length=len(system_password)
	if entered_password_length == system_password_length or 1:
		fm=0
		for pwdl in range(min(entered_password_length,system_password_length)):
			fnm=0
			en_pwd_frame_len=len(entered_password[pwdl])-1
			sys_pwd_frame_len=len(system_password[pwdl])-1
			if en_pwd_frame_len==sys_pwd_frame_len:
				exact_match=0
				score=0
				match20=0
				match40=0
				match50=0
				totally_diffenent=0
				path=os.getcwd()
				for i in range(en_pwd_frame_len):
					diff=float(entered_password[pwdl][i])-float(system_password[pwdl][i])
					if diff==0:
						error_perc=0
						exact_match=exact_match+1
						score=score+1
					elif float(system_password[pwdl][i])!=0.0:
						error_perc=abs(diff)/float(system_password[pwdl][i])*100
						if error_perc<20:
							match20=match20+1
							if error_perc<10:
								score=score+1
							else:
								score=score+0.9
						elif error_perc<40:
							match40=match40+1
							if error_perc<30:
								score=score+0.8
							else:
								score=score+0.7
						else:
							match50=match50+1
							score=score+0.2
					else:
						error_perc=100
						totally_diffenent=totally_diffenent+1
						score=0


				#print("totally matched points = "+str(exact_match)+"\nless than 20% ="+str(match20)+"\n less than 40% ="+str(match40)+"\nmore than 40 % ="+str(match50)+"\nnot matched ="+str(totally_diffenent))
				fm=fm+score
				#print(fm)

				if score>33:
					fm+=10
					#print("\nhand matched with score"+str(score))
				
					#print("\n hand not matched score"+str(score))

		perc=(fm)/(39*(min(entered_password_length,system_password_length)))
		perc*=100
		print("\n percentage :"+str(perc))
		if perc>75:
			print("passed")
		else:
			print("failed")
