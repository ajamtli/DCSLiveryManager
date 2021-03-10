from requests import get
import re

def correct_dcs_user_files_url(fileURL):
  DCSFilesURLRoot = "https://www.digitalcombatsimulator.com/en/files/"
  fileID = re.findall(r'[0-9]+', fileURL)
  if len(fileID):
    if str.isnumeric(fileID[0]):
      return DCSFilesURLRoot + fileID[0] + "/", fileID[0]

def size_text_to_bytes(sizeText):
  if len(sizeText):
    if 'mb' in str.lower(sizeText):
      sizeText = sizeText.split(' ')[0]
    sizeInt = int(float(sizeText) * 100) * (10**4)
    return sizeInt
  return 0

def bytes_to_mb_string(sizeBytes):
  return "{:.2f}".format(float(sizeBytes/(10**6)))

def request_file_size(fileURL):
  return int(get(fileURL, stream=True).headers['Content-length'])
