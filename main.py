def tower_of_hanoi(n, asal, bantuan, tujuan):
    if n == 1:
        print(f"Pindahkan piringan 1 dari {asal} ke {tujuan}")
        return

    tower_of_hanoi(n - 1, asal, tujuan, bantuan)

    print(f"Pindahkan piringan {n} dari {asal} ke {tujuan}")

    tower_of_hanoi(n - 1, bantuan, asal, tujuan)


# Program utama
jumlah_piringan = 3

print("Solusi Tower of Hanoi:")
tower_of_hanoi(jumlah_piringan, "A", "B", "C")
