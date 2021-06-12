import wx
import noname
import model

class DataCustomer (noname.cobaFrame):
    
    def __init__(self):
        noname.cobaFrame.__init__(self,parent=None)
        self.CustomerModel = model.Customer()
        self.coloum_name =  ["id_customer","NamaCustomer","AlamatCustomer","TelpCustomer","Tanggal"]
        self.Coloumn()
        self.IsiCell()

    def Coloumn(self):
        for index,coloum in enumerate(self.coloum_name):
            self.gridcobs.SetColLabelValue(index,coloum)

    def IsiCell(self):
        customer = self.CustomerModel.select()
        for row,index in enumerate(customer):
            for col,colIndex in enumerate(self.coloum_name):
               self.gridcobs.SetCellValue(row, col, str(customer[row][col]))

    def destroy( self, event ):
        self.Hide()        
