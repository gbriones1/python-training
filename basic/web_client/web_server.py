import sys
import cgi
import SocketServer
import SimpleHTTPServer
import pdb
import json

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        print "======= Serving GET method ======="
        print self.address_string()
        print self.headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Python training</title></head>")
        self.wfile.write("<body><p>Hello python trainee!</p>")

    def do_POST(self):
        print "======= Serving POST method ======="
        print self.address_string()
        print self.client_address[0]
        print self.headers
        data = {"content":self.headers['Content-Type'].split("/")[1]}
        if self.headers['Content-Type'] == "application/json":
            req_data = self.rfile.read(int(self.headers['content-Length']))
            data = json.loads(req_data.replace('\'', '\"'))
        else:
            environment = {'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type']}
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ=environment)
            if form.list:
                for item in form.list:
                    data[item.name] = item.value
        res_string = json.dumps(data)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(res_string)

port = int(sys.argv[1]) if sys.argv[1:] else 9000
httpd = SocketServer.TCPServer(('', port), ServerHandler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()