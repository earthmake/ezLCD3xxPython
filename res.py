import win32com.client
strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("Select * from CIM_VideoControllerResolution")
for objItem in colItems:
    print "Caption: ", objItem.Caption
    print "Description: ", objItem.Description
    print "Horizontal Resolution: ", objItem.HorizontalResolution
    print "Max Refresh Rate: ", objItem.MaxRefreshRate
    print "Min Refresh Rate: ", objItem.MinRefreshRate
    print "Number Of Colors: ", objItem.NumberOfColors
    print "Refresh Rate: ", objItem.RefreshRate
    print "Scan Mode: ", objItem.ScanMode
    print "Setting ID: ", objItem.SettingID
    print "Vertical Resolution: ", objItem.VerticalResolution
