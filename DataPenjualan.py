import wx
import noname
import model

class Penjualan (noname.cobaFrame):
    
    def __init__(self):
        noname.cobaFrame.__init__(self,parent=None)
        self.PenjualModel = model.Transaksi()
        self.coloum_name = ["IDPenjualan","NamaCustomer","NamaObat","qty","Tanggal"]
        self.Coloumn()
        self.IsiCell()

    def Coloumn(self):
        for index,coloum in enumerate(self.coloum_name):
            self.gridcobs.SetColLabelValue(index,coloum)

    def IsiCell(self):
        obat = self.PenjualModel.selectjual()
        for row,index in enumerate(obat):
            for col,colIndex in enumerate(self.coloum_name):
               self.gridcobs.SetCellValue(row, col, str(obat[row][col]))

    def destroy( self, event ):
        self.Hide()        
