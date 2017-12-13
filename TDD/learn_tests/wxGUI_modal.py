import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        btn = wx.Button(self, label="SomeProcessing")
        self.Bind(wx.EVT_BUTTON, self.SomeProcessing, btn)

    def SomeProcessing(self,event):
        self.dlg = Dlg_GetUserInput(self)
        if self.dlg.ShowModal() == wx.ID_OK:
            if self.dlg.sel1.GetValue():
                print 'sel1 processing'
                self.data_after_processing = 'bar'
            if self.dlg.sel2.GetValue():
                print 'sel2 processing'
                self.data_after_processing = 'foo'

class Dlg_GetUserInput(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent)
        self.sel1 = wx.CheckBox(self, label='Selection 1')
        self.sel2 = wx.CheckBox(self, label='Selection 2')
        self.OK = wx.Button(self, wx.ID_OK)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.sel1)
        sizer.Add(self.sel2)
        sizer.Add(self.OK)
        self.SetSizer(sizer)

def test():
    app = wx.App()
    mf = MyFrame(None, 'testgui')
    for item in mf.GetChildren():
        if item.GetLabel() == 'SomeProcessing':
            btn = item
            break

    def clickOK():
        dlg = wx.GetActiveWindow()
        dlg.sel2.SetValue(True)
        clickEvent = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, wx.ID_OK)
        dlg.ProcessEvent(clickEvent)

    event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, btn.GetId())
    wx.CallAfter(clickOK)
    mf.GetEventHandler().ProcessEvent(event)

    print 'data_after_processing:', mf.data_after_processing
    mf.Destroy()


test()