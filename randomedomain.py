import random
import string

def tao_domain_ngau_nhien(base_domain, length=3, limit=55):
    for _ in range(limit):
        random_chars = ''.join(random.choices(string.ascii_lowercase, k=length))
        new_domain = base_domain.replace('xxx', random_chars)
        print(new_domain)

base_domain = 'mygiftcardmallxxx.com'
tao_domain_ngau_nhien(base_domain)
