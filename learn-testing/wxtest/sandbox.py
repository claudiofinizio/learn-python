import wx
from wx.lib.pubsub import pub

TOPIC_VALUE_UPDATED = 'value-updated'

class Test(wx.Frame):
    def __init__(self, *a, **k):
        wx.Frame.__init__(self, *a, **k)
        p = wx.Panel(self)
        self.slider = wx.Slider(p, -1, 50, 0, 100,
                                style=wx.SL_VERTICAL)
        check = wx.CheckBox(p, -1, 'connesso')
        button = wx.Button(p, -1, 'nuovo')

        self.slider.Bind(wx.EVT_SLIDER, self.on_slider)
        check.Bind(wx.EVT_CHECKBOX, self.on_check)
        button.Bind(wx.EVT_BUTTON, self.on_clic)

        s = wx.BoxSizer(wx.VERTICAL)
        for ctl in (self.slider, check, button):
            s.Add(ctl, 0, wx.ALIGN_CENTRE_HORIZONTAL|wx.ALL, 20)
        p.SetSizer(s)
        s.Fit(self)

        pub.subscribe(self.update_value, TOPIC_VALUE_UPDATED)
        check.SetValue(True)

    def update_value(self, message):
        self.slider.SetValue(message)

    def on_slider(self, evt):
        pub.sendMessage(TOPIC_VALUE_UPDATED,
                        message=self.slider.GetValue())

    def on_check(self, evt):
        if evt.IsChecked():
            pub.subscribe(self.update_value, TOPIC_VALUE_UPDATED)
        else:
            pub.unsubscribe(self.update_value, TOPIC_VALUE_UPDATED)

    def on_clic(self, evt):
        Test(self).Show()

if __name__ == '__main__':
    app = wx.App(False)
    Test(None).Show()
    app.MainLoop()