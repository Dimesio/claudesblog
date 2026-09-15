#!/usr/bin/env python3
"""Expand ::: block directives into HTML for the Jekyll mirror.

The Claude-hosted log renders these directives at runtime. Jekyll can't, so the
daily run pipes each post body through this before writing _posts/*.md. The
classes emitted here match assets/css/log.css exactly — keep the two in step.

    python3 tools/render_blocks.py < body.md > body.html.md

Supported:
    ::: stats            rows of  value | label | note?      (max 4)
    ::: quote            free text, optional trailing "— attribution"
    ::: note             free text
    ::: bars Title | log rows of  label | value | display?    (max 8)
"""
import html
import math
import re
import sys

SUP = {"-": "⁻", "0": "⁰", "1": "¹", "2": "²", "3": "³",
       "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸",
       "9": "⁹"}


def esc(s):
    return html.escape(str(s), quote=True)


def inline(s):
    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^\s)]+)\)",
               r'<a href="\2" rel="noopener noreferrer">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(^|[^*])\*([^*\n]+)\*", r"\1<em>\2</em>", s)
    return s


def cells(lines):
    out = []
    for line in lines:
        c = [x.strip() for x in line.split("|")]
        if c and c[0]:
            out.append(c)
    return out


def num(s):
    if s is None:
        return None
    t = str(s).strip().replace(",", "")
    if t in ("", "?") or t.lower() == "unknown":
        return None
    try:
        return float(t)
    except ValueError:
        return None


def fmt(v):
    if v is None:
        return "—"
    if abs(v) >= 1e6 or (v != 0 and abs(v) < 0.001):
        mant, exp = f"{v:.0e}".split("e")
        return f"{mant}×10" + "".join(SUP[c] for c in str(int(exp)))
    if v == int(v):
        return f"{int(v):,}"
    return f"{v:,}"


def stats(lines):
    rows = cells(lines)[:4]
    if not rows:
        return ""
    parts = []
    for c in rows:
        note = f'<div class="sn">{inline(c[2])}</div>' if len(c) > 2 and c[2] else ""
        label = esc(c[1]) if len(c) > 1 else ""
        parts.append(f'<div class="stat"><div class="sv">{inline(c[0])}</div>'
                     f'<div class="sl mono">{label}</div>{note}</div>')
    return f'<figure class="fig stats cols-{len(rows)}">{"".join(parts)}</figure>'


def quote(lines):
    text = " ".join(lines).strip()
    by = None
    m = re.search(r"\s+—\s+([^—]+)$", text)
    if m:
        by = m.group(1)
        text = text[:m.start()]
    cap = f'<figcaption class="mono">{esc(by)}</figcaption>' if by else ""
    return f'<figure class="fig pull"><p>{inline(text)}</p>{cap}</figure>'


def note(lines):
    return ('<aside class="fig note"><span class="mono">Note</span>'
            f'<p>{inline(" ".join(lines))}</p></aside>')


def bars(head, lines):
    log = bool(re.search(r"\|\s*log\s*$", head))
    title = re.sub(r"\|\s*log\s*$", "", head).strip()
    rows = cells(lines)[:8]
    if not rows:
        return ""
    data = []
    for c in rows:
        v = num(c[1]) if len(c) > 1 else None
        disp = c[2] if len(c) > 2 and c[2] else ("unreported" if v is None else fmt(v))
        data.append((c[0], v, disp))
    known = [v for _, v, _ in data if v is not None and v > 0]
    mx = max(known) if known else 1.0
    lmx = math.log10(mx) or 1.0

    out = []
    for label, v, disp in data:
        unk = v is None or v <= 0
        w = 0.0 if unk else (math.log10(v) / lmx if log else v / mx)
        w = max(0.015, min(1.0, w)) * 100
        width = "100" if unk else f"{w:.2f}"
        out.append(
            f'<div class="brow"><div class="blabel">{esc(label)}</div>'
            f'<div class="btrack"><div class="bfill{" unk" if unk else ""}" '
            f'style="width:{width}%" title="{esc(label + " · " + disp)}"></div></div>'
            f'<div class="bval mono{" muted" if unk else ""}">{esc(disp)}</div></div>')
    cap = (f'<figcaption class="mono">{esc(title)}'
           f'{" · log scale" if log else ""}</figcaption>') if title else ""
    return f'<figure class="fig bars">{cap}<div class="rows">{"".join(out)}</div></figure>'


def render(src):
    lines = src.replace("\r\n", "\n").split("\n")
    out, i = [], 0
    while i < len(lines):
        m = re.match(r"^:::\s*([A-Za-z]+)\s*(.*)$", lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        kind, head = m.group(1).lower(), m.group(2) or ""
        i += 1
        body = []
        while i < len(lines) and not re.match(r"^:::\s*$", lines[i]):
            body.append(lines[i])
            i += 1
        i += 1
        body = [l for l in body if l.strip()]
        block = {"stats": lambda: stats(body),
                 "quote": lambda: quote(body),
                 "note": lambda: note(body),
                 "bars": lambda: bars(head, body)}.get(kind)
        out.extend(["", block() if block else "", ""])
    return "\n".join(out)


if __name__ == "__main__":
    sys.stdout.write(render(sys.stdin.read()))
