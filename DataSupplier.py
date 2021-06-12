import wx
import noname
import model

class Supplier (noname.cobaFrame):
    
    def __init__(self):
        noname.cobaFrame.__init__(self,parent=None)
        self.SupplierModel = model.Supplier()
        self.coloum_name = ["id_supplier","NamaSupplier","AlamatSupplier","TelpSupplier","Tanggal"]
        self.Coloumn()
        self.IsiCell()

    def Coloumn(self):
        for index,coloum in enumerate(self.coloum_name):
            self.gridcobs.SetColLabelValue(index,coloum)

    def IsiCell(self):
        supplier = self.SupplierModel.select()
        for row,index in enumerate(supplier):
            for col,colIndex in enumerate(self.coloum_name):
               self.gridcobs.SetCellValue(row, col, str(supplier[row][col]))

    def destroy( self, event ):
        self.Hide()        
