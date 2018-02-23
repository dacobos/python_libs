#PERSONAL PYTHON LIBRARIES BY DACOBOS

#1) LOG_HELPER.PY: This library redirects the stdoutput to a .log file

     Depends:
     sys library

     Arguments:
     String: Full path of logfile.log

     Usage:
     To start logging instance an object from the class Logger to the sys.stdout: sys.stdout = Logger(../logfile.log)
     To clear the logfile use: sys.stdout.clear(../logfile.log)

#2) FILE_HELPER.PY: This Library allows to select a file or folder for any python script, it depends on PythonQt4

     Depends: PyQt4 Library

     Arguments:
     String: 'file' or 'folder' keyword

     Usage:
     from file_helper import *
     f = select('file')
     Or
     f = select('folder')

     Returns: file or folder path

     Un official Windows binaries to install PyQt4 https://www.lfd.uci.edu/~gohlke/pythonlibs/pyqt4
     In the filenames cp27 means C-python version 2.7, cp35 means python 3.5, etc.
     C:\path\where\wheel\is\> pip install PyQt4-4.11.4-cp35-none-win_amd64.whl


#3) EXCEL_HELPER.PY This library simplify the reading and writing of excel files using the best combination of  xlrd and openpyxl

      Depends:
      xlrd, openpyxl
      Usage:
      from excel_helper import *


      Methods:

      read_data(filename)
      Arguments:
      filename: Full path of filename .xls or .xlsx to read the data
      Usage:
      data = read_data(../file.xlsx)

      Returns:
      Multilevel List with all the information of the xlsx file, where each element of the list corresponds to a row

-------------------------------------------------------------------------------------------------------------------

#getColumnId(data, columnName)

      Arguments:
      data - Multilevel list containing the xlsx file result of read_data method
      columnName - String with the name of the table header

      Usage:
      columnId = getColumnId(data, columnName)

      Returns:
      Integer number of position in the row inner list

-------------------------------------------------------------------------------------------------------------------

#getRowsByKey(data, key)

      Arguments:
      data - Multilevel list containing the xlsx file result of read_data method
      key - String with one particular name in the whole xlsx file that corresponds to a key
      Usage:
      rows = getRowsByKey(data, key)

      Returns:
      Dictionary with the key equals to key argument and value corresponds to a list with the row numbers where key was found in xlsx document

-------------------------------------------------------------------------------------------------------------------

#getRowsByColumn(data, columnId, value)

      Arguments:
      data - Multilevel list containing the xlsx file result of read_data method
      columnId - Integer with the specific position in row list to limit the search of value to the specific column, given by manual entry or return by getColumnId method.
      value - String with one particular value in an specific column given by columnId

      Usage:
      Rows =  getRowsByColumn(data, columnId, value)

      Returns:
      Different than getRowsByKey this method returns a list not a dictionary of the rows where the value was found on an specific column

-------------------------------------------------------------------------------------------------------------------

#getValues(data, rows)

      Arguments:
      data - Multilevel list containing the xlsx file result of read_data method
      rows - Dictionary return by getRowsByKey method

      Usage:
      values = getValues(data, rows)

      Returns:
      Multi level list with the values of each rows found by getRowsByKey

-------------------------------------------------------------------------------------------------------------------

#getCellValue(data, rowId, columnId)

      Arguments:
      data - Multilevel list containing the xlsx file result of read_data method
      rowId - Integer number that belongs to the row corresponding to the value, can be an element of the list obtained by getRowsByKey or getRowsbyColumn
      columnId - Integer with the specific position in row list to limit the search of value to the specific column, given by manual entry or return by getColumnId method.

      Usage:
      value = getCellValue(data, rowId, columnId)

      Returns:
      The value corresponding to the cell defined by rowId and columnId in the correspondig format (float, integer, boolean, string, etc)

-------------------------------------------------------------------------------------------------------------------

#updateCell(data, rowId, columnId, newValue)

      Arguments:
      data - Multilevel list containing the xlsx file result of read_data method
      rowId - Integer number that belongs to the row corresponding to the value, can be an element of the list obtained by getRowsByKey or getRowsbyColumn
      columnId - Integer with the specific position in row list to limit the search of value to the specific column, given by manual entry or return by getColumnId method.
      newValue - The value to replace the specific cell defined by rowId and columnId

      Usage:
      updateCell(data, rowId, columnId, newValue)

      Returns:
      None

-------------------------------------------------------------------------------------------------------------------

#readXlsxSheet(filename)

      Arguments:
      filename: Full path of filename .xls or .xlsx to read the data

      Usage:
      wb = readXlsxSheet(filename)

      Returns:
      Openpyxl Worksheet containing all the information of xlsx

-------------------------------------------------------------------------------------------------------------------

#writeXlsx(data, newfilename)

      Arguments:
      data - Multilevel list containing the xlsx file result of read_data method
      newfilename - Full path of the new filename to be written

      Usage:
      writeXlsx(data, newfilename)

      Returns:
      Writes the newfilename in xlsx format

-------------------------------------------------------------------------------------------------------------------

#duplicateXlsx(template_file, new_data_file)

      Arguments:
      template_file - Original xlsx to be cloned
      new_data_file - Multi level list with all the values to be written using the template_file

      Usage:
      duplicataXlsx(template_file, new_data_file)

      Returns:
      Openpyxl Workbook with all the information of the original xlsx file using the new_data_file multilevel list

-------------------------------------------------------------------------------------------------------------------

#saveWb(wb, newfilename)

      Arguments:
      wb - Openpyxl workbook with all xlsx information, posible returned by duplicataXlsx
      newfilename - newfilename - Full path of the new filename to be written

      Usage:

      Returns:

-------------------------------------------------------------------------------------------------------------------

#dataFromDic(dictionary,sheet_by_sub_key)

      Arguments:
      dictionary - Two level dictionary in format {'key1':{'sub_key1':[[],[],[]], 'sub_key2':[[],[],[]]}, 'key2':{'sub_key1':[[],[],[]], 'sub_key2':[[],[],[]]}}
      sheet_by_sub_key - Boolean variable if True the new xlsx file sheet names will be defined by sub_key if False
      sheetnames will be defined by key

      Usage:
      dataFromDic(dictionary, sheet_by_sub_key)

      Returns:
      Openpyxl Workbook with all the information of the original xlsx file using the new_data_file multilevel list
