import numpy as np
import cv2

def colors(frame):
    # define the lower and upper boundaries of the "color object"
    # in the HSV color space, then initialize the
    # list of tracked points
    
    #colorLower = (24, 100, 100)
    #colorUpper = (44, 255, 255)
    h_sensivity = 20
    s_h = 255
    v_h = 255
    s_l = 100
    v_l = 100
    
    red_upper = np.array([20 + h_sensivity, s_h, v_h])
    red_lower = np.array([20 - h_sensivity, s_l, v_l])
    
    yellow_upper = np.array([40 + h_sensivity, s_h, v_h])
    yellow_lower = np.array([40 - h_sensivity, s_l, v_l])
    
    green_upper = np.array([60 + h_sensivity, s_h, v_h])
    green_lower = np.array([60 - h_sensivity, s_l, v_l])
    
    cian_upper = np.array([100 + h_sensivity, s_h, v_h])
    cian_lower = np.array([100 - h_sensivity, s_l, v_l])
    
    blue_upper = np.array([125 + h_sensivity, s_h, v_h])
    blue_lower = np.array([125 - h_sensivity, s_l, v_l])
    
    violet_upper = np.array([145 + h_sensivity, s_h, v_h])
    violet_lower = np.array([145 - h_sensivity, s_l, v_l])
    
    magneta_upper = np.array([160 + h_sensivity, s_h, v_h])
    magneta_lower = np.array([160 - h_sensivity, s_l, v_l])

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_red = cv2.inRange(hsv_frame, red_lower, red_upper)
    mask_yellow = cv2.inRange(hsv_frame, yellow_lower, yellow_upper)
    mask_green = cv2.inRange(hsv_frame, green_lower, green_upper)
    mask_cian = cv2.inRange(hsv_frame, cian_lower, blue_upper)
    mask_blue = cv2.inRange(hsv_frame, blue_lower, blue_upper)
    mask_violet = cv2.inRange(hsv_frame, violet_lower, violet_upper)
    mask_magneta = cv2.inRange(hsv_frame, magneta_lower, magneta_upper)
    
    masks = [mask_red, mask_yellow, mask_green, mask_cian, mask_blue, mask_violet, mask_magneta]
    
    process(frame, masks[1]) # track yellow object
        
'''
    red_rate = np.count_nonzero(mask_red)/(rect_size*rect_size)
    yellow_rate = np.count_nonzero(mask_yellow)/(rect_size*rect_size)
    green_rate = np.count_nonzero(mask_green)/(rect_size*rect_size)
    cian_rate = np.count_nonzero(mask_cian)/(rect_size*rect_size)
    blue_rate = np.count_nonzero(mask_blue)/(rect_size*rect_size)
    violet_rate = np.count_nonzero(mask_violet)/(rect_size*rect_size)
    magneta_rate = np.count_nonzero(mask_magneta)/(rect_size*rect_size)
'''

def process(frame, mask):

    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
 
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
 
    if len(cnts) > 0:
        #c = max(cnts, key=cv2.contourArea)
        for c in cnts:
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            radius = (rect[1][0] / 2, rect[1][1]/2)
 
            if radius[0] > 20 and radius[1] > 20:
                cv2.rectangle(frame, box[2], box[0], (0, 0, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
