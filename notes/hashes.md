**Hashes may be stored in different formats. Like: _hash:salt_ or _$id$salt$hash_.**

## Hash ID's
```
$1$  : MD5
$2a$ : Blowfish
$2y$ : Blowfish, with correct handling of 8 bit characters
$5$  : SHA256
$6$  : SHA512
```

## Hashcat
### Hash types `-a`
- 0: MD5
- 1000: NTLM
  
### Attack modes `-m`
- 0: Straight
- 1: Combination
- 3: Brute-force
- 6: Hybrid Wordlist + Mask
- 7: Hybrid Mask + Wordlist
  