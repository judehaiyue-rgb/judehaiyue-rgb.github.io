# -*- coding: utf-8 -*-
"""Static site generator for the Heart Bridge corporate site.
Built from: GlooMaps sitemap, ディレクトリマップ本体（GlooMaps最新版反映）,
デザイン作成 指示書。Outputs plain HTML files under heartbridge-site/.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.hb789.info"
COMPANY = "株式会社Heart Bridge"
import time
CSS_VERSION = str(int(time.time()))

# ---------------------------------------------------------------
# Icon set — Feather-style outline icons (consistent line-icon system,
# replaces emoji per design instruction doc decision "アイコンセット化")
# ---------------------------------------------------------------
ICONS = {
  "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>',
  "droplet": '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"></path>',
  "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>',
  "printer": '<path d="M6 9V2h12v7"></path><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect>',
  "sun": '<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>',
  "cycle": '<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="4"></circle>',
  "heart": '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>',
  "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>',
  "help": '<circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line>',
  "mail": '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline>',
  "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle>',
  "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>',
  "home": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9,22 9,12 15,12 15,22"></polyline>',
  "broadcast": '<circle cx="12" cy="12" r="2"></circle><path d="M8.5 8.5a5 5 0 0 0 0 7"></path><path d="M15.5 8.5a5 5 0 0 1 0 7"></path><path d="M5.6 5.6a9 9 0 0 0 0 12.8"></path><path d="M18.4 5.6a9 9 0 0 1 0 12.8"></path>',
  "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>',
  "globe": '<circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>',
  "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>',
  "check": '<polyline points="20 6 9 17 4 12"></polyline>',
  "chevron": '<polyline points="6 9 12 15 18 9"></polyline>',
  "clock": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
  "trend": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline>',
  "checkcircle": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>',
  "coin": '<circle cx="12" cy="12" r="9"></circle><path d="M9 9h1.5a1.5 1.5 0 0 1 0 3H9m0 0h1.5a1.5 1.5 0 0 1 0 3H9M12 7v10"></path>',
}

def icon(name, cls=""):
    return '<svg class="icon %s" viewBox="0 0 24 24">%s</svg>' % (cls, ICONS[name])

# ---------------------------------------------------------------
# Navigation structure (from ディレクトリマップ / GlooMaps)
# ---------------------------------------------------------------
NAV = [
    {"label": "固定費削減コンサル", "href": "/cost-reduction/", "children": [
        ("電気代削減", "/cost-reduction/electricity/"),
        ("水道代削減", "/cost-reduction/water/"),
        ("人件費最適化", "/cost-reduction/labor/"),
        ("複合機・OA機器コスト削減", "/cost-reduction/office-equipment/"),
    ]},
    {"label": "炭化炉事業", "href": "/carbonization/", "children": [
        ("乾熱滅菌減量装置", "/carbonization/sterilizer/"),
        ("製炭事業", "/carbonization/charcoal/"),
        ("スポンサー募集", "/carbonization/sponsor/"),
    ]},
    {"label": "導入事例", "href": "/case-studies/", "children": []},
    {"label": "メディア・スポンサー", "href": "/media/", "children": [
        ("メディア", "/media/press/"),
        ("スポンサーを務めてる選手・団体", "/media/sponsorship/"),
    ]},
    {"label": "会社情報", "href": "/company/", "children": [
        ("会社概要", "/company/"),
        ("SDGsへの取り組み", "/sdgs/"),
        ("よくある質問", "/faq/"),
        ("採用情報", "/recruit/"),
    ]},
]

FOOTER_LINKS = [
    ("事業", [
        ("固定費削減コンサル", "/cost-reduction/"),
        ("炭化炉事業", "/carbonization/"),
        ("スポンサー募集", "/carbonization/sponsor/"),
        ("導入事例", "/case-studies/"),
    ]),
    ("会社情報", [
        ("会社概要", "/company/"),
        ("SDGsへの取り組み", "/sdgs/"),
        ("メディア・スポンサー", "/media/"),
        ("採用情報", "/recruit/"),
    ]),
    ("サポート", [
        ("よくある質問", "/faq/"),
        ("お問い合わせ・資料請求", "/contact/"),
        ("プライバシーポリシー", "/policy/"),
    ]),
]

# ---------------------------------------------------------------
# Shell: header / footer / page wrapper
# ---------------------------------------------------------------

def header_html():
    items = []
    for sec in NAV:
        if not sec["children"]:
            items.append('<div class="gnav-item"><a href="%s">%s</a></div>' % (sec["href"], sec["label"]))
            continue
        subs = "".join('<a href="%s">%s</a>' % (h, l) for l, h in sec["children"])
        items.append(
            '<div class="gnav-item"><button type="button">%s %s</button>'
            '<div class="mega">%s</div></div>' % (sec["label"], icon("chevron"), subs)
        )
    desktop_nav = '<nav class="gnav">%s</nav>' % "".join(items)

    mobile_items = []
    for sec in NAV:
        if not sec["children"]:
            mobile_items.append('<a class="top-link" href="%s">%s</a>' % (sec["href"], sec["label"]))
            continue
        subs = "".join('<a href="%s">%s</a>' % (h, l) for l, h in sec["children"])
        mobile_items.append(
            '<details><summary>%s %s</summary><div class="sub">%s</div></details>'
            % (sec["label"], icon("chevron"), subs)
        )
    mobile_nav = (
        '<div class="mobile-nav">'
        '<a class="top-link" href="/">TOP</a>'
        + "".join(mobile_items)
        + '<a class="top-link" href="/faq/">よくある質問</a>'
        + '<a class="btn btn-orange nav-btn" href="/contact/">お問い合わせ</a>'
        "</div>"
    )

    return (
        '<header>'
        '<a class="logo-wrap" href="/"><span class="logo-main">Heart<em>Bridge</em></span></a>'
        + desktop_nav
        + '<a class="btn nav-btn" href="/contact/">お問い合わせ</a>'
        '<button class="hamburger" type="button" aria-label="メニュー"><span></span><span></span><span></span></button>'
        '</header>'
        + mobile_nav
    )


def footer_html():
    cols = "".join(
        '<div class="ft-col"><h4>%s</h4>%s</div>'
        % (title, "".join('<a href="%s">%s</a>' % (h, l) for l, h in links))
        for title, links in FOOTER_LINKS
    )
    return (
        '<footer><div class="ft-inner">'
        '<div class="ft-top">'
        '<div class="ft-brand">'
        '<div class="fl">Heart<em>Bridge</em></div>'
        '<p>株式会社Heart Bridge<br>「捨てる」を「つなぐ」に。廃棄物を資源に変え、人と地球をつなぐ会社です。</p>'
        '<div class="ft-sns">'
        '<a class="sns-btn" href="https://x.com/HeartBridg789" target="_blank" rel="noopener">@HeartBridg789</a>'
        '<a class="sns-btn" href="https://instagram.com/heartbridg789" target="_blank" rel="noopener">heartbridg789</a>'
        '</div></div>'
        '<div class="ft-links">' + cols + '</div>'
        '</div>'
        '<div class="ft-bottom">'
        '<span>&copy; 2026 株式会社Heart Bridge. All Rights Reserved.</span>'
        '<a href="/policy/">プライバシーポリシー・特定商取引法に基づく表記</a>'
        '</div></div></footer>'
    )


def page(url_path, title, description, body, og_type="website"):
    canonical = SITE + url_path
    return """<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(description)s">
<link rel="canonical" href="%(canonical)s">
<meta property="og:type" content="%(og_type)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(description)s">
<meta property="og:url" content="%(canonical)s">
<meta property="og:site_name" content="%(company)s">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Noto+Serif+JP:wght@600;700&family=Inter:wght@700;900&display=swap">
<link rel="stylesheet" href="/assets/css/style.css?v=%(cssv)s">
</head>
<body>
%(header)s
%(body)s
%(footer)s
<script src="/assets/js/main.js"></script>
</body>
</html>""" % {
        "title": title, "description": description, "canonical": canonical,
        "og_type": og_type, "company": COMPANY,
        "header": header_html(), "body": body, "footer": footer_html(),
        "cssv": CSS_VERSION,
    }


def mhero(eyebrow, h1, desc, crumbs, btns=""):
    return (
        '<section class="mhero"><div class="mhero-in">'
        '<div class="crumbs">%s</div>'
        '<div class="hero-eyebrow"><i></i><span>%s</span></div>'
        '<h1>%s</h1><p>%s</p>'
        '<div class="btns">%s</div>'
        '</div></section>' % (crumbs, eyebrow, h1, desc, btns)
    )


CRUMB_TOP = '<a href="/">TOP</a> ／ '

# ---------------------------------------------------------------
# TOP
# ---------------------------------------------------------------

def build_top():
    body = f"""
<section class="hero">
  <div class="hero-grid-bg"></div><div class="hero-glow"></div><div class="hero-glow2"></div>
  <div class="hero-eyebrow"><i></i><span>Decarbonization &amp; Wellbeing</span></div>
  <h1 class="hero-catch">「捨てる」を<br>「<span class="accent">つなぐ</span>」に。</h1>
  <p class="hero-desc">産廃を炭に変え、障がい者の雇用をつくり、人の心をケアする。環境・社会・人を橋でつなぐ、新しい形の事業を展開しています。</p>
  <div class="hero-actions">
    <a class="btn btn-orange" href="/cost-reduction/">固定費削減コンサルを見る {icon('check')}</a>
    <a class="btn btn-ghost" href="/carbonization/">炭化炉事業を見る</a>
  </div>
  <div class="hero-stats">
    <div class="stat"><div class="stat-n">30<sup>%</sup></div><div class="stat-l">水道料金削減</div></div>
    <div class="stat"><div class="stat-n">20<sup>%</sup></div><div class="stat-l">節電効果</div></div>
    <div class="stat"><div class="stat-n">1,500<sup>+</sup></div><div class="stat-l">取引施設数</div></div>
    <div class="stat"><div class="stat-n">2022</div><div class="stat-l">設立年</div></div>
  </div>
</section>

<div class="mission-strip"><div class="mission-strip-inner">
  <h2>脱炭素と福祉を、一つの仕組みでつなぐ。</h2>
  <p>産業廃棄物を炭に変える「炭化事業」と、障がい者の就労支援を組み合わせた投資型フランチャイズを展開しています。</p>
</div></div>

<section class="sec" style="background:var(--warm-bg);">
  <div class="inner">
    <span class="sec-label">Our Business</span>
    <h2 class="sec-title">2つの軸で、企業と社会に貢献する。</h2>
    <p class="sec-body" style="margin-bottom:44px;">固定費という「守り」のコスト削減と、炭化炉事業という「攻め」の新規事業。どちらも脱炭素・地域社会への貢献につながります。</p>
    <div class="pillars">
      <a class="pillar" href="/cost-reduction/">
        <div class="pic">{icon('coin')}</div>
        <h3>固定費削減コンサル</h3>
        <p>電気代・水道代・人件費・複合機コストまで、医療法人・社会福祉法人の固定費を専門家が無料診断。実績に基づいた経費見直しをワンストップでご提案します。</p>
        <ul>
          <li>{icon('check')} 電気代・水道代の削減</li>
          <li>{icon('check')} 人件費の最適化</li>
          <li>{icon('check')} 複合機・OA機器コスト削減</li>
        </ul>
        <span class="more">サービス詳細を見る →</span>
      </a>
      <a class="pillar" href="/carbonization/">
        <div class="pic">{icon('sun')}</div>
        <h3>炭化炉事業</h3>
        <p>医療産廃対応の乾熱滅菌減量装置と、有機物炭化炉による製炭事業。廃棄物処理コストの削減と、地域資源循環を同時に実現します。</p>
        <ul>
          <li>{icon('check')} 乾熱滅菌減量装置（MD1000型）</li>
          <li>{icon('check')} 有機物炭化炉・バイオ炭の活用</li>
          <li>{icon('check')} スポンサー・協賛の募集</li>
        </ul>
        <span class="more">サービス詳細を見る →</span>
      </a>
    </div>
  </div>
</section>

<section class="sec" style="background:var(--white);">
  <div class="inner trust-grid">
    <div>
      <span class="sec-label">Trust</span>
      <h2 class="sec-title">導入実績と、社会からの信頼。</h2>
      <p class="sec-body" style="margin-bottom:28px;">医療法人・社会福祉法人など幅広い実績に加え、SDGs協会の正式会員として、メディア掲載やスポーツ・地域団体のスポンサーとしても活動しています。</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;">
        <a class="btn btn-ghost on-light" href="/case-studies/">導入事例を見る</a>
        <a class="btn btn-ghost on-light" href="/sdgs/">SDGsの取り組み</a>
        <a class="btn btn-ghost on-light" href="/media/">メディア・スポンサー</a>
      </div>
    </div>
    <div class="about-big-card">
      <span class="quote-mark">&ldquo;</span>
      <blockquote>投資家・施設・社会、すべてにプラスをもたらす仕組みがあれば、ビジネスはもっと人を幸せにできる。</blockquote>
    </div>
  </div>
</section>

<section class="sec" style="background:var(--ink);padding-bottom:80px;">
  <div class="inner" style="text-align:center;">
    <span class="sec-label">Contact</span>
    <h2 class="sec-title sec-title-white">まずは、お気軽にご相談ください。</h2>
    <p style="color:rgba(255,255,255,.55);font-size:.9rem;max-width:520px;margin:0 auto 32px;">炭化炉の導入・固定費の削減・スポンサーのご相談など、担当者より2営業日以内にご連絡いたします。</p>
    <a class="btn btn-orange" href="/contact/">お問い合わせ・資料請求 →</a>
  </div>
</section>
"""
    return page("/", "株式会社Heart Bridge｜「捨てる」を「つなぐ」に。",
                "医療法人・社会福祉法人向けの固定費削減コンサルティングと、乾熱滅菌減量装置・製炭事業による廃棄物処理コスト削減を提供する株式会社Heart Bridgeの公式サイトです。",
                body)

# ---------------------------------------------------------------
# サービス詳細テンプレート（固定費削減コンサル・炭化炉 個別ページ共通）
# ---------------------------------------------------------------

def service_page(url, eyebrow, h1_html, hero_desc, crumbs, body_intro_title, body_intro,
                  feats, stats_label, stats, stat_note, cta_back_label, cta_back_href,
                  extra_sections="", title="", description=""):
    feats_html = "".join(
        '<div class="svc-feat">%s<div><b>%s</b><span>%s</span></div></div>'
        % (icon(ic, "ic"), t, d) for ic, t, d in feats
    )
    stats_html = "".join(
        '<div class="svc-stat-row"><span class="l">%s</span><span class="n">%s<sup>%s</sup></span></div>' % (l, n, s)
        for l, n, s in stats
    )
    body = f"""
{mhero(eyebrow, h1_html, hero_desc, crumbs,
       f'<a class="btn btn-orange" href="/contact/">無料で診断を依頼する →</a>'
       f'<a class="btn btn-ghost" href="/case-studies/">導入事例を見る</a>')}
<div class="svc-body">
  <div>
    <h2>{body_intro_title}</h2>
    <p>{body_intro}</p>
    <div class="svc-feats">{feats_html}</div>
    {extra_sections}
  </div>
  <div class="svc-stats">
    <div class="lbl">{stats_label}</div>
    {stats_html}
  </div>
</div>
<div class="svc-cta">
  <a class="btn btn-ghost on-light" href="{cta_back_href}">{cta_back_label}</a>
  <a class="btn btn-orange" href="/contact/">お問い合わせ・資料請求</a>
</div>
"""
    return page(url, title, description, body)


def build_electricity():
    return service_page(
        "/cost-reduction/electricity/", "Cost Reduction Service",
        "医療法人の<span style='color:var(--orange)'>電気代削減</span>",
        "高圧電力の契約見直しと電力会社の切替支援で、病院・医療機関の電気代を専門コンサルタントが無料診断します。",
        CRUMB_TOP + '<a href="/cost-reduction/">固定費削減コンサル</a> ／ 電気代削減',
        "サービス内容", "電力使用量・契約プランを可視化し、無理のない範囲でコストだけを削減。現場のオペレーションを変えずに導入できます。",
        [("zap", "高圧電力の契約見直し", "デマンド値・単価を精査し、最適な契約プランへ切替提案します。"),
         ("trend", "電力会社の切替支援", "比較・申込・切替までを専門スタッフが代行します。"),
         ("clock", "使用量モニタリング", "導入後も月次レポートで削減効果を継続的に可視化します。")],
        "導入効果（実績）", [("平均削減率", "20", "%"), ("診断〜提案までの期間", "2", "週間"), ("初期費用", "0", "円")],
        "", "固定費削減コンサル一覧へ戻る", "/cost-reduction/",
        title="医療法人の電気代削減｜Heart Bridge",
        description="病院・医療機関向けに高圧電力の契約見直しや電力会社の切替支援を実施。専門コンサルタントが電気代削減の具体策をご提案します。")


def build_water():
    return service_page(
        "/cost-reduction/water/", "Cost Reduction Service",
        "介護施設の<span style='color:var(--orange)'>水道代削減</span>",
        "水道の基本料金見直しから使用量最適化まで、介護施設・医療法人の水道代を専門家が無料診断します。",
        CRUMB_TOP + '<a href="/cost-reduction/">固定費削減コンサル</a> ／ 水道代削減',
        "サービス内容", "契約プラン・使用量の見直しにより、無理のない範囲でコストだけを削減。経営基盤の強化をサポートします。",
        [("droplet", "水道 基本料金の見直し", "施設規模に対して契約プランが過大でないかを精査します。"),
         ("trend", "使用量の最適化", "漏水・過剰使用のチェックと節水設備の提案を行います。"),
         ("clock", "継続モニタリング", "導入後も定期的に使用量データを確認し改善提案します。")],
        "導入効果（実績）", [("平均削減率", "30", "%"), ("診断〜提案までの期間", "2", "週間"), ("初期費用", "0", "円")],
        "", "固定費削減コンサル一覧へ戻る", "/cost-reduction/",
        title="介護施設の水道代削減｜Heart Bridge",
        description="介護施設・医療法人向けに水道の基本料金見直しから使用量最適化まで対応。無駄なコストを削減し、経営基盤の強化をサポートします。")


def build_labor():
    return service_page(
        "/cost-reduction/labor/", "Cost Reduction Service",
        "医療法人の<span style='color:var(--orange)'>人件費最適化</span>",
        "社会福祉法人・医療法人の人員配置を見直し、無理のない人件費最適化を実現します。",
        CRUMB_TOP + '<a href="/cost-reduction/">固定費削減コンサル</a> ／ 人件費最適化',
        "サービス内容", "現場の負担を増やさずに、シフト・配置・業務フローの見直しでコストを最適化します。",
        [("users", "人員配置の見直し", "業務量に対する適正人員をデータに基づき診断します。"),
         ("trend", "業務フローの効率化", "重複業務・非効率な動線を洗い出し改善提案します。"),
         ("clock", "定着支援", "コスト削減と同時に、職員の働きやすさにも配慮した設計を行います。")],
        "導入効果（実績）", [("平均改善率", "15", "%"), ("診断〜提案までの期間", "3", "週間"), ("初期費用", "0", "円")],
        "", "固定費削減コンサル一覧へ戻る", "/cost-reduction/",
        title="医療法人の人件費最適化｜Heart Bridge",
        description="社会福祉法人・医療法人の人員配置を見直し、無理のない人件費最適化を実現。現場の負担を増やさないコスト削減プランをご提案します。")


def build_office_equipment():
    return service_page(
        "/cost-reduction/office-equipment/", "Cost Reduction Service",
        "複合機・OA機器の<span style='color:var(--orange)'>コスト削減</span>",
        "複合機のリース契約見直しやOA機器全般のコスト削減を法人向けにサポートします。",
        CRUMB_TOP + '<a href="/cost-reduction/">固定費削減コンサル</a> ／ 複合機・OA機器コスト削減',
        "サービス内容", "現状契約を無料診断し、印刷枚数・リース条件に見合った最適なプランをご提案します。",
        [("printer", "複合機リースの見直し", "契約期間・単価・保守条件を精査し再交渉します。"),
         ("coin", "OA機器全般のコスト削減", "PC・電話機等も含めた機器コストを見直します。"),
         ("clock", "継続コスト管理", "契約更新のタイミングで再診断し、コストを継続管理します。")],
        "導入効果（実績）", [("平均削減率", "18", "%"), ("診断〜提案までの期間", "2", "週間"), ("初期費用", "0", "円")],
        "", "固定費削減コンサル一覧へ戻る", "/cost-reduction/",
        title="複合機・OA機器のコスト削減｜Heart Bridge",
        description="複合機のリース契約見直しやOA機器全般のコスト削減を法人向けにサポート。現状契約を無料診断し、最適なプランをご提案します。")


def build_cost_reduction_hub():
    cards = [
        ("01", "zap", "電気代削減", "/cost-reduction/electricity/", "高圧電力の契約見直し・電力会社の切替支援で、病院・医療機関の電気代を削減します。", "平均20%削減", ["8", "13"]),
        ("02", "droplet", "水道代削減", "/cost-reduction/water/", "水道の基本料金見直しから使用量最適化まで、介護施設向けにサポートします。", "平均30%削減", ["6", "12"]),
        ("03", "users", "人件費最適化", "/cost-reduction/labor/", "人員配置・業務フローを見直し、現場負担を増やさず人件費を最適化します。", "平均15%改善", ["8"]),
        ("04", "printer", "複合機・OA機器コスト削減", "/cost-reduction/office-equipment/", "複合機のリース契約見直しやOA機器全般のコストを法人向けに削減します。", "平均18%削減", ["12"]),
    ]
    grid = "".join(f"""
    <a class="biz-card" href="{href}">
      <div class="biz-card-top"><span class="biz-num">{num}</span><span class="biz-icon">{icon(ic)}</span></div>
      <h3>{title}</h3><p>{desc}</p>
      <span class="biz-effect">{icon('trend')} {eff}</span>
      <div class="sdg-badges" style="margin-top:14px;">{"".join(f'<span class="sdg-tile sdg-{s}">{s}</span>' for s in sdgs)}</div>
    </a>""" for num, ic, title, href, desc, eff, sdgs in cards)

    body = f"""
{mhero("Cost Reduction", "固定費削減<span style='color:var(--orange)'>コンサル</span>",
       "電気代・水道代・人件費・複合機まで、医療法人・社会福祉法人の固定費を専門家が無料診断。実績に基づいた経費見直しをワンストップでご提案します。",
       CRUMB_TOP + "固定費削減コンサル",
       '<a class="btn btn-orange" href="/contact/">無料診断を依頼する →</a>')}
<section class="sec" style="background:var(--warm-bg);">
  <div class="inner">
    <span class="sec-label">Service</span>
    <h2 class="sec-title">4つの領域でコストを削減します。</h2>
    <div class="biz-grid cols-4">{grid}</div>
  </div>
</section>
<section class="sec" style="background:var(--white);">
  <div class="inner" style="text-align:center;">
    <div class="about-big-card" style="text-align:left;">
      <span class="quote-mark">&ldquo;</span>
      <blockquote>固定費削減は"守り"の経営改善。捻出した原資を、人材への投資や利用者サービスの向上に。</blockquote>
    </div>
  </div>
</section>
"""
    return page("/cost-reduction/", "固定費削減コンサルティング｜Heart Bridge",
                "電気代・水道代・人件費・OA機器費まで、医療法人・社会福祉法人の固定費を専門家が無料診断。実績に基づいた経費見直しをワンストップでご提案します。",
                body)

# ---------------------------------------------------------------
# 炭化炉事業（一覧・乾熱滅菌・製炭・スポンサー募集）
# ---------------------------------------------------------------

def build_carbonization_hub():
    body = f"""
{mhero("Carbonization Business", "炭化炉事業<br><span style='color:var(--orange)'>（乾熱滅菌・製炭）</span>",
       "医療・介護施設向け乾熱滅菌減量装置と、地域資源を活かした製炭事業をご紹介。廃棄物処理のコスト削減と環境負荷軽減を同時に実現します。",
       CRUMB_TOP + "炭化炉事業",
       '<a class="btn btn-orange" href="/contact/">資料請求はこちら →</a>')}
<section class="sec" style="background:var(--warm-bg);">
  <div class="inner">
    <span class="sec-label">Business</span>
    <h2 class="sec-title">3つの取り組み</h2>
    <div class="biz-grid">
      <a class="biz-card" href="/carbonization/sterilizer/">
        <div class="biz-card-top"><span class="biz-num">01</span><span class="biz-icon">{icon('sun')}</span></div>
        <h3>乾熱滅菌減量装置</h3>
        <div class="biz-sub-list">
          <div class="biz-sub-item"><strong>医療産廃対応炭化炉（MD1000型）</strong><p>医療廃棄物・紙おむつ・感染性廃棄物を高温で乾熱滅菌・炭化処理する専用炉。焼却せず炭に変えることで処理コスト削減と有害物質の無害化を同時に実現します。仕様・導入コストの詳細はこちら。</p></div>
        </div>
        <span class="biz-effect">{icon('trend')} 処理コスト削減</span>
      </a>
      <a class="biz-card" href="/carbonization/charcoal/">
        <div class="biz-card-top"><span class="biz-num">02</span><span class="biz-icon">{icon('cycle')}</span></div>
        <h3>製炭事業（有機物炭化炉）</h3>
        <p>竹や木材などのバイオマス資源を高品質な炭に変える有機物炭化炉。生ごみ・牡蠣殻等の地域資源循環にも対応し、炭の活用・販売サポートまで一貫して行います。</p>
        <span class="biz-effect">{icon('trend')} 地域資源循環</span>
      </a>
      <a class="biz-card" href="/carbonization/sponsor/">
        <div class="biz-card-top"><span class="biz-num">03</span><span class="biz-icon">{icon('heart')}</span></div>
        <h3>スポンサー募集</h3>
        <p>投資型フランチャイズとして、炭化炉事業の協賛企業・投資家・地域パートナーを募集しています。</p>
        <span class="biz-effect">{icon('trend')} 協賛募集中</span>
      </a>
    </div>
  </div>
</section>
"""
    return page("/carbonization/", "炭化炉事業（乾熱滅菌・製炭）｜Heart Bridge",
                "医療・介護施設向け乾熱滅菌減量装置と、地域資源を活かした製炭事業をご紹介。廃棄物処理のコスト削減と環境負荷軽減を同時に実現します。",
                body)


def build_sterilizer():
    body = f"""
{mhero("Sterilizer Device", "乾熱滅菌減量装置<br><span style='color:var(--orange)'>（MD1000型）</span>",
       "紙おむつや感染性廃棄物を乾熱滅菌・減容化する装置です。病院・介護施設の廃棄物処理コストと処理量を大幅に削減します。",
       CRUMB_TOP + '<a href="/carbonization/">炭化炉事業</a> ／ 乾熱滅菌減量装置',
       '<a class="btn btn-orange" href="/contact/">資料請求はこちら →</a>'
       '<a class="btn btn-ghost" href="/case-studies/">導入事例を見る</a>')}
<div class="svc-body">
  <div>
    <h2>MD1000型 製品詳細</h2>
    <p>医療産廃対応の専用炉で、紙おむつ・感染性廃棄物を焼却せず高温で乾熱滅菌・減容化。処理コスト削減と有害物質の無害化を同時に実現します。</p>
    <div style="border-radius:var(--r-lg);overflow:hidden;margin-bottom:20px;box-shadow:var(--sh-sm);">
      <img src="/assets/img/hero.jpg" alt="乾熱滅菌減量装置 MD1000型">
    </div>
    <div class="svc-feats">
      <div class="svc-feat">{icon('sun','ic')}<div><b>乾熱滅菌処理</b><span>高温処理により病原菌・感染性廃棄物を安全に無害化します。</span></div></div>
      <div class="svc-feat">{icon('cycle','ic')}<div><b>大幅な減容化</b><span>処理後は容積・重量が大きく減少し、廃棄コストを削減します。</span></div></div>
      <div class="svc-feat">{icon('checkcircle','ic')}<div><b>医療産廃に対応</b><span>紙おむつ・感染性廃棄物など医療・介護現場特有の廃棄物に対応します。</span></div></div>
    </div>
  </div>
  <div class="svc-stats">
    <div class="lbl">導入効果（実績）</div>
    <div class="svc-stat-row"><span class="l">廃棄物容積削減率</span><span class="n">80<sup>%</sup>前後</span></div>
    <div class="svc-stat-row"><span class="l">設置〜稼働までの期間</span><span class="n">1.5〜2<sup>ヶ月</sup></span></div>
    <div class="svc-stat-row"><span class="l">対応エリア</span><span class="n">全国</span></div>
  </div>
</div>
<div class="svc-cta">
  <a class="btn btn-ghost on-light" href="/carbonization/">炭化炉事業一覧へ戻る</a>
  <a class="btn btn-orange" href="/contact/">お問い合わせ・資料請求</a>
</div>
"""
    return page("/carbonization/sterilizer/", "乾熱滅菌減量装置(MD1000型)｜病院・介護施設向け｜Heart Bridge",
                "紙おむつや感染性廃棄物を乾熱滅菌・減容化するMD1000型装置の仕様・導入コストをご紹介。病院・介護施設の廃棄物処理コストと処理量を大幅に削減します。",
                body)


def build_charcoal():
    body = f"""
{mhero("Charcoal Business", "製炭事業<br><span style='color:var(--orange)'>（有機物炭化炉）</span>",
       "生ごみや牡蠣殻など有機物を炭化し地域資源として循環させる製炭事業です。バイオ炭の活用方法・販売サイトのご案内もこちらでご紹介します。",
       CRUMB_TOP + '<a href="/carbonization/">炭化炉事業</a> ／ 製炭事業',
       '<a class="btn btn-orange" href="/contact/">資料請求はこちら →</a>'
       '<a class="btn btn-ghost" href="/case-studies/">導入事例を見る</a>')}
<div class="svc-body">
  <div>
    <h2>有機物炭化炉と、炭の活用・販売サポート</h2>
    <p>竹や木材などのバイオマス資源を高品質な炭に変え、農業・工業向けに販売。産炭由来の炭を活用した土壌改良や環境保全型農業にもつながります。</p>
    <div class="svc-feats">
      <div class="svc-feat">{icon('cycle','ic')}<div><b>牡蠣殻等 地域資源循環</b><span>地域で発生する牡蠣殻・生ごみ等を炭化し、資源として循環させます。</span></div></div>
      <div class="svc-feat">{icon('users','ic')}<div><b>就労支援との連携</b><span>就労継続支援B型事業所と連携し、障がい者雇用の創出にもつなげています。</span></div></div>
      <div class="svc-feat">{icon('coin','ic')}<div><b>炭の活用・販売サポート</b><span>生産した炭の買取・販路開拓をサポート。外部販売サイトもご案内します。</span></div></div>
    </div>
    <p style="margin-top:20px;"><a class="btn btn-ghost on-light" href="#" onclick="return false;">炭の販売サイトを見る（外部リンク）→</a></p>
  </div>
  <div class="svc-stats">
    <div class="lbl">導入効果（実績）</div>
    <div class="svc-stat-row"><span class="l">廃棄物削減率</span><span class="n">70<sup>%</sup>前後</span></div>
    <div class="svc-stat-row"><span class="l">対応原料</span><span class="n">竹・木材・生ごみ 等</span></div>
    <div class="svc-stat-row"><span class="l">SDGs該当目標</span><span class="n">8 / 12 / 13</span></div>
  </div>
</div>
<div class="svc-cta">
  <a class="btn btn-ghost on-light" href="/carbonization/">炭化炉事業一覧へ戻る</a>
  <a class="btn btn-orange" href="/contact/">お問い合わせ・資料請求</a>
</div>
"""
    return page("/carbonization/charcoal/", "有機物炭化炉による製炭事業｜バイオ炭の活用・販売｜Heart Bridge",
                "生ごみや牡蠣殻など有機物を炭化し地域資源として循環させる製炭事業です。バイオ炭の活用方法・販売サイトのご案内もこちらでご紹介します。",
                body)


def build_sponsor():
    body = f"""
{mhero("Sponsor Recruitment", "あなたの一歩が、<br><span style='color:var(--orange)'>まちを変える</span>力になる。",
       "産業廃棄物を炭に変える技術と、障がい者雇用支援を組み合わせた仕組みに、スポンサー・協賛企業として参加しませんか。",
       CRUMB_TOP + '<a href="/carbonization/">炭化炉事業</a> ／ スポンサー募集',
       '<a class="btn btn-orange" href="/contact/">資料請求はこちら →</a>'
       '<a class="btn btn-ghost" href="/carbonization/">炭化炉事業を見る</a>')}

<div class="mission-strip"><div class="mission-strip-inner">
  <p style="color:#fff;">産業廃棄物を炭に変える技術と、障がい者雇用支援を組み合わせた仕組みに、<strong>あなたも参加しませんか。</strong></p>
</div></div>

<section class="sec" style="background:var(--warm-bg);">
  <div class="inner">
    <span class="sec-label">Benefit</span>
    <h2 class="sec-title">スポンサーになるメリット</h2>
    <div class="spr-benefits">
      <div class="spr-bcard">{icon('globe','ic')}<b>SDGs貢献の対外PR</b><span>取り組みをSDGsバッジ付きで自社IR・採用広報に活用できます。</span></div>
      <div class="spr-bcard">{icon('users','ic')}<b>地域・行政との接点</b><span>地方創生・行政連携の実績を持つHeartBridgeとの共創機会。</span></div>
      <div class="spr-bcard">{icon('trend','ic')}<b>投資リターン</b><span>投資型フランチャイズとして、事業成長に応じたリターンを設計。</span></div>
      <div class="spr-bcard">{icon('heart','ic')}<b>ブランドイメージ向上</b><span>環境課題＋福祉課題の同時解決というストーリーを共有できます。</span></div>
    </div>
  </div>
</section>

<section class="sec" style="background:var(--cream);">
  <div class="inner">
    <span class="sec-label">Plan</span>
    <h2 class="sec-title">協賛プラン（例）</h2>
    <div class="spr-tiers">
      <div class="spr-tier"><div class="num">01</div><h3>法人スポンサー</h3><span class="biz-effect">{icon('trend')} SDGs対外PR向き</span><p>自社の環境・社会貢献活動として、炭化炉事業への協賛・出資を通じたパートナーシップを締結します。</p><div class="sdg-badges"><span class="sdg-tile sdg-13">13</span><span class="sdg-tile sdg-17">17</span></div></div>
      <div class="spr-tier"><div class="num">02</div><h3>個人スポンサー</h3><span class="biz-effect">{icon('trend')} 少額から参加可</span><p>個人投資家として、少額からの協賛・応援が可能。活動レポートを定期的にお届けします。</p><div class="sdg-badges"><span class="sdg-tile sdg-8">8</span><span class="sdg-tile sdg-13">13</span></div></div>
      <div class="spr-tier"><div class="num">03</div><h3>行政・地域連携</h3><span class="biz-effect">{icon('trend')} 地域課題解決型</span><p>自治体・地域企業向け。株式会社GATTELとの連携のように、地域全体を巻き込む座組を設計します。</p><div class="sdg-badges"><span class="sdg-tile sdg-11">11</span><span class="sdg-tile sdg-17">17</span></div></div>
    </div>
  </div>
</section>

<section class="sec" style="background:var(--white);">
  <div class="inner">
    <div class="biz-header"><h2 class="sec-title" style="margin-bottom:0;">すでに広がっている輪</h2><span style="font-size:.8rem;color:var(--gray-500);">既存のスポンサー・パートナーの皆様</span></div>
    <div class="spr-proof">
      <div class="spr-pcard"><div class="av">{icon('star')}</div><span class="case-tag">プロゴルファー</span><h3 style="font-size:.9rem;margin-bottom:4px;">柴田 将弥 選手</h3><p style="font-size:.76rem;color:var(--gray-500);">フェアウェイに夢を追う若き才能</p></div>
      <div class="spr-pcard"><div class="av">{icon('star')}</div><span class="case-tag">ハンドボール</span><h3 style="font-size:.9rem;margin-bottom:4px;">琉球コラソン</h3><p style="font-size:.76rem;color:var(--gray-500);">沖縄を拠点とするプロチーム</p></div>
      <div class="spr-pcard"><div class="av">{icon('cycle')}</div><span class="case-tag">パートナー企業</span><h3 style="font-size:.9rem;margin-bottom:4px;">株式会社GATTEL</h3><p style="font-size:.76rem;color:var(--gray-500);">都市×地方の新たなパートナーシップ</p></div>
    </div>
  </div>
</section>

<section class="sec" style="background:var(--ink);text-align:center;">
  <div class="inner">
    <h2 class="sec-title sec-title-white">まずはお話を聞かせてください</h2>
    <p style="color:rgba(255,255,255,.55);font-size:.88rem;max-width:480px;margin:0 auto 28px;">協賛プランの詳細・金額は個別にご案内しています。お気軽にお問い合わせください。</p>
    <a class="btn btn-orange" href="/contact/">資料請求・お問い合わせ →</a>
  </div>
</section>
"""
    return page("/carbonization/sponsor/", "スポンサー募集｜炭化炉事業への協賛・投資｜Heart Bridge",
                "産業廃棄物を炭に変える技術と、障がい者雇用支援を組み合わせた炭化炉事業のスポンサー・協賛企業を募集しています。法人・個人・行政連携の3プランをご用意。",
                body)

# ---------------------------------------------------------------
# 導入事例
# ---------------------------------------------------------------

def record_row(facility, pref, waste):
    return f"""
<div class="record-row">
  <div class="record-facility">{icon('checkcircle')}{facility}</div>
  <div class="record-pref">{pref}</div>
  <div class="record-waste">{waste}</div>
</div>"""


def build_case_hub():
    records = [
        ("総合病院", "北海道", "紙おむつ"),
        ("病院", "新潟県", "紙おむつ"),
        ("リハビリ病院", "千葉県", "紙おむつ"),
        ("市立病院", "千葉県", "紙おむつ・脱脂綿"),
        ("介護老人保健施設", "東京都", "紙おむつ・生ごみ"),
        ("特別養護老人ホーム", "東京都", "紙おむつ"),
        ("病院", "神奈川県", "紙おむつ・生ごみ"),
        ("市立病院", "静岡県", "紙おむつ"),
        ("検査会社", "京都府", "血液"),
        ("中間処理業者", "鹿児島県", "紙おむつ"),
    ]
    rows = "".join(record_row(f, p, w) for f, p, w in records)
    body = f"""
{mhero("Case Studies", "導入実績", "乾熱滅菌減量装置（MD1000型）の導入実績を一部抜粋してご紹介します。全国の病院・介護施設・検査会社等で稼働中です。",
       CRUMB_TOP + "導入事例",
       '<a class="btn btn-orange" href="/contact/">無料相談する →</a>')}
<section class="sec" style="background:var(--white);">
  <div class="inner">
    <span class="sec-label">Track Record</span>
    <h2 class="sec-title">導入実績（抜粋）</h2>
    <div class="record-table">
      <div class="record-row record-head">
        <div class="record-facility">施設種別</div>
        <div class="record-pref">都道府県</div>
        <div class="record-waste">処理対象</div>
      </div>
      {rows}
    </div>
  </div>
  <div class="inner" style="text-align:center;margin-top:32px;">
    <a class="btn btn-orange" href="/contact/">同じような相談をしてみる →</a>
  </div>
</section>
"""
    return page("/case-studies/", "導入実績｜株式会社Heart Bridge",
                "乾熱滅菌減量装置（MD1000型）の導入実績を一部抜粋してご紹介します。全国の病院・介護施設・検査会社等で稼働中です。",
                body)

# ---------------------------------------------------------------
# メディア・スポンサー
# ---------------------------------------------------------------

def build_media_hub():
    body = f"""
{mhero("Media &amp; Sponsor", "メディア・<span style='color:var(--orange)'>スポンサー</span>",
       "株式会社Heart Bridgeのメディア掲載実績と、スポンサーとして応援している選手・団体をご紹介します。",
       CRUMB_TOP + "メディア・スポンサー")}
<section class="sec" style="background:var(--white);">
  <div class="inner pillars">
    <a class="pillar" href="/media/press/">
      <div class="pic">{icon('broadcast')}</div>
      <h3>メディア掲載情報</h3>
      <p>テレビ・新聞・Web媒体等でご紹介いただいた掲載実績をまとめています。</p>
      <span class="more">詳しく見る →</span>
    </a>
    <a class="pillar" href="/media/sponsorship/">
      <div class="pic">{icon('star')}</div>
      <h3>スポンサーを務めてる選手・団体</h3>
      <p>HeartBridgeがスポンサーとして応援しているプロ選手・団体をご紹介します。</p>
      <span class="more">詳しく見る →</span>
    </a>
  </div>
</section>
"""
    return page("/media/", "メディア・スポンサー｜Heart Bridge",
                "株式会社Heart Bridgeのメディア掲載実績と、スポンサーとして応援している選手・団体をご紹介します。",
                body)


def build_media_press():
    play_svg = '<svg viewBox="0 0 24 24"><polygon points="6 3 20 12 6 21 6 3"></polygon></svg>'
    cards = [
        ("INTERVIEW", "経営者プライム", "炭と就労支援が繋ぐ社会貢献のかたち",
         "https://keieisha-prime.com/interview/1329/",
         "/assets/img/media-keieisha.png", False),
        ("INTERVIEW", "SAMURAI CEO（社長メシ）", "「社会貢献」と「利益」の両立を追求。関わるすべての人を幸せにする仕組みをつくる",
         "https://www.samurai-ceo.jp/%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BEheart-bridge/",
         "/assets/img/media-samurai-ceo.webp", False),
        ("VIDEO", "YouTube", "【営業で結果を出す秘訣】3年でトップセールスマンになった理由とは？株式会社Heart Bridge 髙橋社長が登場！！｜vol.367",
         "https://youtu.be/I_WG63tPyVM", "https://img.youtube.com/vi/I_WG63tPyVM/hqdefault.jpg", True),
        ("VIDEO", "YouTube", "【社会貢献×就労支援】炭で国内エネルギー循環を実現した新ビジネスの全貌に迫る！！｜vol.368",
         "https://youtu.be/FqkWwyqDRYk", "https://img.youtube.com/vi/FqkWwyqDRYk/hqdefault.jpg", True),
        ("VIDEO", "YouTube", "未来の子供たちのための挑戦。世界展開も見据えている脱炭素事業とは？｜vol.369",
         "https://youtu.be/S-Ip2KT1uDo", "https://img.youtube.com/vi/S-Ip2KT1uDo/hqdefault.jpg", True),
    ]
    grid = "".join(f"""
    <a class="media-card" href="{href}" target="_blank" rel="noopener">
      <div class="media-thumb">
        <span class="media-badge">{tag}</span>
        <img src="{img}" alt="{title}">{f'<div class="play-badge">{play_svg}</div>' if is_video else ''}
      </div>
      <div class="media-body"><div class="media-source">{source}</div><div class="media-title">{title}</div></div>
    </a>""" for tag, source, title, href, img, is_video in cards)
    body = f"""
{mhero("Media", "メディア<span style='color:var(--orange)'>掲載情報</span>",
       "テレビ・新聞・Web媒体等でご紹介いただいた株式会社Heart Bridgeの掲載実績をまとめています。",
       CRUMB_TOP + '<a href="/media/">メディア・スポンサー</a> ／ メディア')}
<section class="sec" style="background:var(--ink);">
  <div class="inner"><div class="media-grid">{grid}</div></div>
</section>
"""
    return page("/media/press/", "メディア掲載情報｜株式会社Heart Bridge",
                "テレビ・新聞・Web媒体等でご紹介いただいた株式会社Heart Bridgeの掲載実績をまとめています。",
                body)


def build_media_sponsorship():
    body = f"""
{mhero("Sponsorship", "スポンサーを務めてる<span style='color:var(--orange)'>選手・団体</span>",
       "HeartBridgeがスポンサーとして応援している選手・団体の活動をご紹介します。",
       CRUMB_TOP + '<a href="/media/">メディア・スポンサー</a> ／ スポンサー')}
<section class="sec" style="background:var(--orange-pale);">
  <div class="inner">
    <div class="sponsor-grid">
      <div class="sponsor-card">
        <div class="sponsor-card-img carousel">
          <img class="active" src="/assets/img/sponsor-shibata-1.jpg" alt="柴田将弥選手 1">
          <img src="/assets/img/sponsor-shibata-2.jpg" alt="柴田将弥選手 2">
        </div>
        <span class="sponsor-tag">プロゴルファー</span>
        <h4>柴田 将弥 選手</h4>
        <p>HeartBridgeがスポンサーを務めるプロゴルファー。フェアウェイに夢を追い続ける若き才能を全力でサポートします。</p>
      </div>
      <div class="sponsor-card">
        <div class="sponsor-card-img logo"><img src="/assets/img/sponsor-ryukyu-corazon.webp" alt="琉球コラソン"></div>
        <span class="sponsor-tag">ハンドボール</span>
        <h4>琉球コラソン</h4>
        <p>沖縄を拠点とするプロハンドボールチーム。地域に根ざしたスポーツ文化の発展と、チームの更なる飛躍を応援します。</p>
      </div>
      <div class="sponsor-card">
        <div class="sponsor-card-img logo"><img src="/assets/img/sponsor-gattel.jpg" alt="株式会社GATTEL"></div>
        <span class="sponsor-tag">パートナー企業</span>
        <h4>株式会社GATTEL</h4>
        <p>都市と地方の企業を繋ぐパートナー企業。地方創生を通じて地域経済の活性化に貢献しています。</p>
      </div>
    </div>
    <div style="text-align:center;margin-top:44px;">
      <a class="btn btn-orange" href="/carbonization/sponsor/">スポンサー募集ページを見る →</a>
    </div>
  </div>
</section>
"""
    return page("/media/sponsorship/", "スポンサー活動｜応援している選手・団体｜Heart Bridge",
                "株式会社Heart Bridgeがスポンサーとして応援している選手・団体の活動をご紹介します。",
                body)

# ---------------------------------------------------------------
# SDGs
# ---------------------------------------------------------------

def build_sdgs():
    goals = [
        (8, "働きがいも経済成長も"), (11, "住み続けられるまちづくりを"), (12, "つくる責任つかう責任"),
        (13, "気候変動に具体的な対策を"), (15, "陸の豊かさも守ろう"), (17, "パートナーシップで目標を達成しよう"),
        (6, "安全な水とトイレを世界中に"), (7, "エネルギーをみんなにそしてクリーンに"),
    ]
    tiles = "".join(
        f'<div class="sdg-big"><img class="sdg-big-icon" src="/assets/img/sdg/sdg{n}.png" alt="SDGs目標{n} {t}" width="80" height="80" loading="lazy"><div class="sdg-big-title">{t}</div></div>'
        for n, t in goals
    )
    body = f"""
{mhero("SDGs", "SDGsへの<span style='color:var(--orange)'>取り組み</span>",
       "炭化・節水・節電・農業・行政連携・地方創生――それぞれの事業が国連の持続可能な開発目標と直結しています。",
       CRUMB_TOP + "SDGsへの取り組み")}
<section class="sdgs-sec">
  <div class="sdgs-intro">
    <span class="sec-label">Sustainable Development Goals</span>
    <h2 class="sec-title sec-title-white">事業を通じて貢献しているSDGs</h2>
    <p>固定費削減コンサルによる資源の有効利用から、炭化炉事業による廃棄物削減・地域資源循環、障がい者雇用の創出まで、Heart Bridgeの事業は複数のSDGs目標と直結しています。</p>
  </div>
  <div class="sdgs-wheel">{tiles}</div>
  <div class="sdgs-assoc">
    <span class="sdgs-assoc-badge">{icon('shield')} SDGs協会 会員</span>
    <div class="sdgs-assoc-text">株式会社Heart BridgeはSDGs協会の正式会員として、持続可能な社会の実現に向けた活動を推進しています。</div>
  </div>
</section>
"""
    return page("/sdgs/", "SDGsへの取り組み｜株式会社Heart Bridge",
                "株式会社Heart BridgeはSDGs協会の正式会員として、事業を通じて貢献しているSDGsの取り組みをご紹介します。",
                body)

# ---------------------------------------------------------------
# 会社概要
# ---------------------------------------------------------------

def build_company():
    body = f"""
{mhero("Company", "会社概要", "株式会社Heart Bridgeの会社概要・代表挨拶・沿革・アクセス情報をまとめてご案内します。",
       CRUMB_TOP + "会社概要")}
<section class="sec" style="background:var(--white);">
  <div class="inner co-grid">
    <div>
      <span class="sec-label">Company</span>
      <h2 class="sec-title">会社概要</h2>
      <table class="info-table">
        <tr><th>会社名</th><td>株式会社Heart Bridge</td></tr>
        <tr><th>代表取締役</th><td>髙橋 充</td></tr>
        <tr><th>設立</th><td>2022年5月2日</td></tr>
        <tr><th>本社</th><td>〒592-8342 大阪府堺市浜寺船尾町370</td></tr>
        <tr><th>所在地</th><td>〒567-0805 大阪府茨木市橋の内3-13-4-201</td></tr>
        <tr><th>主な事業</th><td>固定費削減コンサルティング／炭化炉販売・炭の販売／節水節電対策／障がい者就労支援・ウェルビーイング支援</td></tr>
      </table>
    </div>
    <div class="map-card">
      <div class="map-icon">{icon('pin')}</div>
      <p>〒592-8342 大阪府堺市浜寺船尾町370（本社）<br>〒567-0805 大阪府茨木市橋の内3-13-4-201（所在地）</p>
    </div>
  </div>
</section>

<section class="sec" style="background:var(--warm-bg);">
  <div class="inner msg-layout">
    <div class="msg-ceo-block">
      <img class="photo" src="/assets/img/ceo.jpg" alt="代表取締役 髙橋充">
      <div class="body">
        <div class="ceo-name">髙橋 充</div>
        <div class="ceo-title">代表取締役 ／ 兵庫県尼崎市出身</div>
        <div class="ceo-origin">建築材メーカーで<strong>入社3年目にトップセールス</strong>を記録後、独立。高齢者施設の友人の現実から省エネ事業をスタートし、現在は<strong>炭化事業×障がい者雇用</strong>に挑戦中。</div>
      </div>
    </div>
    <div class="msg-body">
      <p>「嘘をつかない」──それだけを、ずっと守ってきました。</p>
      <p>独立のきっかけは、高齢者施設で働く友人の一言でした。<strong>月給16〜17万円。</strong>あれだけ献身的に人に寄り添っている人が、それだけしかもらえていない。何かがおかしい、何かできないか──その思いから、施設の電気代・水道代を下げる省エネ事業を始めました。</p>
      <p>やがて、もっと根本的な課題に向き合うようになりました。産業廃棄物を炭に変える技術と、重度障がい者の就労支援を組み合わせたら、<em>投資家・施設・社会の全員がプラスになる仕組み</em>がつくれるのではないか。日本の重度障がい者の就労率はわずか5%。この数字を変えるために、炭化事業の収益化を進めています。</p>
      <p>高校時代、野球で脱臼して推薦を失ったとき、世界が崩れた気がしました。でもその経験が教えてくれたことがある。<em>裏切られてもいいから、人を信じ抜く。</em>その姿勢だけが、本当の信頼をつくると。</p>
      <p>「捨てる」を「つなぐ」に変える。廃棄物も、困難も、すべてを橋にしていく。それがHeartBridgeの存在理由です。</p>
    </div>
  </div>
</section>
"""
    return page("/company/", "会社概要・代表挨拶・アクセス｜株式会社Heart Bridge",
                "株式会社Heart Bridgeの会社概要・代表挨拶・沿革・アクセス情報をまとめてご案内します。固定費削減コンサルと炭化炉事業の2軸で事業を展開しています。",
                body)

# ---------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------

def build_faq():
    faqs = [
        ("相談・見積もりに費用はかかりますか？", "初回のご相談・現状診断・お見積もりはすべて無料です。導入をお決めいただくまで費用は一切発生しません。", True),
        ("乾熱滅菌減量装置の導入にはどのくらい期間がかかりますか？", "現地調査から設置完了まで、標準的なケースで約1.5〜2ヶ月です。施設の状況により前後します。", False),
        ("対応エリアを教えてください。", "本社（大阪府堺市）を中心に全国対応しております。遠方の場合も一度お問い合わせください。", False),
        ("固定費削減コンサルの契約期間の縛りはありますか？", "サービスによって異なります。単発の診断のみのご依頼も可能です。詳細はお問い合わせ時にご案内します。", False),
        ("スポンサー・協賛はどのように申し込めますか？", "「スポンサー募集」ページからお問い合わせいただくか、お問い合わせフォームの内容欄に「スポンサーに関する相談」とご記入ください。", False),
        ("採用の応募方法を教えてください。", "採用情報ページに掲載の求人詳細（Indeed）よりご応募いただけます。ご不明点はお問い合わせフォームからもご連絡いただけます。", False),
    ]
    items = "".join(
        f'<details class="faq-item"{" open" if op else ""}>'
        f'<summary class="faq-q"><span class="badge">Q</span><span class="txt">{q}</span><span class="plus"></span></summary>'
        f'<div class="faq-a">{a}</div></details>'
        for q, a, op in faqs
    )
    body = f"""
{mhero("FAQ", "よくある<span style='color:var(--orange)'>質問</span>",
       "固定費削減コンサルティングと炭化炉事業（乾熱滅菌減量装置・製炭）について、よくいただくご質問にまとめてお答えします。",
       CRUMB_TOP + "よくある質問")}
<section class="sec" style="background:var(--white);">
  <div class="faq-list">{items}</div>
  <div class="inner" style="text-align:center;margin-top:40px;">
    <p style="color:var(--gray-500);font-size:.86rem;margin-bottom:16px;">解決しない場合はお気軽にお問い合わせください。</p>
    <a class="btn btn-orange" href="/contact/">お問い合わせ・資料請求 →</a>
  </div>
</section>
"""
    return page("/faq/", "よくある質問｜Heart Bridge",
                "固定費削減コンサルティングと炭化炉事業（乾熱滅菌減量装置・製炭）について、よくいただくご質問にまとめてお答えします。",
                body)

# ---------------------------------------------------------------
# お問い合わせ／送信完了
# ---------------------------------------------------------------

def build_contact():
    body = f"""
<section class="contact-sec sec">
  <div class="inner contact-grid">
    <div class="contact-left">
      <span class="sec-label">Contact</span>
      <h2>まずは、お気軽に<br>ご相談ください。</h2>
      <p>炭化炉の導入・固定費削減・スポンサーのご相談など、担当者より2営業日以内にご連絡いたします。</p>
      <div class="contact-chips">
        <div class="contact-chip">{icon('pin')}〒567-0805 大阪府茨木市橋の内3-13-4-201</div>
        <div class="contact-chip">{icon('mail')}www.hb789.info</div>
        <div class="contact-chip">{icon('clock')}平日 9:00〜18:00 対応</div>
        <a class="contact-chip" href="https://x.com/HeartBridg789" target="_blank" rel="noopener">{icon('star')}@HeartBridg789</a>
        <a class="contact-chip" href="https://instagram.com/heartbridg789" target="_blank" rel="noopener">{icon('broadcast')}heartbridg789</a>
      </div>
    </div>
    <div class="contact-form-wrap">
      <form id="contact-form" data-thanks="/contact/thanks/">
        <div class="form-row">
          <div class="fg"><label>会社名<span class="req">※</span></label><input type="text" id="company" name="company" placeholder="株式会社〇〇" required></div>
          <div class="fg"><label>お名前<span class="req">※</span></label><input type="text" id="name" name="name" placeholder="山田 太郎" required></div>
        </div>
        <div class="form-row">
          <div class="fg"><label>メールアドレス<span class="req">※</span></label><input type="email" id="email" name="email" placeholder="example@company.com" required></div>
          <div class="fg"><label>電話番号</label><input type="tel" id="tel" name="tel" placeholder="06-0000-0000"></div>
        </div>
        <div class="fg">
          <label>お問い合わせ種別<span class="req">※</span></label>
          <select id="category" name="category" required>
            <option value="">選択してください</option>
            <option>固定費削減コンサルについて</option>
            <option>乾熱滅菌減量装置・製炭事業について</option>
            <option>スポンサー・協賛に関するお問い合わせ</option>
            <option>採用について</option>
            <option>その他</option>
          </select>
        </div>
        <div class="fg"><label>お問い合わせ内容<span class="req">※</span></label><textarea id="message" name="message" placeholder="ご相談内容・ご質問をご記入ください" required></textarea></div>
        <button class="btn-submit" type="submit">送信する</button>
      </form>
    </div>
  </div>
</section>
"""
    return page("/contact/", "お問い合わせ・資料請求｜Heart Bridge",
                "固定費削減の無料診断や炭化炉事業に関するご相談、資料請求はこちらから。専門スタッフが丁寧にご対応いたします。",
                body)


def build_thanks():
    body = f"""
<div class="thanks-wrap">
  <div class="thanks-card">
    <div class="thanks-icon">{icon('checkcircle')}</div>
    <h1>送信が完了しました</h1>
    <p>お問い合わせいただきありがとうございます。内容を確認のうえ、担当者より2営業日以内にご連絡いたします。</p>
    <div class="thanks-meta">お急ぎの場合は平日9:00〜18:00の間にX（@HeartBridg789）DMでもご連絡いただけます。</div>
    <a class="btn btn-orange" href="/" style="width:100%;justify-content:center;">TOPページへ戻る</a>
  </div>
</div>
"""
    return page("/contact/thanks/", "送信完了しました｜Heart Bridge",
                "お問い合わせありがとうございます。内容を確認のうえ、担当者より折り返しご連絡いたします。", body)

# ---------------------------------------------------------------
# 採用情報
# ---------------------------------------------------------------

def build_recruit():
    body = f"""
{mhero("Recruit", "採用情報", "株式会社Heart Bridgeの採用情報ページです。固定費削減コンサルと炭化炉事業、それぞれの職種で仲間を募集しています。",
       CRUMB_TOP + "採用情報")}
<section class="sec" style="background:var(--white);">
  <div class="inner">
    <div class="recruit-top">
      <table class="info-table">
        <tr><th>募集背景</th><td>炭化炉事業・障がい者就労支援の拡大に伴う増員</td></tr>
        <tr><th>雇用形態</th><td>正社員／契約社員／パート</td></tr>
        <tr><th>勤務地</th><td>大阪府堺市（本社）／大阪府茨木市</td></tr>
        <tr><th>選考フロー</th><td>書類選考 → 面談1回 → 内定</td></tr>
      </table>
      <div class="r-side">
        <div class="lbl">Message</div>
        <p>「捨てる」を「つなぐ」に変える仲間を募集しています。環境問題にも、人の心にも向き合える会社です。</p>
      </div>
    </div>
    <div class="r-note">現在募集中の職種・給与・勤務条件などの詳細は、Indeedの求人ページに掲載しています。募集内容は随時更新されるため、最新の求人情報は必ずIndeedにてご確認のうえご応募ください。</div>
    <div style="text-align:center;margin-top:32px;">
      <a class="btn btn-orange" href="https://jp.indeed.com/viewjob?jk=e6aeadbbaf190795&from=shareddesktop_copy" target="_blank" rel="noopener">Indeedで求人を見る →</a>
    </div>
  </div>
</section>
"""
    return page("/recruit/", "採用情報｜株式会社Heart Bridge",
                "株式会社Heart Bridgeの採用情報ページです。固定費削減コンサルと炭化炉事業、それぞれの職種で仲間を募集しています。",
                body)

# ---------------------------------------------------------------
# プライバシーポリシー
# ---------------------------------------------------------------

def build_policy():
    body = f"""
{mhero("Policy", "プライバシーポリシー<br>特定商取引法に基づく表記", "個人情報の取り扱い、および特定商取引法に基づく表記です。", CRUMB_TOP + "プライバシーポリシー")}
<div class="policy-body">
  <h2>プライバシーポリシー</h2>
  <p>株式会社Heart Bridge（以下「当社」）は、お客様の個人情報を適切に取り扱うことが社会的責務であると考え、以下の方針に基づき個人情報の保護に努めます。</p>
  <ul>
    <li>お問い合わせ・資料請求フォームでお預かりした個人情報は、お問い合わせへの対応・資料送付の目的以外には使用しません。</li>
    <li>法令に基づく場合を除き、ご本人の同意なく第三者に個人情報を提供することはありません。</li>
    <li>取得した個人情報は、適切な安全管理措置のもとで保管し、漏えい・滅失・毀損の防止に努めます。</li>
    <li>ご本人からの個人情報の開示・訂正・削除等のご請求には、法令に従い適切に対応します。</li>
  </ul>
  <h2>特定商取引法に基づく表記</h2>
  <table>
    <tr><th>事業者名</th><td>株式会社Heart Bridge</td></tr>
    <tr><th>代表者</th><td>髙橋 充</td></tr>
    <tr><th>所在地</th><td>〒567-0805 大阪府茨木市橋の内3-13-4-201</td></tr>
    <tr><th>お問い合わせ</th><td><a href="/contact/">お問い合わせフォーム</a>よりご連絡ください</td></tr>
    <tr><th>提供サービス</th><td>固定費削減コンサルティング、炭化炉事業（乾熱滅菌減量装置・製炭事業）等</td></tr>
  </table>
</div>
"""
    return page("/policy/", "プライバシーポリシー・特定商取引法に基づく表記｜Heart Bridge",
                "株式会社Heart Bridgeの個人情報保護方針および特定商取引法に基づく表記です。", body)

# ---------------------------------------------------------------
# Build all pages
# ---------------------------------------------------------------

PAGES = {
    "index.html": build_top,
    "cost-reduction/index.html": build_cost_reduction_hub,
    "cost-reduction/electricity/index.html": build_electricity,
    "cost-reduction/water/index.html": build_water,
    "cost-reduction/labor/index.html": build_labor,
    "cost-reduction/office-equipment/index.html": build_office_equipment,
    "carbonization/index.html": build_carbonization_hub,
    "carbonization/sterilizer/index.html": build_sterilizer,
    "carbonization/charcoal/index.html": build_charcoal,
    "carbonization/sponsor/index.html": build_sponsor,
    "case-studies/index.html": build_case_hub,
    "media/index.html": build_media_hub,
    "media/press/index.html": build_media_press,
    "media/sponsorship/index.html": build_media_sponsorship,
    "sdgs/index.html": build_sdgs,
    "company/index.html": build_company,
    "faq/index.html": build_faq,
    "contact/index.html": build_contact,
    "contact/thanks/index.html": build_thanks,
    "recruit/index.html": build_recruit,
    "policy/index.html": build_policy,
}

URL_PATHS = [
    "/", "/cost-reduction/", "/cost-reduction/electricity/", "/cost-reduction/water/",
    "/cost-reduction/labor/", "/cost-reduction/office-equipment/", "/carbonization/",
    "/carbonization/sterilizer/", "/carbonization/charcoal/", "/carbonization/sponsor/",
    "/case-studies/", "/media/", "/media/press/", "/media/sponsorship/",
    "/sdgs/", "/company/", "/faq/", "/contact/", "/contact/thanks/", "/recruit/", "/policy/",
]


def main():
    for relpath, builder in PAGES.items():
        full = os.path.join(ROOT, relpath)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(builder())
        print("wrote", relpath)

    # sitemap.xml
    urls = "".join(
        "<url><loc>%s%s</loc></url>" % (SITE, p) for p in URL_PATHS
    )
    sitemap = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>' % urls
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    robots = "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)
    print("wrote sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
