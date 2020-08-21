#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from django_demo import settings

class TokenHandler(object):

    def __init__(self, mode=AES.MODE_CBC):
        self.key = settings.TOKEN_KEY.encode('utf-8')
        # 密钥key长度必须为16,24或者32bytes的长度
        self.mode = mode
        self.iv = b'0000000000000000'

    def encrypt(self, text:str):
        """
        加密函数，如果text不足16位就用空格补足为16位
        如果大于16当时不是16的倍数，那就补足为16的倍数
        :param text:
        :return:
        """
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    def decrypt(self, text:str):
        """
        解密后，去掉补足的空格用strip() 去掉
        :param text:
        :return:
        """
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')