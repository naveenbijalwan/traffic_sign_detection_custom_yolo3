MSBuild yourproject.sln /p:Configuration=Release /p:Platform=x64


traffic_sign_detection_custom_yolo3\darknet\build\darknet\x64\darknet.exe detector train cfg\labelled_data.data cfg\yolov3_labeled.cfg -dont_show