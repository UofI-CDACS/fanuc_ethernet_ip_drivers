# Basler Camera Demo for Robotics - CDA and MOSCOW

import cv2
from pypylon import pylon

CAMERA_IP_CDA = "10.1.1.57"
#CAMERA_IP_MOSCOW = "10.2.1.57"

def main():
    CAMERA_IP = CAMERA_IP_CDA

    try:
        info = pylon.DeviceInfo()
        info.SetPropertyValue('IpAddress', CAMERA_IP)

        #print("info", info)

        tl_factory = pylon.TlFactory.GetInstance()
        camera = pylon.InstantCamera(tl_factory.CreateFirstDevice(info))
        camera.Open()
        #print(f"Connected to camera at {CAMERA_IP}")

        # modififcation of exposure
        if hasattr(camera, 'ExposureAuto'):
            camera.ExposureAuto.SetValue('Off')
        
        # exposure is in microseconds
        # target_exposure = 10000
        # the below value seemed to be the sweet spot for the camera exposure, please change if you find a better
        target_exposure = 717382 
        
        if hasattr(camera, 'ExposureTime'):
            target_exposure = max(camera.ExposureTime.Min, min(target_exposure, camera.ExposureTime.Max))
            camera.ExposureTime.SetValue(target_exposure)
            print(f"Exposure set to: {camera.ExposureTime.GetValue()} µs")
        # for older GigE models
        elif hasattr(camera, 'ExposureTimeAbs'):  
            target_exposure = max(camera.ExposureTimeAbs.Min, min(target_exposure, camera.ExposureTimeAbs.Max))
            camera.ExposureTimeAbs.SetValue(target_exposure)
            print(f"Exposure set to: {camera.ExposureTimeAbs.GetValue()} µs")

    except Exception as e:
        print(f"Error: {e}")
        return

    # live stream start
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    converter = pylon.ImageFormatConverter()
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed

    print("Streaming... Press 'q' to quit.")
    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            image = converter.Convert(grabResult)
            img = image.GetArray()
            cv2.imshow('GigE cam stream for CDA and MOS', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        grabResult.Release()

    camera.StopGrabbing()
    camera.Close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
