import jetson.utils
import jetson.inference

input = jetson.utils.videoSource("/dev/video0")
output = jetson.utils.videoOutput("display://0")
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

while output.IsStreaming():
    img=input.Capture()
    detections = net.Detect(img)
    output.Render(img)
    output.SetStatus("Performance {:.0f}FPS".format(net.GetNetworkFPS()))