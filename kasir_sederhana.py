# Program Kasir Sederhana (update, bisa input harga pakai titik/koma)
print("=== Kasir Sederhana ===")
print("Masukkan daftar belanjaanmu")
print("Ketik 'selesai' kalau sudah selesai belanja.\n")

daftar_belanja = []
total = 0

while True:
    nama_barang = input("Nama barang: ")
    if nama_barang.lower() == "selesai":
        break
    try:
        harga_input = input("Harga barang (Rp): ")
        # Hilangkan titik/koma/strip biar bisa terbaca angka
        harga_input = harga_input.replace(".", "").replace(",", "")
        harga = float(harga_input)
        
        daftar_belanja.append((nama_barang, harga))
        total += harga
    except ValueError:
        print("⚠️ Masukkan harga berupa angka ya!")

print("\n=== Struk Belanja ===")
for barang, harga in daftar_belanja:
    print(f"- {barang}: Rp{harga:,.0f}")

print(f"\nTotal: Rp{total:,.0f}")

# Diskon 10% jika belanja di atas 100 ribu
if total > 100000:
    diskon = total * 0.10
    total_bayar = total - diskon
    print(f"Diskon 10%: Rp{diskon:,.0f}")
    print(f"Total Bayar: Rp{total_bayar:,.0f}")
else:
    print("Tidak ada diskon.")
    print(f"Total Bayar: Rp{total:,.0f}")

print("\nTerima kasih sudah belanja di toko kami! 😊")
