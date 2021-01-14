__help__ = """
 Jika Anda mencari cara untuk memperingatkan pengguna secara otomatis ketika mereka mengatakan hal-hal tertentu, gunakan perintah /addwarn.
 Contoh pengaturan filter multiword memperingatkan:
 × `/addwarn "sangat marah" Ini adalah pengguna yang marah
 Ini secara otomatis akan memperingatkan pengguna yang memicu "sangat marah", dengan alasan 'Ini adalah pengguna yang marah'.
 Contoh cara menyetel peringatan multi kata baru:
`/warn @user Karena peringatan itu menyenangkan`
 × /warns <userhandle>: Mendapatkan nomor pengguna, dan alasan, peringatan.
 × /warnlist: Mencantumkan semua filter peringatan saat ini
*Khusus Admin:*
 × /warn <userhandle>: Memperingatkan pengguna. Setelah 3 peringatan, pengguna akan diblokir dari grup. Bisa juga digunakan sebagai balasan.
 × /resetwarn <userhandle>: Menyetel ulang peringatan untuk pengguna. Bisa juga digunakan sebagai balasan.
 × /rmwarn <userhandle>: Menghapus peringatan terbaru untuk pengguna. Itu juga bisa digunakan sebagai balasan.
 × /unwarn <userhandle>: Sama dengan /rmwarn
 × /addwarn <keyword> <reply message>: Menetapkan filter peringatan untuk kata kunci tertentu. Jika Anda ingin kata kunci Anda \
adilah kalimat, lengkapi dengan tanda kutip, seperti: `/addwarn" very angry "This is an angry user`.
 × /nowarn <keyword>: enghentikan filter peringatan
 × /warnlimit <num>: Menetapkan batas peringatan
 × /strongwarn <on/yes/off/no>: Jika disetel ke aktif, melebihi batas peringatan akan mengakibatkan larangan. Lain, hanya akan menendang.
"""

__mod_name__ = "Warnings"
