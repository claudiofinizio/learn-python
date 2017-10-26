# -*- coding: utf-8 -*-

import wx


def unicode_or_bust(obj):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding="utf-8")
    return obj


def list_the_bytes(stream):
    return  ":".join("{:02x}".format(ord(byte_)) for byte_ in stream)


class Frame(wx.Frame):
    def __init__(self, parent):
        super(Frame, self).__init__(parent)

        # 1. Struttura dei widgets.
        self.panel = wx.Panel(parent=self)
        self.text_widget = wx.TextCtrl(parent=self.panel)
        self.save_button = wx.Button(parent=self.panel, label="Save")
        self.load_button = wx.Button(parent=self.panel, label="Load")

        buttons_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        panel_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        text_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        gap_sizer = wx.BoxSizer(orient=wx.VERTICAL)

        text_sizer.Add(self.text_widget, proportion=1)
        buttons_sizer.Add(
            self.save_button, proportion=0, flag = wx.ALIGN_RIGHT,
        )
        buttons_sizer.Add(
            self.load_button, proportion=0, flag = wx.ALIGN_RIGHT,
        )
        gap_sizer.Add(wx.StaticText(parent=self.panel, label=""))
        panel_sizer.Add(text_sizer, proportion=0)
        panel_sizer.Add(gap_sizer, proportion=1, flag=wx.EXPAND)
        panel_sizer.Add(buttons_sizer, proportion=1, flag=wx.ALIGN_RIGHT)
        self.panel.SetSizer(panel_sizer)
        self.panel.Fit()

        # 2. Valori di default
        text_value = "Ivan Krstić"
        text_value = "palla"
        self.text_widget.SetValue(text_value)
        self.text_widget.SetInsertionPointEnd()

        # 3. Events' binding.
        self.Bind(wx.EVT_BUTTON, self.load, self.load_button)
        self.Bind(wx.EVT_BUTTON, self.save, self.save_button)

        # 4. External file definition.
        self.filename = "grafemi/prova.sql"

        # 5. Help for fast interactive session: set default widget focus.
        self.load_button.SetFocus()

    def load(self, event):
        print 'loading...'
        with open(self.filename, "r") as infile:

            # 1. Read the stream of bytes from the external source.
            stream = infile.read()
            # <stream> as stream of bytes
            print list_the_bytes(stream)
            # <stream> as repr
            print repr(stream)
            # <stream> as print, which means that the console decoding will decide what to show on the screen
            print stream
            print 'end of stream\n'

            # 2. First golden rule: Decode early (aka: "DECIFRATO")
            deciphered = unicode_or_bust(stream)
            print list_the_bytes(deciphered)
            print repr(deciphered)
            print deciphered
            print 'end of deciphered\n'

            # 3. Pass the deciphered info (aka the unicode object) to the wx interface.
            self.text_widget.SetValue(deciphered)

    def save(self, event):
        print 'saving...'
        with open(self.filename, "a") as outfile:
            # 1. Third golden rule: encode late.
            # before the encoding we have unicode graphemes
            print 'Graphemes'
            graphemes = self.text_widget.GetValue()
            print type(graphemes)
            print repr(graphemes)
            print graphemes
            # Now do the criptography, aka Encode
            crypted = graphemes.encode("utf-8")
            # NOTA CHE "utf-8" SI RIFERISCE AL CONTENUTO DEI GRAFEMI
            # E QUINDI DEVI SAPERE A PRIORI CHE I GRAFEMI SONO DEI
            # CODE POINTS UNICODE. ALTRIMENTI OTTERRESTI
            # AttributeError: 'list' object has no attribute 'encode'
            # (UN ESEMPIO DI PROVARE A CRITTOGRAFARE UNA LISTA),
            # GLI OGGETTI PYTHON HANNO dir() E QUELLI CHE NON HANNO encode
            # NELLA LORO dir SIGNIFICA CHE NON SONO 'CRITTOGRAFABILI'.

            # after the encoding we have a Py2 <string>
            print '\nCrypted'
            print type(crypted)
            print repr(crypted)
            print crypted
            # 3. Save the string to an external source, i.e.: a file.
            outfile.write(crypted)


app = wx.App()
frame = Frame(parent=None)
frame.Show()

app.MainLoop()

