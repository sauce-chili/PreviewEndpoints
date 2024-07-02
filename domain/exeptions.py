class CameraException(Exception):
    pass


class CameraNotAvailableException(CameraException):
    def __init__(self, cam_name: str, port: str):
        super().__init__()
        self.cam_name = cam_name
        self.port = port

    def __str__(self):
        return f"CameraNotAvailableException(name='{self.cam_name}', port='{self.port}')"


class ScalesException(Exception):
    pass


class ScalesUnavailable(ScalesException):
    def __init__(self, scale_name: str):
        self.scale_name = scale_name

    def __str__(self):
        return f"ScalesUnavailable(scales_name='{self.scale_name}')"


class WeightDecodingException(ScalesException):
    def __init__(self, msg: str | None = None, uncoded_data: str | None = None) -> None:
        super().__init__()
        self.msg = msg
        self.uncoded_data = uncoded_data

    def __str__(self) -> str:
        return f"WeightDecodingException(msg='{self.msg}', uncoded_data='{self.uncoded_data}')"
