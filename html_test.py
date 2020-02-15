#!/usr/local/bin/python3
# 上はPythonのインストールパスの指定
# プログラムの先頭行で"#!"に続けて指定する必要がある

# 参考
# クジラ飛行机『Pythonで作ったwebサイトは100円で運用できる その1』(https://news.mynavi.jp/article/zeropython-43/)

# 日本語を使うために必要な設定
import os, sys, io, cgi
sys.stdin = open(sys.stdin.fileno(), 'r', encoding = 'UTF-8')
sys.stdout = open(sys.stdout.fileno(), 'w', encoding = 'UTF=8')
sys.stderr = open(sys.stderr.fileno(), 'w', encoding = 'UTF=8')

out = lambda msg: print(msg, end = "\r\n")

# ヘッダの出力
out("Content-Type: text/html; charset-utf-8")
out("")

# HTMLの出力
out("<html><meta charset='utf-8'><body>")
out("<h1>こんにちは</h1>")
out("</body></html>")