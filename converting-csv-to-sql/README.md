This script will convert a csv file with multiple values to sql query

example :
--------------------------

Tom,Imphal,Men,2,0,0,2

Sia,Delhi,Women,1,0,0,30 

--------------------------
convert to :

update sn_cameras set name='Tom', location='Imphal', type='Men', fk_host=2, road_num=0, local_road_num=0 WHERE pk_name=2;
update sn_cameras set name='Sia', location='Delhi', type='Women', fk_host=1, road_num=0, local_road_num=0 WHERE pk_name=30;
