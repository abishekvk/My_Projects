# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:35:54 2019

@author: AVariyan
"""

from  geopy.geocoders import Nominatim
import pandas as pd
geolocator = Nominatim()
import cx_Oracle

class Geo_locator:
    def geo_locator(self,host,port,user,psw,service,tb_name,address_col_name,lat_col_name,long_col_name):
        #quoted = urllib.parse.quote_plus("DRIVER="+driver+";SERVER="+servr+";DATABASE="+db+";UID="+usrid+";PWD="+psw) 
        #engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
        
        CONN_INFO={'host': host,'port': port,'user': user,'psw': psw,'service': service}
        
        CONN_STR = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)
        try:
            
            conn = cx_Oracle.connect(CONN_STR)
        except Exception as e:
            print(str(e))
        cur=conn.cursor()     
        sql_command='SELECT * FROM '+tb_name
        try:
            
            df = pd.read_sql(sql_command, cur)       
        except Exception as ex:
            print(str(ex))
        #res=cur.execute(sql_command)
        #df = DataFrame(resoverall.fetchall())           
                
        #df.head()
        for index,row in  df.iterrows():
            address=row[address_col_name]
            print(address)
            #str=row['Address']
            try:
                location = geolocator.geocode(address)
                statement = 'UPDATE '+tb_name+' set'+ lat_col_name + '=' + str(location.latitude)+ long_col_name + '=' +str(location.longitude)+'WHERE Address='+"'"+str(address)+"'"
                curs.execute(statement)
                connection.commit
                #engine.execute('UPDATE '+tb_name+' set Lat='+str(location.latitude)+',Long='+str(location.longitude)+'WHERE Address='+"'"+str(address)+"'")
                #print(location.latitude,location.longitude)
                #print((row[Lat], row[Long]))
            except Exception as e:
                pass
            
        #print('UPDATE Geo_data set Lan='+str(location.latitude))+',Long='+location.longitude+'WHERE Address='+address)
if __name__ == '__main__':
    host=''             #server or host
    port=''             #port number
    user=''             #user name
    psw=''              #password
    service=''          #GIVE SERVICE NAME OR SID
    tb_name=''          #TABLE NAME
    address_col_name=''  #column name which contains the address
    lat_col_name= ''           #column name which contains latitude
    long_col_name= ''         #column name which contains Longitude
    Geo_loc = Geo_locator()
    Geo_loc.geo_locator(host,port,user,psw,service,tb_name,address_col_name,lat_col_name,long_col_name)