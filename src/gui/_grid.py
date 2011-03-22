#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyspread.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

"""
_grid
=====

Provides
--------
 1. Grid: The main grid of pyspread
 2. MainWindowEventHandlers: Event handlers for Grid

"""

import wx.grid

from _events import *


class Grid(wx.grid.Grid):
    """Pyspread's main grid"""

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        
        wx.grid.Grid.__init__(self, parent, *args, **kwargs)
        
        self.handlers = GridEventHandlers(self)
        
        self._bind()
    
    def _bind(self):
        """Bind events to handlers"""
        
        # Grid cell events
        
        # File events
        
        self.parent.Bind(EVT_COMMAND_NEW, self.handlers.OnNew)
        self.parent.Bind(EVT_COMMAND_OPEN, self.handlers.OnOpen)
        self.parent.Bind(EVT_COMMAND_SAVE, self.handlers.OnSave)
        self.parent.Bind(EVT_COMMAND_SAVEAS, self.handlers.OnSaveAs)
        self.parent.Bind(EVT_COMMAND_IMPORT, self.handlers.OnImport)
        self.parent.Bind(EVT_COMMAND_EXPORT, self.handlers.OnExport)
        self.parent.Bind(EVT_COMMAND_APPROVE, self.handlers.OnApprove)
        
        # Print events
        
        self.parent.Bind(EVT_COMMAND_PRINT, self.handlers.OnPrint)
        
        # Clipboard events
        
        self.parent.Bind(EVT_COMMAND_CUT, self.handlers.OnCut)
        self.parent.Bind(EVT_COMMAND_COPY, self.handlers.OnCopy)
        self.parent.Bind(EVT_COMMAND_COPY_RESULT, self.handlers.OnCopyResult)
        self.parent.Bind(EVT_COMMAND_PASTE, self.handlers.OnPaste)
        
        # Grid view events
        
        self.parent.Bind(EVT_COMMAND_REFRESH_SELECTION, 
                  self.handlers.OnRefreshSelectedCells)
        self.parent.Bind(EVT_COMMAND_GOTO_CELL, self.handlers.OnGoToCell)
        self.parent.Bind(EVT_COMMAND_ZOOM, self.handlers.OnZoom)
        
        # Find events
        
        self.parent.Bind(EVT_COMMAND_FIND, self.handlers.OnFind)
        self.parent.Bind(EVT_COMMAND_REPLACE, self.handlers.OnShowFindReplace)
        
        # Grid change events
        
        self.parent.Bind(EVT_COMMAND_INSERT_ROWS, self.handlers.OnInsertRows)
        self.parent.Bind(EVT_COMMAND_INSERT_COLS, self.handlers.OnInsertCols)
        self.parent.Bind(EVT_COMMAND_INSERT_TABS, self.handlers.OnInsertTabs)
        
        self.parent.Bind(EVT_COMMAND_DELETE_ROWS, self.handlers.OnDeleteRows)
        self.parent.Bind(EVT_COMMAND_DELETE_COLS, self.handlers.OnDeleteCols)
        self.parent.Bind(EVT_COMMAND_DELETE_TABS, self.handlers.OnDeleteTabs)
        
        self.parent.Bind(EVT_COMMAND_RESIZE_GRID, self.handlers.OnResizeGrid)
        
        # Grid attribute events
        
        # Undo/Redo events

        self.parent.Bind(EVT_COMMAND_UNDO, self.handlers.OnUndo)
        self.parent.Bind(EVT_COMMAND_REDO, self.handlers.OnRedo)

class GridEventHandlers(object):
    """Contains grid event handlers"""
    
    def __init__(self, parent):
        self.main_window = parent
    
    # Grid cell events
    
    def OnText(self, event):
        """Text entry event handler"""
        
        code = event.GetString()
        
        if code != "":
            try:
                post_entryline_text(self, code)
            except TypeError: 
                post_entryline_text(self, "")
        
        event.Skip()
    
    def OnCellEditorShown(self, event):
        """Cell editor shown event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnCellEditorHidden(self, event):
        """Cell editor hidden event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnCellSelected(self, event):
        """Cell selection event handler"""
        
        raise NotImplementedError
        
        event.Skip()

    def OnMouseMotion(self, event):
        """Mouse motion event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    # File events
    
    def OnNew(self, event):
        """New grid event handler"""
        
        raise NotImplementedError
        
        event.Skip()

    def OnOpen(self, event):
        """File open event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnSave(self, event):
        """File save event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnSaveAs(self, event):
        """File save as event handler"""
        
        raise NotImplementedError
        
        event.Skip()
        
    def OnImport(self, event):
        """File import event handler"""
        
        raise NotImplementedError
        
        event.Skip()
        
    def OnExport(self, event):
        """File export event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnApprove(self, event):
        """File approve event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    # Print events
    
    def OnPrint(self, event):
        """Print event handler"""
        
        raise NotImplementedError
        
        event.Skip()

    # Clipboard events

    def OnCut(self, event): 
        """Clipboard cut event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnCopy(self, event):
        """Clipboard copy event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnCopyResult(self, event):
        """Clipboard copy results event handler"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnPaste(self, event):
        """Clipboard paste event handler"""
        
        raise NotImplementedError
        
        event.Skip()

    # Grid view events

    def OnGoToCell(self, event):
        """Shift a given cell into view"""
        
        raise NotImplementedError
        
        event.Skip()

    def OnRefreshSelectedCells(self, event):
        """Event handler for refreshing the selected cells via menu"""
        
        raise NotImplementedError
        
        event.Skip()
        
    def OnZoom(self, event):
        """Event handler for setting grid zoom via menu"""
        
        raise NotImplementedError
        
        event.Skip()
        
    def OnScroll(self, event):
        """Event handler for grid scroll event"""
        
        self.parent.MainGrid.view.clear()
        
        event.Skip()
    
    def OnContextMenu(self, event):
        """Context menu event handler"""
        
        raise NotImplementedError
        
        #self.PopupMenu(self.contextmenu)
        
        event.Skip()
    
    def OnMouseWheel(self, event):
        """Event handler for mouse wheel actions
        
        Invokes zoom when mouse when Ctrl is also pressed
        
        """
        
        if event.ControlDown():
            raise NotImplementedError
            
        event.Skip()
    
    # Find events

    def OnFind(self, event):
        """Find functionality should be in interfaces"""
        
        raise NotImplementedError
                
        event.Skip()
        
    def OnFindClose(self, event):
        """Refreshes the grid after closing the find dialog"""
        
        raise NotImplementedError
        
        event.Skip()

    def OnShowFindReplace(self, event):
        """Calls the find-replace dialog"""
        
        raise NotImplementedError
        
        event.Skip()

    # Grid change events
    
    def OnInsertRows(self, event):
        """Insert the maximum of 1 and the number of selected rows"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnInsertCols(self, event):
        """Inserts the maximum of 1 and the number of selected columns"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnInsertTabs(self, event):
        """Insert one table into MainGrid and pysgrid"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnDeleteRows(self, event):
        """Deletes rows from all tables of the grid"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnDeleteCols(self, event):
        """Deletes columnss from all tables of the grid"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnDeleteTabs(self, event):
        """Deletes tables"""
        
        raise NotImplementedError
        
        event.Skip()
    
    def OnResizeGrid(self, event):
        """Resizes current grid by appending/deleting rows, cols and tables"""
        
        raise NotImplementedError
        
        event.Skip()

    # Grid attribute events

    def OnRowSize(self, event):
        """Row size event handler"""
        
        raise NotImplementedError
        
        event.Skip()
        
    def OnColSize(self, event):
        """Column size event handler"""
        
        raise NotImplementedError
        
        event.Skip()

    # Undo/Redo events

    def OnUndo(self, event):
        """Calls the gris undo method"""
        
        raise NotImplementedError
        
        event.Skip()
        
    def OnRedo(self, event):
        """Calls the gris redo method"""
        
        raise NotImplementedError
        
        event.Skip()

    
# End of class GridEventHandlers
