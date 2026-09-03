"""Hero scenes for the Minnesota site — layered-silhouette SVG illustrations in
the brand palette. Each is a 1440x360 scene that sits along the bottom of the
hero. No photos are used anywhere on the site, so every page has its own
weight-free landscape."""

SKY = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
       '<stop offset="0" stop-color="#f4f2ec"/><stop offset="1" stop-color="#dbe6ee"/>'
       '</linearGradient></defs><rect width="1440" height="360" fill="url(#sky)"/>')

def wrap(inner):
    return ('<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">'
            + SKY + inner + '</svg>')

def pines(spec, fill="#1f3d33"):
    """spec: list of (x, base_y, height, half_width)"""
    out = []
    for x, y, h, w in spec:
        tiers = 3
        step = h / (tiers + 1)
        parts = []
        for i in range(tiers):
            top = y - h + i * step
            bottom = top + step * 1.35
            ww = w * (0.45 + 0.28 * i)
            parts.append(f"M{x} {top:.0f}l{ww:.0f} {bottom-top:.0f}h{-2*ww:.0f}z")
        out.append(f'<path d="{"".join(parts)}" fill="{fill}"/>'
                   f'<rect x="{x-2}" y="{y-8}" width="4" height="10" fill="#10251d"/>')
    return "".join(out)

def loon(x, y, s=1.0, fill="#1c2630"):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="{fill}">'
            '<path d="M0 0c14-6 34-6 48 0-8 6-40 6-48 0z"/>'
            '<path d="M32-2c2-12 4-22 12-24 8 0 12 6 12 12-4 2-10 4-12 8-2 4-4 6-12 4z"/>'
            '<path d="M54-15l12-3-12 6z"/></g>')

def sun(cx=1160, cy=118, r=60):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e7c486" opacity=".55"/>'

def lake_line(y=300, fill="#1d4f6e", op=".95"):
    return (f'<path d="M0 {y}C240 {y-6} 480 {y+8} 720 {y} 960 {y-8} 1200 {y+6} 1440 {y}V360H0Z" '
            f'fill="{fill}" opacity="{op}"/>')

def northwoods():
    return wrap(
        sun()
        + '<path d="M0 262C200 232 380 250 560 236 760 220 940 246 1440 224V360H0Z" fill="#c9d6d9"/>'
        + '<path d="M0 292C260 262 520 296 780 276 1040 258 1240 290 1440 268V360H0Z" fill="#6f9a8a"/>'
        + pines([(120, 300, 92, 26), (168, 302, 70, 20), (1270, 298, 96, 28), (1320, 302, 64, 18), (1030, 300, 58, 16)], "#2f5d4a")
        + lake_line(304)
        + '<path d="M300 318c120-6 240 4 360-2 120-6 240 6 360 0" stroke="#e9f1f5" stroke-width="2" fill="none" opacity=".55"/>'
        + loon(560, 322, 1.0)
    )

def skyline():
    b = '<g fill="#2b4b62">'
    b += ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{360-y}"/>' for x, y, w in
                 [(430,190,40),(480,150,34),(524,118,52),(586,166,30),(626,96,44),(680,176,36),(726,140,58),(794,188,30),(834,132,40),(884,158,52),(946,200,36)])
    b += '<path d="M626 96l22-30 22 30z" fill="#2b4b62"/><rect x="740" y="118" width="6" height="24" fill="#2b4b62"/>'
    b += '</g>'
    windows = '<g fill="#e7c486" opacity=".7">' + ''.join(
        f'<rect x="{x}" y="{y}" width="4" height="6"/>' for x, y in
        [(536,140),(548,160),(560,180),(640,120),(652,150),(736,160),(760,180),(900,180),(846,150)]) + '</g>'
    arches = ''.join(f'<path d="M{x} 300a22 22 0 0 1 44 0v14h-44z" fill="#a89478"/>' for x in range(1020, 1240, 48))
    bridge = '<rect x="1000" y="284" width="290" height="16" fill="#b9a688"/>' + arches
    return wrap(sun(1200, 100, 52) + '<path d="M0 262C200 250 300 262 420 250L1440 236V360H0Z" fill="#c9d6d9"/>'
                + b + windows + bridge + lake_line(314) + loon(200, 332, .8))

def capitol():
    dome = ('<g fill="#2b4b62"><rect x="560" y="230" width="320" height="130"/>'
            '<rect x="640" y="176" width="160" height="60"/><path d="M640 180a80 80 0 0 1 160 0z"/>'
            '<rect x="714" y="130" width="12" height="46"/><circle cx="720" cy="126" r="8"/>'
            '<rect x="470" y="264" width="90" height="96"/><rect x="880" y="264" width="90" height="96"/></g>'
            '<g fill="#e7c486" opacity=".55">' + ''.join(f'<rect x="{x}" y="256" width="10" height="26"/>' for x in range(584, 870, 30)) + '</g>')
    cathedral = ('<g fill="#3a5a6e"><rect x="1080" y="250" width="140" height="110"/><path d="M1080 254a70 70 0 0 1 140 0z"/>'
                 '<rect x="1144" y="160" width="12" height="30"/><rect x="1100" y="228" width="22" height="30"/><rect x="1178" y="228" width="22" height="30"/></g>')
    return wrap(sun(200, 110, 50) + '<path d="M0 270C300 250 600 268 1440 246V360H0Z" fill="#c9d6d9"/>'
                + dome + cathedral + pines([(300, 340, 80, 24), (360, 344, 60, 18)], "#2f5d4a")
                + '<path d="M0 330C480 318 960 338 1440 326V360H0Z" fill="#6f9a8a"/>')

def lighthouse():
    cliff = '<path d="M0 360V250l140-30 120 14 90-30 70 24 110-6V360z" fill="#5a4a3c"/><path d="M0 250l140-30 120 14 90-30 70 24 110-6v30L0 280z" fill="#7c9a76"/>'
    tower = ('<g><path d="M262 236h34l-4-110h-26z" fill="#e9e2d4"/><rect x="254" y="124" width="50" height="10" fill="#b5471f"/>'
             '<rect x="266" y="100" width="26" height="24" fill="#2b4b62"/><rect x="270" y="104" width="18" height="16" fill="#e7c486"/>'
             '<path d="M258 100h42l-21-14z" fill="#b5471f"/><rect x="300" y="200" width="60" height="36" fill="#e9e2d4"/><path d="M296 200h68l-34-18z" fill="#b5471f"/></g>')
    beam = '<path d="M290 112L700 60V160z" fill="#e7c486" opacity=".18"/>'
    return wrap(sun(1180, 120, 58) + '<path d="M0 300C400 290 800 306 1440 292V360H0Z" fill="#1d4f6e"/>'
                + '<path d="M500 322c140-8 280 6 420-2 140-8 280 6 420 0" stroke="#e9f1f5" stroke-width="2" fill="none" opacity=".5"/>'
                + beam + cliff + tower + pines([(60, 254, 60, 18), (105, 250, 48, 14)], "#2f5d4a"))

def bluffs():
    return wrap(sun(1160, 110, 56)
                + '<path d="M0 244C180 214 340 250 520 226 700 202 880 232 1060 214 1240 196 1340 226 1440 214V360H0Z" fill="#c9d6d9"/>'
                + '<path d="M0 282l200-70 160 46 180-62 200 60 180-50 220 56 300-40V360H0Z" fill="#7c9a76"/>'
                + '<path d="M0 320l260-40 220 30 240-44 300 40 420-24V360H0Z" fill="#3f6b58"/>'
                + pines([(1180, 300, 70, 20), (1230, 304, 52, 16)], "#1f3d33")
                + lake_line(330))

def prairie():
    elev = ('<g fill="#2b4b62"><rect x="1010" y="200" width="70" height="160"/><path d="M1010 200h70l-35-28z"/>'
            '<rect x="1090" y="236" width="90" height="124"/><rect x="1090" y="236" width="90" height="10" fill="#1d3a4e"/></g>')
    turbines = ''.join(
        f'<g transform="translate({x} {y})" stroke="#cfd8dc" stroke-width="3" fill="none"><line x1="0" y1="0" x2="0" y2="{h}"/>'
        f'<g transform="rotate({r})"><line x1="0" y1="0" x2="0" y2="-34"/><line x1="0" y1="0" x2="30" y2="17"/><line x1="0" y1="0" x2="-30" y2="17"/></g></g>'
        for x, y, h, r in [(220, 250, 70, 20), (330, 262, 58, 75), (410, 256, 62, 130)])
    return wrap(sun(1200, 118, 62)
                + '<path d="M0 300C360 290 720 306 1440 292V360H0Z" fill="#b8a76c"/>'
                + '<path d="M0 330C360 320 720 336 1440 322V360H0Z" fill="#7c9a4a"/>'
                + turbines + elev)

def lakes_cabin():
    cabin = ('<g><rect x="1100" y="236" width="120" height="60" fill="#7a5a3c"/><path d="M1090 240h140l-70-46z" fill="#5a3f2a"/>'
             '<rect x="1148" y="262" width="24" height="34" fill="#2b4b62"/><rect x="1112" y="252" width="20" height="18" fill="#e7c486"/>'
             '<rect x="1188" y="252" width="20" height="18" fill="#e7c486"/></g>')
    dock = '<rect x="980" y="306" width="150" height="8" fill="#8a6a48"/><rect x="990" y="314" width="6" height="18" fill="#6a4e34"/><rect x="1110" y="314" width="6" height="18" fill="#6a4e34"/>'
    return wrap(sun(260, 116, 56)
                + '<path d="M0 262C280 236 560 266 840 244 1120 222 1300 258 1440 240V360H0Z" fill="#c9d6d9"/>'
                + '<path d="M0 296C300 270 600 302 900 282 1200 262 1360 294 1440 280V360H0Z" fill="#6f9a8a"/>'
                + pines([(80, 300, 88, 26), (130, 304, 66, 20), (900, 288, 82, 24), (950, 292, 60, 18), (1300, 296, 74, 22)], "#2f5d4a")
                + cabin + lake_line(310) + dock + loon(420, 330, .9))

def aurora():
    bands = ''.join(f'<path d="M{x} 40C{x+120} 90 {x+240} 20 {x+360} 120L{x+330} 200C{x+230} 130 {x+110} 180 {x-10} 130z" fill="{c}" opacity=".35"/>'
                    for x, c in [(120, "#7fc6a4"), (520, "#a7d8c1"), (900, "#7fc6a4")])
    stars = '<g fill="#fff" opacity=".8">' + ''.join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for x, y in
              [(80,50),(200,30),(350,70),(500,40),(640,90),(760,30),(880,60),(1000,40),(1120,80),(1260,36),(1380,70)]) + '</g>'
    return ('<svg viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" role="img" aria-hidden="true">'
            '<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#143a52"/><stop offset="1" stop-color="#2b4b62"/></linearGradient></defs>'
            '<rect width="1440" height="360" fill="url(#sky)"/>' + bands + stars
            + '<path d="M0 290C300 270 600 300 900 280 1200 262 1360 292 1440 280V360H0Z" fill="#1f3d33"/>'
            + pines([(100, 296, 90, 26), (150, 300, 70, 20), (700, 292, 96, 28), (760, 296, 70, 20), (1240, 294, 88, 26), (1300, 298, 64, 18)], "#10251d")
            + lake_line(318, "#0f2c3f", "1") + '</svg>')

def snow():
    return wrap(sun(1190, 116, 60)
                + '<path d="M0 262C280 236 560 266 840 244 1120 222 1300 258 1440 240V360H0Z" fill="#dfe6ea"/>'
                + '<path d="M0 300C300 280 600 310 900 292 1200 274 1360 300 1440 290V360H0Z" fill="#f6f8f9"/>'
                + pines([(110, 306, 90, 26), (160, 310, 66, 20), (1040, 300, 84, 24), (1090, 304, 60, 18), (1310, 306, 76, 22)], "#2f5d4a")
                + '<g fill="#fff" opacity=".9">' + ''.join(f'<circle cx="{x}" cy="{y}" r="2.2"/>' for x, y in
                   [(300,120),(420,200),(560,90),(640,170),(780,240),(860,110),(960,60),(1000,190),(1150,230),(1270,150)]) + '</g>')

SCENES = {
    "northwoods": northwoods(),
    "skyline": skyline(),
    "capitol": capitol(),
    "lighthouse": lighthouse(),
    "bluffs": bluffs(),
    "prairie": prairie(),
    "lakes": lakes_cabin(),
    "aurora": aurora(),
    "snow": snow(),
}
