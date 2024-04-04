import socket
import json
import time
 
#创建 socket对象
socket_client=socket.socket()
cmds = {"command":'null',"value":0}
 
# 让 socket对象 socket_client 连接到服务端
socket_client.connect(("192.168.1.185",8888))
 
while True:
   msg=input("请输入你旋转的方向：")
   command = str(msg)
   msg=input("输入value: ")
   value = float(msg)
   cmds['command'] = command
   cmds['value'] = value
   #发送消息
   data = json.dumps(cmds)
   socket_client.send(data.encode("UTF-8"))
   if cmds["command"]=='exit':
      break
   time.sleep(cmds['value'])
socket_client.close()