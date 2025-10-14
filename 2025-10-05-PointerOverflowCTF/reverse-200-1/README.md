# Reverse 200-1 On Hinge and Pin
## Introduction
A tiny Android app refuses to trust your device and hides a secret. Your job: recover the flag. Any technique is fair game as long as you get the correct flag. 

## Files
* [rev200-1.apk](rev200-1.apk)

## Investigation
The files is an Android package. Lets open it in `JADX GUI`.

Looked at the source code for any clues related to the flag. When searching for `"flag"` we find the following class.

```java
public final class Crypto {
    public static final Crypto INSTANCE = new Crypto();
    private static final String KEY = "ONOFFONOFF";

    private Crypto() {
    }

    public static /* synthetic */ String loadAndDecrypt$default(Crypto crypto, Context context, String str, int i, Object obj) {
        if ((i & 2) != 0) {
            str = "enc_flag.bin";
        }
        return crypto.loadAndDecrypt(context, str);
    }

    public final String loadAndDecrypt(Context ctx, String assetName) throws IOException {
        Intrinsics.checkNotNullParameter(ctx, "ctx");
        Intrinsics.checkNotNullParameter(assetName, "assetName");
        InputStream inputStreamOpen = ctx.getAssets().open(assetName);
        try {
            InputStream it = inputStreamOpen;
            Intrinsics.checkNotNull(it);
            byte[] data = ByteStreamsKt.readBytes(it);
            CloseableKt.closeFinally(inputStreamOpen, null);
            byte[] key = StringsKt.encodeToByteArray(KEY);
            byte[] out = new byte[data.length];
            int length = data.length;
            for (int i = 0; i < length; i++) {
                out[i] = (byte) (data[i] ^ key[i % key.length]);
            }
            return new String(out, Charsets.UTF_8);
        } finally {
        }
    }
}
```

Looks like the code XORs each byte with a key to decrypt it. The file `enc_flag.bin` can be found in the Android package.

![jadx.png](jadx.png)

From here we just extract the file, create a short python script for doing the XOR with key `ONOFFONOFF`, and run it.

```python
key = b"ONOFFONOFF"
data = open("enc_flag.bin", "rb").read()

decrypted = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
print(decrypted.decode("utf-8"))
```

This provides the flag in its entirety.

## Flag
<details>
<summary>Click to reveal the flag</summary>

```text
poctf{uwsp_c4nc3l_c0u7ur3}
```