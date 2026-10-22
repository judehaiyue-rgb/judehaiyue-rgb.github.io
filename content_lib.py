# -*- coding: utf-8 -*-
"""Small HTML helpers for the long-form body of each detail page."""


def p(t):
    return "<p>%s</p>" % t


def h3(t):
    return "<h3>%s</h3>" % t


def checks(items):
    return '<ul class="check">%s</ul>' % "".join("<li>%s</li>" % i for i in items)


def callout(label, text):
    return '<div class="callout"><b>%s</b><p>%s</p></div>' % (label, text)


def cards(items):
    out = []
    for i, (title, text) in enumerate(items, 1):
        out.append('<div class="card"><div class="no">%02d</div><h4>%s</h4><p>%s</p></div>' % (i, title, text))
    return '<div class="cards">%s</div>' % "".join(out)


def table(headers, rows, rowheads=True):
    head = "".join("<th>%s</th>" % h for h in headers)
    body = []
    for r in rows:
        cells = []
        for idx, c in enumerate(r):
            if idx == 0 and rowheads:
                cells.append("<th>%s</th>" % c)
            else:
                cells.append("<td>%s</td>" % c)
        body.append("<tr>%s</tr>" % "".join(cells))
    return ('<div class="tbl-wrap"><table class="tbl"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            % (head, "".join(body)))


def steps(items):
    return '<div class="steps">%s</div>' % "".join(
        '<div class="step"><div><h4>%s</h4><p>%s</p></div></div>' % (t, d) for t, d in items
    )


def twocol(ok_title, ok_items, ng_title, ng_items):
    ok = "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in ok_items)
    ng = "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in ng_items)
    return ('<div class="two"><div class="ok"><h4>%s</h4>%s</div><div class="ng"><h4>%s</h4>%s</div></div>'
            % (ok_title, ok, ng_title, ng))


def faqs(items):
    out = []
    for q, a in items:
        out.append(
            '<details class="faq-item"><summary class="faq-q"><span class="badge">Q</span>'
            '<span class="txt">%s</span><span class="plus"></span></summary>'
            '<div class="faq-a">%s</div></details>' % (q, a)
        )
    return '<div class="faq-list">%s</div>' % "".join(out)


def kw(words):
    return '<div class="kw">%s</div>' % "".join("<span>%s</span>" % w for w in words)


def section(h2, *parts):
    return "<section><h2>%s</h2>%s</section>" % (h2, "".join(parts))


def cta(title, text, href="/contact/", label="無料で相談する →"):
    return ('<div class="lf-cta"><h3>%s</h3><p>%s</p>'
            '<a class="btn btn-orange" href="%s">%s</a></div>' % (title, text, href, label))


def lf(*sections):
    return '<div class="lf"><div class="lf-in">%s</div></div>' % "".join(sections)
