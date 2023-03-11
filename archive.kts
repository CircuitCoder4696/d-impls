import java.util.Arrays;
fun main(args: Array<String>) {
    val files:Array<String> = arrayOf("./dub.sdl");
    for(f in files)
        println(f);
    // ZipOutputStream(BufferedOutputStream(FileOutputStream("/home/matte/Desktop/test.zip"))).use { out ->
    //     for (file in files) {
    //         FileInputStream(file).use { fi ->
    //             BufferedInputStream(fi).use { origin ->
    //                 val entry = ZipEntry(file.substring(file.lastIndexOf("/")))
    //                 out.putNextEntry(entry)
    //                 origin.copyTo(out, 1024)
    //             }
    //         }
    //     }
    // }
}