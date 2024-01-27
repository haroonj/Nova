class Constants:
    __PI_IP_ADDRESS = "192.168.9.107"
    __FRAME_W = 640
    __FRAME_H = 480

    @classmethod
    def get_pi_ip_address(cls):
        return cls.__PI_IP_ADDRESS

    @classmethod
    def get_frame_w(cls):
        return cls.__FRAME_W

    @classmethod
    def get_frame_h(cls):
        return cls.__FRAME_H
