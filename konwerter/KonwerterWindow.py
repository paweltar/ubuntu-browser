# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk, WebKit # pylint: disable=E0611
import logging
logger = logging.getLogger('konwerter')

from konwerter_lib import Window
from konwerter.AboutKonwerterDialog import AboutKonwerterDialog
from konwerter.PreferencesKonwerterDialog import PreferencesKonwerterDialog

# See konwerter_lib.Window.py for more details about how this class works
class KonwerterWindow(Window):
    __gtype_name__ = "KonwerterWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(KonwerterWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutKonwerterDialog
        self.PreferencesDialog = PreferencesKonwerterDialog

        # Code for other initialization actions should be added here.

        self.refreshbutton = self.builder.get_object("refreshbutton")
        self.urlEntry = self.builder.get_object("urlEntry")
        self.scrolledwindow = self.builder.get_object("scrolledwindow")
        self.toolbar = self.builder.get_object("toolbar")


        context = self.toolbar.get_style_context()
        context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)

        self.webview = WebKit.WebView()
        self.scrolledwindow.add(self.webview)
        self.webview.show()


    def on_refreshbutton_clicked(self, widget):
        self.webview.reload()

    def on_urlEntry_activate(self, widget):
        url = widget.get_text()

        self.webview.open(url)

