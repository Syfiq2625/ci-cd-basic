const tambah = require('./index');

// 1. Kita buat fungsi bernama 'jalankanTes' menggunakan JavaScript biasa
function jalankanTes() {
    console.log("Memulai pengujian logika kode...");
    
    // Periksa apakah fungsi tambah(2, 3) hasilnya 5
    if (tambah(2, 3) !== 5) {
        // Jika salah, lempar eror agar robot CI tahu kodenya gagal
        throw new Error("Tes Gagal: Hasil dari tambah(2, 3) bukan 5!");
    }
    
    // Jika benar, jalankan baris ini
    console.log("Tes Lolos! Perhitungan matematika benar.");
}

// 2. Panggil fungsi yang sudah kita buat di atas
jalankanTes();