#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def decode_str(msg):
    value, charset = decode_header(msg)[0]
    if charset != None:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_info(msg, depth=0):
    if depth == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * depth, header, value))

    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * depth, n))
            print('%s--------------------' % ('  ' * depth))
            print_info(part, depth + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * depth, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * depth, content_type))


email = '18701994373@163.com'
passwd = 'aiying1007'
pop3_addr = 'pop3.163.com'

pop3=poplib.POP3(pop3_addr)
pop3.set_debuglevel(1)
print(pop3.getwelcome().decode('utf-8'))
pop3.user(email)
pop3.pass_(passwd)
print('Message %s; Size %s' % pop3.stat())
resp, mails, octetcs = pop3.list()
print(mails, "%%%%%%%%%%%%%%%")
index = len(mails)
resp, lines, octetcs = pop3.retr(index)
content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(content)
print_info(msg)
pop3.quit()