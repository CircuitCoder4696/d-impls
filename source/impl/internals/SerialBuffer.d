module impl.internal.SerialBuffer;

public class SerialBuffer {
    private size_t rPtr,wPtr;
    private void[] data;
    public this(size_t size) {
        this.data= new void[size];
    };
    public void wValue(T)(T value) {
        uint size= sizeof(value);
        void[] d0= (cast(void*) (&value))[0 .. size];
        this.data[this.wPtr .. (this.wPtr + size)]= d0;
        this.wPtr += size;
    };
    public void wArray(T)(T[] data) {
        uint size= sizeof(data);
        void[] d0= (cast(void*) (data.ptr))[0 .. size];
        this.data[this.wPtr .. (this.wPtr + size)]= d0;
        this.wPtr += size;
    };
    public T rValue(ValueT)(ref T value) {
        uint len= value.length;
        uint size= sizeof(value);
        void* d0= this.data.ptr + this.rPtr;
        T* d1= d0;
        value= *d1;
    };
    public void wArray(T)(ref T data) {
        uint len= value.length;
        uint size= sizeof(data);
        void* d0= this.data.ptr + this.rPtr;
        T* d1= d0;
        data= d1[0 .. len];
    };
};

@safe unittest {
	import std.stdio:writeln;
	auto buffer= new SerialBuffer(400);
	buffer.wArray("Hello world.  ");
	char[] v0= new char[14];
	buffer.rArray(v0);
	writeln(v0);
};
