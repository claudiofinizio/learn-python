import wx



class NotEmptyValidator(wx.PyValidator):
    def __init__(self, person, key):
        wx.PyValidator.__init__(self)
        self._person = person
        self._key = key

    def Clone(self):
        return NotEmptyValidator(self._person, self._key)

    def TransferToWindow(self):
        win = self.GetWindow()
        win.SetValue(self._person.get(self._key, ''))
        return True

    def TransferFromWindow(self):
        win = self.GetWindow()
        self._person[self._key] = win.GetValue()
        return True

    def Validate(self, ctl):
        win = self.GetWindow()
        val = win.GetValue().strip()
        if val == '':
            msg = '%s: non deve essere vuoto.' % win.GetName()
            wx.MessageBox(msg)
            return False
        else:
            return True


class AgeValidator(wx.PyValidator):
    def __init__(self, person):
        wx.PyValidator.__init__(self)
        self._person = person

    def Clone(self): return AgeValidator(self._person)

    def Validate(self, win): return True  # non facciamo validazione

    def TransferToWindow(self):
        win = self.GetWindow()
        win.SetRange(0, 100)  # minimo e massimo
        win.SetValue(self._person.get('eta', 20))  # valore di default
        return True

    def TransferFromWindow(self):
        win = self.GetWindow()
        self._person['eta'] = win.GetValue()
        return True


class PersonDialog(wx.Dialog):
    def __init__(self, *a, **k):
        print 'LATO APP - PersonDialog.OnInit'

        wx.Dialog.__init__(self, *a, **k)
        person = self.GetParent().current_person
        self.first_name = wx.TextCtrl(
            self, name='Nome',
            validator=NotEmptyValidator(person, 'nome')
        )
        self.family_name = wx.TextCtrl(
            self, name='Cognome',
            validator=NotEmptyValidator(person, 'cognome')
        )
        self.year = wx.SpinCtrl(self, name="Eta'")
        self.year.SetValidator(AgeValidator(person))
        ok = wx.Button(self, wx.ID_OK, 'conferma')
        cancel = wx.Button(self, wx.ID_CANCEL, 'annulla')

        s = wx.FlexGridSizer(3, 2, 5, 5)
        s.AddGrowableCol(1)
        for ctl, lab in (
                (self.first_name, 'nome:'),
                (self.family_name, 'cognome:'),
                (self.year, "eta':")
            ):
            s.Add(wx.StaticText(self, -1, lab), 0, wx.ALIGN_CENTER_VERTICAL)
            s.Add(ctl, 1, wx.EXPAND)

        s1 = wx.BoxSizer()
        s1.Add(ok, 1, wx.EXPAND | wx.ALL, 5)
        s1.Add(cancel, 1, wx.EXPAND | wx.ALL, 5)

        s2 = wx.BoxSizer(wx.VERTICAL)
        s2.Add(s, 1, wx.EXPAND | wx.ALL, 5)
        s2.Add(s1, 0, wx.EXPAND)
        self.SetSizer(s2)
        s2.Fit(self)


class TopFrame(wx.Frame):
    def __init__(self, *a, **k):
        print 'LATO APP - TopFrame.OnInit'

        wx.Frame.__init__(self, *a, **k)
        p = wx.Panel(self)
        self.people = wx.ListBox(p)
        self.people.Bind(wx.EVT_LISTBOX_DCLICK, self.on_view_person)
        new = wx.Button(p, -1, 'Add a person')
        new.Bind(wx.EVT_BUTTON, self.on_new)
        # Per unittest
        self.bottone = new

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(self.people, 1, wx.EXPAND | wx.ALL, 5)
        s.Add(new, 0, wx.EXPAND | wx.ALL, 5)
        p.SetSizer(s)

        self.current_person = {}
        self.reload_people_list()


    def reload_people_list(self):
        self.people.Clear()
        people = wx.GetApp().PEOPLE
        for p in people:
            s = '%i: %s %s %i' % (
                p, people[p]['nome'],
                people[p]['cognome'],
                people[p]['eta']
            )
            self.people.Append(s)
        self.current_person = {}

    def on_view_person(self, evt):
        app = wx.GetApp()
        selected = self.people.GetString(evt.GetSelection())
        # questo e' molto brutto, ma e' per fare in fretta....
        id = int(selected.split(':')[0])
        self.current_person = app.PEOPLE[id]
        self.prova = PersonDialog(self, title='Vedi persona')
        ret = self.prova.ShowModal()
        if ret == wx.ID_OK:
            app.PEOPLE[id] = self.current_person
            self.reload_people_list()
        self.prova.Destroy()



    def on_new(self, evt):
        print 'LATO APP - on=new'
        self.current_person = {}
        self.dialog = PersonDialog(self, title='Nuova persona')
        ret = self.dialog.ShowModal()
        if ret == wx.ID_OK:
            app = wx.GetApp()
            id = max(app.PEOPLE.keys()) + 1
            app.PEOPLE[id] = self.current_person
            self.reload_people_list()
        self.dialog.Destroy()


class WxApp(wx.App):
    def OnInit(self):
        print 'LATO APP - WxApp.OnInit'

        self.PEOPLE = {1: {'nome': 'Mario', 'cognome': 'Rossi', 'eta': 37},
                       2: {'nome': 'Giuseppe', 'cognome': 'Bianchi', 'eta': 25},
                       3: {'nome': 'Andrea', 'cognome': 'Verdi', 'eta': 42}}
        self.top_frame = TopFrame(None, title='Persone', size=(300, 300))
        self.top_frame.Show()
        return True

if __name__ == "__main__":
    print 'prima'
    app = WxApp(False)
    app.MainLoop()
    print 'dopo\n'
