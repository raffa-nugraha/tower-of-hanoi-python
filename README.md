# Tower of Hanoi Menggunakan Python

## Deskripsi
Tower of Hanoi adalah permainan matematika yang bertujuan memindahkan piringan dari tiang asal ke tiang tujuan dengan bantuan tiang lainnya. Program ini dibuat menggunakan bahasa pemrograman Python dengan menerapkan algoritma rekursi.

## Tujuan
Memahami penerapan algoritma rekursi dalam menyelesaikan permasalahan Tower of Hanoi.

## Aturan Permainan
1. Hanya satu piringan yang boleh dipindahkan dalam satu langkah.
2. Hanya piringan paling atas yang boleh dipindahkan.
3. Piringan yang lebih besar tidak boleh diletakkan di atas piringan yang lebih kecil.

## Cara Kerja Program
Program menggunakan fungsi `tower_of_hanoi()` dengan parameter jumlah piringan, tiang asal, tiang bantuan, dan tiang tujuan.

Proses penyelesaian dilakukan melalui tiga langkah:
1. Memindahkan piringan-piringan di atasnya ke tiang bantuan.
2. Memindahkan piringan terbesar ke tiang tujuan.
3. Memindahkan piringan dari tiang bantuan ke tiang tujuan.

Proses tersebut dilakukan secara rekursif hingga semua piringan berpindah ke tiang tujuan.

## Hasil Program
Program menggunakan tiga piringan dan memindahkannya dari tiang A ke tiang C dengan bantuan tiang B. Jumlah minimum perpindahan yang diperlukan adalah tujuh langkah.

Rumus jumlah minimum perpindahan:

T(n) = 2^n - 1

Untuk tiga piringan:

T(3) = 2^3 - 1 = 7 langkah.

## Kesimpulan
Program Tower of Hanoi menunjukkan penerapan algoritma rekursi menggunakan Python. Dengan membagi permasalahan menjadi langkah-langkah yang lebih kecil, seluruh piringan dapat dipindahkan dari tiang asal ke tiang tujuan sesuai aturan permainan.
