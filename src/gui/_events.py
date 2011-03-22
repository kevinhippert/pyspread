#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6 on Sun May 25 23:31:23 2008

# Copyright 2008 Martin Manns
# Distributed under the terms of the GNU General Public License
# generated by wxGlade 0.6 on Mon Mar 17 23:22:49 2008

# --------------------------------------------------------------------
# pyspread is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyspread is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyspread. If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

"""
_events
=======

Event handler module

Provides
--------

* post_command_event: Posts a command event

"""

import wx

def post_command_event(target, msg_cls, **kwargs):
    """Posts command event to main window
    
    Command events propagate.
    
    Parameters
    ----------
     * msg_cls: class
    \tMessage class from new_command_event()
     * kwargs: dict
    \tMessage arguments
    
    """
    
    msg = msg_cls(id=-1, **kwargs)
    wx.PostEvent(target, msg)


new_command_event = wx.lib.newevent.NewCommandEvent
    
# Main window
# ===========

TitleMsg, EVT_COMMAND_TITLE = new_command_event()

CloseMsg, EVT_COMMAND_CLOSE = new_command_event()

ManualMsg, EVT_COMMAND_MANUAL = new_command_event()
TutorialMsg, EVT_COMMAND_TUTORIAL = new_command_event()
FaqMsg, EVT_COMMAND_FAQ = new_command_event()
AboutMsg, EVT_COMMAND_ABOUT = new_command_event()

MacroListMsg, EVT_COMMAND_MACROLIST = new_command_event()
MacroLoadMsg, EVT_COMMAND_MACROLOAD = new_command_event()
MacroSaveMsg, EVT_COMMAND_MACROSAVE = new_command_event()

# Grid
# ====

# Grid cell events

# File events

NewMsg, EVT_COMMAND_NEW = new_command_event()
OpenMsg, EVT_COMMAND_OPEN = new_command_event()
SaveMsg, EVT_COMMAND_SAVE = new_command_event()
SaveAsMsg, EVT_COMMAND_SAVEAS = new_command_event()
ImportMsg, EVT_COMMAND_IMPORT = new_command_event()
ExportMsg, EVT_COMMAND_EXPORT = new_command_event()
ApproveMsg, EVT_COMMAND_APPROVE = new_command_event()

# Print events

PrintMsg, EVT_COMMAND_PRINT = new_command_event()

# Clipboard events

CutMsg, EVT_COMMAND_CUT = new_command_event()
CopyMsg, EVT_COMMAND_COPY = new_command_event()
CopyResultMsg, EVT_COMMAND_COPY_RESULT = new_command_event()
PasteMsg, EVT_COMMAND_PASTE = new_command_event()

# Grid view events

RefreshSelectionMsg , EVT_COMMAND_REFRESH_SELECTION = new_command_event()
GotoCellMsg , EVT_COMMAND_GOTO_CELL = new_command_event()
ZoomMsg , EVT_COMMAND_ZOOM = new_command_event()

# Find events

FindMsg, EVT_COMMAND_FIND = new_command_event()
ReplaceMsg, EVT_COMMAND_REPLACE = new_command_event()

# Grid change events

InsertRowsMsg, EVT_COMMAND_INSERT_ROWS = new_command_event()
InsertColsMsg, EVT_COMMAND_INSERT_COLS = new_command_event()
InsertTabsMsg, EVT_COMMAND_INSERT_TABS = new_command_event()
DeleteRowsMsg, EVT_COMMAND_DELETE_ROWS = new_command_event()
DeleteColsMsg, EVT_COMMAND_DELETE_COLS = new_command_event()
DeleteTabsMsg, EVT_COMMAND_DELETE_TABS = new_command_event()

ResizeGridMsg, EVT_COMMAND_RESIZE_GRID = new_command_event()

# Grid attribute events

# Undo/Redo events

UndoMsg, EVT_COMMAND_UNDO = new_command_event()
RedoMsg, EVT_COMMAND_REDO = new_command_event()

# EntryLine
# =========

##EntryLineMsg, EVT_ENTRYLINE_MSG = new_command_event()
##EntryLineSelectionMsg, EVT_ENTRYLINE_SELECTION_MSG = new_command_event()

# Statusbar
# =========

StatusBarMsg, EVT_STATUSBAR_MSG = wx.lib.newevent.NewEvent()


###############################






#GridMsg, EVT_GRID_MSG = wx.lib.newevent.NewEvent()
#
#TableChangeMsg, EVT_TABLE_CHANGE = wx.lib.newevent.NewEvent()
#GridShapeMsg, EVT_GRID_SHAPE = wx.lib.newevent.NewEvent()
#
#def post_status_text(evt_handler, text):
#    """Posts a StatusBarMsg event for the main statusbar widget"""
#
#    msg = StatusBarMsg(text=text)
#    wx.PostEvent(evt_handler, msg)
#
#def post_entryline_text(evt_handler, text):
#    """Posts a StatusBarMsg event for the main statusbar widget"""
#
#    msg = EntryLineMsg(text=text)
#    wx.PostEvent(evt_handler, msg)
#
#def post_entryline_selection(evt_handler, start, stop):
#    """Posts a StatusBarMsg event for the main statusbar widget"""
#
#    msg = EntryLineSelectionMsg(start=start, stop=stop)
#    wx.PostEvent(evt_handler, msg)
#
#def post_grid_text(evt_handler, text):
#    """Posts a text for pysgrid[<current_cell>]"""
#    
#    msg = GridMsg(text=text)
#    wx.PostEvent(evt_handler, msg)
#
#def post_table_change(evt_handler, new_table):
#    """Posts a StatusBarMsg event for the main statusbar widget"""
#    
#    msg = TableChangeMsg(new_table=new_table)
#    wx.PostEvent(evt_handler, msg)
#
#def post_shape_change(evt_handler, shape):
#    """Posts a grid shape event for the main statusbar widget"""
#    
#    msg = GridShapeMsg(shape=shape)
#    wx.PostEvent(evt_handler, msg)
