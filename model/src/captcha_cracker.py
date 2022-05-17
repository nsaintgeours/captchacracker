"""
Function that returns the captcha word from some captcha image.
"""

from pathlib import Path

import cv2
import numpy as np
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

OCR_MODEL_CHECKPOINT = 'microsoft/trocr-large-printed'
OCR_IMG_PROCESSOR = TrOCRProcessor.from_pretrained(OCR_MODEL_CHECKPOINT)
OCR_MODEL = VisionEncoderDecoderModel.from_pretrained(OCR_MODEL_CHECKPOINT)


class CaptchaCracker(object):

    def crack(self, image_bytes: bytes, verbose: bool = False) -> str:
        """ Cracks captcha image and returns the colored word. """
        input_img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
        clustered_img = self._cluster_image(img=input_img)
        cropped_img = self._crop_smallest_cluster(img=clustered_img)
        word = self._optical_character_recognition(img=cropped_img)

        if verbose:
            cv2.imshow('Input image', input_img)
            cv2.imshow('Clustered image', cv2.cvtColor(80 * np.uint8(clustered_img), cv2.COLOR_GRAY2RGB))
            cv2.imshow('Cropped image', cropped_img)
            cv2.waitKey()

        return word

    @staticmethod
    def _cluster_image(img: np.ndarray, n: int = 3) -> np.ndarray:
        """
        Segment image into n color clusters using KMeans algorithm.

        Args:
            img (Image): RGB image with shape (width, height, 3)
            n (int): number of clusters

        Returns: (np.ndarray) gray-scale image with shape (width, height);
         Output pixels have integer values ranging from 0 to (n-1) that indicate cluster id.
        """
        flat_matrix = np.float32(np.array(cv2.cvtColor(img[:, :, :3], cv2.COLOR_RGB2HLS)).reshape((-1, 3)))
        _, cluster_ids, _ = cv2.kmeans(
            data=flat_matrix,
            K=n,
            bestLabels=None,
            criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
            attempts=10,
            flags=cv2.KMEANS_RANDOM_CENTERS
        )
        return cluster_ids.reshape((img.shape[0], img.shape[1]))

    @staticmethod
    def _crop_smallest_cluster(img: np.ndarray) -> np.ndarray:
        """
        Extract the color cluster with smallest size from input image.

        Args:
            img (np.ndarray): gray scale image with size (width, height)

        Returns: (np.ndarray) RGB image with shape (small_width, small_height, 3).
            Output image contains only one color cluster from the input image.
            Output image width and height are smaller than (or equal to) input image size.
        """
        smallest_cluster_id = np.bincount(img.flatten()).argmin()
        output_img = 255 * np.uint8((img != smallest_cluster_id))
        output_img = cv2.dilate(output_img, np.ones((3, 3)), iterations=1)
        mask = np.where(output_img == 0)
        xmin, xmax, ymin, ymax = mask[0].min(), mask[0].max(), mask[1].min(), mask[1].max()
        output_img = output_img[xmin:xmax, ymin:ymax]
        output_img = cv2.cvtColor(output_img, cv2.COLOR_GRAY2RGB)
        return output_img

    @staticmethod
    def _optical_character_recognition(img: np.ndarray):
        """
        Optical character recognition.

        Args:
            img (np.ndarray): RGB image with shape (small_width, small_height, 3).

        Returns: (str) recognized word from input image
        """
        pixel_values = OCR_IMG_PROCESSOR(images=img, return_tensors="pt").pixel_values
        recognized_word_ids = OCR_MODEL.generate(pixel_values)
        recognized_word = OCR_IMG_PROCESSOR.batch_decode(recognized_word_ids, skip_special_tokens=True)[0]
        return recognized_word


if __name__ == '__main__':
    cracker = CaptchaCracker()
    with open(Path(__file__).parent.parent.parent / 'data' / 'sample5.png', 'rb') as file:
        text = cracker.crack(image_bytes=file.read())
        print(text)
