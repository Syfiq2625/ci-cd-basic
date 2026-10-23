const tambah = require('./index');

test('Menguji 2 + 3 harus menghasilkan 5', () => {
    if (tambah(2, 3) !== 5) {
        throw new Error("Tes Gagal: Hasilnya bukan 5!");
    }
    console.log("Tes Lolos! Perhitungan benar.");
});

test()