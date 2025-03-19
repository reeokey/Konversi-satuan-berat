# fungsi ini digunakan untuk mengknversi satuan berat
def konversi_satuan_berat(nilai,satuan_awal,satuan_tujuan,nama_user):
    
    # daftar satuan berat
    satuan_berat = {
        'ons':0.0311035,
        'kwintal':100,
        'ton':1000,
        'kg':1,
        'gram':0.001,
        'pound':0.453592,
        'lbs':0.453592
    }
    
    # validasi satuan
    if satuan_awal not in satuan_berat or satuan_tujuan not in satuan_berat:
        return "Satuan yang anda masukkan salah!"
    
    # konversi ke kilogram
    nilai_kg = nilai * satuan_berat[satuan_awal]
    
    # konversi dari kilogram ke satuan tujuan
    hasil = nilai_kg / satuan_berat[satuan_tujuan]
    
    # tampilkan hasil
    print(f"Hallo, {nama_user}!")
    print(f"{int(nilai)} {satuan_awal} setara dengan {int(hasil)} {satuan_tujuan}.")
    
    return hasil

# input dari user
nama = input("Masukkan Nama Anda: ")
nilai = float(input("Masukkan Nilai Berat: "))
satuan_awal = input("Masukkan Satuan Awal (ons,kwintal,ton,kg,gram,pound,lbs): ").lower()
satuan_tujuan = input("Masukkan Satuan Tujuan (ons,kwintal,ton,kg,gram,pound,lbs): ").lower()

# panggil fungsi konversi
hasil = konversi_satuan_berat(nilai,satuan_awal,satuan_tujuan,nama)