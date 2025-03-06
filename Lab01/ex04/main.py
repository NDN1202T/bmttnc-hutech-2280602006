from QuanLySinhVien import QuanLySinhVien

def main():
    qlsv = QuanLySinhVien()
    
    while (True):
        print("\nCHUONG TRINH QUAN LY SINH VIEN")
        print("""
************************MENU*****************************
** 1. Them sinh vien.                                  **
** 2. Cap nhat thong tin sinh vien boi ID.             **
** 3. Xoa sinh vien boi ID.                            **
** 4. Tim kiem sinh vien theo ten.                     **
** 5. Sap xep sinh vien theo diem trung binh.          **
** 6. Sap xep sinh vien theo ten chuyen nganh.         **
** 7. Hien thi danh sach sinh vien.                    **
** 0. Thoat                                            **
*********************************************************
        """)
        
        key = int(input("Nhap tuy chon: "))
        
        if (key == 1):
            print("\n1. Thêm sinh viên.")
            qlsv.nhapSinhVien()
            print("\nThem sinh vien thanh cong!")
        
        elif (key == 2):
            if (qlsv.soLuongSinhVien() > 0):
                print("\n2. Cap nhat thong tin sinh vien.")
                print("Nhập ID: ")
                ID = int(input())
                if qlsv.updateSinhVien(ID):
                    print("\nCap nhat thong tin sinh vien thanh cong!")
                else:
                    print("\nKhong tim thay sinh vien voi ID:", ID)
            else:
                print("\nDanh sach sinh vien trong!")
        
        elif (key == 3):
            if (qlsv.soLuongSinhVien() > 0):
                print("\n3. Xoa sinh vien.")
                print("Nhập ID: ")
                ID = int(input())
                if (qlsv.deleteById(ID)):
                    print("\nSinh vien co id =", ID, "da bi xoa.")
                else:
                    print("\nSinh vien co id =", ID, "khong ton tai.")
            else:
                print("\nDanh sach sinh vien trong!")
        
        elif (key == 4):
            if (qlsv.soLuongSinhVien() > 0):
                print("\n4. Tim kiem sinh vien theo ten.")
                name = input("Nhap ten de tim kiem: ")
                searchResult = qlsv.findByName(name)
                qlsv.showSinhVien(searchResult)
            else:
                print("\nDanh sach sinh vien trong!")
        
        elif (key == 5):
            if (qlsv.soLuongSinhVien() > 0):
                print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
                qlsv.sortByDiemTB()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sach sinh vien trong!")
        
        elif (key == 6):
            if (qlsv.soLuongSinhVien() > 0):
                print("\n6. Sap xep sinh vien theo ten.")
                qlsv.sortByName()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sach sinh vien trong!")
        
        elif (key == 7):
            if (qlsv.soLuongSinhVien() > 0):
                print("\n7. Hien thi danh sach sinh vien.")
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sach sinh vien trong!")
        
        elif (key == 0):
            print("\nBan da chon thoat chuong trinh!")
            break
        
        else:
            print("\nKhong co chuc nang nay!")
            print("\nHay chon chuc nang trong hop menu.")

if __name__ == "__main__":
    main()