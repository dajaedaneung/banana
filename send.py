import requests


def sendData(people: int):
    # TODO :: 카메라 마다 번호 변경
    camera = 2
    requests.post('http://10.150.150.191:8080/density', data={
        'camera': camera,
        'people': people,
    })