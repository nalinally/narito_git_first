# -*- coding: utf-8 -*-
import numpy as np
import cv2
import serial
import time
import curses.ascii

#シリアル通信初期設定
ser = serial.Serial('/dev/serial0')
ser.baudrate = 4800
ser.parity = serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 5

def senddata(a):
    b = int(a / 100)
    a -= 100 * b
    ser.write(str.encode(str(b)))
    #time.sleep(0.01)
    c = int(a / 10)
    a -= 10 * c
    ser.write(str.encode(str(c)))
    #time.sleep(0.01)
    ser.write(str.encode(str(a)))
    #time.sleep(0.01)

#指定された色の円を検出(最小外接円)
def getCircle(frame, lower_color, upper_color):
    MIN_RADIUS = 25

    lower_red2 = np.array([162, 30, 0])
    upper_red2 = np.array([175, 255, 255])

    # HSVによる画像情報に変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ガウシアンぼかしを適用して、認識精度を上げる
    blur = cv2.GaussianBlur(hsv, (9, 9), 0)

    # 指定した色範囲のみを抽出する
    color = cv2.inRange(blur, lower_red2, upper_red2)

    # オープニング・クロージングによるノイズ除去
    element8 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.uint8)
    oc = cv2.morphologyEx(color, cv2.MORPH_OPEN, element8)
    oc = cv2.morphologyEx(oc, cv2.MORPH_CLOSE, element8)

    #cv2.imshow('color', oc)

    # 輪郭抽出
    contours, hierarchy = cv2.findContours(oc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("{0} contours.".format(len(contours)))

    if len(contours) > 0:
        # 一番大きい赤色領域を指定する
        contours.sort(key=cv2.contourArea, reverse=True)
        cnt = contours[0]

        # 最小外接円を用いて円を検出する
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)

        # 円が小さすぎたら円を検出していないとみなす
        if radius < MIN_RADIUS:
            return None
        else:
            return center, radius
    else:
        return None


#メインの記述
if __name__ == '__main__':
    # 内蔵カメラを起動(カメラが一つしか繋がっていない場合は、引数に0を渡せば良い)
    cap = cv2.VideoCapture(0)
    s = 0
    x = [0, 0]
    y = [0, 0]
    r = [0, 0]

    while True:
        # 赤色の円を抽出する
        frame = cap.read()[1]
        #frame = cv2.imread("./redcircle.png")
        getframe = getCircle(frame, np.array([130, 80, 80]), np.array([200, 255, 255]))

        if getframe is not None:
            # 見つかった円の上に青い円を描画
            # getframe[0]:中心座標、getframe[1]:半径
            #cv2.circle(frame, getframe[0], getframe[1], (255, 0, 0), 2)
            x[s] = int(getframe[0][0] / 10)
            y[s] = int(getframe[0][1] / 10)
            r[s] = int(getframe[1] / 10)
            #位置情報渡す
            #if (x[0] != x[1]) or (y[0] != y[1]) or (r[0] != r[1]):
            print(x[s], ", ", y[s], ", ", r[s])
            ser.write(str.encode("128b"))
            ser.write(str.encode(str(x[s])))
            ser.write(str.encode("b"))
            ser.write(str.encode(str(y[s])))
            ser.write(str.encode("b"))
            ser.write(str.encode(str(r[s])))
            ser.write(str.encode("b"))

            if s:
                s = 0
            else:
                s = 1

            time.sleep(0.05)

        # 検出結果とともに映像を表示
        #cv2.imshow('Circle Detect', frame)

        #if cv2.waitKey(100) & 0xFF == ord('q'):
        #    break

    # 終了時にカメラを解放
    #cap.release()
    #cv2.destroyAllWindows()
