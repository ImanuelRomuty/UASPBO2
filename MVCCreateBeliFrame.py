import wx
import noname
import model

class CreatePembelian (noname.CreatePembelianFrame):
    
    def __init__ (self):
        noname.CreatePembelianFrame.__init__(self,parent=None)
        self.TransaksiModel = model.Transaksi()
        self.id = None

    def SetId (self,id):
        self.id = id

    def SetNamaSupplier (self,nama_supplier):
        self.NamaSupplier.SetValue(nama_supplier)
    
    def SetAlamatSupplier (self,alamat_supplier):
        self.AlamatSupplier.SetValue(alamat_supplier)

    def SetTelpSupplier (self,telp_supplier):
        self.TelpSupplier.SetValue(telp_supplier)

    def SetNamaObat (self,nama_obat):
        self.NamaObat.SetValue(nama_obat)

    def SetStockObat (self,stok):
        self.StockObat.SetValue(stok)

    def simpan_event( self,event):
        nama_supplier = self.NamaSupplier.GetValue().strip()
        alamat_supplier = self.AlamatSupplier.GetValue().strip()
        telp_supplier = self.TelpSupplier.GetValue().strip()
        nama_obat = self.NamaObat.GetValue().strip()
        stok = self.StockObat.GetValue().strip()
        if len(nama_supplier) == 0:
            wx.MessageBox('An error occured.', style=wx.OK | wx.ICON_ERROR) 
        else:
           self.TransaksiModel.Beli(nama_supplier, alamat_supplier,telp_supplier,nama_obat,stok)
           wx.MessageBox('Bisa yee.', style=wx.OK | wx.ICON_INFORMATION)

    def batal_event( self, event ):
        self.Destroy()

