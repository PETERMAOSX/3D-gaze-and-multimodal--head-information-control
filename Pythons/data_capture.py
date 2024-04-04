import socket
import threading
import time
import json
import pandas as pd
import datetime
count = 10
# df_dict = {
#     "Count":[],
#     "realx":[],
#     "realy":[],
#     "EyeX":[],
#     "EyeY":[],
#     "HeadPosX":[],
#     "HeadPosY":[],
#     "HeadPosZ":[]
# }
# df_dict = {
#     "time":[],
#     "EyeX":[],
#     "EyeY":[],
#     "HeadPosY":[],
#     "EMG1":[],
#     "EMG2":[]
# }
df_dict = {
    "time":[],
    "EyeX":[],
    "EyeY":[],
    "HeadPosY":[]
}

def on_connection(client_executor,addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:
        msg = client_executor.recv(1024).decode('utf-8')
        #print(msg)
        if msg == "end":
            df = pd.DataFrame.from_dict(df_dict)
            df.to_csv('SingleModule/DemoCSV_{0}.csv'.format(count),encoding='utf-8',index=False,header=True)
            break
        else:  
            try:
                server_reply = json.loads(msg)
            except:
                print("Swith Faild")
                continue
            df_dict['time'].append(datetime.datetime.now())
            eye_x = server_reply["EyeX"]
            df_dict["EyeX"].append(eye_x)
            eye_y = server_reply["EyeY"]
            df_dict["EyeY"].append(eye_y)
            HY = server_reply["HeadPosY"]
            df_dict["HeadPosY"].append(HY)
            # EMG1 = server_reply["EMG1"]
            # df_dict["EMG1"].append(EMG1)
            # EMG2 = server_reply["EMG2"]
            # df_dict["EMG2"].append(EMG2)
            print("Infomation :"+"Count: "+str(count)+"("+str(eye_x)+" : "+str(eye_y)+")"+" Head Pose :("
            ":"+str(HY)+")")
            

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.bind(('127.0.0.1',9999))
listener.listen(1)
print('Server is Opening, Wait For Connect ...')

client_executor,addr = listener.accept()
t = threading.Thread(target=on_connection,args=(client_executor,addr))
t.start()
print("BEGIN.... - :P")