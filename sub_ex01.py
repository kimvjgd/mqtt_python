import paho.mqtt.client as mqtt

# 브로커 접속 시도 결과 처리 콜백함수
def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  if rc == 0:
    client.subscribe("iot/#")
  else:
    print("연결 실패 : ", rc)

# 관련 토픽 메시지 수신 콜백 함수
def on_message(client, userdata, msg):
  value = float(msg.payload.decode())
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
  # client.loop_forever()    밑의 print("프로그램을 종료합니다.")가 실행되지 않고 꺼진다.
  # client.loop_start() 이렇게만 추가하면 바로 꺼진다.       
  client.loop_start()    # 새로운 thread 실행 --> daemon 스레드로 default되어있다. -> Main thread 종료시에 강제 종료된다.
  
  
except Exception as err: 
  print('에러 : %s'%err)
  
from time import sleep

sleep(10)       # 10초간 대기   -> 메인쓰레드가 60초간 정지가 된다.   => 그러면 새로 만들어진 mqtt thread는 유지가 되는것이다.

print("프로그램을 종료합니다.")