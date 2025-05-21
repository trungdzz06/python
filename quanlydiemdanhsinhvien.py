import json

def tai_thong_tin_diem_danh():
    with open("diemdanh.json", "r", encoding="utf-8") as f:
        return json.load(f)

def luu_thong_tin_diem_danh(data):
    with open("diemdanh.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def tai_thong_tin():
    with open("dssv.json", "r", encoding="utf-8") as f:
        return json.load(f)

def luu_thong_tin(data):
    with open("dssv.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def them_lop_hoc():
    data = tai_thong_tin()
    so_lop = int(input("Nhập số lớp học cần thêm: "))
    for i in range(so_lop):
        lop = input(f"Nhập tên lớp học thứ {i + 1}: ")
        if lop in data:
            print("Lớp đã có trong danh sách lớp.")
        else:
            data[lop] = {}
            print(f"Đã lưu thông tin lớp {lop} thành công.")
        luu_thong_tin(data)

def them_sinh_vien():
    data = tai_thong_tin()
    lop = input("Nhập tên lớp cần thêm thông tin: ")
    if lop in data:
        so_sinh_vien = int(input(f"Nhập số sinh viên cần thêm cho lớp {lop}: "))
        for i in range(so_sinh_vien):
            print(f"Nhập thông tin sinh viên thứ {i + 1} của lớp {lop}.")
            msv = input("Nhập mã sinh viên: ")
            if msv not in data[lop]:
                ten_sinh_vien = input("Nhập tên sinh viên: ")
                ngay_sinh = input("Nhập ngày sinh: ")
                gioi_tinh = input("Nhập giới tính: ")
                sdt = input("Nhập số điện thoại: ")
                data[lop][msv] = {
                    "msv": msv,
                    "ten_sinh_vien": ten_sinh_vien,
                    "ngay_sinh": ngay_sinh,
                    "gioi_tinh": gioi_tinh,
                    "sdt": sdt
                }
                print(f"Thêm thành công sinh viên có mã sinh viên là {msv}")
                luu_thong_tin(data)
            else:
                print(f"Đã có sinh viên với mã số {msv} trong lớp {lop}.")
    else:
        print(f"Lớp {lop} không tồn tại trong danh sách lớp.")

def xoa_sinh_vien():
    data = tai_thong_tin()
    lop = input("Nhập lớp cần xóa sinh viên: ")
    if lop not in data:
        print("Lớp không tồn tại trong danh sách lớp.")
    else:
        so_sinh_vien = int(input(f"Nhập số sinh viên cần xóa trong lớp {lop}: "))
        for i in range(so_sinh_vien):
            sinh_vien = input(f"Nhập mã sinh viên cần xóa trong lớp {lop}: ")
            if sinh_vien not in data[lop]:
                print(f"Sinh viên không tồn tại trong lớp {lop} vui lòng kiểm tra lại mã sinh viên.")
            else:
                del data[lop][sinh_vien]
                print(f"Đã xóa sinh viên có mã {sinh_vien} khỏi lớp {lop}.")
    luu_thong_tin(data)
def hien_thi_danh_sach():
    data = tai_thong_tin()
    danh_sach_lop = list(data.items())
    i = 0
    while i < len(danh_sach_lop):
        lop, sinh_vien = danh_sach_lop[i]
        print(f"Danh sách sinh viên của lớp {lop}")
        danh_sach_sinh_vien = list(sinh_vien.items())
        j = 0
        while j < len(danh_sach_sinh_vien):
            mssv, thong_tin = danh_sach_sinh_vien[j]
            print(f"Mã sinh viên: {thong_tin["msv"]}")
            print(f"Tên: {thong_tin["ten_sinh_vien"]}")
            print(f"Ngày Sinh: {thong_tin["ngay_sinh"]}")
            print(f"Giới tính: {thong_tin["gioi_tinh"]}")
            print(f"Số điện thoại: {thong_tin["sdt"]}")
            print("--------------------")
            j += 1
        i += 1
def tim_kiem_sinh_vien():
    data = tai_thong_tin()
    lop_hoc = input("Nhập lớp cần tìm kiếm sinh viên: ")
    if lop_hoc not in data:
        print("Lớp không tồn tại trong danh sách lớp.")
    else:
            sinh_vien_find = input(f"Nhập mã sinh viên cần tìm kiếm trong lớp {lop_hoc}: ")
            if sinh_vien_find not in data[lop_hoc]:
                print(f"Không tìm thấy sinh viên có mã {sinh_vien_find} trong lớp {lop_hoc}.")
            else:
                print(f"Thông tin của sinh viên có mã sinh viên: {data[lop_hoc][sinh_vien_find]["msv"]}")
                print(f"Tên: {data[lop_hoc][sinh_vien_find]["ten_sinh_vien"]}")
                print(f"Ngày Sinh: {data[lop_hoc][sinh_vien_find]["ngay_sinh"]}")
                print(f"Giới tính: {data[lop_hoc][sinh_vien_find]["gioi_tinh"]}")
                print(f"Số điện thoại: {data[lop_hoc][sinh_vien_find]["sdt"]}")
                print("--------------------")      
def tao_buoi_diem_danh():
    data = tai_thong_tin_diem_danh()
    print("Nhập thông tin buổi học.")
    thoi_gian = input("Nhập ngày học (13/5/2025): ")
    ten_mon = input("Nhập tên môn học: ")
    so_lop = int(input("Nhập số lớp học tham gia: "))
    data[thoi_gian] = {}
    data[thoi_gian][ten_mon] = {}
    for i in range(so_lop):
        lop = input("Nhập tên lớp học tham gia:")
        data[thoi_gian][ten_mon][lop] = {}
        luu_thong_tin_diem_danh(data)
def diem_danh_thu_cong():
    data_diemdanh = tai_thong_tin_diem_danh()
    data = tai_thong_tin()
    ngay_hoc = input("Chọn buổi học cần điểm danh (20/02/2006): ")
    if ngay_hoc not in data_diemdanh:
        print("Không có ngày học này, vui lòng chọn ngày khác.")
    else:
        mon_hoc = input("Nhập tên môn học cần điểm danh: ")
        if mon_hoc not in data_diemdanh[ngay_hoc]:
            print("Môn học không tồn tại hoặc không có trong ngày hôm nay.")
        else:
            lop_hoc = input("Chọn lớp học cần điểm danh: ")
            if lop_hoc not in data_diemdanh[ngay_hoc][mon_hoc]:
                print("Lớp học không tồn tại hoặc không phải học trong ngày hôm nay.")
            else:
                lop_list = list(data.items())
                for i in range(2):
                    msv = input("Nhập mã sinh viên: ")
                    if msv not in data[lop_hoc]:
                        print(f"Sinh viên không tồn tại trong lớp {lop_hoc}.")
                    else:
                        if msv not in data_diemdanh[ngay_hoc][mon_hoc][lop_hoc]:
                            trang_thai = input("Nhập trạng thái (vắng, muộn, có mặt): ")
                            data_diemdanh[ngay_hoc][mon_hoc][lop_hoc][msv] = {
                                "msv" : int(msv),
                                "trang_thai" : trang_thai
                            }
                            luu_thong_tin_diem_danh(data_diemdanh)
                        else:
                            print("Sinh viên đã được điểm danh.")
def doc_diem_danh_tu_file():
    data = tai_thong_tin()
    data_diemdanh = tai_thong_tin_diem_danh()

    for ngay, mon_dict in data_diemdanh.items():
        print(f"\n=== Ngày: {ngay} ===")
        for mon_hoc, lop_dict in mon_dict.items():
            print(f"  --- Môn: {mon_hoc} ---")
            for lop_hoc, danh_sach_sv_diemdanh in lop_dict.items():
                print(f"Lớp: {lop_hoc}")
                if lop_hoc not in data:
                    print(f"Không tìm thấy lớp {lop_hoc} trong dữ liệu sinh viên.")
                    continue
                sinh_vien_lop = data[lop_hoc]
                for msv, sv_info in sinh_vien_lop.items():
                    if msv in danh_sach_sv_diemdanh:
                        trang_thai = danh_sach_sv_diemdanh[msv]["trang_thai"]
                        trang_thai = "chưa điểm danh"
                    print(f"      Mã SV {msv} - {sv_info['ten_sinh_vien']} - Trạng thái: {trang_thai}")
def cap_nhat_trang_thai():
    data = tai_thong_tin()
    data_diemdanh = tai_thong_tin_diem_danh()
    ngay = input("Nhập ngày điểm danh: ")
    mon_hoc = input("Nhập môn học: ")
    lop_hoc = input("Nhập lớp học: ")
    msv = int(input("Nhập mã sinh viên cần cập nhật: "))
    trang_thai_moi = input("Nhập trạng thái mới (có/vắng): ")

    if ngay not in data_diemdanh:
        print("Ngày không tồn tại trong dữ liệu điểm danh.")
    if mon_hoc not in data_diemdanh[ngay]:
        print("Môn học không tồn tại trong dữ liệu điểm danh.")
    if lop_hoc not in data_diemdanh[ngay][mon_hoc]:
        print("Lớp học không tồn tại trong dữ liệu điểm danh.") 
    data_diemdanh[ngay][mon_hoc][lop_hoc][msv] = {"msv": msv, "trang_thai": trang_thai_moi}
    print(f"Đã cập nhật trạng thái sinh viên {msv} thành '{trang_thai_moi}'.")
    luu_thong_tin_diem_danh(data_diemdanh)

def thong_ke_vang():
    data_diemdanh = tai_thong_tin_diem_danh()
    so_lan_vang = {}

    for ngay, mon_dict in data_diemdanh.items():
        for mon, lop_dict in mon_dict.items():
            for lop, sv_dict in lop_dict.items():
                for msv, info in sv_dict.items():
                    if info.get("trang_thai", "") == "vắng":
                        so_lan_vang[msv] = so_lan_vang.get(msv, 0) + 1

    print("Thống kê số lần vắng của sinh viên:")
    for msv, lan_vang in so_lan_vang.items():
        print(f"Mã SV {msv}: {lan_vang} lần vắng")

def xem_sinh_vien_vang_nhieu():
    data = tai_thong_tin()
    data_diemdanh = tai_thong_tin_diem_danh()
    so_lan_vang = {}

    for ngay, mon_dict in data_diemdanh.items():
        for mon, lop_dict in mon_dict.items():
            for lop, sv_dict in lop_dict.items():
                for msv, info in sv_dict.items():
                    if info.get("trang_thai", "").lower() == "vắng":
                        so_lan_vang[msv] = so_lan_vang.get(msv, 0) + 1


    danh_sach_vang_nhieu = sorted(so_lan_vang.items(), key=lambda x: x[1], reverse=True)

    print("Danh sách sinh viên vắng nhiều nhất:")
    for msv, lan_vang in danh_sach_vang_nhieu:
        ten_sv = None
        for lop, svs in data.items():
            if msv in svs:
                ten_sv = svs[msv].get("ten_sinh_vien")
                break
        print(f"Mã SV {msv} - Tên: {ten_sv} - Số lần vắng: {lan_vang}")

def xem_lich_su_diem_danh():
    data = tai_thong_tin()
    data_diemdanh = tai_thong_tin_diem_danh()
    msv = input("Nhập mã sinh viên cần xem lịch sử điểm danh: ").strip()
    print(f"Lịch sử điểm danh sinh viên {msv}:")

    for ngay, mon_dict in data_diemdanh.items():
        for mon, lop_dict in mon_dict.items():
            for lop, sv_dict in lop_dict.items():
                if msv in sv_dict:
                    trang_thai = sv_dict[msv].get("trang_thai", "chưa điểm danh")
                    print(f"Ngày {ngay} - Môn {mon} - Lớp {lop} - Trạng thái: {trang_thai}")

def xuat_bao_cao_ra_file():
    data = tai_thong_tin()
    data_diemdanh = tai_thong_tin_diem_danh()
    filename = input("Nhập tên file báo cáo (ví dụ: baocao.txt): ").strip()

    with open(filename, 'w', encoding='utf-8') as f:
        for ngay, mon_dict in data_diemdanh.items():
            f.write(f"=== Ngày: {ngay} ===\n")
            for mon, lop_dict in mon_dict.items():
                f.write(f"  --- Môn: {mon} ---\n")
                for lop, sv_dict in lop_dict.items():
                    f.write(f"    Lớp: {lop}\n")
                    for msv, info in sv_dict.items():
                        trang_thai = info.get("trang_thai", "chưa điểm danh")
                        f.write(f"      Mã SV {msv} - Trạng thái: {trang_thai}\n")

    print(f"Đã xuất báo cáo ra file {filename}")


def loc_theo_trang_thai():
    data = tai_thong_tin()
    data_diemdanh = tai_thong_tin_diem_danh()
    trang_thai_loc = input("Nhập trạng thái cần lọc (có/vắng): ").strip().lower()

    print(f"Danh sách sinh viên có trạng thái '{trang_thai_loc}':")
    for ngay, mon_dict in data_diemdanh.items():
        for mon, lop_dict in mon_dict.items():
            for lop, sv_dict in lop_dict.items():
                for msv, info in sv_dict.items():
                    if info.get("trang_thai", "").lower() == trang_thai_loc:
                        ten_sv = None
                        if lop in data and msv in data[lop]:
                            ten_sv = data[lop][msv].get("ten_sinh_vien")
                        print(f"Ngày {ngay} - Môn {mon} - Lớp {lop} - Mã SV {msv} - Tên: {ten_sv}")

def tim_chua_diem_danh():
    data = tai_thong_tin()
    data_diemdanh = tai_thong_tin_diem_danh()

    print("Danh sách sinh viên chưa được điểm danh:")
    for lop, sv_dict in data.items():
        for msv, sv_info in sv_dict.items():
            da_diem_danh = False
            for ngay, mon_dict in data_diemdanh.items():
                for mon, lop_dict in mon_dict.items():
                    if lop in lop_dict and msv in lop_dict[lop]:
                        da_diem_danh = True
                        break
                if da_diem_danh:
                    break
            if not da_diem_danh:
                print(f"Lớp {lop} - Mã SV {msv} - Tên: {sv_info.get('ten_sinh_vien')}")

if __name__ == "__main__":
    while True:
        print("\n===== MENU CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM DANH =====")
        print("1. Thêm lớp học")
        print("2. Thêm sinh viên vào lớp")
        print("3. Xóa sinh viên")
        print("4. Hiển thị danh sách sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Tạo buổi điểm danh mới")
        print("7. Điểm danh thủ công")
        print("8. Đọc dữ liệu điểm danh từ file")
        print("9. Cập nhật trạng thái điểm danh")
        print("10. Thống kê số buổi vắng")
        print("11. Xem sinh viên vắng nhiều hơn N buổi")
        print("12. Xem lịch sử điểm danh")
        print("13. Xuất báo cáo ra file")
        print("14. Lọc danh sách theo trạng thái")
        print("15. Tìm sinh viên chưa điểm danh")
        print("16. Tạo mã buổi học")
        print("17. Sắp xếp sinh viên")
        print("18. Xử lý ngoại lệ nhập sai")
        print("0. Thoát chương trình")
        choice = input("Chọn chức năng (0-19): ")
        if choice == '1':
            them_lop_hoc()
        elif choice == '2':
            them_sinh_vien()
        elif choice == '3':
            xoa_sinh_vien()
        elif choice == '4':
            hien_thi_danh_sach()
        elif choice == '5':
            tim_kiem_sinh_vien()
        elif choice == '6':
            tao_buoi_diem_danh()
        elif choice == '7':
            diem_danh_thu_cong()
        elif choice == '8':
            doc_diem_danh_tu_file()
        elif choice == '9':
            cap_nhat_trang_thai()
        elif choice == '10':
            thong_ke_vang()
        elif choice == '11':
            xem_sinh_vien_vang_nhieu()
        elif choice == '12':
            xem_lich_su_diem_danh()
        elif choice == '13':
            xuat_bao_cao_ra_file()
        elif choice == '14':
            loc_theo_trang_thai()
        elif choice == '15':
            tim_chua_diem_danh()
        elif choice == '16':
            tao_ma_buoi_hoc()
        elif choice == '17':
            sap_xep_sinh_vien()
        elif choice == '18':
            xu_ly_ngoai_le()
        elif choice == '0':
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")