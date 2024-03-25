# Konversi bilangan
def konversi_bilangan(bilangan, basis_awal, basis_tujuan):
    if basis_awal == 'biner':
        if basis_tujuan == 'desimal':
            return int(bilangan, 2)
        elif basis_tujuan == 'oktal':
            return oct(int(bilangan, 2))[2:]
        elif basis_tujuan == 'heksadesimal':
            return hex(int(bilangan, 2))[2:]
    elif basis_awal == 'oktal':
        if basis_tujuan == 'desimal':
            return int(bilangan, 8)
        elif basis_tujuan == 'biner':
            return bin(int(bilangan, 8))[2:]
        elif basis_tujuan == 'heksadesimal':
            return hex(int(bilangan, 8))[2:]
    elif basis_awal == 'desimal':
        if basis_tujuan == 'biner':
            return bin(int(bilangan))[2:]
        elif basis_tujuan == 'oktal':
            return oct(int(bilangan))[2:]
        elif basis_tujuan == 'heksadesimal':
            return hex(int(bilangan))[2:]
    elif basis_awal == 'heksadesimal':
        if basis_tujuan == 'desimal':
            return int(bilangan, 16)
        elif basis_tujuan == 'biner':
            return bin(int(bilangan, 16))[2:]
        elif basis_tujuan == 'oktal':
            return oct(int(bilangan, 16))[2:]

# Input dari pengguna
bilangan = input("Masukkan bilangan: ")
basis_awal = input("Masukkan basis bilangan (biner/oktal/desimal/heksadesimal): ")
basis_tujuan = input("Masukkan basis tujuan (biner/oktal/desimal/heksadesimal): ")

# Konversi dan cetak hasil
hasil_konversi = konversi_bilangan(bilangan, basis_awal, basis_tujuan)
print("Hasil konversi:", hasil_konversi)