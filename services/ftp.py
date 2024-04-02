import sys, enum


class FTPConfig(enum.Enum):
    LISTEN = "listen"
    LISTEN_IPV6 = "listen_ipv6"
    ANONYMOUS_ENABLE = "anonymous_enable"
    LOCAL_ENABLE = "local_enable"
    DIRMESSAGE_ENABLE = "dirmessage_enable"
    USE_LOCALTIME = "use_localtime"
    XFERLOG_ENABLE = "xferlog_enable"
    CONNECT_FROM_PORT_20 = "connect_from_port_20"
    SECURE_CHROOT_DIR = "secure_chroot_dir"
    PAM_SERVICE_NAME = "pam_service_name"
    RSA_CERT_FILE = "rsa_cert_file"
    RSA_PRIVATE_KEY_FILE = "rsa_private_key_file"
    SSL_ENABLE = "ssl_enable"


path = "/etc/vsftpd.conf"
if len(sys.argv) > 1:
    path = sys.argv[1]

try:
    f = open(path)
    lines = f.readlines()
    for line in lines:
        for config in FTPConfig:
            if config.value in line:
                print(f"{line}")

except Exception as e:
    print(f"Exception: {e}")
    sys.exit(1)
