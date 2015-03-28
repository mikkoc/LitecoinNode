#!/usr/bin/python 

from bitcoinrpc.authproxy import AuthServiceProxy
import time
import json
import urllib2, re

get_ip_info = urllib2.urlopen('http://ipinfo.io/json')
ip_data = json.load(get_ip_info)

lcd_data = get_lcd_info.getinfo()


ff.write("""<!DOCTYPE html>""")
ff.write("""<html lang="en">""")
ff.write("""<head>""")
ff.write("""<meta http-equiv="content-type" content="text/html; charset=UTF-8">""")
ff.write("""<meta charset="utf-8">""")
ff.write("""<title>Litecoin node status - By litecoinnode.org</title>""")
ff.write("""<meta name="viewport" content="width=device-width, initial-scale=1.0">""")
ff.write("""<meta name="description" content="Litecoin node status - By litecoinnode.org">""")
ff.write("""<meta name="keywords" content="litecoin, litecoinnode, litecoin node, node status, litecoin node status">""")
ff.write("""<link rel="apple-touch-icon-precomposed" href="./favicon.png">""")
ff.write("""<link rel="shortcut icon" href="./favicon.png">""")
ff.write("""<link href="./bootstrap.css" rel="stylesheet">""")
ff.write("""<link href="./style.css" rel="stylesheet">""")
ff.write("""</head>""")
ff.write("""<body>""")
ff.write("""<div class="container-narrow">""")
ff.write("""<div>""")
ff.write("""<div class"pull-left>""")
ff.write("""<h3>Litecoin node status - By litecoinnode.org</h3><hr>""")
ff.write("""</div>""")
ff.write("""</div>""")
ff.write("""<div>""")
ff.write("""<div>""")
ff.write("""<img class="map" src="./banner.png" alt="litecoin" title="litecoin">""")
ff.write("""</div>""")
ff.write("""<h4>Node info</h4>""")
ff.write("""<table class="table table-striped">""")
ff.write("<tbody><tr><td>IP</td><td>" + str(ip_data['ip']) + "</td></tr>")
ff.write("<tr><td>Hostname</td><td>" + str(ip_data['hostname']) + "</td></tr>")
ff.write("<tr><td>Network</td><td>" + str(ip_data['org']) + "</td></tr>")
ff.write("<tr><td>City</td><td>" + str(ip_data['city']) + "</td></tr>")
ff.write("<tr><td>Country</td><td>" + str(ip_data['country']) + "</td></tr>")
ff.write("""<tr><td></td><td></td></tr>""")
ff.write("""</tbody></table>""")
ff.write("""<h4>Litecoin status</h4>""")
ff.write("""<table class="table table-striped">""")
ff.write("<tbody><tr><td>Version</td><td>" + str(lcd_data['version']) + "</td></tr>")
ff.write("<tr><td>Blocks</td><td>" + str(lcd_data['blocks']) + "</td></tr>")
ff.write("<tr><td>Connections</td><td>" + str(lcd_data['connections']) + "</td></tr>")
ff.write("<tr><td>Difficulty</td><td>" + str(lcd_data['difficulty']) + "</td></tr>")
ff.write("<tr><td>Last update</td><td>" + time.strftime("%Y-%m-%d @ %H:%M:%S") + "</td></tr>")
ff.write("""<tr><td></td><td></td></tr>""")
ff.write("""</tbody></table>""")
ff.write("""<h4>What is this page?</h4>""")
ff.write("""<p>This page is a display of status information of a Litecoin full node. Litecoin full nodes are responsible for hosting and distributing the Litecoin block chain and for relaying Litecoin transactions across the network.</p>""")
ff.write("""</br>""")
ff.write("""<h4>What is LitecoinNode</h4>""")
ff.write("""<p><a href="http://litecoinnode.org/">LitecoinNode</a> is a small project that aims to make it easy for individuals to deploy and maintain Litecoin nodes.</p>""")
ff.write("""<p>If you like the project please consider making a donation with Litecoin <a href="litecoin:LYSBpbh7NFmTykMg5PcrMgEuN7tVNmVA4Q?amount=0.0&label=litecoinnode.org">here</a> or Bitcoin <a href="bitcoin:1Gv3vJsg2ybnh9rRBfwG55YmXqNVEtPDy4?amount=0.0&label=litecoinnode.org">here</a>.</p>""") 
ff.write("""</div>""")
ff.write("""<div class="footer">""")
ff.write("""<hr>""")
ff.write("""<ul class="nav nav-pills">""")
ff.write("""<li class="pull-left"><a href="http://litecoinnode.org/">LitecoinNode</a></li>""")
ff.write("""<li class="pull-left"><a href="https://github.com/LitecoinNode">GitHub</a></li>""")
ff.write("""<li class="pull-right"><a href="https://litecoin.org/">Litecoin</a></li></ul>""")
ff.write("""</div>""")
ff.write("""</div>""")
ff.write("""</body>""")
ff.write("""</html>""")

ff.close()
