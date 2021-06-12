import wx
import noname
import model

class CreateJual (noname.CreateFrame):

    def __init__ (self):
        noname.CreateFrame.__init__(self,parent=None)
        self.TransaksiModel = model.Transaksi()
        self.cek_stok = model.Obat()
        self.id = None

    def SetId (self,id):
        self.id = id

    def SetNamaCustomer (self,nama_customer):
        self.NamaCustomer.SetValue(nama_customer)
    
    def SetAlamatCustomer (self,alamat_customer):
        self.AlamatCustomer.SetValue(alamat_customer)

    def SetTelpCustomer (self,telp_customer):
        self.TelpCustomer.SetValue(telp_customer)

    def SetNamaObat (self,nama_obat):
        self.NamaObat.SetValue(nama_obat)

    def SetStockObat (self,stok):
        self.StockObat.SetValue(stok)

    def simpan_event( self,event):
        nama_customer = self.NamaCustomer.GetValue().strip()
        alamat_customer = self.AlamatCustomer.GetValue().strip()
        telp_customer = self.TelpCustomer.GetValue().strip()
        nama_obat = self.NamaObat.GetValue().strip()
        stok = self.StockObat.GetValue().strip()
        tampung = self.cek_stok.cek_stok(nama_obat)
        if len(nama_customer) == 0 or tampung <= int(stok) :
            wx.MessageBox('An error occured.','Gagal Kawan', style=wx.OK | wx.ICON_ERROR)
        else:
           self.TransaksiModel.Jual(nama_customer, alamat_customer,telp_customer,nama_obat,stok)
           wx.MessageBox('Bisa yee.','Bisa', style=wx.OK | wx.ICON_INFORMATION)

    def batal_event( self, event ):
        self.Hide()

# if __name__ == '__main__':
#     app = wx.App()
#     frame = CreateJual (parent=None)
#     frame.Show(True)
#     app.MainLoop()