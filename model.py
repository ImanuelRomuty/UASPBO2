from ConnectDB import connection
from datetime import datetime as dt

class Customer(connection):
    def __init__ (self):
        super().__init__()
        
    def select (self):
        query = str("SELECT * FROM customer ")
        result = self.select_all(query)
        return result
        
    def insertData(self,nama_customer,alamat_customer,telp_customer):
        query = ("INSERT INTO CUSTOMER (nama_customer, alamat_customer,telp_customer,Tanggal) VALUES(%s, %s, %s, %s)")
        value = (nama_customer, alamat_customer,telp_customer, dt.now())
        result = self.execute(query,value)
        return result
        
    def deleteData(self):
        ID = int
        query = "DELETE from Customer where id_customer=%s"
        value = (ID,)
        result = self.execute(query,value)
        return result

class Obat(connection):
    def __init__ (self):
        super().__init__()

    def select (self):
        query = ("SELECT * FROM Obat ")
        result = self.select_all(query)
        return result

    def insertData(self,nama_obat,stok):
        query = ("INSERT INTO Obat (nama_obat, stok) VALUES(%s, %s)")
        value = (nama_obat, stok)
        result = self.execute(query,value)
        return result
        
    def deleteData(self):
        ID = int
        query = "DELETE from Obat where id_obat=%s"
        value = (ID)
        result = self.execute(query,value)
        return result

    def cek_obat(self,nama_obat):
        query = "SELECT nama_obat FROM obat WHERE nama_obat=%s"
        value = (nama_obat,)
        res = self.select_one(query,value)
        if res != None:
            return True
        else :
            return False

    def cek_stok(self,nama_obat):
        query = "SELECT stok FROM obat WHERE nama_obat=%s"
        value = (nama_obat,)
        res = self.select_one(query,value)
        if res != None:
            # print(type(res[0]))
            return int(res[0])

    
class Supplier(connection):
    def __init__ (self):
        super().__init__()

    def select (self):
        query = ("SELECT * FROM Supplier ")
        result = self.select_all(query)
        return result

    def insertData(self,nama_supplier,alamat_supplier,telp_supplier):
        query = ("INSERT INTO Supplier (nama_supplier, alamat_supplier,telp_supplier,Tanggal) VALUES(%s, %s, %s, %s)")
        value = (nama_supplier, alamat_supplier,telp_supplier,dt.now())
        result = self.execute(query,value)
        return result

    def deleteData(self):
        self.select()
        ID = int(input("Pilih ID : "))
        query = "DELETE from Supplier where id_supplier=%s"
        value = (ID,)
        Choosing = str(input("Apakah anda yakin ingin menghapus data tersebut? [No/Yes] : ")).lower()
        if Choosing == "yes":
            self.execute(query,value)
            print("Done")
        else:
            print("Error")

class Transaksi(Obat,Supplier,Customer):

    def Beli(self,nama_supplier,alamat_supplier,telp_supplier,nama_obat,stok):
        Supplier().insertData(nama_supplier,alamat_supplier,telp_supplier)
        qty = stok
        
        if Obat().cek_obat(nama_obat) == False:        
            try :
                Obat().insertData(nama_obat,stok)
                query = "INSERT INTO pembelian (nama_supplier,nama_obat,qty)   VALUES( %s,%s,%s)"
                value = (nama_supplier,nama_obat,qty)
                self.execute(query,value)
            except Exception as e:
                return e
        else:
            try:
                try:
                    query = "SELECT stok  FROM obat WHERE nama_obat=%s"
                    value = (nama_obat,)
                    res = self.select_one(query,value)
                except Exception:
                    print("Error")
                stok = int(stok) + int(res[0])
                stok = str(stok)
                sql = "UPDATE obat SET stok=%s where nama_obat=%s "
                value = (stok,nama_obat)
                self.execute(sql,value)

                query = "INSERT INTO pembelian (nama_supplier,nama_obat,qty) VALUES(%s,%s,%s)"
                value = (nama_supplier,nama_obat,qty)
                self.execute(query,value)

            except Exception as e:
                return e


    def Jual(self,nama_customer,alamat_customer,telp_customer,nama_obat,stok):
        allquery = Customer().insertData(nama_customer,alamat_customer,telp_customer)
        qty = stok
        try:
            if Obat().cek_obat(nama_obat) == True:
                try:
                    try:
                        query = "SELECT stok FROM obat WHERE nama_obat=%s"
                        value = (nama_obat,)
                        res = self.select_one(query,value)
                    except Exception as e:
                        return e 
                    stok = int(res[0]) - int(stok)
                    if stok >= 0 : 
                        stok = str(stok)
                        sql = "UPDATE obat SET stok=%s where nama_obat=%s "
                        value = (stok,nama_obat)
                        self.execute(sql,value)
                        try:
                            query = "SELECT id_customer from customer where nama_customer =%s"
                            value = (nama_customer,)
                            res = self.select_one(query,value)
                        except Exception as e:
                            return e
                        query = "INSERT INTO penjualan (id_customer,nama_obat,qty)   VALUES(%s,%s,%s)"
                        value = (res[0],nama_obat,qty)
                        self.execute(query,value)
                    else :
                        try:
                            query = 'DELETE FROM Customer where nama_customer=%s'
                            value = (allquery,)
                            self.execute(query,value)
                        except Exception as e:
                           return e                     
                except Exception as e:
                    return e
            else:
                try:
                    query = 'DELETE FROM Customer where nama_customer=%s'
                    value = (allquery,)
                    self.execute(query,value)
                except Exception as e:
                    return e 
                try:
                    query = "SELECT id_customer from customer where nama_customer =%s"
                    value = (nama_customer,)
                    res = self.select_one(query,value)
                except Exception:
                    print("Error")
                query = "INSERT INTO penjualan (id_customer,nama_obat,qty)   VALUES(%s,%s,%s)"
                value = (res[0],nama_obat,qty)
                self.execute(query,value)
        except Exception:
            print("Error")            
        query = "DELETE FROM obat WHERE stok<=0"
        self.execute_abis(query)
    
    def selectbeli (self):
        query = "select * from pembelian"
        result = self.select_all(query)
        return result


    def selectjual (self):
        query = ("SELECT penjualan.no_penjualan, customer.nama_customer, penjualan.nama_obat , penjualan.qty , penjualan.tg_jual FROM penjualan inner join customer on penjualan.id_customer = customer.id_customer ")
        result = self.select_all(query)
        return result

# Obat().cek_stok("halo")