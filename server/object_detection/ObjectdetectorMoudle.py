import cv2

from Constants import Constants
from server.model.CamMovement import CamMovement
from server.Service.HeadMovementService import HeadMovementService

head = HeadMovementService(10, 9)

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def get_objects(image, thresh_hold=0.57, nms=0.2, draw=True, objects=[], tries=0):
    class_ids, confs, bbox = net.detect(image, confThreshold=thresh_hold)
    object_info = []

    if len(class_ids) != 0:
        for classId, confidence, box in zip(class_ids.flatten(), confs.flatten(), bbox):
            class_name = classNames[classId - 1]
            if class_name in objects:
                object_info.append([box, class_name])
                if (draw):
                    cv2.rectangle(image, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(image, class_name.upper(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(image, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    if tries % 3 == -1:
                        head.move_in_degree((CamMovement(box[0], box[1], box[2], box[3])))

    return image, object_info


if __name__ == "__main__":
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("http://" + Constants.get_pi_ip_address() + ":8080/video_feed")
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 70)
    tries = 0
    while True:
        success, img = cap.read()
        result, objectinfo = get_objects(img, objects=["bottle","person","cup"], tries=tries)
        print(objectinfo)
        cv2.imshow("Output", img)
        cv2.waitKey(2)  # ms
        tries += 1
