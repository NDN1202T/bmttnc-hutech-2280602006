from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = int(self.listSinhVien[0]._id)
            for sv in self.listSinhVien:
                if (int(maxId) < int(sv._id)):
                    maxId = sv._id
            maxId = int(maxId) + 1
        return str(maxId)

    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def findByID(self, ID):
        search_result = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    search_result = sv
        return search_result

    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._bocluc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._bocluc = "Kha"
        elif (sv._diemTB >= 5):
            sv._bocluc = "Trung binh"
        else:
            sv._bocluc = "Yeu"

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<12} {:<8} {:<8}".format(
            "ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if (len(listSV) > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<12} {:<8} {:<8}".format(
                    sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._bocluc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien

    def example_usage(self, ID):
        if self.findByID(ID) is None:
            print("Sinh vien co ID {} khong ton tai.".format(ID))
        else:
            print("Sinh vien co ID {} ton tai.".format(ID))

# Ví dụ sử dụng
if __name__ == "__main__":
    qlsv = QuanLySinhVien()
    # Thêm sinh viên
    qlsv.nhapSinhVien()
    qlsv.nhapSinhVien()
    
    # Sắp xếp và hiển thị
    qlsv.sortByDiemTB()
    qlsv.showSinhVien(qlsv.getListSinhVien())
    
    # Tìm kiếm và xóa
    qlsv.example_usage("1")
    qlsv.deleteById("1")
    qlsv.example_usage("1")