import replicate
import os

class ImageModify():

    dft_scale = 2
    dft_fidelity = 0.7
    modelName = ""
    versionNo = ""

    def __init__(self):
        self.dft_scale = 2
        self.dft_fidelity = 0.7
        self.modelName = "sczhou/codeformer"
        self.versionNo = "7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56"

    def testImg(self):
        model = replicate.models.get(self.modelName)
        version = model.versions.get(self.versionNo)
        inputs = {
            # Input image
            'image': open("/Users/admin/rnctech/RNCServ/imgs/img1.png", "rb"),
            # Balance the quality (lower number) and fidelity (higher number).
            # Range: 0 to 1
            'codeformer_fidelity': self.dft_fidelity,
            # Enhance background image with Real-ESRGAN
            'background_enhance': True,
            # Upsample restored faces for high-resolution AI-created images
            'face_upsample': True,
            # The final upsampling scale of the image
            'upscale': self.dft_scale,
        }
        output = version.predict(**inputs)
        print(output)

    def chgImg(self, ofile, scale=2, fidelity=0.7):
        model = replicate.models.get(self.modelName)
        version = model.versions.get(self.versionNo)
        inputs = {
            'image': open((ofile), "rb"),
            'codeformer_fidelity': fidelity,
            'background_enhance': True,
            'face_upsample': True,
            'upscale': scale,
        }
        output = version.predict(**inputs)
        return output

if __name__ == '__main__':
    imgm = ImageModify()
    imgm.testImg()