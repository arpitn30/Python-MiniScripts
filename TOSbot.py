import win32com.client as comclt
wsh = comclt.Dispatch("WScript.Shell")
wsh.AppActivate("Client_tos")
for i in range(100000)
    wsh.SendKeys("z")
