import numpy as np

class DetectAndDescribe:
    def __init__(self, detector, descriptor):
        # store the keypoint detector and local invariant detector 
        self.detector = detector
        self.descriptor = descriptor

    def describe(self, image, useKpList=True):
        kps = self.detector.detect(image)
        (kps, descs) = self.descriptor.compute(image, kps)

        if len(kps) == 0:
            return (None, None)

        if useKpList:
            kps = np.int0([kp.pt for kp in kps])

        return (kps, descs)
