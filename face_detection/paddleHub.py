import paddlehub as hub
import cv2

def paddlePyramidBox_Lite(imgPath):
	module = hub.Module(name="pyramidbox_lite_server")

	test_img_path = imgPath
	img = cv2.imread(test_img_path)
	# 使用字典形式输入
	input_dict = {"data": [img]}

	results = module.face_detection(data=input_dict)

	det = results[0]['data']
	for condition in det:
	    left, top, right, bottom, confidence = condition['left'], condition['top'], \
	                                            condition['right'], condition['bottom'], condition['confidence']
	    # 画出一个框，框住脸
	    cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 255), 2)
	    font = cv2.FONT_HERSHEY_DUPLEX
	    cv2.putText(img, '%2.2f' % confidence, (int(left) + 4, int(bottom) + 24), font, 1.0,
	                (255, 255, 255), 1)

	return img