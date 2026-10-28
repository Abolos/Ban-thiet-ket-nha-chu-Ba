# -*- coding: utf-8 -*-
"""Sinh hồ sơ thiết kế nhà ở 2 tầng 6x15m (SVG + DXF) cho thư mục D:\\Ban-thiet-ke-chu-ba"""
import math, os, html

OUT = r"D:\Ban-thiet-ke-chu-ba"
DATE = "28/10/2026"
PROJECT = "NHÀ Ở 2 TẦNG MÁI BẰNG – PHONG CÁCH HIỆN ĐẠI"
OWNER = "Gia đình chú Ba"

# ---------------------------------------------------------------- styles
CSS = """
.t{font-family:'Segoe UI',Arial,Helvetica,sans-serif;fill:#1d1d1d}
.tb{font-weight:700}.ti{font-style:italic}.tw{fill:#fff}.tr{fill:#b03a2e}.tbl{fill:#1a4f9c}
.wall{fill:#262626;stroke:#000;stroke-width:.4}
.wall2{fill:#8c8c8c;stroke:#333;stroke-width:.3}
.rail{fill:#cfe3ee;stroke:#2f6f8f;stroke-width:.4}
.col{fill:#000}
.gap{fill:#fff;stroke:none}
.win{fill:#fff;stroke:#1f5f8b;stroke-width:.5}
.winl{stroke:#1f5f8b;stroke-width:.45;fill:none}
.door{fill:none;stroke:#0b6e2e;stroke-width:.6}
.doorarc{fill:none;stroke:#0b6e2e;stroke-width:.35;stroke-dasharray:2 1.2}
.furn{fill:#fff;stroke:#666;stroke-width:.4}
.furn2{fill:none;stroke:#888;stroke-width:.35}
.furnd{fill:#e9e4dc;stroke:#666;stroke-width:.4}
.dash{fill:none;stroke:#777;stroke-width:.4;stroke-dasharray:3 2}
.dashr{fill:none;stroke:#b03a2e;stroke-width:.4;stroke-dasharray:4 2}
.stair{fill:none;stroke:#333;stroke-width:.45}
.staird{fill:none;stroke:#777;stroke-width:.35;stroke-dasharray:2.5 1.5}
.dim{stroke:#1a4f9c;stroke-width:.35;fill:none}
.axis{stroke:#c0392b;stroke-width:.35;stroke-dasharray:10 2 1.5 2;fill:none}
.bub{fill:#fff;stroke:#c0392b;stroke-width:.5}
.sec{stroke:#b03a2e;stroke-width:1.2;fill:none}
.arrow{stroke:#333;stroke-width:.5;fill:none;marker-end:url(#arr)}
.arrowr{stroke:#b03a2e;stroke-width:.8;fill:none;marker-end:url(#arrR)}
.sun{stroke:#e0a100;stroke-width:.9;fill:none;stroke-dasharray:4 2;marker-end:url(#arrS)}
.wind{stroke:#2e86c1;stroke-width:.9;fill:none;stroke-dasharray:4 2;marker-end:url(#arrW)}
.frame{fill:none;stroke:#000;stroke-width:.8}
.frame2{fill:none;stroke:#000;stroke-width:.4}
.tbfill{fill:#f4f1ea;stroke:#000;stroke-width:.4}
.r-khach{fill:#fff3df}.r-bep{fill:#fde6d4}.r-ngu{fill:#e3edfb}.r-wc{fill:#dcf3f3}
.r-tho{fill:#fbe3e1}.r-shc{fill:#eaf5e1}.r-san{fill:#e4f0da}.r-hall{fill:#f3f3f3}
.r-bc{fill:#efe8dc}.r-kho{fill:#ececec}.r-void{fill:#ffffff}.r-yard{fill:#eef2e8}
.r-road{fill:#d9d9d9}.r-roof{fill:#efefef}.r-glass{fill:url(#glass);stroke:#2f6f8f;stroke-width:.5}
.r-nb{fill:url(#nb);stroke:#999;stroke-width:.3}
.plant{fill:#9ccc7a;stroke:#4f7f35;stroke-width:.4}
.car{fill:#f7f7f7;stroke:#555;stroke-width:.5}
/* mat dung */
.e-wall{fill:#f6f4ef;stroke:#444;stroke-width:.5}
.e-recess{fill:#dcd9d1;stroke:#555;stroke-width:.4}
.e-stone{fill:#8e8b84;stroke:#444;stroke-width:.4}
.e-stl{stroke:#6d6a63;stroke-width:.3}
.e-glass{fill:#9fc2d6;stroke:#2d3b45;stroke-width:.5}
.e-glass2{fill:#b9d6e6;fill-opacity:.45;stroke:#2d3b45;stroke-width:.4}
.e-alu{fill:none;stroke:#2b2b2b;stroke-width:.9}
.e-frame{fill:#fdfdfb;stroke:#333;stroke-width:.6}
.e-wood{fill:#9b6a3c;stroke:#5e3d1e;stroke-width:.3}
.e-dark{fill:#3d3d3d;stroke:#222;stroke-width:.4}
.e-gr{stroke:#111;stroke-width:1.6}
.e-ghost{fill:none;stroke:#aaa;stroke-width:.4;stroke-dasharray:4 3}
.e-shadow{stroke:#555;stroke-width:1.4}
.e-light{fill:#ffe9a8;stroke:#c9a227;stroke-width:.3}
/* mat cat */
.cut{fill:url(#hatch);stroke:#000;stroke-width:.55}
.cutb{fill:#3a3a3a;stroke:#000;stroke-width:.4}
.earth{fill:url(#earth);stroke:none}
.beyond{fill:none;stroke:#7d7d7d;stroke-width:.35}
.beyondf{fill:#f1f1f1;stroke:#8d8d8d;stroke-width:.35}
.insul{fill:#f3d9a4;stroke:#8a6d2b;stroke-width:.3}
.glassc{fill:#bfe0f0;stroke:#2f6f8f;stroke-width:.5}
"""

DEFS = """
<pattern id="hatch" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
 <rect width="5" height="5" fill="#d6d6d6"/><line x1="0" y1="0" x2="0" y2="5" stroke="#444" stroke-width="0.8"/></pattern>
<pattern id="earth" width="12" height="12" patternUnits="userSpaceOnUse">
 <rect width="12" height="12" fill="#efe6d6"/><path d="M0 12 L12 0 M-3 3 L3 -3 M9 15 L15 9" stroke="#b9a37f" stroke-width="0.6"/>
 <circle cx="3" cy="8" r="0.7" fill="#b9a37f"/></pattern>
<pattern id="glass" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
 <rect width="8" height="8" fill="#dff0f8"/><line x1="0" y1="0" x2="0" y2="8" stroke="#8fc1da" stroke-width="0.7"/></pattern>
<pattern id="nb" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">
 <rect width="10" height="10" fill="#f5f5f5"/><line x1="0" y1="0" x2="0" y2="10" stroke="#c8c8c8" stroke-width="0.6"/></pattern>
<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#333"/></marker>
<marker id="arrR" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#b03a2e"/></marker>
<marker id="arrS" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#e0a100"/></marker>
<marker id="arrW" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#2e86c1"/></marker>
"""

LAYERS = {"0": 7, "WALL": 7, "COL": 7, "WIN": 4, "DOOR": 3, "FURN": 8, "DIM": 5, "AXIS": 1,
          "TEXT": 7, "STAIR": 6, "ROOM": 9, "SITE": 3, "CUT": 7, "BEYOND": 8, "FRAME": 7, "ELEV": 7}


def dxf_txt(t):
    return "".join(c if ord(c) < 128 else "\\U+%04X" % ord(c) for c in t)


class Sheet:
    def __init__(self, code, fname, title, scale, umin, umax, vmin, vmax,
                 ml=1500, mr=1500, mt=1500, mb=3800):
        self.code, self.fname, self.title, self.scale = code, fname, title, scale
        self.umin, self.umax, self.vmin, self.vmax = umin, umax, vmin, vmax
        self.ml, self.mr, self.mt, self.mb = ml, mr, mt, mb
        self.W = (umax - umin + ml + mr) / 10.0
        self.H = (vmax - vmin + mt + mb) / 10.0
        self.svg, self.dxf = [], []

    # model (mm, v up) -> svg px (1px = 10mm => 1:100 when svg width in mm = px/10)
    def P(self, u, v):
        return ((u - self.umin + self.ml) / 10.0, (self.vmax - v + self.mt) / 10.0)

    def _dl(self, a, b, layer):
        self.dxf.append("0\nLINE\n8\n%s\n10\n%.1f\n20\n%.1f\n30\n0\n11\n%.1f\n21\n%.1f\n31\n0\n"
                        % (layer, a[0], a[1], b[0], b[1]))

    def poly(self, pts, cls="", layer="0", closed=True, dxf=True, extra=""):
        tag = "polygon" if closed else "polyline"
        ps = " ".join("%.1f,%.1f" % self.P(u, v) for u, v in pts)
        self.svg.append('<%s class="%s" points="%s"%s/>' % (tag, cls, ps, extra))
        if dxf:
            seq = list(pts) + ([pts[0]] if closed else [])
            for a, b in zip(seq, seq[1:]):
                self._dl(a, b, layer)

    def rect(self, u0, v0, u1, v1, cls="", layer="0", dxf=True):
        u0, u1 = min(u0, u1), max(u0, u1)
        v0, v1 = min(v0, v1), max(v0, v1)
        self.poly([(u0, v0), (u1, v0), (u1, v1), (u0, v1)], cls, layer, True, dxf)

    def line(self, u0, v0, u1, v1, cls="", layer="0", dxf=True):
        x0, y0 = self.P(u0, v0)
        x1, y1 = self.P(u1, v1)
        self.svg.append('<line class="%s" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (cls, x0, y0, x1, y1))
        if dxf:
            self._dl((u0, v0), (u1, v1), layer)

    def circle(self, u, v, r, cls="", layer="0", dxf=True):
        x, y = self.P(u, v)
        self.svg.append('<circle class="%s" cx="%.1f" cy="%.1f" r="%.1f"/>' % (cls, x, y, r / 10.0))
        if dxf:
            self.dxf.append("0\nCIRCLE\n8\n%s\n10\n%.1f\n20\n%.1f\n30\n0\n40\n%.1f\n" % (layer, u, v, r))

    def text(self, u, v, t, h=200, cls="", anchor="middle", layer="TEXT", rot=0, dxf=True):
        x, y = self.P(u, v)
        tr = ' transform="rotate(%g %.1f %.1f)"' % (-rot, x, y) if rot else ""
        self.svg.append('<text class="t %s" x="%.1f" y="%.1f" font-size="%.1f" text-anchor="%s" '
                        'dominant-baseline="central"%s>%s</text>' % (cls, x, y, h / 10.0, anchor, tr, html.escape(t)))
        if dxf:
            ha = {"start": 0, "middle": 1, "end": 2}[anchor]
            self.dxf.append("0\nTEXT\n8\n%s\n10\n%.1f\n20\n%.1f\n30\n0\n40\n%.1f\n1\n%s\n50\n%g\n72\n%d\n11\n%.1f\n21\n%.1f\n31\n0\n73\n2\n"
                            % (layer, u, v, h * 0.8, dxf_txt(t), rot, ha, u, v))

    def arrow(self, pts, cls="arrow", layer="0"):
        self.poly(pts, cls, layer, closed=False)

    # ---------------------------------------------------- sheet furniture
    def finish(self, notes=None):
        u0, u1 = self.umin - self.ml + 150, self.umax + self.mr - 150
        v0, v1 = self.vmin - self.mb + 150, self.vmax + self.mt - 150
        self.rect(u0, v0, u1, v1, "frame", "FRAME")
        # title strip
        tb0, tb1 = v0 + 150, v0 + 1550
        self.rect(u0 + 150, tb0, u1 - 150, tb1, "tbfill", "FRAME")
        W = (u1 - 150) - (u0 + 150)
        cols = [("CHỦ ĐẦU TƯ", OWNER, 0.16), ("CÔNG TRÌNH", PROJECT, 0.30),
                ("TÊN BẢN VẼ", self.title, 0.26), ("TỶ LỆ", self.scale, 0.08),
                ("NGÀY", DATE, 0.09), ("KÝ HIỆU", self.code, 0.11)]
        x = u0 + 150
        for i, (k, val, f) in enumerate(cols):
            w = W * f
            if i:
                self.line(x, tb0, x, tb1, "frame2", "FRAME")
            self.text(x + 150, tb1 - 300, k, 150, "", "start")
            hv = min(260, (w - 300) / (len(val) * 0.62))
            self.text(x + 150, tb0 + 520, val, hv, "tb", "start")
            x += w
        self.text(u0 + 300, tb1 + 260, "Thiết kế sơ bộ (phương án kiến trúc) – lập bởi KTS AI Claude. Kích thước tính bằng mm, cao độ tính bằng m. "
                  "Hồ sơ thi công cần được kỹ sư kết cấu/M&E có chứng chỉ hành nghề thẩm tra, ký duyệt.", 150, "ti", "start")
        if notes:
            for i, n in enumerate(notes):
                self.text(u0 + 300, tb1 + 560 + i * 260, n, 160, "", "start")

    def save(self, dxf_out=True):
        body = "\n".join(self.svg)
        svg = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<svg xmlns="http://www.w3.org/2000/svg" width="%.1fmm" height="%.1fmm" viewBox="0 0 %.1f %.1f">\n'
               '<title>%s</title>\n<defs><style>%s</style>%s</defs>\n'
               '<rect x="0" y="0" width="%.1f" height="%.1f" fill="#ffffff"/>\n%s\n</svg>\n'
               % (self.W / 10, self.H / 10, self.W, self.H, html.escape(self.title), CSS, DEFS, self.W, self.H, body))
        with open(os.path.join(OUT, self.fname + ".svg"), "w", encoding="utf-8") as f:
            f.write(svg)
        if not dxf_out:
            return
        lay = "".join("0\nLAYER\n2\n%s\n70\n0\n62\n%d\n6\nCONTINUOUS\n" % (k, c) for k, c in LAYERS.items())
        dxf = ("0\nSECTION\n2\nHEADER\n9\n$ACADVER\n1\nAC1009\n9\n$DWGCODEPAGE\n3\nANSI_1258\n9\n$INSBASE\n10\n0\n20\n0\n30\n0\n0\nENDSEC\n"
               "0\nSECTION\n2\nTABLES\n"
               "0\nTABLE\n2\nLTYPE\n70\n1\n0\nLTYPE\n2\nCONTINUOUS\n70\n0\n3\nSolid line\n72\n65\n73\n0\n40\n0.0\n0\nENDTAB\n"
               "0\nTABLE\n2\nLAYER\n70\n%d\n%s0\nENDTAB\n"
               "0\nTABLE\n2\nSTYLE\n70\n1\n0\nSTYLE\n2\nSTANDARD\n70\n0\n40\n0.0\n41\n1.0\n50\n0.0\n71\n0\n42\n2.5\n3\narial.ttf\n4\n\n0\nENDTAB\n"
               "0\nENDSEC\n0\nSECTION\n2\nENTITIES\n%s0\nENDSEC\n0\nEOF\n" % (len(LAYERS), lay, "".join(self.dxf)))
        with open(os.path.join(OUT, "DXF", self.fname + ".dxf"), "w", encoding="ascii", newline="\r\n") as f:
            f.write(dxf)


# ------------------------------------------------------------ common helpers
def dim_h(s, us, v, h=170, ext=180):
    for u in us:
        s.line(u, v - ext, u, v + ext, "dim", "DIM")
        s.line(u - 70, v - 70, u + 70, v + 70, "dim", "DIM")
    s.line(us[0] - 150, v, us[-1] + 150, v, "dim", "DIM")
    for i, (a, b) in enumerate(zip(us, us[1:])):
        d = b - a
        small = d < 450
        s.text((a + b) / 2, v + (150 if not small else (150 if i % 2 == 0 else -170)), "%d" % d,
               h if not small else 120, "tbl", layer="DIM")


def dim_v(s, vs, u, h=170, ext=180):
    for v in vs:
        s.line(u - ext, v, u + ext, v, "dim", "DIM")
        s.line(u - 70, v - 70, u + 70, v + 70, "dim", "DIM")
    s.line(u, vs[0] - 150, u, vs[-1] + 150, "dim", "DIM")
    for i, (a, b) in enumerate(zip(vs, vs[1:])):
        d = b - a
        small = d < 450
        s.text(u - (150 if not small else (150 if i % 2 == 0 else -170)), (a + b) / 2, "%d" % d,
               h if not small else 120, "tbl", layer="DIM", rot=90)


def level(s, u, v, label, right=True, length=900):
    """ký hiệu cao độ"""
    s.poly([(u, v), (u - 110, v + 160), (u + 110, v + 160)], "cutb", "DIM")
    e = u + length if right else u - length
    s.line(u, v + 160, e, v + 160, "dim", "DIM")
    s.text(u + 180 if right else u - 180, v + 330, label, 170, "tb tbl", "start" if right else "end", "DIM")


class Plan:
    """mặt bằng: X = chiều ngang lô (0..6000, X=0 phía trên), Y = chiều sâu (Y=0 mặt tiền nhà, sân Y<0)"""

    def __init__(self, s):
        self.s = s

    def uv(self, X, Y):
        return (Y, 6000 - X)

    def rect(self, X0, X1, Y0, Y1, cls="", layer="0", dxf=True):
        self.s.rect(Y0, 6000 - X1, Y1, 6000 - X0, cls, layer, dxf)

    def line(self, X0, Y0, X1, Y1, cls="", layer="0", dxf=True):
        self.s.line(Y0, 6000 - X0, Y1, 6000 - X1, cls, layer, dxf)

    def poly(self, pts, cls="", layer="0", closed=True, dxf=True):
        self.s.poly([self.uv(X, Y) for X, Y in pts], cls, layer, closed, dxf)

    def circle(self, X, Y, r, cls="", layer="0", dxf=True):
        self.s.circle(Y, 6000 - X, r, cls, layer, dxf)

    def text(self, X, Y, t, h=200, cls="", anchor="middle", layer="TEXT", rot=0):
        self.s.text(Y, 6000 - X, t, h, cls, anchor, layer, rot)

    def arrow(self, pts, cls="arrow"):
        self.s.arrow([self.uv(X, Y) for X, Y in pts], cls)

    # ---- symbols
    def wall(self, X0, X1, Y0, Y1, cls="wall"):
        self.rect(X0, X1, Y0, Y1, cls, "WALL")

    def gap(self, X0, X1, Y0, Y1):
        self.rect(X0, X1, Y0, Y1, "gap", "WALL", dxf=False)

    def _arc(self, h, a0, a1, w, n=14):
        pts = []
        for k in range(n + 1):
            a = a0 + (a1 - a0) * k / n
            pts.append((h[0] + w * math.cos(a), h[1] + w * math.sin(a)))
        return pts

    def door_y(self, Xa, Xb, Y0, Y1, side=1, hinge="a"):
        """cửa trên tường chạy theo phương X (dải Y0..Y1). side=+1 mở về phía Y tăng"""
        self.gap(Xa, Xb, Y0 - 1, Y1 + 1)
        Yf = Y1 if side > 0 else Y0
        w = abs(Xb - Xa)
        Xh, Xo = (Xa, Xb) if hinge == "a" else (Xb, Xa)
        self.line(Xh, Yf, Xh, Yf + side * w, "door", "DOOR")
        a0 = math.atan2(0, Xo - Xh)
        a1 = math.atan2(side * w, 0)
        d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        self.poly(self._arc((Xh, Yf), a0, a0 + d, w), "doorarc", "DOOR", closed=False)
        self.line(Xa, Y0, Xa, Y1, "door", "DOOR")
        self.line(Xb, Y0, Xb, Y1, "door", "DOOR")

    def door_x(self, Ya, Yb, X0, X1, side=1, hinge="a"):
        """cửa trên tường chạy theo phương Y (dải X0..X1). side=+1 mở về phía X tăng"""
        self.gap(X0 - 1, X1 + 1, Ya, Yb)
        Xf = X1 if side > 0 else X0
        w = abs(Yb - Ya)
        Yh, Yo = (Ya, Yb) if hinge == "a" else (Yb, Ya)
        self.line(Xf, Yh, Xf + side * w, Yh, "door", "DOOR")
        a0 = math.atan2(Yo - Yh, 0)
        a1 = math.atan2(0, side * w)
        d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        self.poly(self._arc((Xf, Yh), a0, a0 + d, w), "doorarc", "DOOR", closed=False)
        self.line(X0, Ya, X1, Ya, "door", "DOOR")
        self.line(X0, Yb, X1, Yb, "door", "DOOR")

    def door2_y(self, Xa, Xb, Y0, Y1, side=1):
        m = (Xa + Xb) / 2
        self.door_y(Xa, m, Y0, Y1, side, "a")
        self.door_y(m, Xb, Y0, Y1, side, "b")

    def win_y(self, Xa, Xb, Y0, Y1):
        self.gap(Xa, Xb, Y0 - 1, Y1 + 1)
        self.rect(Xa, Xb, Y0, Y1, "win", "WIN")
        m = (Y0 + Y1) / 2
        self.line(Xa, m - 20, Xb, m - 20, "winl", "WIN")
        self.line(Xa, m + 20, Xb, m + 20, "winl", "WIN")

    def slide_y(self, Xa, Xb, Y0, Y1, n=4):
        self.gap(Xa, Xb, Y0 - 1, Y1 + 1)
        self.rect(Xa, Xb, Y0, Y1, "win", "WIN")
        w = (Xb - Xa) / n
        for i in range(n):
            off = 35 if i % 2 == 0 else -35
            m = (Y0 + Y1) / 2 + off
            self.line(Xa + i * w, m, Xa + (i + 1) * w + (60 if i < n - 1 else 0), m, "door", "DOOR")

    def col(self, X0, X1, Y0, Y1):
        self.rect(X0, X1, Y0, Y1, "col", "COL")

    def label(self, X, Y, name, area=None, sub=None, h=230):
        n = 1 + (area is not None) + (sub is not None)
        x = X - (n - 1) * 150
        self.text(x, Y, name, h, "tb")
        if area is not None:
            x += 300
            self.text(x, Y, "S = %.1f m²" % area, 165, "tr")
        if sub:
            x += 270
            self.text(x, Y, sub, 140, "ti")

    # ---- furniture
    def bed(self, X0, X1, Y0, Y1, head="X1"):
        self.rect(X0, X1, Y0, Y1, "furn", "FURN")
        if head == "X1":
            self.rect(X1 - 450, X1 - 80, Y0 + 100, (Y0 + Y1) / 2 - 40, "furnd", "FURN")
            self.rect(X1 - 450, X1 - 80, (Y0 + Y1) / 2 + 40, Y1 - 100, "furnd", "FURN")
            self.line(X0 + 700, Y0, X0 + 700, Y1, "furn2", "FURN")
        else:
            self.rect(X0 + 80, X0 + 450, Y0 + 100, (Y0 + Y1) / 2 - 40, "furnd", "FURN")
            self.rect(X0 + 80, X0 + 450, (Y0 + Y1) / 2 + 40, Y1 - 100, "furnd", "FURN")
            self.line(X1 - 700, Y0, X1 - 700, Y1, "furn2", "FURN")

    def wardrobe(self, X0, X1, Y0, Y1):
        self.rect(X0, X1, Y0, Y1, "furn", "FURN")
        self.line(X0, Y0, X1, Y1, "furn2", "FURN")
        self.line(X0, Y1, X1, Y0, "furn2", "FURN")

    def toilet(self, Xc, Yc, wallside="X1"):
        if wallside == "X1":
            self.rect(Xc + 120, Xc + 300, Yc - 220, Yc + 220, "furn", "FURN")
            self.poly([(Xc + 120, Yc - 180), (Xc - 300, Yc - 170), (Xc - 380, Yc), (Xc - 300, Yc + 170), (Xc + 120, Yc + 180)], "furn", "FURN")

    def lavabo(self, X0, X1, Y0, Y1):
        self.rect(X0, X1, Y0, Y1, "furn", "FURN")
        self.circle((X0 + X1) / 2 - 30, (Y0 + Y1) / 2, min(X1 - X0, Y1 - Y0) * 0.33, "furn2", "FURN")

    def plant(self, X, Y, r=260):
        self.circle(X, Y, r, "plant", "FURN")
        self.circle(X, Y, r * 0.45, "furn2", "FURN")

    def chair(self, X0, X1, Y0, Y1):
        self.rect(X0, X1, Y0, Y1, "furn", "FURN")


# ---------------------------------------------------------------- cầu thang dọc nhà (chữ U, 2 vế song song theo Y)
FA = (4800, 5800)            # vế 1: sát tường phải, bắt đầu trong BẾP (Y = 7200) đi lên về phía trước
FB = (3700, 4700)            # vế 2: từ chiếu nghỉ quay lại, lên tới SHC tầng 2 (Y = 7200)
YLF, YL, YS = 3700, 4700, 7200   # mép trước chiếu nghỉ / mép sau chiếu nghỉ / đầu thang
TREAD = 250
COLS_Y = [(0, 300), (3500, 3800), (7050, 7350), (9200, 9500), (12600, 12900), (14700, 15000)]
AXES_Y = [150, 3650, 7200, 9350, 12750, 14850]


def stair(pl, floor):
    cut = 5900                                   # vị trí đường cắt mặt bằng tầng 1
    for k in range(11):
        Y = YL + k * TREAD
        if floor == 1:
            pl.line(FA[0], Y, FA[1], Y, "stair" if Y >= cut else "staird", "STAIR")
            pl.line(FB[0], Y, FB[1], Y, "staird", "STAIR")
        else:
            pl.line(FA[0], Y, FA[1], Y, "stair", "STAIR")
            pl.line(FB[0], Y, FB[1], Y, "stair", "STAIR")
    if floor == 1:
        pl.line(FA[0], cut, FA[0], YS, "stair", "STAIR")
        pl.line(FA[1], cut, FA[1], YS, "stair", "STAIR")
        pl.line(FA[0], YL, FA[0], cut, "staird", "STAIR")
        pl.rect(FB[0], FB[1], YL, YS, "staird", "STAIR")
        pl.rect(FB[0], 5800, YLF, YL, "staird", "STAIR")
        pl.poly([(FA[0] - 150, cut + 100), (5200, cut + 50), (5400, cut - 150), (FA[1] + 50, cut - 200)], "stair", "STAIR", closed=False)
        pl.arrow([(5300, YS - 120), (5300, cut + 250)])
        pl.text(5300, YS + 250, "LÊN", 150, "tb")
        pl.wall(FB[1], FA[0], cut, YS, "wall2")
    else:
        pl.rect(FA[0], FA[1], YL, YS, "stair", "STAIR")
        pl.rect(FB[0], FB[1], YL, YS, "stair", "STAIR")
        pl.rect(FB[0], 5800, YLF, YL, "stair", "STAIR")
        pl.arrow([(4200, YS - 150), (4200, 4200), (5300, 4200), (5300, YS - 150)])
        pl.text(4200, YS + 250, "XUỐNG", 150, "tb")
        pl.wall(FB[1], FA[0], YL, YS, "wall2")
    if floor == 2:
        pl.text(4750, 4200, "Chiếu nghỉ", 120, "ti")


def columns(pl):
    for (Y0, Y1) in COLS_Y:
        pl.col(0, 200, Y0, Y1)
        pl.col(5800, 6000, Y0, Y1)


def axes(pl, s, ymin=-300, ymax=15300):
    names = ["1", "2", "3", "4", "5", "6"]
    for n, Y in zip(names, AXES_Y):
        s.line(Y, 6000 + 2250, Y, -300, "axis", "AXIS")
        s.circle(Y, 6000 + 2550, 280, "bub", "AXIS")
        s.text(Y, 6000 + 2550, n, 230, "tb tr", layer="AXIS")
    for n, X in (("A", 100), ("B", 5900)):
        s.line(ymin, 6000 - X, 15000 + 2050, 6000 - X, "axis", "AXIS")
        s.circle(15000 + 2350, 6000 - X, 280, "bub", "AXIS")
        s.text(15000 + 2350, 6000 - X, n, 230, "tb tr", layer="AXIS")


SEC_B = 6000


def section_marks(pl, s):
    # A-A: X = 4000 dọc nhà (qua vế 2 cầu thang), nhìn về phía X=0
    for Y, lab in ((-5450, "A"), (15350, "A")):
        pl.line(4000, Y - 500 if Y < 0 else Y - 0, 4000, Y + (0 if Y < 0 else 500), "sec")
        pl.arrow([(4000, Y), (3400, Y)], "arrowr")
        pl.circle(3100, Y, 220, "bub")
        pl.text(3100, Y, lab, 200, "tb tr")
    # B-B: ngang nhà qua cầu thang, nhìn về phía sau
    for X in (-450, 6450):
        pl.line(X - 250, SEC_B, X + 250, SEC_B, "sec")
        pl.arrow([(X, SEC_B), (X, SEC_B + 600)], "arrowr")
        pl.circle(X, SEC_B + 900, 220, "bub")
        pl.text(X, SEC_B + 900, "B", 200, "tb tr")


def north(s, u, v):
    s.circle(u, v, 520, "frame2")
    s.poly([(u, v + 480), (u - 200, v - 300), (u, v - 150), (u + 200, v - 300)], "cutb")
    s.text(u, v + 700, "B", 220, "tb")
    s.text(u, v - 800, "(hướng Bắc giả định –", 120, "ti")
    s.text(u, v - 970, "chỉnh theo sổ đỏ)", 120, "ti")


def outer_walls(pl, rear_full=True):
    pl.wall(0, 200, 0, 15000)
    pl.wall(5800, 6000, 0, 15000)
    pl.wall(200, 5800, 0, 200)
    pl.wall(200, 5800, 14800, 15000)


def plan_sheet(code, fname, title):
    s = Sheet(code, fname, title, "1/100", -5000, 15000, 0, 6000, ml=2400, mr=2900, mt=3000, mb=4600)
    return s, Plan(s)


def plan_dims(pl, s, top_chain, x_chain=(0, 200, 1200, 1300, 2700, 2800, 5800, 6000)):
    dim_h(s, top_chain, 6000 + 650)
    dim_h(s, AXES_Y, 6000 + 1250)
    dim_h(s, [-5000, 0, 15000], 6000 + 1850)
    dim_v(s, [6000 - x for x in reversed(x_chain)], 15000 + 650)
    dim_v(s, [0, 6000], 15000 + 1300)


def wc_furniture(pl):
    pl.lavabo(2200, 2700, 9500, 10100)
    pl.toilet(2400, 10650)
    pl.line(1300, 10950, 2700, 10950, "winl", "FURN")
    pl.circle(2000, 11400, 60, "furn2", "FURN")
    pl.text(2000, 11650, "tắm đứng", 105, "ti")
    for Y in (12100, 12350):
        pl.line(1350, Y, 2650, Y, "furn2", "FURN")


def rear_walls(pl, y_front):
    """khối phía sau (hành lang – WC – kho – phòng ngủ) giống nhau 2 tầng; y_front = mép tường trước phòng ngủ"""
    pl.wall(1200, 1300, y_front, 12700)
    pl.wall(2700, 2800, y_front, 12700)
    pl.wall(1300, 2700, 11800, 11900)
    pl.wall(200, 5800, 12700, 12800)
    pl.door_x(9600, 10300, 1200, 1300, side=1, hinge="a")
    pl.door_x(11950, 12650, 1200, 1300, side=1, hinge="b")
    pl.door_y(300, 1100, 12700, 12800, side=1, hinge="a")
    pl.win_y(3600, 5200, 12700, 12800)


# ================================================================ TẦNG 1
def floor1():
    s, pl = plan_sheet("KT-02", "02_Mat-bang-tang-1", "MẶT BẰNG TẦNG 1 (cos +0.450)")
    # sân trước
    pl.rect(0, 6000, -5000, 0, "r-yard", "SITE")
    pl.rect(100, 700, -4800, -1000, "r-san", "SITE")
    pl.rect(5300, 5900, -4800, -1000, "r-san", "SITE")
    for Y in (-4300, -3300, -2300, -1400):
        pl.plant(400, Y, 230)
        pl.plant(5600, Y, 230)
    pl.wall(0, 100, -5000, 0, "wall2")
    pl.wall(5900, 6000, -5000, 0, "wall2")
    pl.wall(100, 1000, -5000, -4850, "wall2")
    pl.wall(5000, 5900, -5000, -4850, "wall2")
    pl.line(1000, -4925, 5000, -4925, "dashr", "SITE")
    pl.arrow([(4700, -4700), (2000, -4700)])
    pl.text(3000, -4550, "Cổng trượt 4.000", 130, "ti", rot=90)
    pl.poly([(2150, -4700), (3850, -4700), (3900, -4300), (3900, -1500), (3800, -1150), (2200, -1150), (2100, -1500), (2100, -4300)], "car", "FURN")
    pl.text(3000, -2900, "Ô tô cỡ nhỏ / 3–4 xe máy", 140, "ti")
    pl.rect(4100, 5200, -3700, -2100, "dash", "SITE")
    pl.text(4650, -2900, "Bể nước ngầm 3m³", 120, "ti", rot=90)
    pl.rect(700, 3300, -900, 0, "furn", "FURN")
    for Y in (-600, -300):
        pl.line(700, Y, 3300, Y, "stair", "STAIR")
    pl.text(2000, -450, "3 bậc tam cấp", 120, "ti")
    pl.rect(0, 6000, -1200, 0, "dash", "SITE")
    pl.text(5000, -1100, "mép ban công T2 phía trên", 110, "ti")
    pl.label(1500, -2700, "SÂN TRƯỚC", 30.0, "lát gạch chống trơn + bồn cây", 240)

    # phòng
    pl.rect(200, 5800, 200, 3700, "r-khach", "ROOM")
    pl.rect(200, 5800, 3700, 9300, "r-bep", "ROOM")
    pl.rect(2800, 5800, 9400, 12700, "r-ngu", "ROOM")
    pl.rect(1300, 2700, 9400, 11800, "r-wc", "ROOM")
    pl.rect(1300, 2700, 11900, 12700, "r-kho", "ROOM")
    pl.rect(200, 1200, 9300, 12700, "r-hall", "ROOM")
    pl.rect(200, 5800, 12800, 14800, "r-san", "ROOM")

    # phòng khách
    pl.rect(200, 550, 350, 1000, "furn", "FURN")
    pl.text(600, 1080, "tủ giày", 110, "ti", "start")
    pl.rect(200, 600, 1100, 3100, "furn", "FURN")
    pl.line(560, 1400, 560, 2800, "door", "FURN")
    pl.text(380, 2100, "Kệ TV", 120, "ti", rot=90)
    pl.rect(2900, 5000, 900, 3200, "dash", "FURN")
    pl.rect(4950, 5750, 800, 3300, "furn", "FURN")
    pl.rect(5550, 5750, 800, 3300, "furnd", "FURN")
    pl.rect(4950, 5550, 800, 1000, "furnd", "FURN")
    pl.rect(4950, 5550, 3100, 3300, "furnd", "FURN")
    pl.line(4950, 1650, 5550, 1650, "furn2", "FURN")
    pl.line(4950, 2450, 5550, 2450, "furn2", "FURN")
    pl.rect(3500, 4400, 1500, 2600, "furn", "FURN")
    pl.plant(550, 3400)
    # phòng ăn (cạnh cầu thang)
    pl.rect(1400, 2300, 4600, 6200, "furn", "FURN")
    for Y in (4700, 5200, 5700):
        pl.chair(1000, 1350, Y, Y + 400)
        pl.chair(2350, 2700, Y, Y + 400)
    pl.rect(FB[0], 5800, YLF, YL, "furnd", "FURN")
    pl.text(4750, 4200, "kệ trang trí dưới chiếu nghỉ", 100, "ti")
    pl.plant(3300, 3950, 200)
    # bếp chữ I dọc tường sau + tủ lạnh
    pl.rect(1300, 4600, 8700, 9300, "furn", "FURN")
    pl.rect(2000, 2700, 8780, 9220, "furn2", "FURN")
    pl.circle(2350, 9000, 150, "furn2", "FURN")
    for (x, y) in ((3300, 8880), (3300, 9120), (3650, 8880), (3650, 9120)):
        pl.circle(x, y, 90, "furn2", "FURN")
    pl.rect(3100, 3900, 8700, 9300, "dash", "FURN")
    pl.text(3500, 8550, "hút mùi", 105, "ti")
    pl.rect(4700, 5400, 8600, 9300, "furnd", "FURN")
    pl.text(5050, 8950, "TL", 140, "tb")
    pl.rect(4800, 5800, YL, 5900, "dash", "FURN")
    pl.text(5300, 5300, "kho dưới CT", 100, "ti", rot=90)
    # phòng ngủ 1
    pl.bed(3800, 5800, 11000, 12600, "X1")
    pl.rect(5300, 5800, 10550, 10950, "furn", "FURN")
    pl.wardrobe(2800, 3400, 11000, 12600)
    wc_furniture(pl)
    # sân phơi
    pl.rect(1400, 2000, 12900, 13500, "furn", "FURN")
    pl.circle(1700, 13200, 220, "furn2", "FURN")
    pl.text(1700, 13700, "máy giặt", 105, "ti")
    pl.lavabo(2100, 2650, 12900, 13350)
    for X in (3200, 3700, 4200, 4700, 5200):
        pl.line(X, 13200, X, 14400, "dash", "FURN")
    pl.text(4200, 14600, "giàn phơi", 110, "ti")
    pl.plant(5450, 14450)
    pl.plant(500, 14450)
    pl.rect(3000, 5600, 13000, 14600, "dashr", "SITE")
    pl.rect(200, 2700, 12800, 14800, "dash", "SITE")

    # tường + cửa
    outer_walls(pl)
    pl.wall(1200, 5800, 9300, 9400)
    rear_walls(pl, 9400)
    pl.door2_y(800, 3200, 0, 200, side=1)
    pl.win_y(3800, 5400, 0, 200)
    pl.door_y(2900, 3700, 9300, 9400, side=1, hinge="a")
    pl.win_y(3600, 5200, 14800, 15000)
    stair(pl, 1)
    columns(pl)

    pl.label(2400, 1700, "PHÒNG KHÁCH", 19.6)
    pl.label(1850, 6800, "PHÒNG ĂN", 11.9, None, 200)
    pl.label(2600, 7900, "BẾP", 11.8, "bếp chữ I + tủ lạnh", 220)
    pl.label(4100, 10250, "PHÒNG NGỦ 1", 9.9, None, 200)
    pl.label(1700, 10150, "WC1", 3.4, None, 170)
    pl.text(2000, 12500, "Kho", 140, "tb")
    pl.text(700, 11000, "HÀNH LANG", 140, "tb", rot=90)
    pl.label(4300, 13700, "SÂN PHƠI", 11.2, "lộ thiên – giếng trời", 220)
    pl.text(1450, 14550, "dưới sàn T2", 110, "ti")
    pl.text(4250, 6000, "CẦU THANG", 140, "tb", rot=90)
    pl.text(3000, 700, "CỬA CHÍNH 2.400", 120, "ti")

    section_marks(pl, s)
    axes(pl, s)
    plan_dims(pl, s, [-5000, -900, 0, 3700, 7200, 9300, 12800, 15000], (0, 200, 1200, 1300, 2700, 2800, 3700, 4700, 4800, 5800, 6000))
    dim_v(s, [6000 - x for x in [6000, 5900, 5000, 1000, 100, 0]], -5000 - 700)
    north(s, -6200 + 900, 6000 + 1700)
    s.finish(["Cầu thang chữ U chạy DỌC NHÀ, chân thang nằm trong BẾP, lên thẳng KHU SINH HOẠT CHUNG tầng 2: 22 bậc, h = 164, b = 250, vế rộng 1.000.",
              "Mật độ xây dựng 75% (90/120 m²). Cos ±0.000 = mặt sân trước; nền tầng 1 = +0.450. Khung nét đứt đỏ ở sân phơi: bể tự hoại 3 ngăn đặt ngầm."])
    s.save()


# ================================================================ TẦNG 2
def floor2():
    s, pl = plan_sheet("KT-03", "03_Mat-bang-tang-2", "MẶT BẰNG TẦNG 2 (cos +4.050)")
    pl.rect(0, 6000, -5000, 0, "dash", "SITE")
    pl.text(3000, -3000, "(sân trước – tầng dưới)", 160, "ti")
    # ban công
    pl.rect(0, 6000, -1200, 0, "r-bc", "ROOM")
    pl.rect(300, 2400, -1150, -850, "plant", "FURN")
    pl.text(1350, -700, "bồn cây", 110, "ti")
    pl.circle(5000, -600, 250, "furn", "FURN")
    pl.chair(4350, 4700, -800, -400)
    pl.chair(5300, 5650, -800, -400)
    pl.rect(0, 6000, -1200, -1150, "rail", "WALL")
    pl.rect(0, 50, -1150, 0, "rail", "WALL")
    pl.rect(5950, 6000, -1150, 0, "rail", "WALL")
    pl.text(3400, -500, "BAN CÔNG 7,2 m²", 150, "tb", rot=90)
    # phòng
    pl.rect(200, 2400, 200, 3600, "r-tho", "ROOM")
    pl.rect(2500, 5800, 200, 3600, "r-ngu", "ROOM")
    pl.rect(200, 3700, 3700, 8500, "r-shc", "ROOM")
    pl.rect(3700, 5800, YS, 8500, "r-shc", "ROOM")
    pl.rect(3700, 5800, YLF, YS, "r-void", "ROOM")
    pl.rect(1300, 2700, 9400, 11800, "r-wc", "ROOM")
    pl.rect(1300, 2700, 11900, 12700, "r-kho", "ROOM")
    pl.rect(200, 1200, 8500, 12700, "r-hall", "ROOM")
    pl.rect(2800, 5800, 8600, 12700, "r-ngu", "ROOM")
    pl.rect(200, 2700, 12800, 14800, "r-san", "ROOM")
    pl.rect(2800, 5800, 12800, 14800, "r-void", "ROOM")
    pl.line(2800, 12800, 5800, 14800, "dash")
    pl.line(2800, 14800, 5800, 12800, "dash")
    # phòng thờ (phía trước)
    pl.rect(300, 1500, 3000, 3600, "furnd", "FURN")
    pl.rect(450, 1350, 3250, 3600, "furn", "FURN")
    pl.text(900, 3150, "BÀN THỜ", 115, "tb")
    pl.rect(500, 2100, 1000, 2600, "dash", "FURN")
    pl.plant(2150, 500, 180)
    # PN2
    pl.bed(3800, 5800, 1000, 2600, "X1")
    pl.rect(5300, 5800, 550, 950, "furn", "FURN")
    pl.rect(5300, 5800, 2650, 3050, "furn", "FURN")
    pl.wardrobe(2500, 3100, 300, 2400)
    # SHC
    pl.rect(200, 1000, 4200, 6400, "furn", "FURN")
    pl.rect(200, 400, 4200, 6400, "furnd", "FURN")
    pl.line(400, 5300, 1000, 5300, "furn2", "FURN")
    pl.rect(1400, 2100, 4800, 5800, "furn", "FURN")
    pl.circle(2900, 5300, 330, "furn", "FURN")
    pl.circle(2900, 6200, 330, "furn", "FURN")
    pl.rect(4900, 5800, 8150, 8500, "furnd", "FURN")
    pl.text(5300, 7900, "kệ sách", 105, "ti")
    pl.plant(500, 7800, 220)
    pl.wardrobe(1300, 2700, 8550, 9300)
    pl.text(2000, 8350, "tủ âm tường", 100, "ti")
    # PN3
    pl.bed(3800, 5800, 10900, 12300, "X1")
    pl.rect(5300, 5800, 10450, 10850, "furn", "FURN")
    pl.wardrobe(2800, 3400, 10900, 12600)
    pl.rect(5200, 5800, 8700, 9800, "furn", "FURN")
    pl.chair(4750, 5150, 9050, 9450)
    pl.text(5500, 9250, "bàn học", 105, "ti", rot=90)
    wc_furniture(pl)
    # sân phơi T2
    for X in (500, 900, 1300, 1700, 2100):
        pl.line(X, 13300, X, 14500, "dash", "FURN")
    pl.rect(1600, 2100, 12800, 13050, "furnd", "FURN")
    for X in (1700, 1850, 2000):
        pl.line(X, 12800, X, 13050, "furn2", "FURN")
    pl.text(1850, 13250, "thang lên mái", 100, "ti")

    outer_walls(pl)
    pl.wall(200, 5800, 3600, 3700)
    pl.wall(2400, 2500, 200, 3600)
    pl.wall(2700, 5800, 8500, 8600)
    pl.wall(1300, 2700, 9300, 9400)
    rear_walls(pl, 8500)
    pl.rect(3640, 3700, YLF, YS, "rail", "WALL")
    pl.rect(FA[0], FA[1], YS - 30, YS + 30, "rail", "WALL")
    pl.rect(2700, 2780, 12800, 14800, "rail", "WALL")
    # cửa
    pl.win_y(500, 2100, 0, 200)
    pl.slide_y(2900, 4900, 0, 200, n=2)
    pl.door_y(1500, 2300, 3600, 3700, side=-1, hinge="b")
    pl.door_y(2700, 3500, 3600, 3700, side=-1, hinge="a")
    pl.door_y(3900, 4700, 8500, 8600, side=1, hinge="a")
    stair(pl, 2)
    columns(pl)

    pl.label(1300, 1800, "PHÒNG THỜ", 7.5, None, 190)
    pl.label(3700, 1800, "PHÒNG NGỦ 2", 11.2, None, 200)
    pl.label(1900, 7300, "SINH HOẠT CHUNG", 19.2, None, 190)
    pl.text(4750, 5900, "ô thông tầng cầu thang", 105, "ti")
    pl.label(4000, 9900, "PHÒNG NGỦ 3", 12.3, None, 200)
    pl.label(1700, 10150, "WC2", 3.4, None, 170)
    pl.text(2000, 12500, "Kho", 140, "tb")
    pl.text(700, 11000, "HÀNH LANG", 140, "tb", rot=90)
    pl.label(1450, 13900, "SÂN PHƠI", 5.0, None, 190)
    pl.label(4300, 13500, "GIẾNG TRỜI", 6.0, "thông tầng xuống sân phơi T1", 200)
    pl.text(1300, 400, "CỬA SỔ", 110, "ti")
    pl.text(3900, 400, "CỬA KÍNH LÙA", 110, "ti")

    section_marks(pl, s)
    axes(pl, s)
    plan_dims(pl, s, [-1200, 0, 3650, 7200, 8550, 12750, 15000], (0, 200, 1200, 1300, 2400, 2500, 2700, 2800, 3700, 5800, 6000))
    north(s, -6200 + 900, 6000 + 1700)
    s.finish(["Tầng 2: phòng thờ ĐẶT PHÍA TRƯỚC (cạnh phòng ngủ 2, cùng nhìn ra ban công), khu sinh hoạt chung giữa nhà quanh ô cầu thang, phòng ngủ 3 + WC2 phía sau.",
              "Phòng thờ nằm trên cùng, phía trên không có phòng; bàn thờ tựa tường đặc, quay mặt ra phía trước; WC2 ở xa, không chung tường với phòng thờ."])
    s.save()


# ================================================================ MÁI
def roof():
    s, pl = plan_sheet("KT-04", "04_Mat-bang-mai", "MẶT BẰNG MÁI BẰNG (cos +7.450)")
    pl.rect(0, 6000, -5000, 0, "dash", "SITE")
    pl.rect(200, 5800, -1000, 12700, "r-roof", "ROOM")
    pl.rect(3700, 5800, YLF, YS, "r-glass", "WIN")
    pl.rect(200, 5800, 12800, 14800, "r-void", "ROOM")
    pl.line(200, 12800, 5800, 14800, "dash")
    pl.line(200, 14800, 5800, 12800, "dash")
    pl.rect(1300, 2700, 9700, 11500, "furnd", "FURN")
    pl.circle(2000, 10600, 600, "furn", "FURN")
    pl.text(2000, 10600, "Bồn inox 1.500L", 110, "tb", rot=90)
    pl.rect(3300, 5300, 9700, 11500, "r-glass", "FURN")
    for Y in range(9850, 11500, 150):
        pl.line(3300, Y, 5300, Y, "furn2", "FURN")
    for Y0 in (1000, 1900, 2800):
        pl.rect(600, 1400, Y0, Y0 + 500, "furn", "FURN")
    pl.rect(600, 1400, 8000, 8500, "furn", "FURN")
    pl.text(1000, 2150, "Dàn nóng ĐH", 110, "ti", rot=90)
    pl.circle(1500, 11900, 80, "furn2", "FURN")
    for X in (600, 5400):
        pl.circle(X, 12450, 110, "furn", "FURN")
        pl.circle(X, 12450, 50, "furn2", "FURN")
    pl.circle(600, -800, 110, "furn", "FURN")
    pl.circle(5400, -800, 110, "furn", "FURN")
    for X in (2200, 3000):
        pl.arrow([(X, 500), (X, 3200)])
        pl.text(X + 220, 1800, "i = 2%", 130, "tb")
    for X in (900, 5100):
        pl.arrow([(X, 8200), (X, 12200)])
    pl.arrow([(2000, 400), (2000, -700)])
    pl.text(2000 + 230, -300, "i = 2%", 120, "tb")
    pl.wall(0, 200, -1200, 15000)
    pl.wall(5800, 6000, -1200, 15000)
    pl.wall(200, 5800, -1200, -1000)
    pl.wall(200, 1600, 12700, 12800)
    pl.wall(2100, 5800, 12700, 12800)
    pl.wall(200, 5800, 14800, 15000)
    pl.rect(1600, 2100, 12700, 12800, "rail", "WALL")
    pl.rect(3600, 3700, YLF - 100, YS + 100, "wall2", "WALL")
    pl.rect(3700, 5800, YLF - 100, YLF, "wall2", "WALL")
    pl.rect(3700, 5800, YS, YS + 100, "wall2", "WALL")
    columns(pl)

    pl.label(4750, 5450, "GIẾNG TRỜI KÍNH", None, "phía trên cầu thang", 160)
    pl.label(3000, 13800, "", None) if False else None
    pl.text(3000, 13650, "GIẾNG TRỜI SAU NHÀ (lộ thiên)", 160, "tb", rot=90)
    pl.text(3000, 14150, "lưới inox an toàn / mái kính di động", 115, "ti", rot=90)
    pl.text(4300, 11800, "Máy NLMT 180L", 120, "tb")
    pl.text(1850, 12450, "cửa lên mái", 105, "ti")
    pl.text(950, 12150, "phễu thu Ø90", 105, "ti")
    pl.text(5050, 12150, "phễu thu Ø90", 105, "ti")
    pl.text(1500, 11650, "ống thông hơi", 100, "ti")
    pl.label(2200, 6000, "MÁI BẰNG BTCT", None, "chống thấm + chống nóng", 220)
    pl.text(3000, -550, "mái đua ban công", 110, "ti", rot=90)

    axes(pl, s, ymin=-1500)
    plan_dims(pl, s, [-1200, 0, 3700, 7200, 9700, 11500, 12800, 15000], (0, 200, 1300, 2700, 3700, 5800, 6000))
    north(s, -6200 + 900, 6000 + 1700)
    s.finish(["Cấu tạo mái: sàn BTCT 120 – chống thấm gốc xi măng/ màng khò nóng 2 lớp, bò lên tường 300 – vữa tạo dốc 2% – gạch chống nóng 6 lỗ – lát gạch đất nung.",
              "Tường chắn mái cao 1.100 so với mặt mái hoàn thiện; lên mái bằng thang leo inox từ sân phơi tầng 2."])
    s.save()


# ================================================================ TỔNG THỂ
def site():
    s = Sheet("KT-01", "01_Mat-bang-tong-the", "MẶT BẰNG TỔNG THỂ – VỊ TRÍ", "1/100",
              -8500, 15000, -1500, 7500, ml=1500, mr=9800, mt=1500, mb=4600)
    pl = Plan(s)
    pl.rect(-1500, 7500, -8500, -5000, "r-road", "SITE")
    s.text(-6750, 3000, "ĐƯỜNG / NGÕ PHÍA TRƯỚC", 260, "tb", rot=90)
    pl.rect(-1500, 0, -5000, 15000, "r-nb", "SITE")
    pl.rect(6000, 7500, -5000, 15000, "r-nb", "SITE")
    pl.text(-750, 5000, "NHÀ LIỀN KỀ", 220, "tb")
    pl.text(6750, 5000, "NHÀ LIỀN KỀ", 220, "tb")
    pl.rect(0, 6000, -5000, 0, "r-yard", "SITE")
    pl.rect(0, 6000, -1200, 12800, "r-roof", "SITE")
    pl.rect(0, 6000, 12800, 15000, "r-san", "SITE")
    pl.line(0, 12800, 6000, 15000, "dash")
    pl.line(0, 15000, 6000, 12800, "dash")
    pl.rect(3700, 5800, YLF, YS, "r-glass", "WIN")
    pl.rect(0, 6000, -5000, 15000, "axis", "SITE")
    pl.poly([(2150, -4700), (3850, -4700), (3900, -4300), (3900, -1500), (3800, -1150), (2200, -1150), (2100, -1500), (2100, -4300)], "car", "FURN")
    for Y in (-4300, -3300, -2300):
        pl.plant(400, Y, 230)
        pl.plant(5600, Y, 230)
    pl.wall(0, 1000, -5000, -4850, "wall2")
    pl.wall(5000, 6000, -5000, -4850, "wall2")
    pl.line(1000, -4925, 5000, -4925, "dashr")
    pl.text(3000, -4600, "CỔNG", 170, "tb")
    pl.text(3000, -800, "", 10)
    pl.label(2000, 5300, "NHÀ Ở 2 TẦNG – MÁI BẰNG", None, "khối nhà 6 × 15 m, ban công đua 1,2 m", 280)
    pl.text(3000, 6600, "", 10)
    pl.text(3000, 13900, "GIẾNG TRỜI / SÂN PHƠI", 170, "tb")
    pl.text(1500, -2700, "SÂN TRƯỚC 6 × 5 m", 190, "tb", rot=0)
    pl.text(5200, 7350, "", 10)
    pl.arrow([(3000, -7300), (3000, -5300)], "arrowr")
    s.text(-6000, 6000 - 3000 - 900, "LỐI VÀO", 160, "tb tr", rot=90)
    dim_h(s, [-5000, 0, 15000], 6000 + 700)
    dim_h(s, [-5000, 15000], 6000 + 1200)
    dim_v(s, [0, 6000], -5000 - 600)
    # bảng chỉ tiêu
    u0 = 15000 + 900
    rows = [("BẢNG CHỈ TIÊU KỸ THUẬT", ""),
            ("Diện tích lô đất", "120,0 m² (6 × 20 m)"),
            ("Diện tích xây dựng", "90,0 m² (6 × 15 m)"),
            ("Mật độ xây dựng", "75 %"),
            ("Sân trước", "30,0 m² (6 × 5 m)"),
            ("Số tầng", "2 tầng, mái bằng BTCT"),
            ("Sàn tầng 1 (trong nhà)", "76,8 m² + sân phơi 13,2 m²"),
            ("Sàn tầng 2", "76,8 m² + ban công 7,2 + sân phơi 5,4"),
            ("Tổng DT sàn xây dựng", "≈ 179 m²"),
            ("Chiều cao tầng 1 / tầng 2", "3,6 m / 3,4 m"),
            ("Cao độ đỉnh tường chắn mái", "+8,550 m"),
            ("Cos nền tầng 1", "+0,450 so với sân"),
            ("Phong cách", "Hiện đại – tối giản"),
            ]
    for i, (k, v) in enumerate(rows):
        y = 7200 - i * 560
        if i == 0:
            s.text(u0, y, k, 260, "tb", "start")
            s.line(u0, y - 300, u0 + 8000, y - 300, "frame2")
            continue
        s.text(u0, y, k, 180, "", "start")
        s.text(u0 + 3700, y, v, 180, "tb", "start")
        s.line(u0, y - 300, u0 + 8000, y - 300, "dim")
    north(s, 15000 + 7000, -800)
    s.finish(["Ranh giới lô đất thể hiện nét chấm gạch đỏ. Vị trí bể nước ngầm 3 m³ dưới sân trước, bể tự hoại dưới sân phơi tầng 1."])
    s.save()


# ================================================================ MẶT ĐỨNG
def elevation():
    s = Sheet("KT-05", "05_Mat-dung-chinh", "MẶT ĐỨNG CHÍNH (TRỤC B – A)", "1/100",
              -1200, 7200, -600, 9600, ml=900, mr=7400, mt=900, mb=4600)
    s.rect(-1200, 0, 0, 7800, "e-ghost", "ELEV")
    s.rect(6000, 0, 7200, 7800, "e-ghost", "ELEV")
    s.text(-600, 3900, "nhà bên cạnh", 150, "ti", rot=90)
    s.text(6600, 3900, "nhà bên cạnh", 150, "ti", rot=90)
    # bồn nước phía sau
    s.rect(1300, 8550, 2700, 9150, "e-ghost", "ELEV")
    s.text(2000, 9350, "bồn nước (phía sau, khuất)", 110, "ti")
    # đế nhà + tường tầng 1
    s.rect(0, 0, 6000, 450, "e-dark", "ELEV")
    s.rect(0, 450, 6000, 3850, "e-wall", "ELEV")
    s.rect(0, 450, 700, 3850, "e-stone", "ELEV")
    for z in range(750, 3850, 300):
        s.line(0, z, 700, z, "e-stl", "ELEV")
    for z in range(600, 3850, 600):
        s.line(350, z, 350, z + 300, "e-stl", "ELEV")
    s.rect(150, 2550, 550, 2850, "e-dark", "ELEV")
    s.text(350, 2700, "SỐ NHÀ", 70, "tw tb")
    # cửa chính
    s.rect(800, 450, 3200, 3450, "e-glass", "ELEV")
    s.rect(800, 450, 3200, 3450, "e-alu", "ELEV")
    s.line(800, 3050, 3200, 3050, "e-alu", "ELEV")
    for x in (1400, 2000, 2600):
        s.line(x, 450, x, 3050, "e-alu", "ELEV")
    for x in (1900, 2100):
        s.line(x, 1500, x, 2000, "e-alu", "ELEV")
    # cửa sổ
    s.rect(3800, 1250, 5400, 3450, "e-glass", "ELEV")
    s.rect(3800, 1250, 5400, 3450, "e-alu", "ELEV")
    s.line(3800, 3050, 5400, 3050, "e-alu", "ELEV")
    s.line(4600, 1250, 4600, 3050, "e-alu", "ELEV")
    s.rect(3700, 1150, 5500, 1250, "e-dark", "ELEV")
    # đèn
    for x in (500, 5700):
        pass
    # tầng 2 lõm
    s.rect(250, 4050, 5750, 7300, "e-recess", "ELEV")
    for x0, z0, x1 in ((500, 4750, 2100), (2900, 4050, 4900)):      # cửa sổ phòng thờ, cửa lùa phòng ngủ 2
        s.rect(x0, z0, x1, 6850, "e-glass", "ELEV")
        s.rect(x0, z0, x1, 6850, "e-alu", "ELEV")
        s.line((x0 + x1) / 2, z0, (x0 + x1) / 2, 6850, "e-alu", "ELEV")
        s.line(x0, 6450, x1, 6450, "e-alu", "ELEV")
    s.rect(5000, 4050, 5750, 7300, "e-dark", "ELEV")
    x = 5000
    while x < 5750:
        s.rect(x, 4050, x + 50, 7300, "e-wood", "ELEV")
        x += 100
    # bồn cây
    s.rect(300, 4050, 2400, 4500, "e-dark", "ELEV")
    for i, x in enumerate(range(450, 2400, 260)):
        s.circle(x, 4650 + (i % 2) * 120, 200, "plant", "ELEV")
    # lan can kính
    s.rect(250, 4050, 5750, 5150, "e-glass2", "ELEV")
    s.rect(250, 5110, 5750, 5170, "e-dark", "ELEV")
    for x in (1600, 2950, 4300):
        s.line(x, 4050, x, 5150, "e-alu", "ELEV")
    # khung viền
    s.rect(0, 3850, 6000, 4050, "e-frame", "ELEV")
    s.rect(0, 3850, 250, 8550, "e-frame", "ELEV")
    s.rect(5750, 3850, 6000, 8550, "e-frame", "ELEV")
    s.rect(0, 7300, 6000, 8550, "e-frame", "ELEV")
    s.rect(0, 8450, 6000, 8550, "e-dark", "ELEV")
    s.line(250, 7300, 5750, 7300, "e-shadow", "ELEV")
    s.line(0, 3850, 6000, 3850, "e-shadow", "ELEV")
    for x in (1000, 3000, 5000):
        s.rect(x - 80, 7240, x + 80, 7300, "e-light", "ELEV")
    for x in (1000, 2000, 3000, 4000, 5000):
        s.rect(x - 80, 3790, x + 80, 3850, "e-light", "ELEV")
    # bậc
    s.rect(700, 0, 3300, 450, "e-stone", "ELEV")
    for z in (150, 300):
        s.line(700, z, 3300, z, "e-stl", "ELEV")
    s.line(-1200, 0, 7200, 0, "e-gr", "ELEV")
    # cao độ
    for z, lab in ((0, "±0.000"), (450, "+0.450"), (4050, "+4.050"), (7450, "+7.450"), (8550, "+8.550")):
        level(s, 6300, z, lab, right=True, length=850)
    dim_v(s, [0, 450, 4050, 7450, 8550], -700)
    dim_h(s, [0, 700, 800, 3200, 3800, 5400, 6000], -350 - 0)
    # chú thích
    marks = [(1, 3000, 8000, "Khung viền BTCT bao tầng 2, sơn ngoại thất trắng sứ"),
             (2, 5375, 6200, "Lam đứng gỗ nhựa composite màu óc chó, che nắng"),
             (3, 3600, 4700, "Lan can kính cường lực 10,38 mm, tay vịn sơn đen"),
             (4, 3900, 5900, "Cửa lùa PN2 + cửa sổ phòng thờ, nhôm hệ ghi đen"),
             (5, 1300, 4300, "Bồn cây xanh ban công (BTCT, chống thấm)"),
             (6, 2000, 2400, "Cửa chính 4 cánh nhôm kính cường lực 8 mm"),
             (7, 350, 1800, "Cột ốp đá granite xám tro băm mặt"),
             (8, 4200, 2200, "Cửa sổ nhôm kính mở hất + khung bảo vệ âm"),
             (9, 2000, 200, "Đế nhà, bậc tam cấp ốp đá granite đen"),
             (10, 4500, 8500, "Mũ tường, phào chỉ sơn ghi đậm"),
             (11, 3000, 3820, "Đèn LED hắt sáng âm trần ban công & khung viền")]
    for n, x, z, t in marks:
        s.circle(x, z, 170, "bub", "TEXT")
        s.text(x, z, str(n), 150, "tb tr")
        y = 8800 - (n - 1) * 560
        s.circle(7900, y, 170, "bub", "TEXT")
        s.text(7900, y, str(n), 150, "tb tr")
        s.text(8200, y, t, 175, "", "start")
    s.text(7700, 9400, "VẬT LIỆU MẶT ĐỨNG", 240, "tb", "start")
    s.finish(["Tông màu chủ đạo: trắng – ghi đen – gỗ ấm; mặt tiền 2 lớp (kính + lam) giảm bức xạ, tạo chiều sâu cho mặt đứng phẳng mái bằng."])
    s.save()


# ================================================================ MẶT CẮT A-A
def riser():
    return 3600 / 22.0


def stair_profile_y(y0, z0, n, R, direction=1):
    """biên trên bậc thang chạy theo Y: bắt đầu ở (y0, z0), n bậc, mỗi bậc lên R rồi tiến 250 theo direction"""
    pts = [(y0, z0)]
    y, z = y0, z0
    for _ in range(n):
        z += R
        pts.append((y, z))
        y += direction * TREAD
        pts.append((y, z))
    return pts


# ================================================================ MẶT CẮT A-A
def section_a():
    s = Sheet("KT-06", "06_Mat-cat-A-A", "MẶT CẮT A – A (dọc nhà, qua cầu thang)", "1/100",
              -5600, 15600, -2700, 9400, ml=1700, mr=1900, mt=900, mb=4600)
    R = riser()
    s.rect(-5600, -1900, 15600, 0, "earth", "CUT", dxf=False)
    s.line(-5600, 0, 0, 0, "e-gr", "CUT")
    for Yc in AXES_Y:
        s.rect(Yc - 600, -1600, Yc + 600, -1300, "cut", "CUT")
        s.rect(Yc - 150, -1300, Yc + 150, -500, "cut", "CUT")
    for a, b in zip(AXES_Y, AXES_Y[1:]):
        s.rect(a, -700, b, -350, "cut", "CUT")
    s.text(7500, -1050, "Móng băng / móng cọc BTCT – chọn theo kết quả khảo sát địa chất", 150, "ti")
    s.rect(0, 350, 15000, 450, "cut", "CUT")
    s.rect(0, 0, 15000, 350, "beyondf", "CUT")
    s.text(9800, 180, "đất đắp đầm chặt, lớp bê tông lót", 110, "ti")
    s.poly([(-900, 0), (-900, 150), (-600, 150), (-600, 300), (-300, 300), (-300, 450), (0, 450), (0, 0)], "cut", "CUT")
    s.rect(-5050, 0, -4950, 1900, "cut", "CUT")
    s.rect(-5200, 0, -5000, 2100, "beyondf", "BEYOND")
    s.text(-5000, 2350, "cổng", 130, "ti")
    s.poly([(-4700, 150), (-4700, 900), (-3700, 1450), (-2000, 1450), (-1300, 900), (-1150, 800), (-1150, 150)], "beyond", "BEYOND")
    s.circle(-4100, 200, 260, "beyond", "BEYOND")
    s.circle(-1800, 200, 260, "beyond", "BEYOND")
    # mặt tiền tầng 1 (cắt qua cửa sổ)
    s.rect(0, 450, 200, 1250, "cut", "CUT")
    s.rect(30, 1250, 170, 3250, "glassc", "CUT")
    s.rect(0, 3250, 200, 3650, "cut", "CUT")
    # sàn tầng 2 + dầm (ô cầu thang Y 3700–7200)
    s.rect(-1200, 3930, YLF, 4050, "cut", "CUT")
    s.rect(YS, 3930, 12800, 4050, "cut", "CUT")
    for Yc in AXES_Y[:-1]:
        s.rect(Yc - 110, 3650, Yc + 110, 3930, "cut", "CUT")
    s.rect(-1200, 3800, -1000, 3930, "cut", "CUT")
    # ban công
    s.rect(-1200, 4050, -1170, 5150, "glassc", "CUT")
    s.rect(-1220, 5150, -1150, 5200, "cutb", "CUT")
    s.rect(-1150, 4050, -900, 4450, "cut", "CUT")
    # mặt tiền tầng 2 (cửa lùa phòng ngủ 2)
    s.rect(30, 4050, 170, 6850, "glassc", "CUT")
    s.rect(0, 6850, 200, 7050, "cut", "CUT")
    # tường trong
    s.rect(3600, 4050, 3700, 7050, "cut", "CUT")
    s.rect(9300, 450, 9400, 3650, "cut", "CUT")
    s.rect(8500, 6250, 8600, 7050, "cut", "CUT")
    s.rect(8500, 4050, 8600, 6250, "beyondf", "BEYOND")
    s.text(8550, 5150, "cửa PN3", 100, "ti", rot=90)
    s.rect(12700, 450, 12800, 1350, "cut", "CUT")
    s.rect(12720, 1350, 12780, 2850, "glassc", "CUT")
    s.rect(12700, 2850, 12800, 3650, "cut", "CUT")
    s.rect(12700, 4050, 12800, 4950, "cut", "CUT")
    s.rect(12720, 4950, 12780, 6450, "glassc", "CUT")
    s.rect(12700, 6450, 12800, 7050, "cut", "CUT")
    s.rect(14800, 450, 15000, 8550, "cut", "CUT")
    # mái + giếng trời kính trên cầu thang
    s.rect(-1200, 7330, YLF, 7450, "cut", "CUT")
    s.rect(YS, 7330, 12800, 7450, "cut", "CUT")
    for Yc in AXES_Y[:-1]:
        s.rect(Yc - 110, 7050, Yc + 110, 7330, "cut", "CUT")
    s.rect(-1200, 7150, -1000, 7330, "cut", "CUT")
    s.rect(-1200, 7450, -1000, 8550, "cut", "CUT")
    s.rect(-1000, 7450, YLF - 100, 7580, "insul", "CUT")
    s.rect(YS + 100, 7450, 12700, 7580, "insul", "CUT")
    s.rect(12700, 7450, 12800, 8550, "cut", "CUT")
    s.rect(YLF - 100, 7450, YLF, 7900, "cut", "CUT")
    s.rect(YS, 7450, YS + 100, 7700, "cut", "CUT")
    s.poly([(YLF - 100, 7900), (YS + 100, 7700), (YS + 100, 7750), (YLF - 100, 7950)], "glassc", "CUT")
    s.rect(9700, 7580, 11500, 8000, "beyond", "BEYOND")
    s.rect(9800, 8000, 11400, 9000, "beyondf", "BEYOND")
    s.text(10600, 8500, "bồn nước", 120, "ti")
    # cầu thang: chiếu nghỉ + vế 2 bị cắt dọc theo chiều dài (X = 4000 nằm trong vế 2)
    top = [(YLF, 2250)] + stair_profile_y(YL, 2250, 11, R)
    top[-1] = (YS, 4050)
    bottom = [(YS, 3880), (YL, 2100), (YLF, 2100)]
    s.poly(top + bottom, "cut", "STAIR")
    s.line(YL, 2250 + 900, YS, 4050 + 900, "e-alu", "STAIR")
    for k in range(0, 11, 2):
        yy = YL + k * TREAD + TREAD / 2
        zz = 2250 + (k + 1) * R
        s.line(yy, zz, yy, zz + 900, "beyond", "STAIR")
    s.rect(YLF, 450, YL + 500, 2100, "beyondf", "BEYOND")
    s.text(YL - 250, 1300, "kệ dưới chiếu nghỉ", 100, "ti")
    # đồ đạc phía sau mặt cắt
    s.rect(4950, 450, 5750, 1250, "beyond", "BEYOND") if False else None
    s.rect(4600, 450, 6200, 1210, "beyond", "BEYOND")
    s.rect(8700, 450, 9300, 1300, "cut", "FURN")
    s.rect(8950, 2000, 9300, 2700, "beyond", "BEYOND")
    s.rect(3800, 450, 4400, 900, "beyond", "BEYOND")
    s.rect(1000, 4050, 2600, 4550, "beyond", "BEYOND")
    s.rect(10900, 450, 12300, 1050, "beyond", "BEYOND")
    s.rect(10900, 4050, 12300, 4650, "beyond", "BEYOND")
    s.rect(4200, 4050, 6400, 4470, "beyond", "BEYOND")
    # ánh sáng & gió
    s.arrow([(13300, 9300), (13800, 7600), (13800, 5800)], "sun")
    s.arrow([(14300, 9300), (14200, 3000)], "sun")
    s.arrow([(5200, 9200), (5000, 5600)], "sun")
    s.arrow([(6300, 9200), (6000, 3000)], "sun")
    s.arrow([(-2500, 2500), (1800, 2500)], "wind")
    s.arrow([(10500, 2300), (13600, 2300), (13900, 8800)], "wind")
    s.text(14000, 9150, "nắng", 120, "ti")
    s.text(-2200, 2750, "gió", 120, "ti")
    labels = [(1900, 2300, "PHÒNG KHÁCH"), (5450, 1600, "phòng ăn (phía sau)"), (5450, 3150, "CẦU THANG"),
              (8250, 2300, "BẾP"), (11050, 2300, "PHÒNG NGỦ 1"), (13800, 1200, "SÂN PHƠI"), (-2900, 2200, "SÂN TRƯỚC"),
              (-600, 6300, "BAN CÔNG"), (1850, 5700, "PHÒNG NGỦ 2"), (5450, 6300, "thông tầng"),
              (7850, 5700, "SHC"), (10700, 5700, "PHÒNG NGỦ 3"), (13800, 5200, "GIẾNG TRỜI"),
              (5450, 8250, "giếng trời kính")]
    for y, z, t in labels:
        s.text(y, z, t, 180 if t.isupper() else 130, "tb" if t.isupper() else "ti")
    for z, lab in ((0, "±0.000"), (450, "+0.450"), (4050, "+4.050"), (7450, "+7.450"), (8550, "+8.550")):
        level(s, 15300, z, lab, right=True, length=200)
    level(s, YLF - 300, 2250, "+2.250", right=False, length=200)
    dim_v(s, [0, 450, 4050, 7450, 8550], -5300)
    dim_h(s, [-5000, -1200, 0, YLF, YL, YS, 9350, 12750, 15000], -2350)
    s.finish(["Cầu thang chạy dọc nhà: vế 1 sát tường phải bắt đầu trong bếp, chiếu nghỉ phía trước (+2.250), vế 2 lên tới khu SHC. Giếng trời kính trên ô cầu thang và giếng trời sau nhà tạo đối lưu thông gió."])
    s.save()


# ================================================================ MẶT CẮT B-B
def section_b():
    s = Sheet("KT-07", "07_Mat-cat-B-B", "MẶT CẮT B – B (ngang nhà, qua cầu thang)", "1/100",
              -1200, 7200, -2700, 9400, ml=1700, mr=7400, mt=900, mb=4600)
    R = riser()
    y = SEC_B
    s.rect(-1200, -1900, 7200, 0, "earth", "CUT", dxf=False)
    s.rect(-1200, 0, 0, 7800, "e-ghost", "BEYOND")
    s.rect(6000, 0, 7200, 7800, "e-ghost", "BEYOND")
    for xc in (100, 5900):
        s.rect(xc - 600 if xc > 3000 else xc - 100, -1600, xc + 100 if xc > 3000 else xc + 600, -1300, "cut", "CUT")
        s.rect(xc - 100, -1300, xc + 100, 450, "cut", "CUT")
    s.rect(200, -700, 5800, -350, "cut", "CUT")
    s.rect(200, 350, 5800, 450, "cut", "CUT")
    s.rect(200, 0, 5800, 350, "beyondf", "CUT")
    s.rect(0, 450, 200, 8550, "cut", "CUT")
    s.rect(5800, 450, 6000, 8550, "cut", "CUT")
    # sàn T2 (khu SHC) + dầm viền ô cầu thang
    s.rect(200, 3930, 3700, 4050, "cut", "CUT")
    s.rect(3480, 3650, 3700, 3930, "cut", "CUT")
    s.rect(3640, 4050, 3700, 4950, "glassc", "CUT")
    # mái + giếng trời kính
    s.rect(200, 7330, 3700, 7450, "cut", "CUT")
    s.rect(3480, 7050, 3700, 7330, "cut", "CUT")
    s.rect(200, 7450, 3600, 7580, "insul", "CUT")
    s.rect(3600, 7450, 3700, 7900, "cut", "CUT")
    s.poly([(3700, 7900), (5800, 7750), (5800, 7800), (3700, 7950)], "glassc", "CUT")
    s.rect(0, 7450, 200, 8550, "cut", "CUT")
    # vế 1 (sát tường phải) và vế 2 bị cắt ngang
    i1 = int(math.ceil((YS - y) / TREAD))
    z1 = 450 + i1 * R
    s.rect(FA[0], z1 - 200, FA[1], z1, "cut", "STAIR")
    j2 = int(math.ceil((y - YL) / TREAD))
    z2 = 2250 + j2 * R
    s.rect(FB[0], z2 - 200, FB[1], z2, "cut", "STAIR")
    s.rect(FB[1], 450, FA[0], z2 - 200, "cut", "STAIR")
    for i in range(1, i1):
        s.line(FA[0], 450 + i * R, FA[1], 450 + i * R, "beyond", "BEYOND")
    for j in range(j2 + 1, 12):
        s.line(FB[0], 2250 + j * R, FB[1], 2250 + j * R, "beyond", "BEYOND")
    s.rect(FB[0], z2, FB[0] + 40, z2 + 900, "glassc", "STAIR")
    s.line(FA[1] - 60, z1 + 900, FA[1] - 60, z1 + 900, "e-alu", "STAIR")
    s.rect(FA[0], 450, FA[1], z1 - 200, "beyondf", "BEYOND")
    s.text(5300, 800, "kho", 110, "ti")
    # nội thất
    s.rect(1400, 1170, 2300, 1210, "cut", "FURN")
    s.rect(1500, 450, 1560, 1170, "beyond", "FURN")
    s.rect(2140, 450, 2200, 1170, "beyond", "FURN")
    s.rect(1000, 450, 1350, 900, "beyondf", "FURN")
    s.rect(2350, 450, 2700, 900, "beyondf", "FURN")
    s.rect(200, 4050, 1000, 4470, "cut", "FURN")
    s.rect(200, 4050, 400, 4850, "cut", "FURN")
    s.rect(1400, 4050, 2100, 4450, "beyondf", "FURN")
    s.rect(200, 450, 800, 1300, "beyond", "FURN") if False else None
    s.rect(1300, 8700 - 8700 + 450, 4600, 1300, "beyond", "FURN")
    # ánh sáng
    s.arrow([(4300, 9200), (4300, 5200)], "sun")
    s.arrow([(5200, 9200), (5100, 2800)], "sun")
    s.arrow([(1200, 2600), (1600, 6600), (4400, 7600)], "wind")
    labels = [(1850, 2500, "PHÒNG ĂN"), (1850, 6000, "SINH HOẠT CHUNG"), (4750, 6300, "Ô THÔNG TẦNG"),
              (4750, 8350, "GIẾNG TRỜI KÍNH"), (4200, z2 + 300, "vế 2"), (5300, z1 + 300, "vế 1"),
              (2950, 1500, "bếp (phía sau)")]
    for x, z, t in labels:
        s.text(x, z, t, 180 if t.isupper() else 130, "tb" if t.isupper() else "ti")
    for z, lab in ((0, "±0.000"), (450, "+0.450"), (4050, "+4.050"), (7450, "+7.450"), (8550, "+8.550")):
        level(s, 6300, z, lab, right=True, length=200)
    dim_v(s, [0, 450, 4050, 7450, 8550], -700)
    dim_h(s, [0, 200, 3700, 4700, 4800, 5800, 6000], -2350)
    notes = ["THÔNG SỐ CẦU THANG",
             "• Cầu thang 2 vế chữ U, chạy DỌC NHÀ (theo chiều sâu)",
             "• Chân thang trong BẾP, đầu thang ra khu SHC tầng 2",
             "• Tổng 22 bậc: h = 164 mm, b = 250 mm (2h + b = 578)",
             "• Mỗi vế 11 bậc, rộng 1.000 mm, dài 2.500 mm",
             "• Chiếu nghỉ 2.100 × 1.000 phía trước, cos +2.250",
             "• Ô cầu thang 2,1 × 3,5 m nằm giữa trục 2 – 3",
             "• Lan can kính, tay vịn gỗ, cao 900",
             "• Giếng trời kính phía trên + ô thoáng chớp",
             "  thoát khí nóng (hiệu ứng ống khói)"]
    for i, t in enumerate(notes):
        s.text(7700, 8800 - i * 520, t, 240 if i == 0 else 175, "tb" if i == 0 else "", "start")
    s.finish(["Mặt cắt tại Y = 6,0 m tính từ mặt tiền, nhìn về phía sau nhà; nét mảnh là các bậc nằm phía sau mặt phẳng cắt."])
    s.save()


# ================================================================ PHỐI CẢNH 3D
class Cam:
    """Phép chiếu phối cảnh. Toạ độ thế giới: x = ngang lô (0..6000), y = sâu (mặt tiền y=0, đường y<0), z = cao."""

    def __init__(self, eye, target, F, cx, cy):
        self.e = eye
        f = [t - e for t, e in zip(target, eye)]
        n = math.sqrt(sum(c * c for c in f))
        self.f = [c / n for c in f]
        r = [self.f[1], -self.f[0], 0.0]          # f × up
        n = math.sqrt(r[0] ** 2 + r[1] ** 2)
        self.r = [r[0] / n, r[1] / n, 0.0]
        fx, fy, fz = self.f
        rx, ry, rz = self.r
        self.u = [ry * fz - rz * fy, rz * fx - rx * fz, rx * fy - ry * fx]
        self.F, self.cx, self.cy = F, cx, cy

    def cam(self, p):
        d = [a - b for a, b in zip(p, self.e)]
        return (sum(a * b for a, b in zip(d, self.r)), sum(a * b for a, b in zip(d, self.u)),
                sum(a * b for a, b in zip(d, self.f)))

    def scr(self, c):
        return (self.cx + self.F * c[0] / c[2], self.cy - self.F * c[1] / c[2])

    def poly(self, pts, near=300):
        cs = [self.cam(p) for p in pts]
        out = []
        for i, a in enumerate(cs):           # cắt theo mặt phẳng gần
            b = cs[(i + 1) % len(cs)]
            ina, inb = a[2] >= near, b[2] >= near
            if ina:
                out.append(a)
            if ina != inb:
                t = (near - a[2]) / (b[2] - a[2])
                out.append(tuple(a[k] + t * (b[k] - a[k]) for k in range(3)))
        return [self.scr(c) for c in out]


def _shade(hexc, k):
    c = [int(hexc[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(v * k))) for v in c)


LIGHT = {"front": 1.0, "left": 0.86, "right": 0.74, "top": 1.06, "bottom": 0.62, "back": 0.6}


class Scene:
    def __init__(self, cam, ox, oy):
        self.c, self.ox, self.oy, self.out = cam, ox, oy, []

    def face(self, pts, fill, stroke="#333", sw=0.5, extra=""):
        sp = self.c.poly(pts)
        if len(sp) < 3:
            return
        ps = " ".join("%.1f,%.1f" % (x + self.ox, y + self.oy) for x, y in sp)
        self.out.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%g" stroke-linejoin="round"%s/>'
                        % (ps, fill, stroke, sw, extra))

    def line(self, a, b, stroke="#222", sw=1.0):
        ca, cb = self.c.cam(a), self.c.cam(b)
        if ca[2] < 300 or cb[2] < 300:
            return
        (x0, y0), (x1, y1) = self.c.scr(ca), self.c.scr(cb)
        self.out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%g" stroke-linecap="round"/>'
                        % (x0 + self.ox, y0 + self.oy, x1 + self.ox, y1 + self.oy, stroke, sw))

    def box(self, x0, x1, y0, y1, z0, z1, col, stroke="#333", sw=0.5, faces=None, extra=""):
        """vẽ các mặt nhìn thấy của khối hộp (loại mặt khuất theo vị trí mắt nhìn)"""
        e = self.c.e
        F = {"front": ([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], e[1] < y0),
             "back": ([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], e[1] > y1),
             "left": ([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], e[0] < x0),
             "right": ([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], e[0] > x1),
             "bottom": ([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], e[2] < z0),
             "top": ([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], e[2] > z1)}
        for k in ("back", "top", "bottom", "right", "left", "front"):
            pts, vis = F[k]
            if vis and (faces is None or k in faces):
                self.face(pts, _shade(col, LIGHT[k]) if col.startswith("#") else col, stroke, sw, extra)

    def sphere(self, x, y, z, r, fill="#7fb256", stroke="#4f7f35"):
        c = self.c.cam((x, y, z))
        if c[2] <= 300:
            return
        sx, sy = self.c.scr(c)
        rr = self.c.F * r / c[2]
        self.out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="0.6"/>'
                        % (sx + self.ox, sy + self.oy, rr, fill, stroke))
        self.out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#ffffff" fill-opacity="0.18"/>'
                        % (sx + self.ox - rr * 0.3, sy + self.oy - rr * 0.3, rr * 0.45))


PERSP_DEFS = """
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9cc6e6"/><stop offset="1" stop-color="#eaf3f8"/></linearGradient>
<linearGradient id="glassG" x1="0" y1="0" x2="0.35" y2="1"><stop offset="0" stop-color="#d6e9f3"/><stop offset="0.45" stop-color="#8fb3c8"/><stop offset="1" stop-color="#4f6f84"/></linearGradient>
<linearGradient id="glassT" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe6f2" stop-opacity="0.55"/><stop offset="1" stop-color="#9cc3d8" stop-opacity="0.3"/></linearGradient>
<linearGradient id="shadowG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.28"/></linearGradient>
<linearGradient id="glow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff3c4" stop-opacity="0.9"/><stop offset="1" stop-color="#fff3c4" stop-opacity="0"/></linearGradient>
"""


def render_view(eye, target, F, W, H, ox, oy):
    cam = Cam(eye, target, F, W / 2.0, H / 2.0)
    sc = Scene(cam, ox, oy)
    o = sc.out
    o.append('<svg x="%.1f" y="%.1f" width="%.1f" height="%.1f" viewBox="%.1f %.1f %.1f %.1f" overflow="hidden">'
             % (ox, oy, W, H, ox, oy, W, H))
    o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#sky)"/>' % (ox, oy, W, H))
    # nền: đường, vỉa hè, sân
    sc.face([(-30000, -60000, 0), (40000, -60000, 0), (40000, -7000, 0), (-30000, -7000, 0)], "#6f7377", "none")
    for x in range(-30000, 40000, 3000):
        sc.face([(x, -11200, 1), (x + 1500, -11200, 1), (x + 1500, -11000, 1), (x, -11000, 1)], "#e8e8e8", "none")
    sc.box(-30000, 40000, -7000, -5000, 0, 150, "#c9c4ba", "none", 0, faces=["front", "top"])
    sc.face([(-30000, -5000, 150), (40000, -5000, 150), (40000, 30000, 150), (-30000, 30000, 150)], "#bdb8ad", "none")
    sc.face([(0, -5000, 151), (6000, -5000, 151), (6000, 0, 151), (0, 0, 151)], "#d8d2c6", "#b5ad9f", 0.4)
    for y in range(-4500, 0, 500):
        sc.line((700, y, 152), (5300, y, 152), "#c6bfb2", 0.4)
    # tán cây xa phía sau
    for x, y, r in ((-14000, 9000, 3200), (-9000, 12000, 2600), (17000, 10000, 3400), (22000, 6000, 2800)):
        sc.sphere(x, y, 9000, r, "#a9c79a", "#a9c79a")
    # nhà bên phải (2 tầng, minh họa)
    sc.box(6000, 13000, 0, 15000, 150, 7200, "#e2ddd3", "#8f8a80", 0.5)
    for x0 in (7000, 10200):
        sc.box(x0, x0 + 2200, -5, 0, 1200, 3200, "#7d8a93", "#555", 0.4, faces=["front"])
        sc.box(x0, x0 + 2200, -5, 0, 4700, 6400, "#7d8a93", "#555", 0.4, faces=["front"])
    sc.box(6000, 13000, -900, 0, 3700, 3850, "#cfc9bd", "#8f8a80", 0.4)
    # nhà bên trái (2 tầng, minh họa)
    sc.box(-7000, 0, 0, 15000, 150, 7000, "#d9d4ca", "#8f8a80", 0.5)
    for z0 in (1200, 4800):
        sc.box(-6000, -1200, -5, 0, z0, z0 + 1800, "#7a8690", "#555", 0.4, faces=["front"])
    sc.box(-7000, 0, -900, 0, 3700, 3850, "#cfc9bd", "#8f8a80", 0.4)
    # tường hồi nhà mình nhô cao hơn nhà bên trái
    sc.face([(0, 200, 7000), (0, 15000, 7000), (0, 15000, 8550), (0, 200, 8550)], _shade("#f6f4ee", 0.86), "#777", 0.4)

    WHITE, DARK, STONE, WOOD = "#f6f4ee", "#3a3a3a", "#8e8a82", "#9a6a3c"
    # ---------- tầng 1
    sc.face([(0, 0, 150), (6000, 0, 150), (6000, 0, 3850), (0, 0, 3850)], WHITE, "#666", 0.5)
    sc.face([(0, -2, 150), (6000, -2, 150), (6000, -2, 450), (0, -2, 450)], DARK, "#222", 0.4)
    sc.box(0, 700, -80, 0, 450, 3850, STONE, "#555", 0.5)
    for z in range(750, 3850, 300):
        sc.line((0, -81, z), (700, -81, z), "#6f6b64", 0.5)
    sc.box(150, 550, -100, -80, 2550, 2850, DARK, "#222", 0.3)
    # cửa chính
    sc.face([(800, -3, 450), (3200, -3, 450), (3200, -3, 3450), (800, -3, 3450)], "url(#glassG)", "#222", 1.2)
    for x in (1400, 2000, 2600):
        sc.line((x, -4, 450), (x, -4, 3050), "#222", 1.0)
    sc.line((800, -4, 3050), (3200, -4, 3050), "#222", 1.0)
    for x in (1930, 2070):
        sc.line((x, -6, 1500), (x, -6, 2100), "#c9c9c9", 1.4)
    # cửa sổ
    sc.face([(3800, -3, 1250), (5400, -3, 1250), (5400, -3, 3450), (3800, -3, 3450)], "url(#glassG)", "#222", 1.2)
    sc.line((4600, -4, 1250), (4600, -4, 3050), "#222", 1.0)
    sc.line((3800, -4, 3050), (5400, -4, 3050), "#222", 1.0)
    sc.box(3700, 5500, -120, 0, 1150, 1250, DARK, "#222", 0.4)
    # bóng đổ của ban công lên mặt tiền tầng 1
    sc.face([(0, -6, 3100), (6000, -6, 3100), (6000, -6, 3850), (0, -6, 3850)], "url(#shadowG)", "none", 0)
    # bậc tam cấp
    for i, (yy, zz) in enumerate(((-900, 250), (-600, 350), (-300, 450))):
        sc.box(700, 3300, yy, 0, 150, zz, "#4a4a4a", "#2a2a2a", 0.4)

    # ---------- tầng 2 (lõm vào trong khung viền)
    sc.face([(250, 200, 4050), (5750, 200, 4050), (5750, 200, 7300), (250, 200, 7300)], "#dcd8cf", "#777", 0.4)
    for x0, z0, x1 in ((500, 4750, 2100), (2900, 4050, 4900)):
        sc.face([(x0, 198, z0), (x1, 198, z0), (x1, 198, 6850), (x0, 198, 6850)], "url(#glassG)", "#222", 1.2)
        sc.line(((x0 + x1) / 2, 196, z0), ((x0 + x1) / 2, 196, 6850), "#222", 1.0)
        sc.line((x0, 196, 6450), (x1, 196, 6450), "#222", 0.8)
    sc.face([(600, 190, 4800), (2000, 190, 4800), (2000, 190, 6400), (600, 190, 6400)], "url(#glow)", "none", 0,
            ' opacity="0.35"')
    sc.box(5000, 5750, 150, 200, 4050, 7300, "#2f2f2f", "none", 0, faces=["front"])
    x = 5000
    while x < 5750:
        sc.box(x, x + 50, 60, 150, 4050, 7300, WOOD, "#5e3d1e", 0.3)
        x += 100
    # mặt trong của khung viền bên phải + trần mái đua
    sc.face([(5750, -1200, 3850), (5750, 200, 3850), (5750, 200, 8550), (5750, -1200, 8550)], _shade(WHITE, 0.8), "#666", 0.4)
    sc.face([(0, -1200, 7300), (6000, -1200, 7300), (6000, 200, 7300), (0, 200, 7300)], _shade(WHITE, 0.68), "#666", 0.4)
    for xx in (1000, 3000, 5000):
        sc.sphere(xx, -500, 7290, 60, "#fff4c2", "#d8b84a")
    # bồn cây + cây ban công
    sc.box(300, 2400, -1150, -850, 4050, 4500, DARK, "#222", 0.4)
    for i, xx in enumerate(range(450, 2400, 230)):
        sc.sphere(xx, -1000, 4720 + (i % 3) * 90, 210 + (i % 2) * 40, "#79ad52" if i % 2 else "#8cc063")
    # lan can kính + tay vịn
    sc.face([(250, -1180, 4050), (5750, -1180, 4050), (5750, -1180, 5150), (250, -1180, 5150)], "url(#glassT)", "#5f8aa3", 0.6)
    for xx in (1600, 2950, 4300):
        sc.line((xx, -1182, 4050), (xx, -1182, 5150), "#333", 0.9)
    sc.box(250, 5750, -1210, -1150, 5130, 5180, "#2b2b2b", "#111", 0.3)
    # khung viền BTCT
    sc.box(0, 6000, -1200, 0, 3850, 4050, WHITE, "#555", 0.5)
    for xx in (1000, 2000, 3000, 4000, 5000):
        sc.sphere(xx, -600, 3840, 55, "#fff4c2", "#d8b84a")
    sc.box(0, 250, -1200, 200, 3850, 8450, WHITE, "#555", 0.5)
    sc.box(5750, 6000, -1200, 200, 3850, 8450, WHITE, "#555", 0.5, faces=["front"])
    sc.box(0, 6000, -1200, 200, 7300, 8450, WHITE, "#555", 0.5, faces=["front", "left"])
    sc.box(-20, 6020, -1220, 200, 8450, 8560, "#4a4a4a", "#222", 0.4, faces=["front", "left"])

    # ---------- sân trước: bồn cây, tường rào, cổng
    for xx in (400, 5600):
        for yy in (-4300, -3300, -2300, -1400):
            sc.box(xx - 300, xx + 300, yy - 300, yy + 300, 150, 450, "#9b9b95", "#666", 0.3, faces=["front", "left", "top"])
            sc.sphere(xx, yy, 750, 330, "#78ac50")
    sc.box(0, 100, -5000, 0, 150, 1400, "#e9e6df", "#777", 0.4)
    sc.box(5900, 6000, -5000, 0, 150, 1400, "#e9e6df", "#777", 0.4)
    sc.box(0, 1000, -5000, -4800, 150, 1800, "#e9e6df", "#777", 0.4)
    sc.box(5000, 6000, -5000, -4800, 150, 1800, "#e9e6df", "#777", 0.4)
    sc.box(0, 1000, -5020, -4780, 1800, 1880, "#3a3a3a", "#222", 0.3)
    sc.box(5000, 6000, -5020, -4780, 1800, 1880, "#3a3a3a", "#222", 0.3)
    # lá cổng trượt (đang mở, nan ngang sơn đen)
    for zz in range(400, 1700, 160):
        sc.box(3700, 5000, -4950, -4920, zz, zz + 70, "#2f2f2f", "#111", 0.2)
    sc.box(3700, 3750, -4950, -4920, 300, 1700, "#2f2f2f", "#111", 0.2)
    # rào nhà bên
    sc.box(-7000, 0, -5000, -4850, 150, 1300, "#d9d4ca", "#888", 0.4)
    sc.box(6000, 13000, -5000, -4850, 150, 1300, "#d9d4ca", "#888", 0.4)
    # cây đường phố
    sc.box(10400, 10600, -6200, -6000, 150, 3200, "#6b4f35", "#4a3524", 0.3)
    for dx, dz, r in ((0, 4200, 1400), (-900, 3600, 1000), (900, 3700, 1050), (0, 5100, 900)):
        sc.sphere(10500 + dx, -6100, dz, r, "#6fa04a", "#4f7f35")
    # người (để so tỷ lệ)
    px, py = -1600, -6000
    sc.box(px - 180, px + 180, py - 120, py + 120, 150, 950, "#3b4a5c", "#222", 0.3)
    sc.box(px - 220, px + 220, py - 130, py + 130, 950, 1550, "#c96a4a", "#7a3a24", 0.3)
    sc.sphere(px, py, 1700, 120, "#e2b48c", "#a57a55")
    o.append("</svg>")
    return o


def perspective():
    s = Sheet("KT-08", "08_Phoi-canh-mat-tien", "PHỐI CẢNH 3D MẶT TIỀN", "—",
              0, 16000, 0, 10600, ml=900, mr=900, mt=900, mb=4400)
    s.svg.append('<defs>%s</defs>' % PERSP_DEFS)
    s.svg += render_view((-4200, -20500, 1650), (2600, 0, 4300), 1350, 1000.0, 1060.0, 90, 90)
    s.svg += render_view((3000, -19000, 1650), (3000, 0, 4300), 680, 580.0, 500.0, 1110, 90)
    s.rect(0, 0, 10000, 10600, "frame2", "FRAME", dxf=False)
    s.rect(10200, 5600, 16000, 10600, "frame2", "FRAME", dxf=False)
    s.text(10350, 5300, "Góc nhìn chính diện (từ giữa đường)", 170, "tb", "start", dxf=False)
    notes = ["GHI CHÚ PHỐI CẢNH",
             "• Góc nhìn chính: từ mép đường đối diện, chéo",
             "  bên trái, tầm mắt người đứng (1,65 m).",
             "• Dựng theo đúng kích thước hồ sơ KT-02 → KT-05.",
             "• Nhà hai bên chỉ để minh họa (khối nhạt).",
             "• Màu sắc, vật liệu mang tính tham khảo:",
             "  – khung viền trắng sứ, mũ tường ghi đậm",
             "  – lam gỗ composite màu óc chó",
             "  – kính xanh nhạt, khung nhôm ghi đen",
             "  – cột tầng 1 ốp đá xám, đế ốp đá đen"]
    for i, t in enumerate(notes):
        s.text(10350, 4800 - i * 430, t, 210 if i == 0 else 160, "tb" if i == 0 else "", "start", dxf=False)
    s.finish()
    s.save(dxf_out=False)



def model_sheet():
    """KT-09: ghép các ảnh chụp từ mô hình 3D (09_Mo-hinh-3D.html, thư mục anh-3d)"""
    views = [("toancanh", "1. Toàn cảnh nhìn từ trên cao (phía trước – trái)"),
             ("mattien", "2. Mặt tiền nhìn từ đường"),
             ("tang1", "3. Tầng 1 – bỏ mái, tầng 2 và tường bên phải"),
             ("tang2", "4. Tầng 2 – bỏ mái và tường bên phải"),
             ("catdoc", "5. Cắt dọc nhà – thấy 2 tầng, cầu thang, giếng trời"),
             ("matsau", "6. Mái bằng, giếng trời kính, bồn nước, NLMT")]
    cw, ch, gap, cap = 7600, 4750, 400, 550
    s = Sheet("KT-09", "09_Phoi-canh-3D-toan-nha", "PHỐI CẢNH 3D TOÀN BỘ NGÔI NHÀ", "—",
              0, 2 * cw + gap, 0, 3 * (ch + cap) + 2 * gap, ml=900, mr=900, mt=900, mb=4200)
    for i, (k, t) in enumerate(views):
        c, r = i % 2, i // 2
        u0 = c * (cw + gap)
        v1 = s.vmax - r * (ch + cap + gap)
        x, y = s.P(u0, v1)
        s.svg.append('<image href="anh-3d/%s.png" x="%.1f" y="%.1f" width="%.1f" height="%.1f" preserveAspectRatio="xMidYMid slice"/>'
                     % (k, x, y, cw / 10, ch / 10))
        s.rect(u0, v1 - ch, u0 + cw, v1, "frame2", "FRAME", dxf=False)
        s.text(u0 + 100, v1 - ch - 280, t, 200, "tb", "start", dxf=False)
    s.finish(["Ảnh chụp từ mô hình 3D tương tác 09_Mo-hinh-3D.html (mở bằng trình duyệt để xoay, ẩn/hiện mái, từng tầng, nội thất). "
              "Nội thất, màu sắc mang tính minh họa."])
    s.save(dxf_out=False)

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "DXF"), exist_ok=True)
    site(); floor1(); floor2(); roof(); elevation(); section_a(); section_b(); perspective(); model_sheet()
    print("done")
