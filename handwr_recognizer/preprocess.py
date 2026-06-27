# digit_reco_app/preprocess.py
import numpy as np
import cv2
import base64
from Handwrittern_digit_recognizer.ImageProcessingMaterials.digit_preprocessing import segment_digits

def compute_hog_features(gray_28x28, winSize=(28,28), blockSize=(14,14),
                         blockStride=(7,7), cellSize=(14,14), nbins=9):
    """Compute HOG features """
    hog = cv2.HOGDescriptor(
        _winSize=winSize,
        _blockSize=blockSize,
        _blockStride=blockStride,
        _cellSize=cellSize,
        _nbins=nbins,
    )
    
    feat = hog.compute(gray_28x28)   
    return feat.flatten()


def detect_and_predict(image_file, model, return_image=False, min_area=80,
                       pad_ratio=0.25, merge_kernel=1, max_aspect=1.1,
                       split_wide=True, do_deskew=True):
    """
    Process uploaded image using the shared preprocessing module,
    predict digits using the loaded pipeline.
    """
    # Read uploaded file into OpenCV image
    file_bytes = image_file.read()
    nparr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Could not read the image file.")

    # Use the training-identical segmentation
    tiles, boxes = segment_digits(
        img,
        min_area=min_area,
        pad_ratio=pad_ratio,
        merge_kernel=merge_kernel,
        max_aspect=max_aspect,
        split_wide=split_wide,
    )

    digits = []
    annotated_img = img.copy() if return_image else None

    for tile, (x, y, w, h) in zip(tiles, boxes):
        # Compute HOG features from the 28x28 tile
        hog_fd = compute_hog_features(tile)     # length 81
        hog_fd = hog_fd.reshape(1, -1)          # (1, 81)

        # Predict (pipeline applies scaling internally)
        pred = model.predict(hog_fd)[0]
        digit = int(pred)
        digits.append(digit)

        if annotated_img is not None:
            cv2.rectangle(annotated_img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(annotated_img, str(digit), (x, y - 10),
                        cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

    img_base64 = None
    if annotated_img is not None:
        _, buffer = cv2.imencode('.png', annotated_img)
        img_base64 = "data:image/png;base64," + base64.b64encode(buffer).decode('utf-8')

    return digits, img_base64