from detection.pytorch_ssd.vision.ssd.vgg_ssd import create_vgg_ssd, create_vgg_ssd_predictor
import cv2


def run_ssd(img):
    model_path="./detection/pytorch_ssd/models/vgg16-ssd-Epoch-70-Loss-2.13.pth"
    label_path = "./detection/pytorch_ssd/models/open-images-model-labels.txt"
    class_names = [name.strip() for name in open(label_path).readlines()]
    color_list = [(0,0,0),(255,255,0),(204,0,0),(0,0,255),(204,0,204),(0,255,0),(0,255,255)]  #소다,파랑,빨강,보라,초록,노랑

    net = create_vgg_ssd(len(class_names), is_test=True)
    net.load(model_path)
    predictor = create_vgg_ssd_predictor(net, candidate_size=200)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes, labels, probs = predictor.predict(img, 10, 0.4)

    total_result = []
    for i in range(boxes.size(0)):
        box = boxes[i, :]
        basic_result = class_names[labels[i]]
        total_result.append(basic_result)

        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), color_list[labels[i]], 4)
        label = f"{class_names[labels[i]]}: {probs[i]:.2f}"
        cv2.putText(img, label,
                    (box[0] + 20, box[1] + 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,  # font scale
                    (255, 0, 255),
                    2)  # line type

    return img, total_result


