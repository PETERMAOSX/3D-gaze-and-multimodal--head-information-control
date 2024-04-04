import time
import cv2
from robomaster import robot
import socket
import json
from threading import Thread
import os
import sys
import arm_control as arm
arm_cc = arm.Arm_control()
x = 0
y = 0

class Car:
    def __init__(self,x_val,y_val,z_angel_val,mode) -> None:
        self.x_val = x_val
        self.y_val = y_val
        self.z_angel_val = z_angel_val
        self.car = robot.Robot()
        self.car.initialize(conn_type='sta')
        self.car_transform = self.car.chassis
        self.ep_camera = self.car.camera
        self.car_gripper = self.car.gripper
        self.car_servo = self.car.servo
        self.car_arm = self.car.robotic_arm
        self.eye_x = 0
        self.eye_y = 0
        self.mode = mode
        self.count = 0
        self.moveOnce = True

        #self.show_camera()
    
    def show_camera_1(self):
        self.car_camera.start_video_stream(display=False)
        while True:
            img = self.car_camera.read_cv2_image()
            cv2.imshow("Robot", img)
            c = cv2.waitKey(1) #判断退出的条件 当按下'Q'键的时候呢，就退出
            if c == ord('q'):
                break
        cv2.destroyAllWindows()
        self.car_camera.stop_video_stream()


    
    def run_forward(self):
        self.car_transform.drive_speed(x=self.x_val, y=0, z=0, timeout=5)
        
    
   

    def run_back(self):
        self.car_transform.drive_speed(x=-self.x_val,y=0,z=0,timeout=5)
        

    def run_left(self):
        self.car_transform.drive_speed(x=0,y=-self.y_val,timeout=5)
        

    def run_right(self):
        self.car_transform.drive_speed(x=0,y=self.y_val,timeout=5)
        

    def run_left_rotate(self):
        self.car_transform.drive_speed(x=0,y=0,z=-self.z_angel_val,timeout=0)
        
    
    def run_right_rotate(self):
        self.car_transform.drive_speed(x=0,y=0,z=self.z_angel_val,timeout=0)
    
    def run_left_rotate_back(self):
        self.car_transform.drive_speed(x=0,y=0,z=self.z_angel_val,timeout=0)
        
    
    def run_right_rotate_back(self):
        self.car_transform.drive_speed(x=0,y=0,z=-self.z_angel_val,timeout=0)
        
    def run_stop(self):
        self.car_transform.drive_speed(x=0, y=0, z=0, timeout=5)
    
    #斜方向
    def run_right_xie(self):
        self.car_transform.drive_speed(x=self.x_val,y=self.y_val,z=0,timeout=5)
    
    def run_left_hou_xie(self):
        self.car_transform.drive_speed(x=-self.x_val,y=-self.y_val,z=0,timeout=5)
        
    def run_left_xie(self):
        self.car_transform.drive_speed(x=self.x_val,y=-self.y_val,z=0,timeout=5)
       
    def run_right_hou_xie(self):
        self.car_transform.drive_speed(x=-self.x_val,y=self.y_val,z=0,timeout=5)
    
    #机械臂
    def arm_up(self):
        self.car_arm.move(0,10)
        
       

    def arm_down(self):
        self.car_arm.move(0,-10)
        
    

    def arm_forward(self):
        self.car_arm.move(10,0)
        
            

    def arm_back(self):
        self.car_arm.move(-10,0)
        
            

    #机械爪
    def open_gripper(self):
        self.car_gripper.open(power=50)
        
        self.car_gripper.pause()
    
    def close_gripper(self):
        self.car_gripper.close(power=50)
        
        self.car_gripper.pause()
    def windows_split(self,x,y):
        if (x > 0 and y >0) and (x < 640 and y < 310):
            return 1
        elif (x > 640 and y > 0) and (x < 1280 and y < 310):
            return 2
        elif (x > 1280 and y > 0) and (x < 1920 and y < 310):
            return 3
        elif (x > 0 and y > 310) and (x < 640 and y < 620):
            return 4
        elif (x > 640 and y > 310) and (x < 1280 and y < 620):
            return 5
        elif (x > 1280 and y > 310) and (x < 1920 and y < 620):
            return 6
        elif (x > 0 and y > 620) and (x < 640 and y < 930):
            return 7
        elif (x > 640 and y > 620) and (x < 1280 and y < 930):
            return 8
        elif (x > 1280 and y > 620) and (x < 1920 and y < 930):
            return 9
        elif (x > 0 and y > 930) and (x <640 and y < 1080):
            return 10
        elif (x > 640 and y > 930) and (x < 1280 and y < 1080):
            return 11
        elif (x > 1280 and y > 930) and (x < 1920 and y < 1080):
            return 12
    
    def arm_judge(self,x,y):
        if (x > 0 and y >0) and (x < 640 and y < 310):
            return 1
        elif (x > 640 and y > 0) and (x < 1280 and y < 310):
            return 2
        elif (x > 1280 and y > 0) and (x < 1920 and y < 310):
            return 3
        elif (x > 0 and y > 310) and (x < 640 and y < 620):
            return 4
        elif (x > 640 and y > 310) and (x < 1280 and y < 620):
            return 5
        elif (x > 1280 and y > 310) and (x < 1920 and y < 620):
            return 6
        elif (x > 0 and y > 620) and (x < 640 and y < 930):
            return 7
        elif (x > 640 and y > 620) and (x < 1280 and y < 930):
            return 8
        elif (x > 1280 and y > 620) and (x < 1920 and y < 930):
            return 9
        elif (x > 0 and y > 930) and (x <640 and y < 1080):
            return 10
        elif (x > 640 and y > 930) and (x < 1280 and y < 1080):
            return 11
        elif (x > 1280 and y > 930) and (x < 1920 and y < 1080):
            return 12
    
    def run_judge(self,x,y):
        if(x >0 and y > 0) and (x < 640 and y <232) :
            return 1
        elif(x >640 and y > 0) and (x < 1280 and y <232) :
            return 2
        elif(x >1280 and y > 0) and (x < 1920 and y <232) :
            return 3
        elif(x >0 and y > 232) and (x < 640 and y <465) :
            return 4
        elif(x >1280 and y > 232) and (x < 1920 and y <465) :
            return 5
        elif(x >0 and y > 465) and (x < 640 and y <697) :
            return 6
        elif(x >1280 and y > 465) and (x < 1920 and y <697) :
            return 7
        elif(x >0 and y > 697) and (x < 640 and y < 930):
            return 8
        elif(x > 640 and y > 697) and ( x < 1280 and y < 930):
            return 9
        elif(x > 1280 and y > 697) and ( x < 1920 and y < 930):
            return 10
        elif(x > 0 and y > 930) and ( x < 640 and y < 1080):
            return 11
        elif(x > 1280 and y > 930) and(x < 1920 and y < 1080):
            return 12
        elif(x > 640 and y > 232) and ( x < 1280 and y < 697):
            return 13
        else:
            pass
    
    def run_judge_mutil(self,x,y):
        if(x >0 and y > 0) and (x < 200 and y <1080) :
            return 1
        elif(x > 200 and y > 0) and (x < 1700 and y < 1080):
            return 2
        elif(x > 1700 and y > 0) and (x < 1920 and y < 1080):
            return 3
        else:
            pass    
        

    def get_eye_data_thread(self):
        ip_port = ('127.0.0.1', 6555)
        s = socket.socket()     # 创建套接字
        s.connect(ip_port)      # 连接服务
        while True:     # 通过一个死循环不断接收用户输入，并发送给服务器
            s.sendall('values'.encode())
            server_reply = s.recv(4096).decode()
            
            try:
                server_reply = json.loads(server_reply)
            except:
                #print("出现了格式错误")
                continue
            # if server_reply["values"]["frame"]["avg"]["x"] == 0 or server_reply["values"]["frame"]["avg"]["y"] == 0:
            #     continue

            # print(server_reply["values"]["frame"]["avg"]['x'])
            self.eye_x = server_reply["values"]["frame"]["avg"]['x']
            self.eye_y = server_reply["values"]["frame"]["avg"]['y']
            #print(self.eye_x,' : ',self.eye_y)

    def use_eye_data_thread(self):
        # global x
        # global y
        # self.eye_x = x
        # self.eye_y = y
        while True:
            if self.mode == 1:
                self.count += 1
                if self.count % 10 == 0:
                    #print(self.run_judge(self.eye_x,self.eye_y))
                    if(self.run_judge(self.eye_x,self.eye_y) == 1):
                        self.run_left_xie()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 2):
                        self.run_forward()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 3):
                        self.run_right_xie()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 4):
                        self.run_left_rotate()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 5):
                        self.run_right_rotate()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 6):
                        self.run_left()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 7):
                        self.run_right()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 8):
                        self.run_left_hou_xie()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 9):
                        self.run_back()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 10):
                        self.run_right_hou_xie()
                    elif(self.run_judge(self.eye_x,self.eye_y) == 11):
                        pass
                    elif(self.run_judge(self.eye_x,self.eye_y) == 12):
                        pass
                    elif(self.run_judge(self.eye_x,self.eye_y) == 13):
                        self.run_stop()
                    else:
                        pass
                elif self.count > 200:
                    self.count = 0
                else:
                    pass
            elif self.mode == 2:
                #开启机械臂模式
                self.count += 1
                if self.count % 10 == 0:
                    if(self.arm_judge(self.eye_x,self.eye_y) == 1):
                        self.arm_up()
                        print("11111")
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 2):
                        self.arm_forward()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 3):
                        self.open_gripper()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 4):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 5):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 6):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 7):
                        self.arm_down()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 8):
                        self.arm_back()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 9):
                        self.close_gripper()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 10):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 11):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 12):
                        pass
                    else:
                        pass
                elif self.count > 200:
                    self.count = 0
                else:
                    pass
            else:
                pass
    
    def use_eye_data_thread_mutil(self):
        # global x
        # global y
        # self.eye_x = x
        # self.eye_y = y
        while True:
            if self.mode == 1:
                self.count += 1
                if self.count % 10 == 0:
                    #print(self.run_judge(self.eye_x,self.eye_y))
                    if(self.run_judge_mutil(self.eye_x,self.eye_y) == 1):
                        self.run_left_rotate()
                    elif(self.run_judge_mutil(self.eye_x,self.eye_y) == 2):
                        self.run_stop()
                    elif(self.run_judge_mutil(self.eye_x,self.eye_y) == 3):
                        self.run_right_rotate()
                    else:
                        pass
                elif self.count > 200:
                    self.count = 0
                else:
                    pass
            elif self.mode == 2:
                #开启机械臂模式
                self.count += 1
                if self.count % 10 == 0:
                    if(self.arm_judge(self.eye_x,self.eye_y) == 1):
                        self.arm_up()
                        print("11111")
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 2):
                        self.arm_forward()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 3):
                        self.open_gripper()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 4):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 5):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 6):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 7):
                        self.arm_down()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 8):
                        self.arm_back()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 9):
                        self.close_gripper()
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 10):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 11):
                        pass
                    elif(self.arm_judge(self.eye_x,self.eye_y) == 12):
                        pass
                    else:
                        pass
                elif self.count > 200:
                    self.count = 0
                else:
                    pass
            else:
                pass
        
    def arm_eye_data_thread(self):
        # global x
        # global y
        # self.eye_x = x
        # self.eye_y = y
        while True:
            #开启机械臂模式
            self.count += 1
            if self.count % 10 == 0:
                if(self.arm_judge(self.eye_x,self.eye_y) == 1):
                    arm_cc.arm_up()
                    print("1")
                    time.sleep(2)
                elif(self.arm_judge(self.eye_x,self.eye_y) == 2):
                    arm_cc.arm_down()
                    print("2")
                    time.sleep(2)
                elif(self.arm_judge(self.eye_x,self.eye_y) == 3):
                    arm_cc.arm_reset()
                    print("3")
                    time.sleep(2)
                elif(self.arm_judge(self.eye_x,self.eye_y) == 4):
                    pass
                elif(self.arm_judge(self.eye_x,self.eye_y) == 5):
                    pass
                elif(self.arm_judge(self.eye_x,self.eye_y) == 6):
                    pass
                elif(self.arm_judge(self.eye_x,self.eye_y) == 7):
                    print("7")
                elif(self.arm_judge(self.eye_x,self.eye_y) == 8):
                    print("8")
                elif(self.arm_judge(self.eye_x,self.eye_y) == 9):
                    pass
                elif(self.arm_judge(self.eye_x,self.eye_y) == 10):
                    pass
                elif(self.arm_judge(self.eye_x,self.eye_y) == 11):
                    pass
                elif(self.arm_judge(self.eye_x,self.eye_y) == 12):
                    pass
                else:
                    pass
            elif self.count > 200:
                self.count = 0
            else:
                pass

    def show_camera(self):
        point_size = 8
        point_color_point = (0, 0, 255) # BGR
        thickness_point = -1 # 可以为 0 、4、8

        ptStart_1 = (0, 206)
        ptEnd_1 = (1280, 206)

        ptStart_2 = (0, 412)
        ptEnd_2 = (1280, 412)

        ptStart_3 = (0, 620)
        ptEnd_3 = (1280, 620)

        ptStart_4 = (426, 0)
        ptEnd_4 = (426, 720)

        ptStart_5 = (853, 0)
        ptEnd_5 = (853, 720)

        point_color = (0, 255, 0) # BGR
        thickness = 2
        lineType = 4

        #----------------------------
        text = 'Move Mode'
        org = (120, 670)
        fontFace = cv2.FONT_HERSHEY_COMPLEX
        fontScale = 1
        fontcolor = (0, 255, 0) # BGR
        thickness = 1 
        lineType = 4

        text2 = "Catch Mode"
        org2 = (973,670)
        # cv.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType, bottomLeftOrigin)



        # 显示200帧图传
        self.ep_camera.start_video_stream(display=False)
        while True:
            img = self.ep_camera.read_cv2_image()
            # img = cv2.resize(img, (1920,1080), interpolation=cv2.INTER_CUBIC)
            cv2.line(img, ptStart_1, ptEnd_1, point_color, thickness, lineType)
            cv2.line(img, ptStart_2, ptEnd_2, point_color, thickness, lineType)
            cv2.line(img, ptStart_3, ptEnd_3, point_color, thickness, lineType)
            cv2.line(img, ptStart_4, ptEnd_4, point_color, thickness, lineType)
            cv2.line(img, ptStart_5, ptEnd_5, point_color, thickness, lineType)
            cv2.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType)
            cv2.putText(img, text2, org2, fontFace, fontScale, fontcolor, thickness, lineType)
            cv2.circle(img, (int(self.eye_x/1.5),int(self.eye_y/1.5)), point_size, point_color_point, thickness_point)
            #print(img.shape)
            cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.namedWindow("frame", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
            cv2.resizeWindow("frame", 1920, 1080)    # 设置长和宽
            cv2.imshow("frame", img)
            c = cv2.waitKey(1) #判断退出的条件 当按下'Q'键的时候呢，就退出
            if c == ord('q'):
                self.ep_camera.stop_video_stream()
                break
            cv2.destroyAllWindows()

    def get_eye_data(self):
        ip_port = ('127.0.0.1', 6555)
        s = socket.socket()     # 创建套接字
        s.connect(ip_port)      # 连接服务器
        count = 0
        while True:    
            s.sendall('values'.encode())
            server_reply = s.recv(8192).decode()
            try:
                server_reply = json.loads(server_reply)
            except:
                print("出现了格式异常")
                self.run_stop()
                continue
            if server_reply["values"]["frame"]["avg"]["x"] == 0 or server_reply["values"]["frame"]["avg"]["y"] == 0:
                continue
            self.eye_x = server_reply["values"]["frame"]["avg"]["x"]
            self.eye_y = server_reply["values"]["frame"]["avg"]["y"]
            #print(self.eye_x)
            count += 1
            if count % 10 == 0:
                if(self.windows_split(self.eye_x,self.eye_y) == 1):
                    self.run_left_rotate()
                elif(self.windows_split(self.eye_x,self.eye_y) == 2):
                    self.run_forward()
                elif(self.windows_split(self.eye_x,self.eye_y) == 3):
                    self.run_right_rotate()
                elif(self.windows_split(self.eye_x,self.eye_y) == 4):
                    self.run_left()
                elif(self.windows_split(self.eye_x,self.eye_y) == 5):
                    self.run_stop()
                elif(self.windows_split(self.eye_x,self.eye_y) == 6):
                    self.run_right()
                elif(self.windows_split(self.eye_x,self.eye_y) == 7):
                    self.run_left_rotate_back()
                elif(self.windows_split(self.eye_x,self.eye_y) == 8):
                    self.run_back()
                elif(self.windows_split(self.eye_x,self.eye_y) == 9):
                    self.run_right_rotate_back()
                elif(self.windows_split(self.eye_x,self.eye_y) == 10):
                    pass
                elif(self.windows_split(self.eye_x,self.eye_y) == 11):
                    pass
                elif(self.windows_split(self.eye_x,self.eye_y) == 12):
                    pass
                
                        
                
                pass
                    
            elif count > 200:
                count = 0
            else:
                pass

def camrea_for_move(x_val,y_val):
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_camera = ep_robot.camera


    point_size = 8
    point_color_point = (0, 0, 255) # BGR
    thickness_point = -1 # 可以为 0 、4、8


    # ptStart_1 = (0, 206)
    # ptEnd_1 = (1280, 206)

    # ptStart_2 = (0, 412)
    # ptEnd_2 = (1280, 412)

    # ptStart_3 = (0, 620)
    # ptEnd_3 = (1280, 620)

    # ptStart_4 = (426, 0)
    # ptEnd_4 = (426, 720)

    # ptStart_5 = (853, 0)
    # ptEnd_5 = (853, 720)
    ptStart_1 = (0,155)
    ptEnd_1 = (1280,155)

    ptStart_2 = (0,465)
    ptEnd_2 = (1280,465)

    ptStart_3 = (0,620)
    ptEnd_3 = (1280,620)

    ptStart_4 = (0,310)
    ptEnd_4 = (426,310)

    ptStart_5 = (853,310)
    ptEnd_5 = (1280,310)

    ptStart_6 = (426,0)
    ptEnd_6 = (426,720)

    ptStart_7 = (853,0)
    ptEnd_7 = (853,720)



    point_color = (0, 255, 0) # BGR
    thickness = 2
    lineType = 4

    #----------------------------
    text = 'Move Mode'
    org = (120, 670)
    fontFace = cv2.FONT_HERSHEY_COMPLEX
    fontScale = 1
    fontcolor = (0, 255, 0) # BGR
    thickness = 1 
    lineType = 4
    bottomLeftOrigin = 1

    text2 = "Catch Mode"
    org2 = (973,670)
    # cv.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType, bottomLeftOrigin)



    # 显示200帧图传
    ep_camera.start_video_stream(display=False)
    while True:
        
        img = ep_camera.read_cv2_image()
        # img = cv2.resize(img, (1920,1080), interpolation=cv2.INTER_CUBIC)
        cv2.line(img, ptStart_1, ptEnd_1, point_color, thickness, lineType)
        cv2.line(img, ptStart_2, ptEnd_2, point_color, thickness, lineType)
        cv2.line(img, ptStart_3, ptEnd_3, point_color, thickness, lineType)
        cv2.line(img, ptStart_4, ptEnd_4, point_color, thickness, lineType)
        cv2.line(img, ptStart_5, ptEnd_5, point_color, thickness, lineType)
        cv2.line(img, ptStart_6, ptEnd_6, point_color, thickness, lineType)
        cv2.line(img, ptStart_7, ptEnd_7, point_color, thickness, lineType)
        cv2.putText(img, text, org, fontFace, fontScale, (0,0,255), thickness, lineType)
        cv2.putText(img, text2, org2, fontFace, fontScale, fontcolor, thickness, lineType)
        cv2.circle(img, (int(car_demo.eye_x/1.5),int(car_demo.eye_y/1.5)), point_size, point_color_point, thickness_point)
        #print(img.shape)
        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.namedWindow("frame", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
        cv2.resizeWindow("frame", 1920, 1080)    # 设置长和宽
        cv2.imshow("frame", img)
        c = cv2.waitKey(1) #判断退出的条件 当按下'Q'键的时候呢，就退出
        if c == ord('q'):
            ep_camera.stop_video_stream()
            
            break
    cv2.destroyAllWindows()
    ep_robot.close()

def camrea_for_move_mutil(x_val,y_val):
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_camera = ep_robot.camera


    point_size = 8
    point_color_point = (0, 0, 255) # BGR
    thickness_point = -1 # 可以为 0 、4、8


    # ptStart_1 = (0, 206)
    # ptEnd_1 = (1280, 206)

    # ptStart_2 = (0, 412)
    # ptEnd_2 = (1280, 412)

    # ptStart_3 = (0, 620)
    # ptEnd_3 = (1280, 620)

    # ptStart_4 = (426, 0)
    # ptEnd_4 = (426, 720)

    # ptStart_5 = (853, 0)
    # ptEnd_5 = (853, 720)
    ptStart_1 = (0,155)
    ptEnd_1 = (1280,155)

    ptStart_2 = (0,465)
    ptEnd_2 = (1280,465)

    ptStart_3 = (0,620)
    ptEnd_3 = (1280,620)

    ptStart_4 = (0,310)
    ptEnd_4 = (426,310)

    ptStart_5 = (853,310)
    ptEnd_5 = (1280,310)

    ptStart_6 = (426,0)
    ptEnd_6 = (426,720)

    ptStart_7 = (853,0)
    ptEnd_7 = (853,720)



    point_color = (0, 255, 0) # BGR
    thickness = 2
    lineType = 4

    #----------------------------
    text = 'Move Mode'
    org = (120, 670)
    fontFace = cv2.FONT_HERSHEY_COMPLEX
    fontScale = 1
    fontcolor = (0, 255, 0) # BGR
    thickness = 1 
    lineType = 4
    bottomLeftOrigin = 1

    text2 = "Catch Mode"
    org2 = (973,670)
    # cv.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType, bottomLeftOrigin)



    # 显示200帧图传
    ep_camera.start_video_stream(display=False)
    while True:
        
        img = ep_camera.read_cv2_image()
        # img = cv2.resize(img, (1920,1080), interpolation=cv2.INTER_CUBIC)
        cv2.line(img, ptStart_1, ptEnd_1, point_color, thickness, lineType)
        cv2.line(img, ptStart_2, ptEnd_2, point_color, thickness, lineType)
        # cv2.line(img, ptStart_3, ptEnd_3, point_color, thickness, lineType)
        # cv2.line(img, ptStart_4, ptEnd_4, point_color, thickness, lineType)
        # cv2.line(img, ptStart_5, ptEnd_5, point_color, thickness, lineType)
        # cv2.line(img, ptStart_6, ptEnd_6, point_color, thickness, lineType)
        # cv2.line(img, ptStart_7, ptEnd_7, point_color, thickness, lineType)
        # cv2.putText(img, text, org, fontFace, fontScale, (0,0,255), thickness, lineType)
        # cv2.putText(img, text2, org2, fontFace, fontScale, fontcolor, thickness, lineType)
        cv2.circle(img, (int(car_demo.eye_x/1.5),int(car_demo.eye_y/1.5)), point_size, point_color_point, thickness_point)
        #print(img.shape)
        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.namedWindow("frame", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
        cv2.resizeWindow("frame", 1920, 1080)    # 设置长和宽
        cv2.imshow("frame", img)
        c = cv2.waitKey(1) #判断退出的条件 当按下'Q'键的时候呢，就退出
        if c == ord('q'):
            ep_camera.stop_video_stream()
            
            break
    cv2.destroyAllWindows()
    ep_robot.close()
    
def camrea_for_grap(x_val,y_val):
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_camera = ep_robot.camera


    point_size = 8
    point_color_point = (0, 0, 255) # BGR
    thickness_point = -1 # 可以为 0 、4、8


    ptStart_1 = (0, 206)
    ptEnd_1 = (1280, 206)

    ptStart_2 = (0, 412)
    ptEnd_2 = (1280, 412)

    ptStart_3 = (0, 620)
    ptEnd_3 = (1280, 620)

    ptStart_4 = (426, 0)
    ptEnd_4 = (426, 720)

    ptStart_5 = (853, 0)
    ptEnd_5 = (853, 720)

    point_color = (0, 255, 0) # BGR
    thickness = 2
    lineType = 4

    #----------------------------
    text = 'Move Mode'
    org = (120, 670)
    fontFace = cv2.FONT_HERSHEY_COMPLEX
    fontScale = 1
    fontcolor = (0, 255, 0) # BGR
    thickness = 1 
    lineType = 4
    bottomLeftOrigin = 1

    text2 = "Catch Mode"
    org2 = (973,670)
    # cv.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType, bottomLeftOrigin)



    # 显示200帧图传
    ep_camera.start_video_stream(display=False)
    while True:
        
        img = ep_camera.read_cv2_image()
        # img = cv2.resize(img, (1920,1080), interpolation=cv2.INTER_CUBIC)
        cv2.line(img, ptStart_1, ptEnd_1, point_color, thickness, lineType)
        cv2.line(img, ptStart_2, ptEnd_2, point_color, thickness, lineType)
        cv2.line(img, ptStart_3, ptEnd_3, point_color, thickness, lineType)
        cv2.line(img, ptStart_4, ptEnd_4, point_color, thickness, lineType)
        cv2.line(img, ptStart_5, ptEnd_5, point_color, thickness, lineType)
        cv2.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType)
        cv2.putText(img, text2, org2, fontFace, fontScale, fontcolor, thickness, lineType)
        cv2.circle(img, (int(car_demo.eye_x/1.5),int(car_demo.eye_y/1.5)), point_size, point_color_point, thickness_point)
        #print(img.shape)
        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.namedWindow("frame", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
        cv2.resizeWindow("frame", 1920, 1080)    # 设置长和宽
        cv2.imshow("frame", img)
        c = cv2.waitKey(1) #判断退出的条件 当按下'Q'键的时候呢，就退出
        if c == ord('q'):
            ep_camera.stop_video_stream()
            
            break
    cv2.destroyAllWindows()
    ep_robot.close()
  

if __name__ == "__main__":
    #前进速度 后退 转向
    car_demo = Car(0.3,0.3,30,1)
    get_data_thread = Thread(target=car_demo.get_eye_data_thread)
    get_data_thread.start()
    while True:
        mode_select = input("模式选择: 1 - 开始实验(移动) , 2 - 退出程序 : ")
        if mode_select == '1':
            car_demo.mode = int(mode_select)
            use_data_thread = Thread(target=car_demo.use_eye_data_thread)
            use_data_thread.start()
            camrea_for_move(car_demo.eye_x,car_demo.eye_y)
            use_data_thread.join(0.5)
            get_data_thread.join(0.5)
        elif mode_select == '2':
            print('程序退出')
            os._exit(0)

        else:
            print('输入有误! 请重新输入...')
    

