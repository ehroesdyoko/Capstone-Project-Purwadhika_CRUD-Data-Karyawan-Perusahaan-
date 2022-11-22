#Capstone Project Module 1 - Erlangga Hario Roesdyoko
#Study Case: Data Karyawan

#Struktur Data pada Capstone Project ini adalah Dictionary dalam List, yang terdiri dari variable NIP (primary key), Nama, No HP, Domisili, Gender
#Primary Key memiliki syarat seperti: Angka/Integer, terdiri dari 6 digit, 2 digit pertama menjelaskan Tahun pegawai masuk sehingga tidak bisa lebih besar dari '22'
DataPegawai = [{'NIP' : 220601, 'Nama' : 'Budiman Amano', 'No HP': 6281316861130, 'Domisili': 'Jakarta', 'Gender' : 'Male'}, 
{'NIP' : 220702, 'Nama' : 'Abdul Husen', 'No HP': 6281316861131, 'Domisili': 'Bekasi', 'Gender': 'Male'}, 
{'NIP' : 210201, 'Nama' : 'Cindy Candy', 'No HP': 6281316861132, 'Domisili': 'Tangerang', 'Gender' : 'Female'}, 
{'NIP' : 210502, 'Nama' : 'Buna Bonita', 'No HP': 6281316861133, 'Domisili': 'Jakarta', 'Gender' : 'Female'}, 
{'NIP' : 210703, 'Nama' : 'Arman Mandou', 'No HP': 6281316861134, 'Domisili': 'Depok', 'Gender' : 'Male'}]

#Function Read digunakan untuk membaca Data berdasarkan Primary Key atau Semua
def Read():
    while True:
        read_command = (input('''
Selamat Datang pada Menu Read Database Pegawai
Pilih opsi fungsi Read dengan keterangan sebagai berikut:
1. All Data Pegawai
2. Data Pegawai berdasarkan NIP
3. Kembali ke Menu Utama

Masukkan Nomor berdasarkan fungsi yang ingin dijalankan :
'''))
        try:
            read_command = int(read_command)
            if (read_command) == 1: #menampilkan semua Data
                Read_Data_Pegawai()
            elif (read_command) == 2:
                read_NIP = (input('\nMasukkan No NIP (6 Digit) : '))
                if DataPegawai == []: #menampilkan 1 Data berdasarkan NIP/Primary Key
                    print('\nData tidak ditemukan. Kembali ke Menu Read.')
                else:
                    for i in DataPegawai: #mencocokan data pada input (NIP) dengan NIP Database Pegawai
                        if len(read_NIP) == 6 and int(read_NIP) < 230000:
                            while i['NIP'] == int(read_NIP):
                                index = len(DataPegawai) + 1
                                read_NIP = ()
                                while index > 0:
                                    index -= 1
                                    try:
                                        print('\nData Pegawai PT Maju Mundur Maju\n') 
                                        print('NIP  \t| Nama  \t| No HP \t| Domisili \t| Gender \t')
                                        print('{}\t| {}\t| {}\t| {}   \t| {}'.format(i['NIP'], i['Nama'], i['No HP'], i['Domisili'], i['Gender']))
                                        read_NIP = ()
                                        read_command = ()
                                        break
                                    except:
                                        print('Data tidak ada di dalam Database Pegawai.')
                                        print('\nBerikut adalah hasil query NIP input terakhir.')
                                        read_command = ()
                                        read_NIP = ()
                                        break
                                else:
                                    read_command = ()
                                    read_NIP = ()
                                    break
                        else:
                            print('\nHarap masukkan input dengan Angka dan NIP yang sesuai.')
                            print('\nKembali ke Fungsi Read.\n')
                            read_command = ()
                            read_NIP = ()
                            break
                    else:
                        print('\nData tidak ada di dalam Database Pegawai.')
                        print('\nKembali ke Fungsi Read.\n')
                        read_NIP = ()
            elif (read_command) == 3: #kembali ke Menu Utama
                print('\nKembali ke Menu Utama.')
                break
            else:
                print('\nHarap masukkan input dengan Angka yang sesuai.')
                print('\nKembali ke Fungsi Read.\n')
                read_command = ()
        except:
            read_command = ()
        

#Function dibawah adalah function tambahan untuk menampilkan seluruh Data Pegawai
def Read_Data_Pegawai():
    if DataPegawai != []:
        print('Data Pegawai PT Maju Mundur Maju\n')
        print('No\t| NIP     \t| Nama   \t| No HP \t| Domisili \t| Gender \t')
        for i in range(len(DataPegawai)):
            print('{}\t| {}\t| {}\t| {}\t| {}   \t| {}\t'.format(i+1,DataPegawai[i]['NIP'], DataPegawai[i]['Nama'], DataPegawai[i]['No HP'], DataPegawai[i]['Domisili'], DataPegawai[i]['Gender']))
    elif DataPegawai == []:
        print('\nTidak Ada Data')

#Function Create digunakan untuk menambahkan data pada Dataset dengan syarat data tersebut tidak Duplikat pada Primary Key
def Create_Data():
    while True: 
        Read_Data_Pegawai
        create = (input('''
Selamat Datang pada Menu Create Data Pegawai
Pilih opsi fungsi Create dengan keterangan sebagai berikut:
1. Create Data Baru
2. Kembali ke Halaman Utama
    
Masukkan Nomor berdasarkan fungsi yang ingin dijalankan :
'''))
        try:
            create = int(create)
            if create == 1: #menambahkan Data Baru
                read_NIP = (input('\nMasukkan No NIP (6 Digit) : '))
                if len(read_NIP) == 6: #NIP harus terdiiri dari 6 digit
                    for i in DataPegawai:
                        if int(read_NIP) < 230000: #2 digit awal pada NIP tidak boleh melewati 23, karena 2 digit awal adalah Tahun
                            while i['NIP'] == int(read_NIP):
                                print('\nData duplikat, kembali ke Menu Create.')
                                return Create_Data()

                    else:
                        print(f'Menginput data baru {read_NIP}') 
                        namaPegawai = input('Masukkan Nama Pegawai : ') #Input Nama data baru
                        namaPegawai = namaPegawai.title()
                        noHP = (input('Masukkan No HP : 62')) #Input No HP data baru, memulai no HP dengan 62
                        ceknoHP = noHP.isnumeric() #no HP harus terdiri dari Angka
                        if ceknoHP == True: 
                            pass
                        else:
                            print('\nNo HP hanya boleh terdiri dari Angka.\n')
                            noHP = (input('Masukkan No HP : 62'))
                        tempattinggal = input('Tempat tinggal sekarang : ') #Input Domisili
                        tempattinggal = tempattinggal.title()
                        while True: #Input Gender
                            gender = (input('''\n
Gender:
1. Male
2. Female
                    
Masukkan Angka sesuai Gender: 
'''))                       
                            try:
                                if gender == '': 
                                    print('Gender wajib diisi. Harap isi kembali.')
                                elif int(gender) == 2: #apabile gender Female
                                    gender = 'Female'
                                    print('Gender = Female')
                                    kode = '62'
                                    databaru = {'NIP': int(read_NIP),'Nama': namaPegawai,'No HP': int(kode+noHP),'Domisili': tempattinggal, 'Gender' : gender}
                                    print('NIP  \t| Nama  \t| No HP \t| Domisili \t| Gender \t')
                                    print('{}\t| {}\t| {}\t| {}   \t| {}'.format(databaru['NIP'], databaru['Nama'], databaru['No HP'], databaru['Domisili'], databaru['Gender']))
                                    konfirmasi = input('Ketika ya jika ingin menyimpan Data baru : ') #konfirmasi untuk menyimpan Data baru pada Database Pegawai
                                    konfirmasi = konfirmasi.upper()
                                    if konfirmasi == 'YA': 
                                        DataPegawai.append(databaru)      
                                        print('\nData terbaru sudah di update ke database.')
                                        Read_Data_Pegawai()
                                        return Create_Data()

                                    else :
                                        print('\nData tidak disimpan. Kembali ke Menu Create.')
                                        return Create_Data()
                                        
                                elif int(gender) == 1: #apabile gender Male
                                    gender = 'Male'
                                    print('Gender = Male')
                                    kode = '62'
                                    databaru = {'NIP': int(read_NIP),'Nama': namaPegawai,'No HP': int(kode+noHP),'Domisili': tempattinggal, 'Gender' : gender}
                                    print('NIP  \t| Nama  \t| No HP \t| Domisili \t| Gender \t')
                                    print('{}\t| {}\t| {}\t| {}   \t| {}'.format(databaru['NIP'], databaru['Nama'], databaru['No HP'], databaru['Domisili'], databaru['Gender']))
                                    konfirmasi = input('Ketika ya jika ingin menyimpan Data baru : ') #konfirmasi untuk menyimpan Data baru pada Database Pegawai
                                    konfirmasi = konfirmasi.upper()
                                    if konfirmasi == 'YA':
                                        DataPegawai.append(databaru)      
                                        print('\nData terbaru sudah di update ke database.')
                                        Read_Data_Pegawai()
                                        return Create_Data()
                                    else :
                                        print('\nData tidak disimpan. Kembali ke Menu Create.')
                                        return Create_Data()
                                else:
                                    print('Input yang anda masukkan tidak sesuai. Harap isi kembali.')
                            except:
                                print('Input yang anda masukkan tidak sesuai. Harap isi kembali.')
                else:
                    print(f'Data yang anda input adalah berikut: {read_NIP}. Data tidak sesuai dengan ketentuan.')
                    print('NIP terdiri dari 6 digit dan 2 digit awal adalah tahun Pegawai masuk.')
                    print('Kembali ke Fungsi Create.')
                    create = ()
            elif create == 2:
                print('\nKembali ke Menu Utama.\n')
                break
            else:
                print('\nHarap masukkan input dengan Angka yang sesuai.')
                print('\nKembali ke Fungsi Create.\n')
                create = ()
    
        except:
            print('\nHarap masukkan input dengan Angka yang sesuai.')
            print('\nKembali ke Fungsi Create.\n')
            create = ()
    
      
#Fungsi Update untuk mengganti variable pada data existing berdasarkan NIP, termasuk Data NIP (Primary Key), setiap update akan di konfirmasi
def Update_Data():
    while True:
        Read_Data_Pegawai()
        konfirmasi = input('''
Selamat Datang pada Menu Update Data Pegawai
Pilih opsi fungsi Create dengan keterangan sebagai berikut:
1. Update Data
2. Kembali ke Halaman Utama
    
Masukkan Nomor berdasarkan fungsi yang ingin dijalankan :
''')
        try:
            konfirmasi = int(konfirmasi)
            if konfirmasi == 1:
                read_NIP = (input('\nMasukkan No NIP (6 Digit) yang ingin diupdate: '))
                if len(read_NIP) == 6:
                    for i in DataPegawai:
                        if int(read_NIP) < 230000:
                            while i['NIP'] == int(read_NIP):                       
                                index = len(DataPegawai) + 1
                                while index > 0:
                                    index -= 1
                                    Read_Data_Pegawai()
                                    print('''
Pilih jenis data yang ingin di Update:
1. NIP
2. Nama
3. No HP
4. Domisili
5. Gender
6. Kembali ke Fungsi Update

Masukkan angka jenis data yang ingin diupdate
''') 
                                    jenisupdate = input()
                                    try:
                                        jenisupdate = int(jenisupdate)
                                        if int(jenisupdate) == 1:
                                            NIP = (input('Masukkan NIP terbaru (6 Digit) : '))
                                            if len(NIP) == 6:
                                                print(f'\nNIP baru: \033[1;32;40m {NIP}\033[00m')
                                                konfirmasi = input('\nKetik Ya jika ingin menyimpan update ke Database : ')
                                                konfirmasi = konfirmasi.upper()
                                                if konfirmasi == 'YA':
                                                    i['NIP'] = int(NIP)
                                                    print('\nData telah tersimpan.\n')
                                                    jenisupdate = ()
                                                    continue
                                                else:
                                                    jenisupdate = ()
                                                    continue
                                            else:
                                                print('\nInput tidak sesuai dengan ketentuan NIP.')
                                                print('\nKembali ke Pilihan Data yang ingin di Update\n')
                                                jenisupdate = ()
                                                continue
                                        elif int(jenisupdate) == 2:
                                            Nama = input('Masukkan Nama yang sesuai : ')
                                            Nama = Nama.title()
                                            print(f'\nNama baru: \033[1;32;40m {Nama}\033[00m')
                                            konfirmasi = input('\nKetik Ya jika ingin menyimpan update ke Database : ')
                                            konfirmasi = konfirmasi.upper()
                                            if konfirmasi == 'YA':
                                                i['Nama'] = (Nama)
                                                print('\nData telah tersimpan.\n')
                                                jenisupdate = ()
                                                continue
                                            else:
                                                jenisupdate = ()
                                                continue
                                        elif int(jenisupdate) == 3:
                                            no_HP = (input('Masukkan No HP yang sesuai : 62')) 
                                            kode = '62'
                                            final = int(kode+no_HP)
                                            print(f'\nNo HP baru: \033[1;32;40m {final}\033[00m')
                                            konfirmasi = input('\nKetik Ya jika ingin menyimpan update ke Database : ')
                                            konfirmasi = konfirmasi.upper()
                                            if konfirmasi == 'YA':
                                                i['No HP'] = (final)
                                                print('\nData telah tersimpan.\n')
                                                jenisupdate = ()
                                                continue
                                            else:
                                                jenisupdate = ()
                                                continue
                                        elif int(jenisupdate) == 4:
                                            Domisili = input('Masukkan Domisili yang sesuai : ')
                                            Domisili = Domisili.title()
                                            print(f'\nDomisili baru: \033[1;32;40m {Domisili}\033[00m')
                                            konfirmasi = input('\nKetik Ya jika ingin menyimpan update ke Database : ')
                                            konfirmasi = konfirmasi.upper()
                                            if konfirmasi == 'YA':
                                                i['Domisili'] = (Domisili)
                                                print('\nData telah tersimpan.\n')
                                                jenisupdate = ()
                                                continue
                                            else:
                                                jenisupdate = ()
                                                continue
                                        elif int(jenisupdate) == 5:
                                            gender = (input('''\n
Gender:
1. Male
2. Female
                    
Masukkan Angka sesuai Gender: 
'''))
                                            if gender == '':
                                                print('Gender wajib diisi. Harap isi kembali.')
                                            elif int(gender) == 2:
                                                gender = 'Female'
                                                print('Gender = \033[1;32;40m Female\033[00m')
                                                konfirmasi = input('\nKetik Ya jika ingin menyimpan update ke Database : ')
                                                konfirmasi = konfirmasi.upper()
                                                if konfirmasi == 'YA':
                                                    i['Gender'] = (gender)
                                                    print('\nData telah tersimpan.\n')
                                                    jenisupdate = ()
                                                    continue
                                                else:
                                                    jenisupdate = ()
                                                    continue
                                            elif int(gender) == 1:
                                                gender = 'Male'
                                                print('Gender = \033[1;32;40m Male\033[00m')
                                                konfirmasi = input('\nKetik Ya jika ingin menyimpan update ke Database : ')
                                                konfirmasi = konfirmasi.upper()
                                                if konfirmasi == 'YA':
                                                    i['Gender'] = (gender)
                                                    print('\nData telah tersimpan.\n')
                                                    jenisupdate = ()
                                                    continue
                                                else:
                                                    jenisupdate = ()
                                                    continue
                                            else:
                                                print('\nAngka yang diinput tidak sesuai.\n')
                                                jenisupdate = ()
                                        elif int(jenisupdate) == 6:
                                            print('\nKembali ke Fungsi Update.\n')
                                            jenisupdate = ()
                                            return Update_Data()
                                    except:
                                        print('\nHarap memasukkan Angka.\n')
                                        jenisupdate = ()
                                        continue
                    else:
                        print('\nData yang diinput tidak ada di database Pegawai.')
                        print('\nKembali ke Fungsi Update.\n')
                        konfirmasi = ()
                else:
                    print(f'Data yang anda input adalah berikut: {read_NIP}. Data tidak sesuai dengan ketentuan.')
                    print('NIP terdiri dari 6 digit dan 2 digit awal adalah tahun Pegawai masuk.')
                    print('Kembali ke Fungsi Update.')
                    konfirmasi = ()

            elif konfirmasi == 2:
                print('\nKembali ke Menu Utama.\n')
                break
            
            else:
                print('\nHarap masukkan input dengan Angka yang sesuai.')
                print('\nKembali ke Fungsi Update.\n')
                konfirmasi = ()
        
        except:
            print('\nHarap masukkan input dengan Angka yang sesuai.')
            print('\nKembali ke Fungsi Update.\n')
            konfirmasi = ()


#Function Delete untuk menghapus Data Pegawai existing berdasarkan NIP, serta terdapat opsi untuk menghapus semua Data Pegawai
def Delete_Data():
    while True:
        Read_Data_Pegawai()
        delete = (input('''
Apakah anda ingin menghapus database pegawai? 
1. Satu data
2. Hapus Semua
3. Kembali ke Menu Awal
        
Masukkan angka sesuai opsi di yg diinginkan : 
'''))
        try:
            if int(delete) == 1:
                read_NIP = (input('\nMasukkan No NIP (6 Digit) yang ingin didelete: '))
                if len(read_NIP) == 6 and int(read_NIP) < 230000:
                    i = []
                    for i in DataPegawai:
                        try:
                            if i['NIP'] == int(read_NIP):
                                index = DataPegawai.index(i)
                                print('NIP  \t| Nama  \t| No HP \t| Domisili \t| Gender \t')
                                print('{}\t| {}\t| {}\t| {}   \t| {}'.format(DataPegawai[index]['NIP'], DataPegawai[index]['Nama'], DataPegawai[index]['No HP'], DataPegawai[index]['Domisili'], DataPegawai[index]['Gender']))
                                konfirmasi = input('\nKetik Ya untuk menghapus data diatas : ')
                                konfirmasi = konfirmasi.upper()
                                if konfirmasi == 'YA':
                                    DataPegawai.pop(index)
                                    print('\nData berhasil di Delete.\n')
                                    print('\nKembali ke Menu Delete.\n')
                                    delete = ()
                                    read_NIP = ()
                                    break
                                else:
                                    read_NIP = ()
                                    delete = ()
                                    print('\nKembali ke Fungsi Delete.\n')

                        except:
                                print('\nTidak ditemukan Data Pegawai dengan NIP tersebut.')
                                print('\nKembali ke Fungsi Delete.\n')
                                read_NIP = ()
                                delete = ()
                                return Delete_Data()
                    else:
                        Delete_Data()
                    
                            
                else:
                    print('\nNIP yang diinput tidak sesuai dengan kriteria NIP.')
                    print('\nNIP terdiri dari 6 digit Angka.')
                    print('\nKembali ke Fungsi Delete.\n')
                    read_NIP = ()
                    delete = ()
                    Delete_Data()

            elif int(delete) == 2:
                delete_all = input('''
Apakah anda yakin ingin menghapus semua data pegawai?
    
Ketik Ya jika untuk menghapus semua data pegawai : 
''')
                delete_all = delete_all.upper()
                if delete_all == 'YA':
                    DataPegawai.clear()
                    Read_Data_Pegawai()
                else:
                    Delete_Data()
            elif int(delete) == 3:
                print('\nAnda kembali ke Menu Awal.\n')
                delete = ()
                read_NIP = ()
                break
            
            else:
                print('\nHarap masukkan input dengan Angka yang sesuai.')
                print('\nKembali ke Fungsi Delete.\n')
                delete = ()
        
        except:
            print('\nHarap masukkan input dengan Angka yang sesuai.')
            print('\nKembali ke Fungsi Delete.\n')
            delete = ()
            
    return


#Menu Utama yang terdiri dari 5 Fungsi yaitu: Read, Create, Update, Delete, dan Exit
while True:
    MenuUtama = input('''
Selamat Datang pada Database Pegawai PT Maju Mundur Maju
    
Menu:
1. Create Data Pegawai
2. Read Data Pegawai
3. Update Data Pegawai
4. Delete Data Pegawai
5. Exit Database
    
Masukkan angka Menu yang ingin digunakan : 
''')
    try:
        if(MenuUtama == '2'):
            Read()
        elif(MenuUtama == '1'):
            Create_Data()
        elif(MenuUtama == '3'):
            Update_Data()
        elif(MenuUtama == '4'):
            Delete_Data()
        elif(MenuUtama == '5'):
            konfirmasikeluar = input('''
Anda yakin ingin keluar dari database pegawai?
        
Ketik Ya untuk keluar: 
''')
            konfirmasikeluar = konfirmasikeluar.upper()
            if konfirmasikeluar == 'YA':
                print('\nAnda telah keluar dari Database Pegawai. Data Pegawai sifatnya rahasia. Terima kasih.')
                break
            else :
                print('\nKembali ke Menu Utama.')
                continue
        else :
            print('\nPilihan menu dengan Input tersebut tidak tersedia. Kembali ke Menu Utama')
            print('\nKembali ke Menu Utama.')
            continue
    except:
        print('\nPilihan menu dengan Input tersebut tidak tersedia. Kembali ke Menu Utama.')
        continue
        
