module impl.internal.FileIO;

public class FileIO {
    import std.file;
    public static void appendFile(string name, void[] data) {
        append(name, data);
    };
    public static bool fileExists(string name) {
        return exists(name);
    };
    public static void[] readFile(string name) {
        return read(name);
    };
    public static void write(string name, void[] data) {
        write(name, data);
    };
};
