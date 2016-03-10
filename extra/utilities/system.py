import os
import subprocess
import sys
import logging
import StringIO
import pycurl
import socket
import base64
try:
    from urllib.parse import urlencode
except:
    from urllib import urlencode

from logger import CustomLogger
logger = CustomLogger(__name__).logger

class CustomException(Exception):

    def __init__(self, code, *args):
        self.code = code
        self.msg = Error.get_code_description(code).format(*args)

    def __str__(self):
        return repr("Error: {code}: {msg}".format(code=self.code, msg=self.msg))


class Error(object):

    GENERIC_ERROR = 1
    NOTHING_TO_DO = 2
    FILE_NOT_FOUND = 100
    DIRECTORY_NOT_FOUND = 101
    PARSING_FAILED = 200
    URL_NOT_VALID = 300

    DESCRIPTIONS = {
        FILE_NOT_FOUND: "File not found: {0}",
        URL_NOT_VALID: "URL not valid: {0}",
        PARSING_FAILED: "File couldn't be parsed, wrong format: {0}",
        GENERIC_ERROR: "Error: {0}",
        NOTHING_TO_DO: "Info not enough to run",
    }

    @staticmethod
    def get_code_description(code):
        message = ""
        for error in Error.DESCRIPTIONS.keys():
            if code == error:
                message = Error.DESCRIPTIONS[error]
        if not message:
            message = Error.DESCRIPTIONS[Errors.GENERIC_ERROR]
        return message

    def __init__(self, code, *args):
        self.code = code
        self.msg = Error.get_code_description(code).format(*args)

class System(object):

    ERRORS = []

    @staticmethod
    def local_cmd(cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out, err, p.returncode

    @staticmethod
    def remote_cmd(rcmd, ipaddr):
        # cmd=['ssh', '-f', '-oStrictHostKeyChecking=no', 'root@'+ipaddr, rcmd]
        cmd = ['ssh', '-oStrictHostKeyChecking=no', 'root@'+ipaddr, rcmd]
        # f = open(os.devnull, 'w')
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # f.close()
        out, err = p.communicate()
        return out, err, p.returncode

    @staticmethod
    def remote_copy(src, dst, ipaddr):
        cmd = ['scp', '-oStrictHostKeyChecking=no',
               src, 'root@'+ipaddr+':'+dst]
        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out, err, p.returncode

    @staticmethod
    def add_error(code, *args):
        System.ERRORS.append(Error(code, *args))

    @staticmethod
    def terminate(code=0):
        if code:
            logger.error(Error.get_code_description(code))
        else:
            for error in System.ERRORS:
                logger.error(error.msg)
                code = error.code
        sys.exit(code)

    @staticmethod
    def createdir(dirname):
        try:
            logger.debug('Creating directory: %s' % dirname)
            os.mkdir(dirname)
            return True
        except:
            logger.debug("Cannot create %s Do you have the right permissions?"
                         % dirname)
        return False

    @staticmethod
    def createfile(filename, content):
        try:
            logger.debug("Creating file: %s" % filename)
            f = open(filename, 'w')
            f.write(content)
            f.close()
            return True
        except:
            logger.debug("Cannot create %s Do you have the right permissions?"
                         % filename)
        return False

    @staticmethod
    def checkpath(filepath, createdir=True):
        filedir = os.path.dirname(filepath)
        exist = False
        if os.path.exists(filedir):
            exist = True
        elif createdir:
            exist = System.createdir(filedir)
        return exist

    @staticmethod
    def checkdir(directory, createdir=True):
        exist = False
        if os.path.exists(directory):
            if os.path.isdir(directory):
                exist = True
        elif createdir:
            exist = System.createdir(directory)
        return exist

    @staticmethod
    def checkfile(filename, createfile=False):
        exist = False
        if os.path.exists(filename):
            if os.path.isfile(filename):
                exist = True
        elif createfile:
            exist = System.createfile(filename, "")
        return exist

    @staticmethod
    def verify_url(url):
        logger.debug("Verifying URL: {url}".format(url=url))
        curl_version = pycurl.Curl()
        curl_version.setopt(curl_version.URL, url)
        curl_version.setopt(curl_version.NOBODY, 1)
        curl_version.perform()
        return curl_version.getinfo(pycurl.HTTP_CODE)
        # if error_code != 200:
        #     raise CustomException(Errors.URL_NOT_VALID, url)
        # curl_version.close()
        # logger.debug("URL OK")
        # return url

    @staticmethod
    def curl_req(url, data={}, print_progress=False, auth=''):
        buff = StringIO.StringIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        # curl.setopt(curl.WRITEDATA, buff)
        curl.setopt(curl.WRITEFUNCTION, buff.write)
        if data:
            curl.setopt(curl.POSTFIELDS, urlencode(data))
        if auth:
            headers = { 'Authorization' : 'Basic %s' % base64.b64encode(auth) }
            curl.setopt(curl.HTTPHEADER, ["%s: %s" % t for t in headers.items()])
        if print_progress:
            curl.setopt(curl.NOPROGRESS, 0)
            curl.setopt(curl.PROGRESSFUNCTION, System.curl_progress)
        curl.perform()
        if print_progress:
            logger.info("[##################################################] 100%")
        code = curl.getinfo(curl.RESPONSE_CODE)
        curl.close()
        return code, buff.getvalue()

    @staticmethod
    def curl_progress(download_t, download_d, upload_t, upload_d):
        if logger.level <= 20 and download_t:
            prog = "["
            acc = 0
            perg = download_d/download_t
            for x in range(int(perg*50)):
                acc += 1
                prog += "#"
            for x in range(50-acc):
                prog += " "
            prog += "]"
            sys.stdout.write("%s %s%%\r" % (prog, int(perg*100)))
            sys.stdout.flush()

    @staticmethod
    def getIPaddr():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        ipaddr = s.getsockname()[0]
        s.close()
        return ipaddr

class EqualsSpaceRemover:
    output_file = None
    def __init__( self, new_output_file ):
        self.output_file = new_output_file

    def write( self, what ):
        self.output_file.write( what.replace( " = ", "=" ) )
