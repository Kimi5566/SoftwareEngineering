import cv2


vc = cv2.VideoCapture("124.avi")

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('testWrite.avi', fourcc, 30.0, (1920, 1080), True)

number = 0
while number < int(vc.get(cv2.CAP_PROP_FRAME_COUNT))/10:
    number = number+1
    ret, frame = vc.read()
    if not ret:
        print("end")
        break

    print(number)
    out.write(frame)
    cv2.imshow('frame', frame)

vc.release()
out.release()
cv2.destroyAllWindows()
