#!/usr/bin/python

import wx
import os

# -- Give the id to the dropdown menu --
ID_ABOUT = 100
ID_OPEN = 102
ID_SAVE = 103
ID_EXIT = 101
ID_VIEW_STAT = 104


# -- Our Main AppClass --
class app(wx.App):
	def OnInit(self):
		frame = MainWindow(None,-1,'Simple Text Editor')
		self.SetTopWindow(frame)
		frame.Show()
		return 1

# -- Our Main Windows as Parent --
class MainWindow(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, wx.ID_ANY, title, size = (640,480), 
						  style = wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
		self.namadir=''
		
		# -- Create the Text Area --
		self.control = wx.TextCtrl(self, 1, style = wx.TE_MULTILINE)
		# -- Create Status Bar --
		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetStatusText("Ini adalah Status Bar")
		
		# -- Setup the Menu Items --
		fileMenu = wx.Menu()
		fileMenu.Append(ID_OPEN, "&Open\tCtrl+o", "Buka File")
		fileMenu.Append(ID_SAVE, "&Save\tCtrl+s", "Simpan File")
		fileMenu.AppendSeparator()
		fileMenu.Append(ID_EXIT, "E&xit\tCtrl+x", "Keluar dari Program ini!")
		
		fileMenu3 = wx.Menu()
		self.id_status = fileMenu3.Append(ID_VIEW_STAT, "&View StatusBar\tCtrl+v", "Perlihatkan Status Bar", kind=wx.ITEM_CHECK)
		
		fileMenu3.Check(self.id_status.GetId(), True)
		
		fileMenu2 = wx.Menu()
		fileMenu2.Append(ID_ABOUT, "&About", "Informasi Tentang Program Ini")
		
		# -- Creating the MenuBar -- 
		menuBar = wx.MenuBar()
		menuBar.Append(fileMenu, "&File")
		menuBar.Append(fileMenu3, "&View")
		menuBar.Append(fileMenu2, "&Help")
		self.SetMenuBar(menuBar)
		
		# -- Event --
		wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
		wx.EVT_MENU(self, ID_OPEN, self.OnOpen)
		wx.EVT_MENU(self, ID_VIEW_STAT, self.ToggleStatus)
		wx.EVT_MENU(self, ID_EXIT, self.OnExit)
		wx.EVT_MENU(self, ID_SAVE, self.OnSave)
		
		self.Center()
		# -- Show the Main Window --
		self.Show(True)

	# -- Event Handler --
	def OnAbout(self, event):
		d = wx.MessageDialog(self, "Sample editor in wxPython \nBy Denna Adhiyaksa", "About Simple Editor", wx.OK)
		d.ShowModal()
		d.Destroy()
		
	def OnOpen(self, event):
		c = wx.FileDialog(self, "Pilih Berkas yg Akan Dibuka", self.namadir, "", "*.*", wx.OPEN)
		if c.ShowModal() == wx.ID_OK:
			self.namafile = c.GetFilename()
			self.namadir = c.GetDirectory()
			f = open(os.path.join(self.namadir,self.namafile), 'r')
			self.control.SetValue(f.read())
			f.close()
		c.Destroy()
		
	def ToggleStatus(self, event):
		if self.id_status.IsChecked():
			self.statusbar.Show()
		else:
			self.statusbar.Hide()


	def OnSave(self,event):
		# Save away the edited text
		# Open the file, do an RU sure check for an overwrite!
		dlg = wx.FileDialog(self, "Choose a file", self.namadir, "", "*.*",
							wx.SAVE | wx.OVERWRITE_PROMPT)
		if dlg.ShowModal() == wx.ID_OK:
			# Grab the content to be saved
			itcontains = self.control.GetValue()

			# Open the file for write, write, close
			self.filename=dlg.GetFilename()
			self.namadir=dlg.GetDirectory()
			filehandle=open(os.path.join(self.namadir, self.filename),'w')
			filehandle.write(itcontains)
			filehandle.close()
		# Get rid of the dialog to keep things tidy
		dlg.Destroy()


	def OnExit(self, event):
		e = wx.MessageDialog(self,"Apakah Anda yakin akan Keluar?", "Exit", wx.YES|wx.NO|wx.ICON_QUESTION)
		if e.ShowModal() == wx.ID_YES:
			self.Close(True)
		else:
			e.Destroy()

if __name__ == "__main__":
	prog = app(0)
	prog.MainLoop()

