import requests

def sendImage(url:str, base64image:str, fileName:str)->dict:
    """ai server send image

    Args:
        url (str): server url
        base64image (str): base64 incoded image
        fileName (str): filename

    Returns:
        dict: server response
    """
    headers = {"Content-Type": "application/json"}
    jsonData = {"img": base64image, "filename": fileName}
    res = requests.post(url, json=jsonData, headers=headers).json()
    if res.status_code != 200:
        raise Exception(f"HTTP ResponseCode : {res.status_code}")
    return res
    