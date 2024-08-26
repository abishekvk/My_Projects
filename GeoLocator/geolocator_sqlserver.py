# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:35:54 2019

@author: AVariyan
"""

from  geopy.geocoders import Nominatim
import pandas as pd
geolocator=Nominatim()user_agent="my-application")

class Geo_locator:
    def geo_locator(self,driver,servr,db,usrid,psw,tb_name):
        quoted = urllib.parse.quote_plus("DRIVER="+driver+";SERVER="+servr+";DATABASE="+db+";UID="+usrid+";PWD="+psw) 
        engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
        
        df=pd.read_excel("D:\sampledata.xlsx",index=False)
        
        df.to_sql(table="",schema='',con= engine,if_exists='append',index=False,chunksize = None)    #writing the records to table
        
        sql_command='SELECT * FROM '+tb_name
        df = pd.read_sql(sql_command, engine)                  
                
        #df.head()
        for index,row in  df.iterrows():
            address=row['Address']
            print(address)
            #str=row['Address']
            try:
                location = geolocator.geocode(address)
                print(str(location.latitude),str(location.longitude))
                engine.execute('UPDATE '+tb_name+' set Lat='+str(location.latitude)+',Long='+str(location.longitude)+'WHERE Address='+"'"+str(address)+"'")
                #print(location.latitude,location.longitude)
                #print((row[Lat], row[Long]))
            except Exception as e:
                pass
            
        #print('UPDATE Geo_data set Lan='+str(location.latitude))+',Long='+location.longitude+'WHERE Address='+address)
if __name__ == '__main__':
    driver=''
    servr=''
    db=''
    usrid=''
    psw=''
    tb_name=''
    Geo_loc = Geo_locator()
    Geo_loc.geo_locator(driver,servr,db,usrid,psw,tb_name)