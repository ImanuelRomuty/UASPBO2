from re import S
import wx
import noname
from MVCcreateFrame import CreateJual
from MVCCreateBeliFrame import CreatePembelian
from DataCustomer import DataCustomer
from DataObat import Obat
from DataSupplier import Supplier
from DataPembelian import Pembelian
from DataPenjualan import Penjualan

class main (noname.Menu):

    def __init__(self,parent):
        noname.Menu.__init__(self,None)
        
    def btn_melihat( self, event ):
        self.menu_panel.Destroy()
        sub = SubMenu(self).Show()

    def btn_jual( self, event ):
        frame = CreateJual()
        frame.Show()

    def btn_pembelian( self, event ):
        frame = CreatePembelian()
        frame.Show()

    def btn_exit( self, event ):
        exit()


class SubMenu (noname.Sub_Menu):

    def __init__(self,parent):
        noname.Sub_Menu.__init__(self, parent)
        self.customer = DataCustomer()
        self.obat = Obat()
        self.supplier = Supplier()
        self.parent = parent
        self.pembelian = Pembelian()
        self.penjualan = Penjualan()

    def btn_customer( self, event ):
        self.customer.Show()

    def btn_supplier( self, event ):
        self.supplier.Show()

    def btn_obat( self, event ):
        self.obat.Show()

    def btn_pembelian( self, event ):
        self.pembelian.Show()

    def btn_penjualan( self, event ):
        self.penjualan.Show() 

    def btn_kembali( self, event ):
        self.Destroy()
        self.parent.Destroy()
        main(self).Show()

if __name__ == '__main__':
    app = wx.App()
    frame = main (parent=None)
    frame.Show(True)
    app.MainLoop()