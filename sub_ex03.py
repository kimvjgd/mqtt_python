import paho.mqtt.client as mqtt
import sqlite3

con = sqlite3.connect('iot.db')
cursor = con.cursor()

def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  if rc == 0:
    client.subscribe("iot/#")
  else:
    print("연결 실패 : ", rc)

def on_message(client, userdata, msg):
  value = float(msg.payload.decode())
  (_, user, place, sensor) = msg.topic.split('/')
  sql = f'''INSERT INTO sensors(user,place,sensor,value)
            values('{user}', '{place}', '{sensor}', {value})'''
  cursor.execute(sql)
  con.commit()
  print(f"{msg.topic} {value}")
  
# 1. MQTT 클라이언트 객체 인스턴스화 
client = mqtt.Client()
# 2. 관련 이벤트에 대한 콜백 함수 등록 
client.on_connect = on_connect 
client.on_message = on_message
try :
# 3. 브로커 연결 
  client.connect("localhost")
# 4. 메시지 루프 - 이벤트 발생시 해당 콜백 함수 호출됨
  # client.loop_forever()    
  client.loop_start()
  
except Exception as err: 
  print('에러 : %s'%err)
  cursor.close()
  con.close()
  
from time import sleep

sleep(10) 

print("프로그램을 종료합니다.")