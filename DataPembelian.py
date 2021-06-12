import wx
import noname
import model

class Pembelian (noname.cobaFrame):
    
    def __init__(self):
        noname.cobaFrame.__init__(self,parent=None)
        self.PembelianModel = model.Transaksi()
        self.coloum_name = ["IDPenjualan","IdCustomer","NamaObat","qty","Tamggal"]
        self.Coloumn()
        self.IsiCell()

    def Coloumn(self):
        for index,coloum in enumerate(self.coloum_name):
            self.gridcobs.SetColLabelValue(index,coloum)

    def IsiCell(self):
        obat = self.PembelianModel.selectbeli()
        for row,index in enumerate(obat):
            for col,colIndex in enumerate(self.coloum_name):
               self.gridcobs.SetCellValue(row, col, str(obat[row][col]))

    def destroy( self, event ):
        self.Hide()        
