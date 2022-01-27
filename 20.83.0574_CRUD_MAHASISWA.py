import mysql.connector as mysql

con = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password="",
    db = "db_akademik_0574"
)

dbcursor = con.cursor()
lanjutkan = True
while lanjutkan:
    print(35 * "=")
    print("MENU")
    print(35 * "=")
    print("1. Tampilan Mahasiswa")
    print("2. Tambah Mahasiswa")
    print("3. Ubah Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")
    print("")

    pilihan = int(input("PILIH MENU :"))
    print("")
    print("")
    if(pilihan == 1):
        sql = "SELECT * FROM tbl_students_0574"
        dbcursor.execute(sql)
        dt = dbcursor.fetchall()
        print("======================")
        print("(No, NIM, Nama, JK, Jurusan, Alamat)")
        for data in dt:
            print(data)

    elif(pilihan == 2):
        nomor = input("No :")
        NIM =  input("NIM :")
        nama = input("Nama :")
        jenis_kelamin = input("JK :")
        jurusan = input("Jurusan: ")
        alamat = input("Alamat: ")
        sql = "INSERT INTO tbl_students_0574 (nomor, NIM, nama, jenis_kelamin, jurusan, alamat VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nomor, NIM, nama, jenis_kelamin, jurusan, alamat)
        dbcursor.execute(sql, val)
        con.commit()
        print(dbcursor.rowcount, "data user berhasil ditambah")

    elif(pilihan == 3):
        nomor = input("Urutan Mahasiswa :")
        dbcursor.execute("SELECT * FROM tbl_students_0574 where id ="+id+" LIMIT 1")
        myresult = dbcursor.fetchall()
        mahasiswa = None
        for data in dt:
            mahasiswa = data
        if(mahasiswa != None):
            NIM = input("NIM ("+mahasiswa[1]+") :") or mahasiswa[1]
            nama = input("Nama ("+mahasiswa[2]+") :") or mahasiswa[2]
            jenis_kelamin = input("JK ("+mahasiswa[3]+") :") or mahasiswa[3]
            jurusan = input("Jurusan ("+mahasiswa[4]+") :") or mahasiswa[4]
            alamat = input("Alamat ("+mahasiswa[5]+") :") or mahasiswa[5]
            sql = "UPDATE mahasiswa SET NIM=%s, jenis_kelamin=%s, jurusan=%s, alamat=%s, WHERE nomor=%s"
            val = (nomor, NIM, nama, jenis_kelamin, jurusan, alamat)
            dbcursor.execute(sql, val)
            con.commit()
            print(dbcursor.rowcount, "data user berhasil disimpan")
        else:
            print("data tidak ditemukan")

    elif(pilihan == 4):
        nomor = input("Urutan Mahasiswa :")
        dbcursor.execute("SELECT * FROM mahasiswa where nomor ="+nomor+" LIMIT 1")
        myresult = dbcursor.fetchall()
        mahasiswa = None
        for data in dt:
            mahasiswa = data
        if(mahasiswa != None):
            print("MENGHAPUS DATA :",mahasiswa)
            sql = "DELETE FROM user WHERE nomor="+nomor
            dbcursor.execute(sql)
            con.commit()
            print(dbcursor.rowcount, "data user berhasil dihapus")
        else:
            print("data tidak ditemukan")
    elif(pilihan == 5):
        lanjut = False