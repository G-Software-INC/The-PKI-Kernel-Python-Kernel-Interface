import os
import sys
import ctypes
import contextlib

class PKIError(Exception):
    pass

class PKIKernel:
    def __init__(self):
        self.lib = None
        self._load_library()

    def _load_library(self):
        try:
            if sys.platform.startswith('linux'):
                self.lib = ctypes.CDLL('./libpki.so')
            elif sys.platform.startswith('win'):
                self.lib = ctypes.WinDLL('pki.dll')
        except Exception:
            self.lib = None

    @contextlib.contextmanager
    def open_file(self, path, flags, mode=0o777):
        fd = self._open_file(path, flags, mode)
        try:
            yield fd
        finally:
            self.close_file(fd)

    def _open_file(self, path, flags, mode):
        if self.lib and hasattr(self.lib, 'pki_open'):
            self.lib.pki_open.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
            self.lib.pki_open.restype = ctypes.c_int
            fd = self.lib.pki_open(path.encode('utf-8'), flags, mode)
            if fd < 0:
                raise PKIError(f"pki_open failed on {path} with flags {flags}")
            return fd
        else:
            return os.open(path, flags, mode)

    def read_file(self, fd, count):
        if self.lib and hasattr(self.lib, 'pki_read'):
            buf = ctypes.create_string_buffer(count)
            self.lib.pki_read.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
            self.lib.pki_read.restype = ctypes.c_int
            bytes_read = self.lib.pki_read(fd, buf, count)
            if bytes_read < 0:
                raise PKIError("pki_read failed")
            return buf.raw[:bytes_read]
        else:
            return os.read(fd, count)

    def write_file(self, fd, data):
        if self.lib and hasattr(self.lib, 'pki_write'):
            buf = ctypes.create_string_buffer(data, len(data))
            self.lib.pki_write.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
            self.lib.pki_write.restype = ctypes.c_int
            bytes_written = self.lib.pki_write(fd, buf, len(data))
            if bytes_written < 0:
                raise PKIError("pki_write failed")
            return bytes_written
        else:
            return os.write(fd, data)

    def close_file(self, fd):
        if self.lib and hasattr(self.lib, 'pki_close'):
            self.lib.pki_close.argtypes = [ctypes.c_int]
            self.lib.pki_close.restype = ctypes.c_int
            result = self.lib.pki_close(fd)
            if result != 0:
                raise PKIError("pki_close failed")
            return result
        else:
            return os.close(fd)

    def seek_file(self, fd, offset, whence=os.SEEK_SET):
        if self.lib and hasattr(self.lib, 'pki_seek'):
            self.lib.pki_seek.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
            self.lib.pki_seek.restype = ctypes.c_int
            pos = self.lib.pki_seek(fd, offset, whence)
            if pos < 0:
                raise PKIError("pki_seek failed")
            return pos
        else:
            return os.lseek(fd, offset, whence)

    def list_directory(self, path):
        return os.listdir(path)

    def stat_file(self, path):
        return os.stat(path)

    def rename_file(self, src, dst):
        os.rename(src, dst)

    def delete_file(self, path):
        os.remove(path)
