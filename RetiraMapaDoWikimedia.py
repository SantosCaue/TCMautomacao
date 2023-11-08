import json
from bs4 import BeautifulSoup

def extrair_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    galleryboxes = soup.find_all('li', class_='gallerybox')
    for gallerybox in galleryboxes:
        img_tag = gallerybox.find('img', alt=True)
        if img_tag:
            alt_text = img_tag['alt']
            img_src = img_tag['src']
            img_src = img_src.replace('.png', '')  # Remover a extensão .png
            urls.append({'alt': alt_text, 'url': img_src})
    return urls

def salvar_urls_em_arquivo(urls, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(urls, arquivo, indent=4)

# HTML de exemplo
html = '''

<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<title>Grey–green orthographic projections maps - Wikimedia Commons</title>
<script>document.documentElement.className="client-js";(function(){var cookie=document.cookie.match(/(?:^|; )commonswikimwclientprefs=([^;]+)/);if(cookie){var featureName=cookie[1];document.documentElement.className=document.documentElement.className.replace(featureName+'-enabled',featureName+'-disabled');}}());RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"62e6d000-dd2d-40b0-89f7-818898f82b91","wgCSPNonce":false,"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Grey–green_orthographic_projections_maps","wgTitle":"Grey–green orthographic projections maps","wgCurRevisionId":771083033,"wgRevisionId":771083033,"wgArticleId":8473283,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"]
,"wgCategories":["Locator maps (gray and green scheme)"],"wgPageViewLanguage":"en","wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgRelevantPageName":"Grey–green_orthographic_projections_maps","wgRelevantArticleId":8473283,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en"},"wgMFDisplayWikibaseDescriptions":{"search":true,"watchlist":true,"tagline":true,"nearby":true},"wgWMESchemaEditAttemptStepOversample":false,"wgWMEPageLength":4000,"wgNoticeProject":"commons","wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":false,"wgULSCurrentAutonym":"English","wgEditSubmitButtonLabelPublish":true,"wbmiDefaultProperties":["P180"],"wbmiPropertyTitles":{"P180":"Items portrayed in this file"},"wbmiPropertyTypes":{"P180":"wikibase-item"},"wbmiRepoApiUrl":"/w/api.php","wbmiHelpUrls":{"P180":
"https://commons.wikimedia.org/wiki/Special:MyLanguage/Commons:Depicts"},"wbmiExternalEntitySearchBaseUri":"https://www.wikidata.org/w/api.php","wbmiSupportedDataTypes":["wikibase-item","string","quantity","time","monolingualtext","external-id","globe-coordinate","url"],"wgCentralAuthMobileDomain":false,"wgULSPosition":"personal","wgULSisCompactLinksEnabled":true,"wgULSisLanguageSelectorEmpty":false,"wgWikibaseItemId":"Q21167586"};RLSTATE={"ext.gadget.Long-Image-Names-in-Categories":"ready","ext.gadget.uploadWizardMobile":"ready","ext.globalCssJs.user.styles":"ready","site.styles":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","mediawiki.page.gallery.styles":"ready","skins.vector.styles.legacy":"ready","jquery.makeCollapsible.styles":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.wikimediaBadges":"ready","ext.uls.pt":"ready","wikibase.client.init":"ready"};RLPAGEMODULES=["site","mediawiki.page.ready",
"jquery.makeCollapsible","skins.vector.legacy.js","mmv.head","mmv.bootstrap.autostart","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.citoid.wikibase.init","ext.eventLogging","ext.wikimediaEvents","ext.wikimediaEvents.wikibase","ext.navigationTiming","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.gadget.Slideshow","ext.gadget.ZoomViewer","ext.gadget.CollapsibleTemplates","ext.gadget.fastcci","ext.gadget.Stockphoto","ext.gadget.WatchlistNotice","ext.gadget.AjaxQuickDelete","ext.gadget.WikiMiniAtlas","ext.gadget.LanguageSelect","ext.gadget.PictureOfTheYearEnhancements","ext.centralauth.centralautologin","ext.echo.centralauth","ext.uls.compactlinks","ext.uls.interface"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.implement("user.options@12s5i",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});});});</script>
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=ext.uls.pt%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cjquery.makeCollapsible.styles%7Cmediawiki.page.gallery.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&amp;only=styles&amp;skin=vector">
<script async="" src="/w/load.php?lang=en&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector"></script>
<meta name="ResourceLoaderDynamicStyles" content="">
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=ext.gadget.Long-Image-Names-in-Categories%2CuploadWizardMobile&amp;only=styles&amp;skin=vector">
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector">
<meta name="generator" content="MediaWiki 1.41.0-wmf.17">
<meta name="referrer" content="origin">
<meta name="referrer" content="origin-when-crossorigin">
<meta name="referrer" content="origin-when-cross-origin">
<meta name="robots" content="max-image-preview:standard">
<meta name="format-detection" content="telephone=no">
<meta property="og:image" content="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/None_%28orthographic_projection%29.svg/1200px-None_%28orthographic_projection%29.svg.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1200">
<meta property="og:image" content="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/None_%28orthographic_projection%29.svg/800px-None_%28orthographic_projection%29.svg.png">
<meta property="og:image:width" content="800">
<meta property="og:image:height" content="800">
<meta property="og:image" content="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/None_%28orthographic_projection%29.svg/640px-None_%28orthographic_projection%29.svg.png">
<meta property="og:image:width" content="640">
<meta property="og:image:height" content="640">
<meta name="viewport" content="width=1000">
<meta property="og:title" content="Grey–green orthographic projections maps - Wikimedia Commons">
<meta property="og:type" content="website">
<link rel="preconnect" href="//upload.wikimedia.org">
<link rel="alternate" media="only screen and (max-width: 720px)" href="//commons.m.wikimedia.org/wiki/Grey%E2%80%93green_orthographic_projections_maps">
<link rel="alternate" type="application/x-wiki" title="Edit" href="/w/index.php?title=Grey%E2%80%93green_orthographic_projections_maps&amp;action=edit">
<link rel="apple-touch-icon" href="/static/apple-touch/commons.png">
<link rel="icon" href="/static/favicon/commons.ico">
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikimedia Commons">
<link rel="EditURI" type="application/rsd+xml" href="//commons.wikimedia.org/w/api.php?action=rsd">
<link rel="canonical" href="https://commons.wikimedia.org/wiki/Grey%E2%80%93green_orthographic_projections_maps">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
<link rel="alternate" type="application/atom+xml" title="Wikimedia Commons Atom feed" href="/w/index.php?title=Special:RecentChanges&amp;feed=atom">
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<link rel="dns-prefetch" href="//login.wikimedia.org">
</head>
<body class="skin-vector-legacy mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-Grey–green_orthographic_projections_maps rootpage-Grey–green_orthographic_projections_maps skin-vector action-view"><div id="mw-page-base" class="noprint"></div>
<div id="mw-head-base" class="noprint"></div>
<div id="content" class="mw-body" role="main">
	<a id="top"></a>
	<div id="siteNotice"><!-- CentralNotice --></div>
	<div class="mw-indicators">
	</div>
	<h1 id="firstHeading" class="firstHeading mw-first-heading"><span class="mw-page-title-main">Grey–green orthographic projections maps</span></h1>
	<div id="bodyContent" class="vector-body">
		<div id="siteSub" class="noprint">From Wikimedia Commons, the free media repository</div>
		<div id="contentSub"><div id="mw-content-subtitle"></div></div>
		<div id="contentSub2"></div>
		
		<div id="jump-to-nav"></div>
		<a class="mw-jump-link" href="#mw-head">Jump to navigation</a>
		<a class="mw-jump-link" href="#searchInput">Jump to search</a>
		<div id="mw-content-text" class="mw-body-content mw-content-ltr" lang="en" dir="ltr"><div class="mw-parser-output"><figure class="mw-halign-right" typeof="mw:File"><a href="/wiki/File:None_(orthographic_projection).svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/None_%28orthographic_projection%29.svg/240px-None_%28orthographic_projection%29.svg.png" decoding="async" width="240" height="240" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/None_%28orthographic_projection%29.svg/360px-None_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/None_%28orthographic_projection%29.svg/480px-None_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a><figcaption></figcaption></figure>
<p>Orthographic projections in the <b>green and grey globe scheme</b> ("gggs").
</p>
<h2><span class="mw-headline" id="Introduction">Introduction</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Grey%E2%80%93green_orthographic_projections_maps&amp;action=edit&amp;section=1" title="Edit section: Introduction">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="description mw-content-ltr my" dir="ltr" lang="my"><span class="language my" title="Burmese"><b>မြန်မာဘာသာ&#58; </b></span> <span style="font-family:Pyidaungsu, &#39;Myanmar Text&#39;, &#39;Noto Sans Myanmar&#39;, Myanmar3, Padauk, Parabaik, TharLon, &#39;Masterpiece Uni Sans&#39;, &#39;Win Uni Innwa&#39;, &#39;MyMyanmar Unicode&#39;, &#39;WinUni Innwa&#39;, Myanmar2, Myanmar1">မြေပုံတွင်အစိမ်းရောင်နှင့် အနက်ရောင်ဖြင့် မှတ်သားထားသောဒေသတစ်ခု သို့မဟုတ်တိုင်းပြည်တစ်ခုပါရှိသည်။</span></div>
<div class="description mw-content-ltr en" dir="ltr" lang="en"><span class="language en" title="English"><b>English&#58; </b></span> Orthographic projection world SVG maps with a region or country marked in dark green.</div>
<div class="description mw-content-ltr es" dir="ltr" lang="es"><span class="language es" title="Spanish"><b>Español&#58; </b></span> Mapamundis en proyección ortográfica SVG con una región o país en verde oscuro.</div>
<div class="description mw-content-ltr fil" dir="ltr" lang="fil"><span class="language fil" title="Filipino"><b>Filipino&#58; </b></span> Mga mapa ng mundo sa SVG na nasa proyeksiyong ortograpiko na may isang rehiyon o bansang nakamarka sa maitim na lunti.</div>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> हरे रंग में चिन्हित, विश्व के विभिन्न देशों व क्षेत्रों के लेखन प्रक्षेप एॅसवीजी मानचित्र</div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> მსოფლიოს SVG რუკები ორთოგრაფიულ პროექციაში მუქი მწვანე ფერის რეგიონით ან ქვეყნით.</div>
<div class="description mw-content-ltr ko" dir="ltr" lang="ko"><span class="language ko" title="Korean"><b>한국어&#58; </b></span> 진한녹색으로 지역과 나라를 표시하는 정사도법 세계지도.</div>
<div class="description mw-content-ltr ja" dir="ltr" lang="ja"><span class="language ja" title="Japanese"><b>日本語&#58;</b></span> 深い緑に地域や国を表示する正射方位図法世界地図。</div>
<div class="description mw-content-ltr tl" dir="ltr" lang="tl"><span class="language tl" title="Tagalog"><b>Tagalog&#58; </b></span> Mga mapa ng mundo sa SVG na nasa proyeksiyong ortograpiko na may isang rehiyon o bansang nakamarka sa maitim na lunti.</div>
<div class="description mw-content-ltr zh" dir="ltr" lang="zh"><span class="language zh" title="Chinese"><b>中文：</b></span>用深绿色标记国家或地区的正交投影矢量地图。</div>
<div class="description mw-content-ltr ru" dir="ltr" lang="ru"><span class="language ru" title="Russian"><b>Русский&#58; </b></span> Ортографические проекции мира в качестве карт формата SVG с регионами или странами, помеченными тёмно-зелёным цветом.</div>
<p><br />
</p>
<div>
<div style="clear:both;"></div>
<div class="description mw-content-rtl ar" dir="rtl" lang="ar"><span class="language ar" title="Arabic"><b>العربية&#58; </b></span> الرجاء، <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">قراءة الميثاق</a>.</div>
<div class="description mw-content-ltr bn" dir="ltr" lang="bn"><span class="language bn" title="Bangla"><b>বাংলা&#58; </b></span> দয়া করে, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">রীতিনীতিটি পড়ুন</a>।</div>
<div class="description mw-content-ltr de" dir="ltr" lang="de"><span class="language de" title="German"><b>Deutsch&#58; </b></span> Bitte lies die <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">Konventionen</a>.</div>
<div class="description mw-content-ltr en" dir="ltr" lang="en"><span class="language en" title="English"><b>English&#58; </b></span> Please, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">read the conventions</a>.</div>
<div class="description mw-content-ltr es" dir="ltr" lang="es"><span class="language es" title="Spanish"><b>Español&#58; </b></span> Por favor, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">lea las convenciones</a>.</div>
<div class="description mw-content-ltr fil" dir="ltr" lang="fil"><span class="language fil" title="Filipino"><b>Filipino&#58; </b></span> Paki-<a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">basa ang mga kumbensyon</a>.</div>
<div class="description mw-content-ltr fr" dir="ltr" lang="fr"><span class="language fr" title="French"><b>Français&#160;&#58; </b></span> S'il vous plaît, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">lisez les conventions</a>.</div>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> कृपया <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">सभागमों को पढ़ लें</a>.</div>
<div class="description mw-content-ltr id" dir="ltr" lang="id"><span class="language id" title="Indonesian"><b>Bahasa Indonesia&#58; </b></span> Silakan, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">baca konvensi</a>.</div>
<div class="description mw-content-ltr it" dir="ltr" lang="it"><span class="language it" title="Italian"><b>Italiano&#58; </b></span> Si prega di leggere le <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">convenzioni</a>.</div>
<div class="description mw-content-ltr ja" dir="ltr" lang="ja"><span class="language ja" title="Japanese"><b>日本語&#58;</b></span> <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">規約をご確認ください</a>。</div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> გთხოვთ, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">გაეცნოთ კონვენციებს</a>.</div>
<div class="description mw-content-ltr mk" dir="ltr" lang="mk"><span class="language mk" title="Macedonian"><b>Македонски&#58; </b></span> Ве молиме, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">прочитајте ги општоприфатените правила</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> Por favor, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">leia as convenções</a>.</div>
<div class="description mw-content-ltr ru" dir="ltr" lang="ru"><span class="language ru" title="Russian"><b>Русский&#58; </b></span> Пожалуйста, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">прочитайте соглашения</a>.</div>
<div class="description mw-content-ltr tl" dir="ltr" lang="tl"><span class="language tl" title="Tagalog"><b>Tagalog&#58; </b></span> Paki-<a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">basa ang mga kumbensyon</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> Будь ласка, <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">прочитайте конвенції</a>.</div>
<div class="description mw-content-ltr vi" dir="ltr" lang="vi"><span class="language vi" title="Vietnamese"><b>Tiếng Việt&#58; </b></span> Hãy <a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" class="extiw" title="w:Wikipedia:WikiProject Maps/Conventions/Orthographic maps">đọc công văn</a> trước khi đăng.</div>
<div style="clear:both;"></div>
<table class="mw-collapsible mw-collapsed" style="clear:both;margin:2px auto;background:#FFF;color:#222;border:1px solid #AAA;padding:1px;width:100%">

<tbody><tr>
<th scope="col" style="font-size:88%;background:#F0F2F5;border:none;color:#000;padding:0 .2em;text-align:center">World maps
</th></tr>
<tr>
<td class="mw-collapsible-content" style="font-size:88%;border:none;padding:0;">== Africa==
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%85%E0%A4%AB%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%95%E0%A4%BE" class="extiw" title="hi:अफ्रीका">अफ्रीका</a></div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%90%E1%83%A4%E1%83%A0%E1%83%98%E1%83%99%E1%83%90" class="extiw" title="ka:აფრიკა">აფრიკა</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Africa_(orthographic_projection).svg" class="mw-file-description" title="Africa"><img alt="Africa" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Africa_%28orthographic_projection%29.svg/80px-Africa_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Africa_%28orthographic_projection%29.svg/120px-Africa_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Africa_%28orthographic_projection%29.svg/160px-Africa_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Africa
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="Eastern_Africa">Eastern Africa</span></h3>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A5%80_%E0%A4%85%E0%A4%AB%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%95%E0%A4%BE" class="extiw" title="hi:पूर्वी अफ्रीका">पूर्वी अफ्रीका</a></div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Burundi_(orthographic_projection).svg" class="mw-file-description" title="Burundi"><img alt="Burundi" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Burundi_%28orthographic_projection%29.svg/80px-Burundi_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Burundi_%28orthographic_projection%29.svg/120px-Burundi_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Burundi_%28orthographic_projection%29.svg/160px-Burundi_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Burundi
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Comoros_(orthographic_projection).svg" class="mw-file-description" title="Comoros"><img alt="Comoros" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Comoros_%28orthographic_projection%29.svg/80px-Comoros_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Comoros_%28orthographic_projection%29.svg/120px-Comoros_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Comoros_%28orthographic_projection%29.svg/160px-Comoros_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Comoros
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Djibouti_(orthographic_projection).svg" class="mw-file-description" title="Djibouti"><img alt="Djibouti" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Djibouti_%28orthographic_projection%29.svg/80px-Djibouti_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Djibouti_%28orthographic_projection%29.svg/120px-Djibouti_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Djibouti_%28orthographic_projection%29.svg/160px-Djibouti_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Djibouti
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Eritrea_(Africa_orthographic_projection).svg" class="mw-file-description" title="Eritrea"><img alt="Eritrea" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Eritrea_%28Africa_orthographic_projection%29.svg/80px-Eritrea_%28Africa_orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Eritrea_%28Africa_orthographic_projection%29.svg/120px-Eritrea_%28Africa_orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Eritrea_%28Africa_orthographic_projection%29.svg/160px-Eritrea_%28Africa_orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Eritrea
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Ethiopia_(Africa_orthographic_projection).svg" class="mw-file-description" title="Ethiopia"><img alt="Ethiopia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Ethiopia_%28Africa_orthographic_projection%29.svg/80px-Ethiopia_%28Africa_orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Ethiopia_%28Africa_orthographic_projection%29.svg/120px-Ethiopia_%28Africa_orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Ethiopia_%28Africa_orthographic_projection%29.svg/160px-Ethiopia_%28Africa_orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Ethiopia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Kenya_(orthographic_projection).svg" class="mw-file-description" title="Kenya"><img alt="Kenya" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Kenya_%28orthographic_projection%29.svg/80px-Kenya_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Kenya_%28orthographic_projection%29.svg/120px-Kenya_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Kenya_%28orthographic_projection%29.svg/160px-Kenya_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Kenya
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Madagascar_(orthographic_projection).svg" class="mw-file-description" title="Madagascar"><img alt="Madagascar" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Madagascar_%28orthographic_projection%29.svg/80px-Madagascar_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Madagascar_%28orthographic_projection%29.svg/120px-Madagascar_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Madagascar_%28orthographic_projection%29.svg/160px-Madagascar_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Madagascar
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Malawi_(orthographic_projection).svg" class="mw-file-description" title="Malawi"><img alt="Malawi" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Malawi_%28orthographic_projection%29.svg/80px-Malawi_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Malawi_%28orthographic_projection%29.svg/120px-Malawi_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Malawi_%28orthographic_projection%29.svg/160px-Malawi_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Malawi
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mauritius_(orthographic_projection).svg" class="mw-file-description" title="Mauritius"><img alt="Mauritius" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Mauritius_%28orthographic_projection%29.svg/80px-Mauritius_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Mauritius_%28orthographic_projection%29.svg/120px-Mauritius_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Mauritius_%28orthographic_projection%29.svg/160px-Mauritius_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Mauritius
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mayotte_(orthographic_projection).svg" class="mw-file-description" title="Mayotte"><img alt="Mayotte" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Mayotte_%28orthographic_projection%29.svg/80px-Mayotte_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Mayotte_%28orthographic_projection%29.svg/120px-Mayotte_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Mayotte_%28orthographic_projection%29.svg/160px-Mayotte_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Mayotte
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mozambique_(orthographic_projection).svg" class="mw-file-description" title="Mozambique"><img alt="Mozambique" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Mozambique_%28orthographic_projection%29.svg/80px-Mozambique_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Mozambique_%28orthographic_projection%29.svg/120px-Mozambique_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Mozambique_%28orthographic_projection%29.svg/160px-Mozambique_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Mozambique
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Tanzania_(orthographic_projection).svg" class="mw-file-description" title="Tanzania"><img alt="Tanzania" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Tanzania_%28orthographic_projection%29.svg/80px-Tanzania_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Tanzania_%28orthographic_projection%29.svg/120px-Tanzania_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Tanzania_%28orthographic_projection%29.svg/160px-Tanzania_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Tanzania
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Somalia_(orthographic_projection).svg" class="mw-file-description" title="Somalia"><img alt="Somalia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Somalia_%28orthographic_projection%29.svg/80px-Somalia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Somalia_%28orthographic_projection%29.svg/120px-Somalia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Somalia_%28orthographic_projection%29.svg/160px-Somalia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Somalia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Uganda_(orthographic_projection).svg" class="mw-file-description" title="Uganda"><img alt="Uganda" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Uganda_%28orthographic_projection%29.svg/80px-Uganda_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Uganda_%28orthographic_projection%29.svg/120px-Uganda_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Uganda_%28orthographic_projection%29.svg/160px-Uganda_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Uganda
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="Southern_Africa">Southern Africa</span></h3>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Lesotho_(orthographic_projection).svg" class="mw-file-description" title="Lesotho"><img alt="Lesotho" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Lesotho_%28orthographic_projection%29.svg/80px-Lesotho_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Lesotho_%28orthographic_projection%29.svg/120px-Lesotho_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Lesotho_%28orthographic_projection%29.svg/160px-Lesotho_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Lesotho
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:South_Africa_(orthographic_projection).svg" class="mw-file-description" title="South Africa"><img alt="South Africa" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/South_Africa_%28orthographic_projection%29.svg/80px-South_Africa_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/South_Africa_%28orthographic_projection%29.svg/120px-South_Africa_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/South_Africa_%28orthographic_projection%29.svg/160px-South_Africa_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>South Africa
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Zambia_(orthographic_projection).svg" class="mw-file-description" title="Zambia"><img alt="Zambia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Zambia_%28orthographic_projection%29.svg/80px-Zambia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Zambia_%28orthographic_projection%29.svg/120px-Zambia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Zambia_%28orthographic_projection%29.svg/160px-Zambia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Zambia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Zimbabwe_(orthographic_projection).svg" class="mw-file-description" title="Zimbabwe"><img alt="Zimbabwe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Zimbabwe_%28orthographic_projection%29.svg/80px-Zimbabwe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Zimbabwe_%28orthographic_projection%29.svg/120px-Zimbabwe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Zimbabwe_%28orthographic_projection%29.svg/160px-Zimbabwe_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Zimbabwe
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="Central_Africa">Central Africa</span></h3>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Angola_(orthographic_projection).svg" class="mw-file-description" title="Angola"><img alt="Angola" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Angola_%28orthographic_projection%29.svg/80px-Angola_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Angola_%28orthographic_projection%29.svg/120px-Angola_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Angola_%28orthographic_projection%29.svg/160px-Angola_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Angola
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Cameroon_(orthographic_projection).svg" class="mw-file-description" title="Cameroon"><img alt="Cameroon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Cameroon_%28orthographic_projection%29.svg/80px-Cameroon_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Cameroon_%28orthographic_projection%29.svg/120px-Cameroon_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Cameroon_%28orthographic_projection%29.svg/160px-Cameroon_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Cameroon
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Central_African_Republic_(orthographic_projection).svg" class="mw-file-description" title="Central African Republic"><img alt="Central African Republic" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Central_African_Republic_%28orthographic_projection%29.svg/80px-Central_African_Republic_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Central_African_Republic_%28orthographic_projection%29.svg/120px-Central_African_Republic_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Central_African_Republic_%28orthographic_projection%29.svg/160px-Central_African_Republic_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Central African Republic
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Chad_(orthographic_projection).svg" class="mw-file-description" title="Chad"><img alt="Chad" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Chad_%28orthographic_projection%29.svg/80px-Chad_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Chad_%28orthographic_projection%29.svg/120px-Chad_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Chad_%28orthographic_projection%29.svg/160px-Chad_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Chad
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Republic_of_the_Congo_(orthographic_projection).svg" class="mw-file-description" title="Republic of the Congo"><img alt="Republic of the Congo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Republic_of_the_Congo_%28orthographic_projection%29.svg/80px-Republic_of_the_Congo_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Republic_of_the_Congo_%28orthographic_projection%29.svg/120px-Republic_of_the_Congo_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Republic_of_the_Congo_%28orthographic_projection%29.svg/160px-Republic_of_the_Congo_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Republic of the Congo
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Democratic_Republic_of_the_Congo_(orthographic_projection).svg" class="mw-file-description" title="Democratic Republic of the Congo"><img alt="Democratic Republic of the Congo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Democratic_Republic_of_the_Congo_%28orthographic_projection%29.svg/80px-Democratic_Republic_of_the_Congo_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Democratic_Republic_of_the_Congo_%28orthographic_projection%29.svg/120px-Democratic_Republic_of_the_Congo_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Democratic_Republic_of_the_Congo_%28orthographic_projection%29.svg/160px-Democratic_Republic_of_the_Congo_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Democratic Republic of the Congo
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Gabon_(orthographic_projection).svg" class="mw-file-description" title="Gabon"><img alt="Gabon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Gabon_%28orthographic_projection%29.svg/80px-Gabon_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Gabon_%28orthographic_projection%29.svg/120px-Gabon_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Gabon_%28orthographic_projection%29.svg/160px-Gabon_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Gabon
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:South_Sudan_(orthographic_projection).svg" class="mw-file-description" title="South Sudan"><img alt="South Sudan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/South_Sudan_%28orthographic_projection%29.svg/80px-South_Sudan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/South_Sudan_%28orthographic_projection%29.svg/120px-South_Sudan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/South_Sudan_%28orthographic_projection%29.svg/160px-South_Sudan_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>South Sudan
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="Northern_Africa">Northern Africa</span></h3>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Algeria_(orthographic_projection).svg" class="mw-file-description" title="Algeria"><img alt="Algeria" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Algeria_%28orthographic_projection%29.svg/80px-Algeria_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Algeria_%28orthographic_projection%29.svg/120px-Algeria_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Algeria_%28orthographic_projection%29.svg/160px-Algeria_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Algeria
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Egypt_(orthographic_projection).svg" class="mw-file-description" title="Egypt"><img alt="Egypt" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Egypt_%28orthographic_projection%29.svg/80px-Egypt_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Egypt_%28orthographic_projection%29.svg/120px-Egypt_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Egypt_%28orthographic_projection%29.svg/160px-Egypt_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Egypt
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Libya_(Libya_centered;_orthographic_projection).svg" class="mw-file-description" title="Libya"><img alt="Libya" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Libya_%28Libya_centered%3B_orthographic_projection%29.svg/80px-Libya_%28Libya_centered%3B_orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Libya_%28Libya_centered%3B_orthographic_projection%29.svg/120px-Libya_%28Libya_centered%3B_orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Libya_%28Libya_centered%3B_orthographic_projection%29.svg/160px-Libya_%28Libya_centered%3B_orthographic_projection%29.svg.png 2x" data-file-width="501" data-file-height="501" /></a></span></div>
			<div class="gallerytext">
<p>Libya
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Morocco_(orthographic_projection,_WS_claimed).svg" class="mw-file-description" title="Morocco"><img alt="Morocco" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Morocco_%28orthographic_projection%2C_WS_claimed%29.svg/80px-Morocco_%28orthographic_projection%2C_WS_claimed%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Morocco_%28orthographic_projection%2C_WS_claimed%29.svg/120px-Morocco_%28orthographic_projection%2C_WS_claimed%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Morocco_%28orthographic_projection%2C_WS_claimed%29.svg/160px-Morocco_%28orthographic_projection%2C_WS_claimed%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Morocco
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Morocco_WS-included_(orthographic_projection).svg" class="mw-file-description" title="Morocco &amp; Western Sahara"><img alt="Morocco &amp; Western Sahara" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Morocco_WS-included_%28orthographic_projection%29.svg/80px-Morocco_WS-included_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Morocco_WS-included_%28orthographic_projection%29.svg/120px-Morocco_WS-included_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Morocco_WS-included_%28orthographic_projection%29.svg/160px-Morocco_WS-included_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Morocco &amp; Western Sahara
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Sahrawi_Arab_Democratic_Republic_(orthographic_projection).svg" class="mw-file-description" title="Sahrawri Arab Democratic Republic"><img alt="Sahrawri Arab Democratic Republic" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Sahrawi_Arab_Democratic_Republic_%28orthographic_projection%29.svg/80px-Sahrawi_Arab_Democratic_Republic_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Sahrawi_Arab_Democratic_Republic_%28orthographic_projection%29.svg/120px-Sahrawi_Arab_Democratic_Republic_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Sahrawi_Arab_Democratic_Republic_%28orthographic_projection%29.svg/160px-Sahrawi_Arab_Democratic_Republic_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Sahrawri Arab Democratic Republic
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Sudan_(orthographic_projection).svg" class="mw-file-description" title="Sudan"><img alt="Sudan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Sudan_%28orthographic_projection%29.svg/80px-Sudan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Sudan_%28orthographic_projection%29.svg/120px-Sudan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Sudan_%28orthographic_projection%29.svg/160px-Sudan_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Sudan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Tunisia_(orthographic_projection).svg" class="mw-file-description" title="Tunisia"><img alt="Tunisia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Tunisia_%28orthographic_projection%29.svg/80px-Tunisia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Tunisia_%28orthographic_projection%29.svg/120px-Tunisia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Tunisia_%28orthographic_projection%29.svg/160px-Tunisia_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Tunisia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Western_Sahara_(orthographic_projection).svg" class="mw-file-description" title="Western Sahara"><img alt="Western Sahara" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Western_Sahara_%28orthographic_projection%29.svg/80px-Western_Sahara_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Western_Sahara_%28orthographic_projection%29.svg/120px-Western_Sahara_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Western_Sahara_%28orthographic_projection%29.svg/160px-Western_Sahara_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Western Sahara
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="Western_Africa">Western Africa</span></h3>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Azawad_(orthographic_projection).svg" class="mw-file-description" title="Azawad"><img alt="Azawad" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Azawad_%28orthographic_projection%29.svg/80px-Azawad_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Azawad_%28orthographic_projection%29.svg/120px-Azawad_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Azawad_%28orthographic_projection%29.svg/160px-Azawad_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Azawad
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Benin_(orthographic_projection_with_inset).svg" class="mw-file-description" title="Benin"><img alt="Benin" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Benin_%28orthographic_projection_with_inset%29.svg/80px-Benin_%28orthographic_projection_with_inset%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Benin_%28orthographic_projection_with_inset%29.svg/120px-Benin_%28orthographic_projection_with_inset%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Benin_%28orthographic_projection_with_inset%29.svg/160px-Benin_%28orthographic_projection_with_inset%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Benin
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Burkina_Faso_(orthographic_projection).svg" class="mw-file-description" title="Burkina Faso"><img alt="Burkina Faso" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Burkina_Faso_%28orthographic_projection%29.svg/80px-Burkina_Faso_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Burkina_Faso_%28orthographic_projection%29.svg/120px-Burkina_Faso_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Burkina_Faso_%28orthographic_projection%29.svg/160px-Burkina_Faso_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Burkina Faso
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Cape_Verde_(orthographic_projection).svg" class="mw-file-description" title="Cape Verde"><img alt="Cape Verde" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Cape_Verde_%28orthographic_projection%29.svg/80px-Cape_Verde_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Cape_Verde_%28orthographic_projection%29.svg/120px-Cape_Verde_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Cape_Verde_%28orthographic_projection%29.svg/160px-Cape_Verde_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Cape Verde
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:C%C3%B4te_d%27Ivoire_(orthographic_projection).svg" class="mw-file-description" title="Côte d&#39;Ivoire"><img alt="Côte d&#39;Ivoire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/C%C3%B4te_d%27Ivoire_%28orthographic_projection%29.svg/80px-C%C3%B4te_d%27Ivoire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/C%C3%B4te_d%27Ivoire_%28orthographic_projection%29.svg/120px-C%C3%B4te_d%27Ivoire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/C%C3%B4te_d%27Ivoire_%28orthographic_projection%29.svg/160px-C%C3%B4te_d%27Ivoire_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Côte d'Ivoire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Gambia_(orthographic_projection_with_inset).svg" class="mw-file-description" title="Gambia"><img alt="Gambia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Gambia_%28orthographic_projection_with_inset%29.svg/80px-Gambia_%28orthographic_projection_with_inset%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Gambia_%28orthographic_projection_with_inset%29.svg/120px-Gambia_%28orthographic_projection_with_inset%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Gambia_%28orthographic_projection_with_inset%29.svg/160px-Gambia_%28orthographic_projection_with_inset%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Gambia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Ghana_(orthographic_projection).svg" class="mw-file-description" title="Ghana"><img alt="Ghana" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Ghana_%28orthographic_projection%29.svg/80px-Ghana_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Ghana_%28orthographic_projection%29.svg/120px-Ghana_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Ghana_%28orthographic_projection%29.svg/160px-Ghana_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Ghana
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Guinea_(orthographic_projection).svg" class="mw-file-description" title="Guinea"><img alt="Guinea" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Guinea_%28orthographic_projection%29.svg/80px-Guinea_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Guinea_%28orthographic_projection%29.svg/120px-Guinea_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Guinea_%28orthographic_projection%29.svg/160px-Guinea_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Guinea
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Liberia_(orthographic_projection).svg" class="mw-file-description" title="Liberia"><img alt="Liberia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Liberia_%28orthographic_projection%29.svg/80px-Liberia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Liberia_%28orthographic_projection%29.svg/120px-Liberia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Liberia_%28orthographic_projection%29.svg/160px-Liberia_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Liberia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mali_(orthographic_projection).svg" class="mw-file-description" title="Mali"><img alt="Mali" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Mali_%28orthographic_projection%29.svg/80px-Mali_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Mali_%28orthographic_projection%29.svg/120px-Mali_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Mali_%28orthographic_projection%29.svg/160px-Mali_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Mali
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mali_de_iure_(orthographic_projection).svg" class="mw-file-description" title="Mali without Azawad"><img alt="Mali without Azawad" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Mali_de_iure_%28orthographic_projection%29.svg/80px-Mali_de_iure_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Mali_de_iure_%28orthographic_projection%29.svg/120px-Mali_de_iure_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Mali_de_iure_%28orthographic_projection%29.svg/160px-Mali_de_iure_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Mali without Azawad
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mauritania_(orthographic_projection).svg" class="mw-file-description" title="Mauritania"><img alt="Mauritania" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Mauritania_%28orthographic_projection%29.svg/80px-Mauritania_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Mauritania_%28orthographic_projection%29.svg/120px-Mauritania_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Mauritania_%28orthographic_projection%29.svg/160px-Mauritania_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Mauritania
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Niger_(orthographic_projection).svg" class="mw-file-description" title="Niger"><img alt="Niger" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Niger_%28orthographic_projection%29.svg/80px-Niger_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Niger_%28orthographic_projection%29.svg/120px-Niger_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Niger_%28orthographic_projection%29.svg/160px-Niger_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Niger
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Nigeria_(orthographic_projection).svg" class="mw-file-description" title="Nigeria"><img alt="Nigeria" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Nigeria_%28orthographic_projection%29.svg/80px-Nigeria_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Nigeria_%28orthographic_projection%29.svg/120px-Nigeria_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Nigeria_%28orthographic_projection%29.svg/160px-Nigeria_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Nigeria
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Senegal_(orthographic_projection).svg" class="mw-file-description" title="Senegal"><img alt="Senegal" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Senegal_%28orthographic_projection%29.svg/80px-Senegal_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Senegal_%28orthographic_projection%29.svg/120px-Senegal_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Senegal_%28orthographic_projection%29.svg/160px-Senegal_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Senegal
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Sierra_Leone_(orthographic_projection).svg" class="mw-file-description" title="Sierra Leone"><img alt="Sierra Leone" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Sierra_Leone_%28orthographic_projection%29.svg/80px-Sierra_Leone_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Sierra_Leone_%28orthographic_projection%29.svg/120px-Sierra_Leone_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Sierra_Leone_%28orthographic_projection%29.svg/160px-Sierra_Leone_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Sierra Leone
</p>
			</div>
		</li>
</ul>
<h2><span class="mw-headline" id="Americas">Americas</span></h2>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%90%E1%83%9B%E1%83%94%E1%83%A0%E1%83%98%E1%83%99%E1%83%90" class="extiw" title="ka:ამერიკა">ამერიკა</a>.</div>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%85%E0%A4%AE%E0%A5%87%E0%A4%B0%E0%A4%BF%E0%A4%95%E0%A4%BE" class="extiw" title="hi:अमेरिका">अमेरिका</a></div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Americas_(orthographic_projection).svg" class="mw-file-description" title="Americas"><img alt="Americas" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Americas_%28orthographic_projection%29.svg/80px-Americas_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Americas_%28orthographic_projection%29.svg/120px-Americas_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Americas_%28orthographic_projection%29.svg/160px-Americas_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Americas
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Northern_America_(orthographic_projection).svg" class="mw-file-description" title="Northern North America"><img alt="Northern North America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Northern_America_%28orthographic_projection%29.svg/80px-Northern_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Northern_America_%28orthographic_projection%29.svg/120px-Northern_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Northern_America_%28orthographic_projection%29.svg/160px-Northern_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Northern North America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:North_America_(orthographic_projection).svg" class="mw-file-description" title="North America"><img alt="North America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/North_America_%28orthographic_projection%29.svg/80px-North_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/North_America_%28orthographic_projection%29.svg/120px-North_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/North_America_%28orthographic_projection%29.svg/160px-North_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>North America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Central_America_(orthographic_projection).svg" class="mw-file-description" title="Central America"><img alt="Central America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Central_America_%28orthographic_projection%29.svg/80px-Central_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Central_America_%28orthographic_projection%29.svg/120px-Central_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Central_America_%28orthographic_projection%29.svg/160px-Central_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Central America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:South_America_(orthographic_projection).svg" class="mw-file-description" title="South America"><img alt="South America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/South_America_%28orthographic_projection%29.svg/80px-South_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/South_America_%28orthographic_projection%29.svg/120px-South_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/South_America_%28orthographic_projection%29.svg/160px-South_America_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>South America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Southern_America_(orthographic_projection).svg" class="mw-file-description" title="Southern South America"><img alt="Southern South America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Southern_America_%28orthographic_projection%29.svg/80px-Southern_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Southern_America_%28orthographic_projection%29.svg/120px-Southern_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Southern_America_%28orthographic_projection%29.svg/160px-Southern_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Southern South America
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="North_America">North America</span></h3>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%89%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%B0%E0%A5%80_%E0%A4%85%E0%A4%AE%E0%A5%87%E0%A4%B0%E0%A4%BF%E0%A4%95%E0%A4%BE" class="extiw" title="hi:उत्तरी अमेरिका">उत्तरी अमेरिका</a></div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Greenland_(orthographic_projection).svg" class="mw-file-description" title="Greenland"><img alt="Greenland" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Greenland_%28orthographic_projection%29.svg/80px-Greenland_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Greenland_%28orthographic_projection%29.svg/120px-Greenland_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Greenland_%28orthographic_projection%29.svg/160px-Greenland_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Greenland
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Canada_(orthographic_projection).svg" class="mw-file-description" title="Canada"><img alt="Canada" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Canada_%28orthographic_projection%29.svg/80px-Canada_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Canada_%28orthographic_projection%29.svg/120px-Canada_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Canada_%28orthographic_projection%29.svg/160px-Canada_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Canada
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:United_States_(orthographic_projection).svg" class="mw-file-description" title="United States of America"><img alt="United States of America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/United_States_%28orthographic_projection%29.svg/80px-United_States_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/United_States_%28orthographic_projection%29.svg/120px-United_States_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/United_States_%28orthographic_projection%29.svg/160px-United_States_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>United States of America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mexico_(orthographic_projection).svg" class="mw-file-description" title="Mexico"><img alt="Mexico" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Mexico_%28orthographic_projection%29.svg/80px-Mexico_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Mexico_%28orthographic_projection%29.svg/120px-Mexico_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Mexico_%28orthographic_projection%29.svg/160px-Mexico_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Mexico
</p>
			</div>
		</li>
</ul>
<h4><span class="mw-headline" id="Central_America">Central America</span></h4>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Guatemala_(orthographic_projection).svg" class="mw-file-description" title="Guatemala"><img alt="Guatemala" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Guatemala_%28orthographic_projection%29.svg/80px-Guatemala_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Guatemala_%28orthographic_projection%29.svg/120px-Guatemala_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Guatemala_%28orthographic_projection%29.svg/160px-Guatemala_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Guatemala
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:El_Salvador_(orthographic_projection).svg" class="mw-file-description" title="El Salvador"><img alt="El Salvador" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/El_Salvador_%28orthographic_projection%29.svg/80px-El_Salvador_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/El_Salvador_%28orthographic_projection%29.svg/120px-El_Salvador_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/El_Salvador_%28orthographic_projection%29.svg/160px-El_Salvador_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>El Salvador
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Honduras_(orthographic_projection).svg" class="mw-file-description" title="Honduras"><img alt="Honduras" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Honduras_%28orthographic_projection%29.svg/80px-Honduras_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Honduras_%28orthographic_projection%29.svg/120px-Honduras_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Honduras_%28orthographic_projection%29.svg/160px-Honduras_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Honduras
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Nicaragua_(orthographic_projection).svg" class="mw-file-description" title="Nicaragua"><img alt="Nicaragua" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Nicaragua_%28orthographic_projection%29.svg/80px-Nicaragua_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Nicaragua_%28orthographic_projection%29.svg/120px-Nicaragua_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Nicaragua_%28orthographic_projection%29.svg/160px-Nicaragua_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Nicaragua
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Costa_Rica_(orthographic_projection).svg" class="mw-file-description" title="Costa Rica"><img alt="Costa Rica" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Costa_Rica_%28orthographic_projection%29.svg/80px-Costa_Rica_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Costa_Rica_%28orthographic_projection%29.svg/120px-Costa_Rica_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Costa_Rica_%28orthographic_projection%29.svg/160px-Costa_Rica_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Costa Rica
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Panama_(orthographic_projection).svg" class="mw-file-description" title="Panama"><img alt="Panama" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Panama_%28orthographic_projection%29.svg/80px-Panama_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Panama_%28orthographic_projection%29.svg/120px-Panama_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Panama_%28orthographic_projection%29.svg/160px-Panama_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Panama
</p>
			</div>
		</li>
</ul>
<h4><span class="mw-headline" id="Caribbean">Caribbean</span></h4>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Trinidad_and_Tobago_(orthographic_projection).svg" class="mw-file-description" title="Trinidad and Tobago"><img alt="Trinidad and Tobago" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Trinidad_and_Tobago_%28orthographic_projection%29.svg/80px-Trinidad_and_Tobago_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Trinidad_and_Tobago_%28orthographic_projection%29.svg/120px-Trinidad_and_Tobago_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Trinidad_and_Tobago_%28orthographic_projection%29.svg/160px-Trinidad_and_Tobago_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Trinidad and Tobago
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Cuba_(orthographic_projection).svg" class="mw-file-description" title="Cuba"><img alt="Cuba" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Cuba_%28orthographic_projection%29.svg/80px-Cuba_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Cuba_%28orthographic_projection%29.svg/120px-Cuba_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Cuba_%28orthographic_projection%29.svg/160px-Cuba_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Cuba
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Dominican_Republic_(orthographic_projection).svg" class="mw-file-description" title="Dominican Republic"><img alt="Dominican Republic" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Dominican_Republic_%28orthographic_projection%29.svg/80px-Dominican_Republic_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Dominican_Republic_%28orthographic_projection%29.svg/120px-Dominican_Republic_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Dominican_Republic_%28orthographic_projection%29.svg/160px-Dominican_Republic_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Dominican Republic
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Haiti_(orthographic_projection).svg" class="mw-file-description" title="Haiti"><img alt="Haiti" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Haiti_%28orthographic_projection%29.svg/80px-Haiti_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Haiti_%28orthographic_projection%29.svg/120px-Haiti_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Haiti_%28orthographic_projection%29.svg/160px-Haiti_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Haiti
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Jamaica_(orthographic_projection).svg" class="mw-file-description" title="Jamaica"><img alt="Jamaica" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Jamaica_%28orthographic_projection%29.svg/80px-Jamaica_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Jamaica_%28orthographic_projection%29.svg/120px-Jamaica_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Jamaica_%28orthographic_projection%29.svg/160px-Jamaica_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Jamaica
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="South_America">South America</span></h3>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%A6%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BF%E0%A4%A3_%E0%A4%85%E0%A4%AE%E0%A5%87%E0%A4%B0%E0%A4%BF%E0%A4%95%E0%A4%BE" class="extiw" title="hi:दक्षिण अमेरिका">दक्षिण अमेरिका</a></div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Argentina_orthographic.svg" class="mw-file-description" title="Argentina"><img alt="Argentina" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Argentina_orthographic.svg/80px-Argentina_orthographic.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Argentina_orthographic.svg/120px-Argentina_orthographic.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Argentina_orthographic.svg/160px-Argentina_orthographic.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Argentina
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Bolivia_(orthographic_projection).svg" class="mw-file-description" title="Bolivia"><img alt="Bolivia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Bolivia_%28orthographic_projection%29.svg/80px-Bolivia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Bolivia_%28orthographic_projection%29.svg/120px-Bolivia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Bolivia_%28orthographic_projection%29.svg/160px-Bolivia_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Bolivia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:BRA_orthographic.svg" class="mw-file-description" title="Brazil"><img alt="Brazil" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/BRA_orthographic.svg/80px-BRA_orthographic.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/BRA_orthographic.svg/120px-BRA_orthographic.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/BRA_orthographic.svg/160px-BRA_orthographic.svg.png 2x" data-file-width="551" data-file-height="551" /></a></span></div>
			<div class="gallerytext">
<p>Brazil
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Chile_(orthographic_projection).svg" class="mw-file-description" title="Chile"><img alt="Chile" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Chile_%28orthographic_projection%29.svg/80px-Chile_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Chile_%28orthographic_projection%29.svg/120px-Chile_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Chile_%28orthographic_projection%29.svg/160px-Chile_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Chile
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:COL_orthographic.svg" class="mw-file-description" title="Colombia"><img alt="Colombia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/COL_orthographic.svg/80px-COL_orthographic.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/COL_orthographic.svg/120px-COL_orthographic.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/COL_orthographic.svg/160px-COL_orthographic.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Colombia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Ecuador_(orthographic_projection).svg" class="mw-file-description" title="Ecuador"><img alt="Ecuador" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Ecuador_%28orthographic_projection%29.svg/80px-Ecuador_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Ecuador_%28orthographic_projection%29.svg/120px-Ecuador_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Ecuador_%28orthographic_projection%29.svg/160px-Ecuador_%28orthographic_projection%29.svg.png 2x" data-file-width="512" data-file-height="512" /></a></span></div>
			<div class="gallerytext">
<p>Ecuador
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:French_Guiana_(orthographic_projection).svg" class="mw-file-description" title="French Guiana"><img alt="French Guiana" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/French_Guiana_%28orthographic_projection%29.svg/80px-French_Guiana_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/French_Guiana_%28orthographic_projection%29.svg/120px-French_Guiana_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/French_Guiana_%28orthographic_projection%29.svg/160px-French_Guiana_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>French Guiana
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Guyana_(orthographic_projection).svg" class="mw-file-description" title="Guyana"><img alt="Guyana" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Guyana_%28orthographic_projection%29.svg/80px-Guyana_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Guyana_%28orthographic_projection%29.svg/120px-Guyana_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Guyana_%28orthographic_projection%29.svg/160px-Guyana_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Guyana
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Paraguay_(orthographic_projection).svg" class="mw-file-description" title="Paraguay"><img alt="Paraguay" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Paraguay_%28orthographic_projection%29.svg/80px-Paraguay_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Paraguay_%28orthographic_projection%29.svg/120px-Paraguay_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Paraguay_%28orthographic_projection%29.svg/160px-Paraguay_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Paraguay
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Peru_(orthographic_projection).svg" class="mw-file-description" title="Peru"><img alt="Peru" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Peru_%28orthographic_projection%29.svg/80px-Peru_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Peru_%28orthographic_projection%29.svg/120px-Peru_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Peru_%28orthographic_projection%29.svg/160px-Peru_%28orthographic_projection%29.svg.png 2x" data-file-width="549" data-file-height="549" /></a></span></div>
			<div class="gallerytext">
<p>Peru
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Suriname_(orthographic_projection).svg" class="mw-file-description" title="Suriname"><img alt="Suriname" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Suriname_%28orthographic_projection%29.svg/80px-Suriname_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Suriname_%28orthographic_projection%29.svg/120px-Suriname_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Suriname_%28orthographic_projection%29.svg/160px-Suriname_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Suriname
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Uruguay_(orthographic_projection).svg" class="mw-file-description" title="Uruguay"><img alt="Uruguay" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Uruguay_%28orthographic_projection%29.svg/80px-Uruguay_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Uruguay_%28orthographic_projection%29.svg/120px-Uruguay_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Uruguay_%28orthographic_projection%29.svg/160px-Uruguay_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Uruguay
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:VEN_orthographic.svg" class="mw-file-description" title="Venezuela"><img alt="Venezuela" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/VEN_orthographic.svg/80px-VEN_orthographic.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/VEN_orthographic.svg/120px-VEN_orthographic.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/VEN_orthographic.svg/160px-VEN_orthographic.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>Venezuela
</p>
			</div>
		</li>
</ul>
<h2><span class="mw-headline" id="Asia">Asia</span></h2>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%8F%E0%A4%B6%E0%A4%BF%E0%A4%AF%E0%A4%BE" class="extiw" title="hi:एशिया">एशिया (जम्भूद्वीप)</a></div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%90%E1%83%96%E1%83%98%E1%83%90" class="extiw" title="ka:აზია">აზია</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/%C3%81sia" class="extiw" title="pt:Ásia">Ásia</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://uk.wikipedia.org/wiki/%D0%90%D0%B7%D1%96%D1%8F" class="extiw" title="uk:Азія">Азія</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Asia_(orthographic_projection).svg" class="mw-file-description" title="&quot;Asia (orthographic projection).svg&quot;, frequently subject to lame edit wars over the Caucasus boundary"><img alt="&quot;Asia (orthographic projection).svg&quot;, frequently subject to lame edit wars over the Caucasus boundary" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Asia_%28orthographic_projection%29.svg/80px-Asia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Asia_%28orthographic_projection%29.svg/120px-Asia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Asia_%28orthographic_projection%29.svg/160px-Asia_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>"Asia (orthographic projection).svg", frequently subject to lame edit wars over the Caucasus boundary
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="East">East</span></h3>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A5%80_%E0%A4%8F%E0%A4%B6%E0%A4%BF%E0%A4%AF%E0%A4%BE" class="extiw" title="hi:पूर्वी एशिया">पूर्वी एशिया</a></div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%90%E1%83%A6%E1%83%9B%E1%83%9D%E1%83%A1%E1%83%90%E1%83%95%E1%83%9A%E1%83%94%E1%83%97%E1%83%98_%E1%83%90%E1%83%96%E1%83%98%E1%83%90" class="extiw" title="ka:აღმოსავლეთი აზია">აღმოსავლეთი აზია</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/%C3%81sia_Oriental" class="extiw" title="pt:Ásia Oriental">Ásia Oriental</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://uk.wikipedia.org/wiki/%D0%A1%D1%85%D1%96%D0%B4%D0%BD%D0%B0_%D0%90%D0%B7%D1%96%D1%8F" class="extiw" title="uk:Східна Азія">Східна Азія</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:East_Asia_(orthographic_projection).svg" class="mw-file-description" title="East Asia"><img alt="East Asia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/East_Asia_%28orthographic_projection%29.svg/80px-East_Asia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/East_Asia_%28orthographic_projection%29.svg/120px-East_Asia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/East_Asia_%28orthographic_projection%29.svg/160px-East_Asia_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>East Asia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:People%27s_Republic_of_China_(orthographic_projection).svg" class="mw-file-description" title="China"><img alt="China" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/People%27s_Republic_of_China_%28orthographic_projection%29.svg/80px-People%27s_Republic_of_China_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/People%27s_Republic_of_China_%28orthographic_projection%29.svg/120px-People%27s_Republic_of_China_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/People%27s_Republic_of_China_%28orthographic_projection%29.svg/160px-People%27s_Republic_of_China_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>China
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Japan_(orthographic_projection).svg" class="mw-file-description" title="Japan"><img alt="Japan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Japan_%28orthographic_projection%29.svg/80px-Japan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Japan_%28orthographic_projection%29.svg/120px-Japan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Japan_%28orthographic_projection%29.svg/160px-Japan_%28orthographic_projection%29.svg.png 2x" data-file-width="536" data-file-height="536" /></a></span></div>
			<div class="gallerytext">
<p>Japan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mongolia_(orthographic_projection).svg" class="mw-file-description" title="Mongolia"><img alt="Mongolia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Mongolia_%28orthographic_projection%29.svg/80px-Mongolia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Mongolia_%28orthographic_projection%29.svg/120px-Mongolia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Mongolia_%28orthographic_projection%29.svg/160px-Mongolia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Mongolia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:North_Korea_(orthographic_projection).svg" class="mw-file-description" title="North Korea (excluding claimed)"><img alt="North Korea (excluding claimed)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/North_Korea_%28orthographic_projection%29.svg/80px-North_Korea_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/North_Korea_%28orthographic_projection%29.svg/120px-North_Korea_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/North_Korea_%28orthographic_projection%29.svg/160px-North_Korea_%28orthographic_projection%29.svg.png 2x" data-file-width="536" data-file-height="536" /></a></span></div>
			<div class="gallerytext">
<p>North Korea (excluding claimed)
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:South_Korea_(orthographic_projection).svg" class="mw-file-description" title="South Korea (excluding claimed)"><img alt="South Korea (excluding claimed)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/South_Korea_%28orthographic_projection%29.svg/80px-South_Korea_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/South_Korea_%28orthographic_projection%29.svg/120px-South_Korea_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/South_Korea_%28orthographic_projection%29.svg/160px-South_Korea_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>South Korea (excluding claimed)
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Kongsi_location.png" class="mw-file-description" title="Jiangxi"><img alt="Jiangxi" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Kongsi_location.png/80px-Kongsi_location.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Kongsi_location.png/120px-Kongsi_location.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Kongsi_location.png/160px-Kongsi_location.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Jiangxi
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Taiwan_(orthographic_projection;_southeast_Asia_centered).svg" class="mw-file-description" title="Taiwan"><img alt="Taiwan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Taiwan_%28orthographic_projection%3B_southeast_Asia_centered%29.svg/80px-Taiwan_%28orthographic_projection%3B_southeast_Asia_centered%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Taiwan_%28orthographic_projection%3B_southeast_Asia_centered%29.svg/120px-Taiwan_%28orthographic_projection%3B_southeast_Asia_centered%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Taiwan_%28orthographic_projection%3B_southeast_Asia_centered%29.svg/160px-Taiwan_%28orthographic_projection%3B_southeast_Asia_centered%29.svg.png 2x" data-file-width="897" data-file-height="897" /></a></span></div>
			<div class="gallerytext">
<p>Taiwan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Republic_of_China_(orthographic_projection).svg" class="mw-file-description" title="Republic of China (including claimed)"><img alt="Republic of China (including claimed)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Republic_of_China_%28orthographic_projection%29.svg/80px-Republic_of_China_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Republic_of_China_%28orthographic_projection%29.svg/120px-Republic_of_China_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Republic_of_China_%28orthographic_projection%29.svg/160px-Republic_of_China_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Republic of China (including claimed)
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Republic_of_Korea_(orthographic_projection).svg" class="mw-file-description" title="Republic of Korea (including claimed)"><img alt="Republic of Korea (including claimed)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Republic_of_Korea_%28orthographic_projection%29.svg/80px-Republic_of_Korea_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Republic_of_Korea_%28orthographic_projection%29.svg/120px-Republic_of_Korea_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Republic_of_Korea_%28orthographic_projection%29.svg/160px-Republic_of_Korea_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Republic of Korea (including claimed)
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Democratic_People%27s_Republic_of_Korea_(orthographic_projection).svg" class="mw-file-description" title="Democratic People&#39;s Republic of Korea (including claimed)"><img alt="Democratic People&#39;s Republic of Korea (including claimed)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Democratic_People%27s_Republic_of_Korea_%28orthographic_projection%29.svg/80px-Democratic_People%27s_Republic_of_Korea_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Democratic_People%27s_Republic_of_Korea_%28orthographic_projection%29.svg/120px-Democratic_People%27s_Republic_of_Korea_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Democratic_People%27s_Republic_of_Korea_%28orthographic_projection%29.svg/160px-Democratic_People%27s_Republic_of_Korea_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Democratic People's Republic of Korea (including claimed)
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Korea_(orthographic_projection).svg" class="mw-file-description" title="Korea"><img alt="Korea" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Korea_%28orthographic_projection%29.svg/80px-Korea_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Korea_%28orthographic_projection%29.svg/120px-Korea_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Korea_%28orthographic_projection%29.svg/160px-Korea_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Korea
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="Central">Central</span></h3>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%AE%E0%A4%A7%E0%A5%8D%E0%A4%AF_%E0%A4%8F%E0%A4%B6%E0%A4%BF%E0%A4%AF%E0%A4%BE" class="extiw" title="hi:मध्य एशिया">मध्य एशिया</a></div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%AA%E1%83%94%E1%83%9C%E1%83%A2%E1%83%A0%E1%83%90%E1%83%9A%E1%83%A3%E1%83%A0%E1%83%98_%E1%83%90%E1%83%96%E1%83%98%E1%83%90" class="extiw" title="ka:ცენტრალური აზია">ცენტრალური აზია</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/%C3%81sia_Central" class="extiw" title="pt:Ásia Central">Ásia Central</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://uk.wikipedia.org/wiki/%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0_%D0%90%D0%B7%D1%96%D1%8F" class="extiw" title="uk:Центральна Азія">Центральна Азія</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Central_Asia_(orthographic_projection).svg" class="mw-file-description" title="Central Asia"><img alt="Central Asia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Central_Asia_%28orthographic_projection%29.svg/80px-Central_Asia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Central_Asia_%28orthographic_projection%29.svg/120px-Central_Asia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Central_Asia_%28orthographic_projection%29.svg/160px-Central_Asia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Central Asia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Kazakhstan_(orthographic_projection).svg" class="mw-file-description" title="Kazakhstan"><img alt="Kazakhstan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Kazakhstan_%28orthographic_projection%29.svg/80px-Kazakhstan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Kazakhstan_%28orthographic_projection%29.svg/120px-Kazakhstan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Kazakhstan_%28orthographic_projection%29.svg/160px-Kazakhstan_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Kazakhstan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Tajikistan_(orthographic_projection).svg" class="mw-file-description" title="Tajikistan"><img alt="Tajikistan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Tajikistan_%28orthographic_projection%29.svg/80px-Tajikistan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Tajikistan_%28orthographic_projection%29.svg/120px-Tajikistan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Tajikistan_%28orthographic_projection%29.svg/160px-Tajikistan_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Tajikistan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Kyrgyzstan_(orthographic_projection).svg" class="mw-file-description" title="Kyrgyzstan"><img alt="Kyrgyzstan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Kyrgyzstan_%28orthographic_projection%29.svg/80px-Kyrgyzstan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Kyrgyzstan_%28orthographic_projection%29.svg/120px-Kyrgyzstan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Kyrgyzstan_%28orthographic_projection%29.svg/160px-Kyrgyzstan_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Kyrgyzstan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg" class="mw-file-description" title="Uzbekistan"><img alt="Uzbekistan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg/80px-%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg/120px-%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg/160px-%D0%A3%D0%B7%D0%B1%D0%B5%D0%BA%D0%B8%D1%81%D1%82%D0%B0%D0%BD_%D0%BD%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D1%83%D1%81%D0%B5.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Uzbekistan
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="Southeast">Southeast</span></h3>
<div class="description mw-content-ltr fil" dir="ltr" lang="fil"><span class="language fil" title="Filipino"><b>Filipino&#58; </b></span> <a href="https://tl.wikipedia.org/wiki/Timog-silangang_Asya" class="extiw" title="tl:Timog-silangang Asya">Timog-silangang Asya</a>.</div>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%A6%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BF%E0%A4%A3-%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A5%80_%E0%A4%8F%E0%A4%B6%E0%A4%BF%E0%A4%AF%E0%A4%BE" class="extiw" title="hi:दक्षिण-पूर्वी एशिया">दक्षिण-पूर्वी एशिया</a></div>
<div class="description mw-content-ltr id" dir="ltr" lang="id"><span class="language id" title="Indonesian"><b>Bahasa Indonesia&#58; </b></span> <a href="https://id.wikipedia.org/wiki/Asia_tenggara" class="extiw" title="id:Asia tenggara">Asia tenggara</a></div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%A1%E1%83%90%E1%83%9B%E1%83%AE%E1%83%A0%E1%83%94%E1%83%97-%E1%83%90%E1%83%A6%E1%83%9B%E1%83%9D%E1%83%A1%E1%83%90%E1%83%95%E1%83%9A%E1%83%94%E1%83%97%E1%83%98_%E1%83%90%E1%83%96%E1%83%98%E1%83%90" class="extiw" title="ka:სამხრეთ-აღმოსავლეთი აზია">სამხრეთ-აღმოსავლეთი აზია</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/Sudeste_Asi%C3%A1tico" class="extiw" title="pt:Sudeste Asiático">Sudeste Asiático</a>.</div>
<div class="description mw-content-ltr tl" dir="ltr" lang="tl"><span class="language tl" title="Tagalog"><b>Tagalog&#58; </b></span> <a href="https://tl.wikipedia.org/wiki/Timog-silangang_Asya" class="extiw" title="tl:Timog-silangang Asya">Timog-silangang Asya</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://uk.wikipedia.org/wiki/%D0%9F%D1%96%D0%B2%D0%B4%D0%B5%D0%BD%D0%BD%D0%BE-%D0%A1%D1%85%D1%96%D0%B4%D0%BD%D0%B0_%D0%90%D0%B7%D1%96%D1%8F" class="extiw" title="uk:Південно-Східна Азія">Південно-Східна Азія</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Southeast_Asia_(orthographic_projection).svg" class="mw-file-description" title="Southeast Asia"><img alt="Southeast Asia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Southeast_Asia_%28orthographic_projection%29.svg/80px-Southeast_Asia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Southeast_Asia_%28orthographic_projection%29.svg/120px-Southeast_Asia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Southeast_Asia_%28orthographic_projection%29.svg/160px-Southeast_Asia_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="551" /></a></span></div>
			<div class="gallerytext">
<p>Southeast Asia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Association_of_Southeast_Asian_Nations_(orthographic_projection).svg" class="mw-file-description" title="Association of Southeast Asian Nations"><img alt="Association of Southeast Asian Nations" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Association_of_Southeast_Asian_Nations_%28orthographic_projection%29.svg/80px-Association_of_Southeast_Asian_Nations_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Association_of_Southeast_Asian_Nations_%28orthographic_projection%29.svg/120px-Association_of_Southeast_Asian_Nations_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Association_of_Southeast_Asian_Nations_%28orthographic_projection%29.svg/160px-Association_of_Southeast_Asian_Nations_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="551" /></a></span></div>
			<div class="gallerytext">
<p>Association of Southeast Asian Nations
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:The_Philippines_and_ASEAN_(orthographic_projection).svg" class="mw-file-description" title="The Philippines and ASEAN"><img alt="The Philippines and ASEAN" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/The_Philippines_and_ASEAN_%28orthographic_projection%29.svg/80px-The_Philippines_and_ASEAN_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/The_Philippines_and_ASEAN_%28orthographic_projection%29.svg/120px-The_Philippines_and_ASEAN_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/The_Philippines_and_ASEAN_%28orthographic_projection%29.svg/160px-The_Philippines_and_ASEAN_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="551" /></a></span></div>
			<div class="gallerytext">
<p>The Philippines and ASEAN
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Indonesia_(orthographic_projection).svg" class="mw-file-description" title="Indonesia"><img alt="Indonesia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Indonesia_%28orthographic_projection%29.svg/80px-Indonesia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Indonesia_%28orthographic_projection%29.svg/120px-Indonesia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Indonesia_%28orthographic_projection%29.svg/160px-Indonesia_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Indonesia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Malaysia_(orthographic_projection).svg" class="mw-file-description" title="Malaysia"><img alt="Malaysia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Malaysia_%28orthographic_projection%29.svg/80px-Malaysia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Malaysia_%28orthographic_projection%29.svg/120px-Malaysia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Malaysia_%28orthographic_projection%29.svg/160px-Malaysia_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="551" /></a></span></div>
			<div class="gallerytext">
<p>Malaysia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Philippines_(orthographic_projection).svg" class="mw-file-description" title="Philippines"><img alt="Philippines" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Philippines_%28orthographic_projection%29.svg/80px-Philippines_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Philippines_%28orthographic_projection%29.svg/120px-Philippines_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Philippines_%28orthographic_projection%29.svg/160px-Philippines_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Philippines
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Thailand_(orthographic_projection).svg" class="mw-file-description" title="Thailand"><img alt="Thailand" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Thailand_%28orthographic_projection%29.svg/80px-Thailand_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Thailand_%28orthographic_projection%29.svg/120px-Thailand_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Thailand_%28orthographic_projection%29.svg/160px-Thailand_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Thailand
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="South">South</span></h3>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%A6%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BF%E0%A4%A3_%E0%A4%8F%E0%A4%B6%E0%A4%BF%E0%A4%AF%E0%A4%BE" class="extiw" title="hi:दक्षिण एशिया">दक्षिण एशिया</a></div> (भारतीय उपमहाद्वीप)
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%A1%E1%83%90%E1%83%9B%E1%83%AE%E1%83%A0%E1%83%94%E1%83%97%E1%83%98_%E1%83%90%E1%83%96%E1%83%98%E1%83%90" class="extiw" title="ka:სამხრეთი აზია">სამხრეთი აზია</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/Sul_da_%C3%81sia" class="extiw" title="pt:Sul da Ásia">Sul da Ásia</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://uk.wikipedia.org/wiki/%D0%9F%D1%96%D0%B2%D0%B4%D0%B5%D0%BD%D0%BD%D0%B0_%D0%90%D0%B7%D1%96%D1%8F" class="extiw" title="uk:Південна Азія">Південна Азія</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:South_Asia_(orthographic_projection)_without_national_boundaries.svg" class="mw-file-description" title="South Asia"><img alt="South Asia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/South_Asia_%28orthographic_projection%29_without_national_boundaries.svg/80px-South_Asia_%28orthographic_projection%29_without_national_boundaries.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/South_Asia_%28orthographic_projection%29_without_national_boundaries.svg/120px-South_Asia_%28orthographic_projection%29_without_national_boundaries.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/South_Asia_%28orthographic_projection%29_without_national_boundaries.svg/160px-South_Asia_%28orthographic_projection%29_without_national_boundaries.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>South Asia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Afghanistan_(orthographic_projection).svg" class="mw-file-description" title="Afghanistan"><img alt="Afghanistan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Afghanistan_%28orthographic_projection%29.svg/80px-Afghanistan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Afghanistan_%28orthographic_projection%29.svg/120px-Afghanistan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Afghanistan_%28orthographic_projection%29.svg/160px-Afghanistan_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Afghanistan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Bangladesh_(orthographic_projection).svg" class="mw-file-description" title="Bangladesh"><img alt="Bangladesh" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Bangladesh_%28orthographic_projection%29.svg/80px-Bangladesh_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Bangladesh_%28orthographic_projection%29.svg/120px-Bangladesh_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Bangladesh_%28orthographic_projection%29.svg/160px-Bangladesh_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Bangladesh
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Bhutan_(orthographic_projection).svg" class="mw-file-description" title="Bhutan"><img alt="Bhutan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Bhutan_%28orthographic_projection%29.svg/80px-Bhutan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Bhutan_%28orthographic_projection%29.svg/120px-Bhutan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Bhutan_%28orthographic_projection%29.svg/160px-Bhutan_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Bhutan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:India_(orthographic_projection).svg" class="mw-file-description" title="India"><img alt="India" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/India_%28orthographic_projection%29.svg/80px-India_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/India_%28orthographic_projection%29.svg/120px-India_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/India_%28orthographic_projection%29.svg/160px-India_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>India
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Maldives_(orthographic_projection).svg" class="mw-file-description" title="Maldives"><img alt="Maldives" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Maldives_%28orthographic_projection%29.svg/80px-Maldives_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Maldives_%28orthographic_projection%29.svg/120px-Maldives_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Maldives_%28orthographic_projection%29.svg/160px-Maldives_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Maldives
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Nepal_(orthographic_projection).svg" class="mw-file-description" title="Nepal"><img alt="Nepal" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Nepal_%28orthographic_projection%29.svg/80px-Nepal_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Nepal_%28orthographic_projection%29.svg/120px-Nepal_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Nepal_%28orthographic_projection%29.svg/160px-Nepal_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Nepal
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:PAK_orthographic.svg" class="mw-file-description" title="Pakistan"><img alt="Pakistan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/PAK_orthographic.svg/80px-PAK_orthographic.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/PAK_orthographic.svg/120px-PAK_orthographic.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/PAK_orthographic.svg/160px-PAK_orthographic.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Pakistan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Sri_Lanka_(orthographic_projection).svg" class="mw-file-description" title="Sri Lanka"><img alt="Sri Lanka" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Sri_Lanka_%28orthographic_projection%29.svg/80px-Sri_Lanka_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Sri_Lanka_%28orthographic_projection%29.svg/120px-Sri_Lanka_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Sri_Lanka_%28orthographic_projection%29.svg/160px-Sri_Lanka_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Sri Lanka
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="Western">Western</span></h3>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%AA%E0%A4%B6%E0%A5%8D%E0%A4%9A%E0%A4%BF%E0%A4%AE%E0%A5%80_%E0%A4%8F%E0%A4%B6%E0%A4%BF%E0%A4%AF%E0%A4%BE" class="extiw" title="hi:पश्चिमी एशिया">पश्चिमी एशिया</a></div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%93%E1%83%90%E1%83%A1%E1%83%90%E1%83%95%E1%83%9A%E1%83%94%E1%83%97_%E1%83%90%E1%83%96%E1%83%98%E1%83%90" class="extiw" title="ka:დასავლეთ აზია">დასავლეთ აზია</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/Sudoeste_da_%C3%81sia" class="extiw" title="pt:Sudoeste da Ásia">Sudoeste da Ásia</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://uk.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%BD%D1%8F_%D0%90%D0%B7%D1%96%D1%8F" class="extiw" title="uk:Передня Азія">Передня Азія</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Western_Asia_(orthographic_projection).svg" class="mw-file-description" title="Western Asia"><img alt="Western Asia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Western_Asia_%28orthographic_projection%29.svg/80px-Western_Asia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Western_Asia_%28orthographic_projection%29.svg/120px-Western_Asia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Western_Asia_%28orthographic_projection%29.svg/160px-Western_Asia_%28orthographic_projection%29.svg.png 2x" data-file-width="683" data-file-height="683" /></a></span></div>
			<div class="gallerytext">
<p>Western Asia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Levant_(orthographic_projection).png" class="mw-file-description" title="Levant"><img alt="Levant" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Levant_%28orthographic_projection%29.png/80px-Levant_%28orthographic_projection%29.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Levant_%28orthographic_projection%29.png/120px-Levant_%28orthographic_projection%29.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Levant_%28orthographic_projection%29.png/160px-Levant_%28orthographic_projection%29.png 2x" data-file-width="2000" data-file-height="2000" /></a></span></div>
			<div class="gallerytext">
<p>Levant
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Georgia_(orthographic_projection).svg" class="mw-file-description" title="Georgia"><img alt="Georgia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Georgia_%28orthographic_projection%29.svg/80px-Georgia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Georgia_%28orthographic_projection%29.svg/120px-Georgia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Georgia_%28orthographic_projection%29.svg/160px-Georgia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Georgia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Georgia_(orthographic_projection_with_inset).svg" class="mw-file-description" title="Georgia (with inset), showing breakaway states"><img alt="Georgia (with inset), showing breakaway states" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Georgia_%28orthographic_projection_with_inset%29.svg/80px-Georgia_%28orthographic_projection_with_inset%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Georgia_%28orthographic_projection_with_inset%29.svg/120px-Georgia_%28orthographic_projection_with_inset%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Georgia_%28orthographic_projection_with_inset%29.svg/160px-Georgia_%28orthographic_projection_with_inset%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Georgia (with inset), showing breakaway states
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Georgia_(orthographic--projection).svg" class="mw-file-description" title="Georgia (with inset), without breakaway states"><img alt="Georgia (with inset), without breakaway states" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Georgia_%28orthographic--projection%29.svg/80px-Georgia_%28orthographic--projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Georgia_%28orthographic--projection%29.svg/120px-Georgia_%28orthographic--projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Georgia_%28orthographic--projection%29.svg/160px-Georgia_%28orthographic--projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Georgia (with inset), without breakaway states
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Armenia_(orthographic_projection).svg" class="mw-file-description" title="Armenia"><img alt="Armenia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Armenia_%28orthographic_projection%29.svg/80px-Armenia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Armenia_%28orthographic_projection%29.svg/120px-Armenia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Armenia_%28orthographic_projection%29.svg/160px-Armenia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Armenia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Azerbaijan_(orthographic_projection).svg" class="mw-file-description" title="Azerbaijan"><img alt="Azerbaijan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Azerbaijan_%28orthographic_projection%29.svg/80px-Azerbaijan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Azerbaijan_%28orthographic_projection%29.svg/120px-Azerbaijan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Azerbaijan_%28orthographic_projection%29.svg/160px-Azerbaijan_%28orthographic_projection%29.svg.png 2x" data-file-width="551" data-file-height="551" /></a></span></div>
			<div class="gallerytext">
<p>Azerbaijan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Republic_of_Artsakh_(orthographic_projection).svg" class="mw-file-description" title="Nagorno-Karabakh Republic"><img alt="Nagorno-Karabakh Republic" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Republic_of_Artsakh_%28orthographic_projection%29.svg/80px-Republic_of_Artsakh_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Republic_of_Artsakh_%28orthographic_projection%29.svg/120px-Republic_of_Artsakh_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Republic_of_Artsakh_%28orthographic_projection%29.svg/160px-Republic_of_Artsakh_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Nagorno-Karabakh Republic
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Iran_(orthographic_projection).svg" class="mw-file-description" title="Iran"><img alt="Iran" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Iran_%28orthographic_projection%29.svg/80px-Iran_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Iran_%28orthographic_projection%29.svg/120px-Iran_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Iran_%28orthographic_projection%29.svg/160px-Iran_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Iran
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Iraq_(orthographic_projection).svg" class="mw-file-description" title="Iraq"><img alt="Iraq" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Iraq_%28orthographic_projection%29.svg/80px-Iraq_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Iraq_%28orthographic_projection%29.svg/120px-Iraq_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Iraq_%28orthographic_projection%29.svg/160px-Iraq_%28orthographic_projection%29.svg.png 2x" data-file-width="680" data-file-height="680" /></a></span></div>
			<div class="gallerytext">
<p>Iraq
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Israel_(orthographic_projection).svg" class="mw-file-description" title="Israel"><img alt="Israel" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Israel_%28orthographic_projection%29.svg/80px-Israel_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Israel_%28orthographic_projection%29.svg/120px-Israel_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Israel_%28orthographic_projection%29.svg/160px-Israel_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Israel
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Jordan_(orthographic_projection).svg" class="mw-file-description" title="Jordan"><img alt="Jordan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Jordan_%28orthographic_projection%29.svg/80px-Jordan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Jordan_%28orthographic_projection%29.svg/120px-Jordan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Jordan_%28orthographic_projection%29.svg/160px-Jordan_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Jordan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Saudi_Arabia_(orthographic_projection).svg" class="mw-file-description" title="Saudi Arabia"><img alt="Saudi Arabia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Saudi_Arabia_%28orthographic_projection%29.svg/80px-Saudi_Arabia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Saudi_Arabia_%28orthographic_projection%29.svg/120px-Saudi_Arabia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Saudi_Arabia_%28orthographic_projection%29.svg/160px-Saudi_Arabia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Saudi Arabia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:State_of_Palestine_(orthographic_projection).svg" class="mw-file-description" title="State of Palestine"><img alt="State of Palestine" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/State_of_Palestine_%28orthographic_projection%29.svg/80px-State_of_Palestine_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/State_of_Palestine_%28orthographic_projection%29.svg/120px-State_of_Palestine_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/State_of_Palestine_%28orthographic_projection%29.svg/160px-State_of_Palestine_%28orthographic_projection%29.svg.png 2x" data-file-width="680" data-file-height="680" /></a></span></div>
			<div class="gallerytext">
<p>State of Palestine
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Syria_(orthographic_projection).svg" class="mw-file-description" title="Syria"><img alt="Syria" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Syria_%28orthographic_projection%29.svg/80px-Syria_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Syria_%28orthographic_projection%29.svg/120px-Syria_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Syria_%28orthographic_projection%29.svg/160px-Syria_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Syria
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Lebanon_(orthographic_projection).svg" class="mw-file-description" title="Lebanon"><img alt="Lebanon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Lebanon_%28orthographic_projection%29.svg/80px-Lebanon_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Lebanon_%28orthographic_projection%29.svg/120px-Lebanon_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Lebanon_%28orthographic_projection%29.svg/160px-Lebanon_%28orthographic_projection%29.svg.png 2x" data-file-width="680" data-file-height="680" /></a></span></div>
			<div class="gallerytext">
<p>Lebanon
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Turkey_(orthographic_projection).svg" class="mw-file-description" title="Turkey"><img alt="Turkey" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Turkey_%28orthographic_projection%29.svg/80px-Turkey_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Turkey_%28orthographic_projection%29.svg/120px-Turkey_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Turkey_%28orthographic_projection%29.svg/160px-Turkey_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Turkey
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:United_Arab_Emirates_(orthographic_projection).svg" class="mw-file-description" title="United Arab Emirates"><img alt="United Arab Emirates" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/United_Arab_Emirates_%28orthographic_projection%29.svg/80px-United_Arab_Emirates_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/United_Arab_Emirates_%28orthographic_projection%29.svg/120px-United_Arab_Emirates_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/United_Arab_Emirates_%28orthographic_projection%29.svg/160px-United_Arab_Emirates_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>United Arab Emirates
</p>
			</div>
		</li>
</ul>
<h2><span class="mw-headline" id="Europe">Europe</span></h2>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%AF%E0%A5%81%E0%A4%B0%E0%A5%8B%E0%A4%AA" class="extiw" title="hi:युरोप">यूरोप</a></div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%94%E1%83%95%E1%83%A0%E1%83%9D%E1%83%9E%E1%83%90" class="extiw" title="ka:ევროპა">ევროპა</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/Europa" class="extiw" title="pt:Europa">Europa</a>.</div>
<div class="description mw-content-ltr ro" dir="ltr" lang="ro"><span class="language ro" title="Romanian"><b>Română&#58; </b></span> <a href="https://ro.wikipedia.org/wiki/Europa" class="extiw" title="ro:Europa">Europa</a>.</div>
<div class="description mw-content-ltr ru" dir="ltr" lang="ru"><span class="language ru" title="Russian"><b>Русский&#58; </b></span> <a href="https://ru.wikipedia.org/wiki/%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0" class="extiw" title="ru:Европа">Европа</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://uk.wikipedia.org/wiki/%D0%84%D0%B2%D1%80%D0%BE%D0%BF%D0%B0" class="extiw" title="uk:Європа">Європа</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Europe_orthographic_Caucasus_Urals_boundary.svg" class="mw-file-description" title="Europe, Caucasus-Urals boundary"><img alt="Europe, Caucasus-Urals boundary" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Europe_orthographic_Caucasus_Urals_boundary.svg/80px-Europe_orthographic_Caucasus_Urals_boundary.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Europe_orthographic_Caucasus_Urals_boundary.svg/120px-Europe_orthographic_Caucasus_Urals_boundary.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Europe_orthographic_Caucasus_Urals_boundary.svg/160px-Europe_orthographic_Caucasus_Urals_boundary.svg.png 2x" data-file-width="537" data-file-height="536" /></a></span></div>
			<div class="gallerytext">
<p>Europe, Caucasus-Urals boundary
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Europe_(orthographic_projection).svg" class="mw-file-description" title="Europe, unclear boundary somewhere in the mid-Caucasus, suffering from edit-wars"><img alt="Europe, unclear boundary somewhere in the mid-Caucasus, suffering from edit-wars" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Europe_%28orthographic_projection%29.svg/80px-Europe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Europe_%28orthographic_projection%29.svg/120px-Europe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Europe_%28orthographic_projection%29.svg/160px-Europe_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Europe, unclear boundary somewhere in the mid-Caucasus, suffering from edit-wars
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Europe_orthographic_Caucasus_Urals_boundary_(with_borders).svg" class="mw-file-description" title="Europe, Caucasus-Urals boundary, with state borders"><img alt="Europe, Caucasus-Urals boundary, with state borders" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Europe_orthographic_Caucasus_Urals_boundary_%28with_borders%29.svg/80px-Europe_orthographic_Caucasus_Urals_boundary_%28with_borders%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Europe_orthographic_Caucasus_Urals_boundary_%28with_borders%29.svg/120px-Europe_orthographic_Caucasus_Urals_boundary_%28with_borders%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Europe_orthographic_Caucasus_Urals_boundary_%28with_borders%29.svg/160px-Europe_orthographic_Caucasus_Urals_boundary_%28with_borders%29.svg.png 2x" data-file-width="537" data-file-height="536" /></a></span></div>
			<div class="gallerytext">
<p>Europe, Caucasus-Urals boundary, with state borders
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Northern_Europe_(orthographic_projection).svg" class="mw-file-description" title="Northern Europe"><img alt="Northern Europe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Northern_Europe_%28orthographic_projection%29.svg/80px-Northern_Europe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Northern_Europe_%28orthographic_projection%29.svg/120px-Northern_Europe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Northern_Europe_%28orthographic_projection%29.svg/160px-Northern_Europe_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Northern Europe
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Southern_Europe_(orthographic_projection).svg" class="mw-file-description" title="Southern Europe"><img alt="Southern Europe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Southern_Europe_%28orthographic_projection%29.svg/80px-Southern_Europe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Southern_Europe_%28orthographic_projection%29.svg/120px-Southern_Europe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Southern_Europe_%28orthographic_projection%29.svg/160px-Southern_Europe_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Southern Europe
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Western_Europe_(orthographic_projection).svg" class="mw-file-description" title="Western Europe"><img alt="Western Europe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Western_Europe_%28orthographic_projection%29.svg/80px-Western_Europe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Western_Europe_%28orthographic_projection%29.svg/120px-Western_Europe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Western_Europe_%28orthographic_projection%29.svg/160px-Western_Europe_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Western Europe
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Northwestern_Europe_(orthographic_projection).svg" class="mw-file-description" title="Northwestern Europe"><img alt="Northwestern Europe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Northwestern_Europe_%28orthographic_projection%29.svg/80px-Northwestern_Europe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Northwestern_Europe_%28orthographic_projection%29.svg/120px-Northwestern_Europe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Northwestern_Europe_%28orthographic_projection%29.svg/160px-Northwestern_Europe_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Northwestern Europe
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mainland_Europe_(orthographic_projection).svg" class="mw-file-description" title="Mainland Europe"><img alt="Mainland Europe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Mainland_Europe_%28orthographic_projection%29.svg/80px-Mainland_Europe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Mainland_Europe_%28orthographic_projection%29.svg/120px-Mainland_Europe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Mainland_Europe_%28orthographic_projection%29.svg/160px-Mainland_Europe_%28orthographic_projection%29.svg.png 2x" data-file-width="537" data-file-height="536" /></a></span></div>
			<div class="gallerytext">
<p>Mainland Europe
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Latin_Europe_(orthographic_projection).svg" class="mw-file-description" title="Latin Europe"><img alt="Latin Europe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Latin_Europe_%28orthographic_projection%29.svg/80px-Latin_Europe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Latin_Europe_%28orthographic_projection%29.svg/120px-Latin_Europe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Latin_Europe_%28orthographic_projection%29.svg/160px-Latin_Europe_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Latin Europe
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Council_of_Europe_(orthographic_projection).svg" class="mw-file-description" title="Council of Europe"><img alt="Council of Europe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Council_of_Europe_%28orthographic_projection%29.svg/80px-Council_of_Europe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Council_of_Europe_%28orthographic_projection%29.svg/120px-Council_of_Europe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Council_of_Europe_%28orthographic_projection%29.svg/160px-Council_of_Europe_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>Council of Europe
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Global_European_Union.svg" class="mw-file-description" title="European Union"><img alt="European Union" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Global_European_Union.svg/80px-Global_European_Union.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Global_European_Union.svg/120px-Global_European_Union.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Global_European_Union.svg/160px-Global_European_Union.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>European Union
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:European_Union_(orthographic_projection).svg" class="mw-file-description" title="European Union with internal borders"><img alt="European Union with internal borders" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/European_Union_%28orthographic_projection%29.svg/80px-European_Union_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/European_Union_%28orthographic_projection%29.svg/120px-European_Union_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/European_Union_%28orthographic_projection%29.svg/160px-European_Union_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>European Union with internal borders
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Benelux_(orthographic_projection).svg" class="mw-file-description" title="Benelux"><img alt="Benelux" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Benelux_%28orthographic_projection%29.svg/80px-Benelux_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Benelux_%28orthographic_projection%29.svg/120px-Benelux_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Benelux_%28orthographic_projection%29.svg/160px-Benelux_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Benelux
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Visegr%C3%A1dsk%C3%A1_skupina.svg" class="mw-file-description" title="Visegrád Group"><img alt="Visegrád Group" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Visegr%C3%A1dsk%C3%A1_skupina.svg/80px-Visegr%C3%A1dsk%C3%A1_skupina.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Visegr%C3%A1dsk%C3%A1_skupina.svg/120px-Visegr%C3%A1dsk%C3%A1_skupina.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Visegr%C3%A1dsk%C3%A1_skupina.svg/160px-Visegr%C3%A1dsk%C3%A1_skupina.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Visegrád Group
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:British_Isles_(orthographic_projection).svg" class="mw-file-description" title="British Isles"><img alt="British Isles" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/British_Isles_%28orthographic_projection%29.svg/80px-British_Isles_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/British_Isles_%28orthographic_projection%29.svg/120px-British_Isles_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/British_Isles_%28orthographic_projection%29.svg/160px-British_Isles_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>British Isles
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Great_Britain_(orthographic_projection).svg" class="mw-file-description" title="Great Britain"><img alt="Great Britain" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Great_Britain_%28orthographic_projection%29.svg/80px-Great_Britain_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Great_Britain_%28orthographic_projection%29.svg/120px-Great_Britain_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Great_Britain_%28orthographic_projection%29.svg/160px-Great_Britain_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>Great Britain
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Island_of_Cyprus_(orthographic_projection).svg" class="mw-file-description" title="Island of Cyprus"><img alt="Island of Cyprus" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Island_of_Cyprus_%28orthographic_projection%29.svg/80px-Island_of_Cyprus_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Island_of_Cyprus_%28orthographic_projection%29.svg/120px-Island_of_Cyprus_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Island_of_Cyprus_%28orthographic_projection%29.svg/160px-Island_of_Cyprus_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Island of Cyprus
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Iberia_(orthographic_projection).svg" class="mw-file-description" title="Iberia"><img alt="Iberia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Iberia_%28orthographic_projection%29.svg/80px-Iberia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Iberia_%28orthographic_projection%29.svg/120px-Iberia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Iberia_%28orthographic_projection%29.svg/160px-Iberia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Iberia
</p>
			</div>
		</li>
</ul>
<h3><span class="mw-headline" id="Countries">Countries</span></h3>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Albania_(orthographic_projection).svg" class="mw-file-description" title="Albania"><img alt="Albania" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Albania_%28orthographic_projection%29.svg/80px-Albania_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Albania_%28orthographic_projection%29.svg/120px-Albania_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Albania_%28orthographic_projection%29.svg/160px-Albania_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Albania
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Armenia_(orthographic_projection).svg" class="mw-file-description" title="Armenia"><img alt="Armenia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Armenia_%28orthographic_projection%29.svg/80px-Armenia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Armenia_%28orthographic_projection%29.svg/120px-Armenia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Armenia_%28orthographic_projection%29.svg/160px-Armenia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Armenia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Azerbaijan_(orthographic_projection).svg" class="mw-file-description" title="Azerbaijan"><img alt="Azerbaijan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Azerbaijan_%28orthographic_projection%29.svg/80px-Azerbaijan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Azerbaijan_%28orthographic_projection%29.svg/120px-Azerbaijan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Azerbaijan_%28orthographic_projection%29.svg/160px-Azerbaijan_%28orthographic_projection%29.svg.png 2x" data-file-width="551" data-file-height="551" /></a></span></div>
			<div class="gallerytext">
<p>Azerbaijan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Belarus_(orthographic_projection).svg" class="mw-file-description" title="Belarus"><img alt="Belarus" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Belarus_%28orthographic_projection%29.svg/80px-Belarus_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Belarus_%28orthographic_projection%29.svg/120px-Belarus_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Belarus_%28orthographic_projection%29.svg/160px-Belarus_%28orthographic_projection%29.svg.png 2x" data-file-width="537" data-file-height="536" /></a></span></div>
			<div class="gallerytext">
<p>Belarus
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Belgium_(orthographic_projection).svg" class="mw-file-description" title="Belgium"><img alt="Belgium" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Belgium_%28orthographic_projection%29.svg/80px-Belgium_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Belgium_%28orthographic_projection%29.svg/120px-Belgium_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Belgium_%28orthographic_projection%29.svg/160px-Belgium_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Belgium
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Bosnia_and_Herzegovina_(orthographic_projection).svg" class="mw-file-description" title="Bosnia and Herzegovina"><img alt="Bosnia and Herzegovina" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Bosnia_and_Herzegovina_%28orthographic_projection%29.svg/80px-Bosnia_and_Herzegovina_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Bosnia_and_Herzegovina_%28orthographic_projection%29.svg/120px-Bosnia_and_Herzegovina_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Bosnia_and_Herzegovina_%28orthographic_projection%29.svg/160px-Bosnia_and_Herzegovina_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Bosnia and Herzegovina
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Bulgaria_(orthographic_projection).svg" class="mw-file-description" title="Bulgaria"><img alt="Bulgaria" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Bulgaria_%28orthographic_projection%29.svg/80px-Bulgaria_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Bulgaria_%28orthographic_projection%29.svg/120px-Bulgaria_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Bulgaria_%28orthographic_projection%29.svg/160px-Bulgaria_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Bulgaria
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Republic_of_Cyprus_(orthographic_projection).svg" class="mw-file-description" title="Republic of Cyprus"><img alt="Republic of Cyprus" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Republic_of_Cyprus_%28orthographic_projection%29.svg/80px-Republic_of_Cyprus_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Republic_of_Cyprus_%28orthographic_projection%29.svg/120px-Republic_of_Cyprus_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Republic_of_Cyprus_%28orthographic_projection%29.svg/160px-Republic_of_Cyprus_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Republic of Cyprus
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Czech_Republic_(orthographic_projection).svg" class="mw-file-description" title="Czech Republic"><img alt="Czech Republic" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Czech_Republic_%28orthographic_projection%29.svg/80px-Czech_Republic_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Czech_Republic_%28orthographic_projection%29.svg/120px-Czech_Republic_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Czech_Republic_%28orthographic_projection%29.svg/160px-Czech_Republic_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>Czech Republic
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Denmark_(orthographic_projection).svg" class="mw-file-description" title="Denmark"><img alt="Denmark" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Denmark_%28orthographic_projection%29.svg/80px-Denmark_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Denmark_%28orthographic_projection%29.svg/120px-Denmark_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Denmark_%28orthographic_projection%29.svg/160px-Denmark_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>Denmark
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Finland_(orthographic_projection).svg" class="mw-file-description" title="Finland"><img alt="Finland" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Finland_%28orthographic_projection%29.svg/80px-Finland_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Finland_%28orthographic_projection%29.svg/120px-Finland_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Finland_%28orthographic_projection%29.svg/160px-Finland_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Finland
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:France_(orthographic_projection).svg" class="mw-file-description" title="France"><img alt="France" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/France_%28orthographic_projection%29.svg/80px-France_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/France_%28orthographic_projection%29.svg/120px-France_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/France_%28orthographic_projection%29.svg/160px-France_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>France
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Georgia_(orthographic_projection).svg" class="mw-file-description" title="Georgia"><img alt="Georgia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Georgia_%28orthographic_projection%29.svg/80px-Georgia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Georgia_%28orthographic_projection%29.svg/120px-Georgia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Georgia_%28orthographic_projection%29.svg/160px-Georgia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Georgia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Georgia_(orthographic_projection_with_inset).svg" class="mw-file-description" title="Georgia (with inset), showing breakaway states"><img alt="Georgia (with inset), showing breakaway states" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Georgia_%28orthographic_projection_with_inset%29.svg/80px-Georgia_%28orthographic_projection_with_inset%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Georgia_%28orthographic_projection_with_inset%29.svg/120px-Georgia_%28orthographic_projection_with_inset%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Georgia_%28orthographic_projection_with_inset%29.svg/160px-Georgia_%28orthographic_projection_with_inset%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Georgia (with inset), showing breakaway states
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Georgia_(orthographic--projection).svg" class="mw-file-description" title="Georgia (with inset), without breakaway states"><img alt="Georgia (with inset), without breakaway states" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Georgia_%28orthographic--projection%29.svg/80px-Georgia_%28orthographic--projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Georgia_%28orthographic--projection%29.svg/120px-Georgia_%28orthographic--projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Georgia_%28orthographic--projection%29.svg/160px-Georgia_%28orthographic--projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Georgia (with inset), without breakaway states
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Germany_(orthographic_projection).svg" class="mw-file-description" title="Germany"><img alt="Germany" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Germany_%28orthographic_projection%29.svg/80px-Germany_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Germany_%28orthographic_projection%29.svg/120px-Germany_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Germany_%28orthographic_projection%29.svg/160px-Germany_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>Germany
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Iceland_(orthographic_projection).svg" class="mw-file-description" title="Iceland"><img alt="Iceland" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Iceland_%28orthographic_projection%29.svg/80px-Iceland_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Iceland_%28orthographic_projection%29.svg/120px-Iceland_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Iceland_%28orthographic_projection%29.svg/160px-Iceland_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Iceland
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Italy_(orthographic_projection).svg" class="mw-file-description" title="Italy"><img alt="Italy" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Italy_%28orthographic_projection%29.svg/80px-Italy_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Italy_%28orthographic_projection%29.svg/120px-Italy_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Italy_%28orthographic_projection%29.svg/160px-Italy_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>Italy
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Kazakhstan_(orthographic_projection).svg" class="mw-file-description" title="Kazakhstan"><img alt="Kazakhstan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Kazakhstan_%28orthographic_projection%29.svg/80px-Kazakhstan_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Kazakhstan_%28orthographic_projection%29.svg/120px-Kazakhstan_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Kazakhstan_%28orthographic_projection%29.svg/160px-Kazakhstan_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Kazakhstan
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Kosovo_(orthographic_projection).svg" class="mw-file-description" title="Kosovo"><img alt="Kosovo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Kosovo_%28orthographic_projection%29.svg/80px-Kosovo_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Kosovo_%28orthographic_projection%29.svg/120px-Kosovo_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Kosovo_%28orthographic_projection%29.svg/160px-Kosovo_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Kosovo
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:North_Macedonia_(orthographic_projection).svg" class="mw-file-description" title="North Macedonia"><img alt="North Macedonia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/North_Macedonia_%28orthographic_projection%29.svg/80px-North_Macedonia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/North_Macedonia_%28orthographic_projection%29.svg/120px-North_Macedonia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/North_Macedonia_%28orthographic_projection%29.svg/160px-North_Macedonia_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>North Macedonia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Montenegro_(orthographic_projection).svg" class="mw-file-description" title="Montenegro"><img alt="Montenegro" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Montenegro_%28orthographic_projection%29.svg/80px-Montenegro_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Montenegro_%28orthographic_projection%29.svg/120px-Montenegro_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Montenegro_%28orthographic_projection%29.svg/160px-Montenegro_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Montenegro
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Netherlands_(orthographic_projection).svg" class="mw-file-description" title="Netherlands"><img alt="Netherlands" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Netherlands_%28orthographic_projection%29.svg/80px-Netherlands_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Netherlands_%28orthographic_projection%29.svg/120px-Netherlands_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Netherlands_%28orthographic_projection%29.svg/160px-Netherlands_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Netherlands
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Norway_(orthographic_projection).svg" class="mw-file-description" title="Norway"><img alt="Norway" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Norway_%28orthographic_projection%29.svg/80px-Norway_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Norway_%28orthographic_projection%29.svg/120px-Norway_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Norway_%28orthographic_projection%29.svg/160px-Norway_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Norway
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Northern_Cyprus_(orthographic_projection).svg" class="mw-file-description" title="Northern Cyprus"><img alt="Northern Cyprus" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Northern_Cyprus_%28orthographic_projection%29.svg/80px-Northern_Cyprus_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Northern_Cyprus_%28orthographic_projection%29.svg/120px-Northern_Cyprus_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Northern_Cyprus_%28orthographic_projection%29.svg/160px-Northern_Cyprus_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Northern Cyprus
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Poland_(orthographic_projection).svg" class="mw-file-description" title="Poland"><img alt="Poland" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Poland_%28orthographic_projection%29.svg/80px-Poland_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Poland_%28orthographic_projection%29.svg/120px-Poland_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Poland_%28orthographic_projection%29.svg/160px-Poland_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Poland
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Portugal_(orthographic_projection).svg" class="mw-file-description" title="Portugal"><img alt="Portugal" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Portugal_%28orthographic_projection%29.svg/80px-Portugal_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Portugal_%28orthographic_projection%29.svg/120px-Portugal_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Portugal_%28orthographic_projection%29.svg/160px-Portugal_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Portugal
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Romania_(orthographic_projection).svg" class="mw-file-description" title="Romania"><img alt="Romania" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Romania_%28orthographic_projection%29.svg/80px-Romania_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Romania_%28orthographic_projection%29.svg/120px-Romania_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Romania_%28orthographic_projection%29.svg/160px-Romania_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Romania
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Russian_Federation_(orthographic_projection)_-_Crimea_disputed.svg" class="mw-file-description" title="Russia"><img alt="Russia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Russian_Federation_%28orthographic_projection%29_-_Crimea_disputed.svg/80px-Russian_Federation_%28orthographic_projection%29_-_Crimea_disputed.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Russian_Federation_%28orthographic_projection%29_-_Crimea_disputed.svg/120px-Russian_Federation_%28orthographic_projection%29_-_Crimea_disputed.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Russian_Federation_%28orthographic_projection%29_-_Crimea_disputed.svg/160px-Russian_Federation_%28orthographic_projection%29_-_Crimea_disputed.svg.png 2x" data-file-width="536" data-file-height="537" /></a></span></div>
			<div class="gallerytext">
<p>Russia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Serbia_(orthographic_projection).svg" class="mw-file-description" title="Serbia"><img alt="Serbia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Serbia_%28orthographic_projection%29.svg/80px-Serbia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Serbia_%28orthographic_projection%29.svg/120px-Serbia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Serbia_%28orthographic_projection%29.svg/160px-Serbia_%28orthographic_projection%29.svg.png 2x" data-file-width="2048" data-file-height="2048" /></a></span></div>
			<div class="gallerytext">
<p>Serbia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Spain_(orthographic_projection).svg" class="mw-file-description" title="Spain"><img alt="Spain" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Spain_%28orthographic_projection%29.svg/80px-Spain_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Spain_%28orthographic_projection%29.svg/120px-Spain_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Spain_%28orthographic_projection%29.svg/160px-Spain_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Spain
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Sweden_(orthographic_projection).svg" class="mw-file-description" title="Sweden"><img alt="Sweden" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Sweden_%28orthographic_projection%29.svg/80px-Sweden_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Sweden_%28orthographic_projection%29.svg/120px-Sweden_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Sweden_%28orthographic_projection%29.svg/160px-Sweden_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Sweden
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Switzerland_(orthographic_projection).svg" class="mw-file-description" title="Switzerland"><img alt="Switzerland" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Switzerland_%28orthographic_projection%29.svg/80px-Switzerland_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Switzerland_%28orthographic_projection%29.svg/120px-Switzerland_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Switzerland_%28orthographic_projection%29.svg/160px-Switzerland_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Switzerland
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Turkey_(orthographic_projection).svg" class="mw-file-description" title="Turkey"><img alt="Turkey" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Turkey_%28orthographic_projection%29.svg/80px-Turkey_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Turkey_%28orthographic_projection%29.svg/120px-Turkey_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Turkey_%28orthographic_projection%29.svg/160px-Turkey_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Turkey
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:United_Kingdom_(orthographic_projection).svg" class="mw-file-description" title="United Kingdom"><img alt="United Kingdom" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/United_Kingdom_%28orthographic_projection%29.svg/80px-United_Kingdom_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/United_Kingdom_%28orthographic_projection%29.svg/120px-United_Kingdom_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/United_Kingdom_%28orthographic_projection%29.svg/160px-United_Kingdom_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>United Kingdom
</p>
			</div>
		</li>
</ul>
<h2><span class="mw-headline" id="Oceania">Oceania</span></h2>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://hi.wikipedia.org/wiki/%E0%A4%93%E0%A4%B6%E0%A4%BF%E0%A4%86%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%BE" class="extiw" title="hi:ओशिआनिया">ओशिआनिया</a></div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%9D%E1%83%99%E1%83%94%E1%83%90%E1%83%9C%E1%83%94%E1%83%97%E1%83%98" class="extiw" title="ka:ოკეანეთი">ოკეანეთი</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/Oceania" class="extiw" title="pt:Oceania">Oceania</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://uk.wikipedia.org/wiki/%D0%9E%D0%BA%D0%B5%D0%B0%D0%BD%D1%96%D1%8F" class="extiw" title="uk:Океанія">Океанія</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Oceania_(orthographic_projection).svg" class="mw-file-description" title="Oceania"><img alt="Oceania" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Oceania_%28orthographic_projection%29.svg/80px-Oceania_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Oceania_%28orthographic_projection%29.svg/120px-Oceania_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Oceania_%28orthographic_projection%29.svg/160px-Oceania_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Oceania
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Australia-New_Guinea_(orthographic_projection).svg" class="mw-file-description" title="Australia-New Guinea"><img alt="Australia-New Guinea" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Australia-New_Guinea_%28orthographic_projection%29.svg/80px-Australia-New_Guinea_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Australia-New_Guinea_%28orthographic_projection%29.svg/120px-Australia-New_Guinea_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Australia-New_Guinea_%28orthographic_projection%29.svg/160px-Australia-New_Guinea_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Australia-New Guinea
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Australia_(orthographic_projection).svg" class="mw-file-description" title="Australia"><img alt="Australia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Australia_%28orthographic_projection%29.svg/80px-Australia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Australia_%28orthographic_projection%29.svg/120px-Australia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Australia_%28orthographic_projection%29.svg/160px-Australia_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Australia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Fiji_(orthographic_projection).svg" class="mw-file-description" title="Fiji"><img alt="Fiji" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Fiji_%28orthographic_projection%29.svg/80px-Fiji_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Fiji_%28orthographic_projection%29.svg/120px-Fiji_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Fiji_%28orthographic_projection%29.svg/160px-Fiji_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Fiji
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:New_Zealand_(orthographic_projection).svg" class="mw-file-description" title="New Zealand"><img alt="New Zealand" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/New_Zealand_%28orthographic_projection%29.svg/80px-New_Zealand_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/New_Zealand_%28orthographic_projection%29.svg/120px-New_Zealand_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/New_Zealand_%28orthographic_projection%29.svg/160px-New_Zealand_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>New Zealand
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Papua_New_Guinea_(orthographic_projection).svg" class="mw-file-description" title="Papua New Guinea"><img alt="Papua New Guinea" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Papua_New_Guinea_%28orthographic_projection%29.svg/80px-Papua_New_Guinea_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Papua_New_Guinea_%28orthographic_projection%29.svg/120px-Papua_New_Guinea_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Papua_New_Guinea_%28orthographic_projection%29.svg/160px-Papua_New_Guinea_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Papua New Guinea
</p>
			</div>
		</li>
</ul>
<h2><span class="mw-headline" id="Intercontinental">Intercontinental</span></h2>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> <a href="https://en.wiktionary.org/wiki/intercontinental" class="extiw" title="wikt:intercontinental">अंतर्महाद्वीपिय</a></div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://en.wiktionary.org/wiki/intercontinental" class="extiw" title="wikt:intercontinental">კონტინენთშორისი</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://en.wiktionary.org/wiki/intercontinental" class="extiw" title="wikt:intercontinental">Intercontinental</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://en.wiktionary.org/wiki/intercontinental" class="extiw" title="wikt:intercontinental">Міжконтинентальні</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Americas_(orthographic_projection).svg" class="mw-file-description" title="The Americas"><img alt="The Americas" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Americas_%28orthographic_projection%29.svg/80px-Americas_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Americas_%28orthographic_projection%29.svg/120px-Americas_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Americas_%28orthographic_projection%29.svg/160px-Americas_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>The Americas
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Afro-Eurasia_(orthographic_projection)_political.svg" class="mw-file-description" title="Afro-eurasia"><img alt="Afro-eurasia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Afro-Eurasia_%28orthographic_projection%29_political.svg/80px-Afro-Eurasia_%28orthographic_projection%29_political.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Afro-Eurasia_%28orthographic_projection%29_political.svg/120px-Afro-Eurasia_%28orthographic_projection%29_political.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Afro-Eurasia_%28orthographic_projection%29_political.svg/160px-Afro-Eurasia_%28orthographic_projection%29_political.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Afro-eurasia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Arctic_(orthographic_projection).svg" class="mw-file-description" title="Arctic"><img alt="Arctic" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Arctic_%28orthographic_projection%29.svg/80px-Arctic_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Arctic_%28orthographic_projection%29.svg/120px-Arctic_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Arctic_%28orthographic_projection%29.svg/160px-Arctic_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Arctic
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Antarctica_(orthographic_projection).svg" class="mw-file-description" title="Antarctica"><img alt="Antarctica" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Antarctica_%28orthographic_projection%29.svg/80px-Antarctica_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Antarctica_%28orthographic_projection%29.svg/120px-Antarctica_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Antarctica_%28orthographic_projection%29.svg/160px-Antarctica_%28orthographic_projection%29.svg.png 2x" data-file-width="537" data-file-height="536" /></a></span></div>
			<div class="gallerytext">
<p>Antarctica
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Kingdom_of_the_Netherlands_(orthographic_projection).svg" class="mw-file-description" title="Kingdom of the Netherlands"><img alt="Kingdom of the Netherlands" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Kingdom_of_the_Netherlands_%28orthographic_projection%29.svg/80px-Kingdom_of_the_Netherlands_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Kingdom_of_the_Netherlands_%28orthographic_projection%29.svg/120px-Kingdom_of_the_Netherlands_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Kingdom_of_the_Netherlands_%28orthographic_projection%29.svg/160px-Kingdom_of_the_Netherlands_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Kingdom of the Netherlands
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Organization_for_Security_and_Co-operation_in_Europe_(orthographic_projection).svg" class="mw-file-description" title="Organization for Security and Co-operation in Europe"><img alt="Organization for Security and Co-operation in Europe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Organization_for_Security_and_Co-operation_in_Europe_%28orthographic_projection%29.svg/80px-Organization_for_Security_and_Co-operation_in_Europe_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Organization_for_Security_and_Co-operation_in_Europe_%28orthographic_projection%29.svg/120px-Organization_for_Security_and_Co-operation_in_Europe_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Organization_for_Security_and_Co-operation_in_Europe_%28orthographic_projection%29.svg/160px-Organization_for_Security_and_Co-operation_in_Europe_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Organization for Security and Co-operation in Europe
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Eurasia_(orthographic_projection).svg" class="mw-file-description" title="Eurasia"><img alt="Eurasia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Eurasia_%28orthographic_projection%29.svg/80px-Eurasia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Eurasia_%28orthographic_projection%29.svg/120px-Eurasia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Eurasia_%28orthographic_projection%29.svg/160px-Eurasia_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Eurasia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Eurasian_Economic_Union_(orthographic_projection)_-_Crimea_disputed_-_no_borders.svg" class="mw-file-description" title="Eurasian Economic Union"><img alt="Eurasian Economic Union" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Eurasian_Economic_Union_%28orthographic_projection%29_-_Crimea_disputed_-_no_borders.svg/80px-Eurasian_Economic_Union_%28orthographic_projection%29_-_Crimea_disputed_-_no_borders.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Eurasian_Economic_Union_%28orthographic_projection%29_-_Crimea_disputed_-_no_borders.svg/120px-Eurasian_Economic_Union_%28orthographic_projection%29_-_Crimea_disputed_-_no_borders.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Eurasian_Economic_Union_%28orthographic_projection%29_-_Crimea_disputed_-_no_borders.svg/160px-Eurasian_Economic_Union_%28orthographic_projection%29_-_Crimea_disputed_-_no_borders.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Eurasian Economic Union
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Greater_Middle_East_(orthographic_projection).svg" class="mw-file-description" title="Greater Middle East"><img alt="Greater Middle East" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Greater_Middle_East_%28orthographic_projection%29.svg/80px-Greater_Middle_East_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Greater_Middle_East_%28orthographic_projection%29.svg/120px-Greater_Middle_East_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Greater_Middle_East_%28orthographic_projection%29.svg/160px-Greater_Middle_East_%28orthographic_projection%29.svg.png 2x" data-file-width="551" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Greater Middle East
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Ibero-America_(orthographic_projection).svg" class="mw-file-description" title="Ibero-America"><img alt="Ibero-America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Ibero-America_%28orthographic_projection%29.svg/80px-Ibero-America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Ibero-America_%28orthographic_projection%29.svg/120px-Ibero-America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Ibero-America_%28orthographic_projection%29.svg/160px-Ibero-America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Ibero-America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Middle_East_(orthographic_projection).svg" class="mw-file-description" title="Middle East"><img alt="Middle East" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Middle_East_%28orthographic_projection%29.svg/80px-Middle_East_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Middle_East_%28orthographic_projection%29.svg/120px-Middle_East_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Middle_East_%28orthographic_projection%29.svg/160px-Middle_East_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Middle East
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:North_Atlantic_Treaty_Organization_(orthographic_projection).svg" class="mw-file-description" title="North Atlantic Treaty Organization"><img alt="North Atlantic Treaty Organization" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/North_Atlantic_Treaty_Organization_%28orthographic_projection%29.svg/80px-North_Atlantic_Treaty_Organization_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/North_Atlantic_Treaty_Organization_%28orthographic_projection%29.svg/120px-North_Atlantic_Treaty_Organization_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/North_Atlantic_Treaty_Organization_%28orthographic_projection%29.svg/160px-North_Atlantic_Treaty_Organization_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>North Atlantic Treaty Organization
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Arab_World_(orthographic_projection).svg" class="mw-file-description" title="Arab World"><img alt="Arab World" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Arab_World_%28orthographic_projection%29.svg/80px-Arab_World_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Arab_World_%28orthographic_projection%29.svg/120px-Arab_World_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Arab_World_%28orthographic_projection%29.svg/160px-Arab_World_%28orthographic_projection%29.svg.png 2x" data-file-width="512" data-file-height="512" /></a></span></div>
			<div class="gallerytext">
<p>Arab World
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Arab_League_member_states_(orthographic_projection).svg" class="mw-file-description" title="Arab League"><img alt="Arab League" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Arab_League_member_states_%28orthographic_projection%29.svg/80px-Arab_League_member_states_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Arab_League_member_states_%28orthographic_projection%29.svg/120px-Arab_League_member_states_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Arab_League_member_states_%28orthographic_projection%29.svg/160px-Arab_League_member_states_%28orthographic_projection%29.svg.png 2x" data-file-width="799" data-file-height="799" /></a></span></div>
			<div class="gallerytext">
<p>Arab League
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Latin_America_(orthographic_projection).svg" class="mw-file-description" title="Latin America"><img alt="Latin America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Latin_America_%28orthographic_projection%29.svg/80px-Latin_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Latin_America_%28orthographic_projection%29.svg/120px-Latin_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Latin_America_%28orthographic_projection%29.svg/160px-Latin_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Latin America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Anglo_America_(orthographic_projection).svg" class="mw-file-description" title="Anglo America"><img alt="Anglo America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Anglo_America_%28orthographic_projection%29.svg/80px-Anglo_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Anglo_America_%28orthographic_projection%29.svg/120px-Anglo_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Anglo_America_%28orthographic_projection%29.svg/160px-Anglo_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Anglo America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:French_America_(orthographic_projection).svg" class="mw-file-description" title="Franco America"><img alt="Franco America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/French_America_%28orthographic_projection%29.svg/80px-French_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/French_America_%28orthographic_projection%29.svg/120px-French_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/French_America_%28orthographic_projection%29.svg/160px-French_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Franco America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Hispanic_America_(orthographic_projection).svg" class="mw-file-description" title="Hispanic America"><img alt="Hispanic America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Hispanic_America_%28orthographic_projection%29.svg/80px-Hispanic_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Hispanic_America_%28orthographic_projection%29.svg/120px-Hispanic_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Hispanic_America_%28orthographic_projection%29.svg/160px-Hispanic_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Hispanic America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:SCO_(orthographic_projection).svg" class="mw-file-description" title="Shanghai Cooperation Organization"><img alt="Shanghai Cooperation Organization" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/SCO_%28orthographic_projection%29.svg/80px-SCO_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/SCO_%28orthographic_projection%29.svg/120px-SCO_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/SCO_%28orthographic_projection%29.svg/160px-SCO_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Shanghai Cooperation Organization
</p>
			</div>
		</li>
</ul>
<h2><span class="mw-headline" id="Historical">Historical</span></h2>
<div class="description mw-content-ltr en" dir="ltr" lang="en"><span class="language en" title="English"><b>English&#58; </b></span> Unions, Organizations, Kingdoms, Empires</div>
<div class="description mw-content-ltr es" dir="ltr" lang="es"><span class="language es" title="Spanish"><b>Español&#58; </b></span> Uniones, Organizaciones, Reinos, Imperios</div>
<div class="description mw-content-ltr fil" dir="ltr" lang="fil"><span class="language fil" title="Filipino"><b>Filipino&#58; </b></span> Mga Unyon, Organisasyon, Kaharian, Imperyo</div>
<div class="description mw-content-ltr fr" dir="ltr" lang="fr"><span class="language fr" title="French"><b>Français&#160;&#58; </b></span> Unions, Organisations, Royaumes, Empires</div>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> संघ, संगठन, राज्य, साम्राज्य व ऐतिहासिक देश</div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> გაერთიანებები, ორგანიზაციები, სამეფოები, იმპერიები</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/Estado_extinto" class="extiw" title="pt:Estado extinto">Estados extintos</a>.</div>
<div class="description mw-content-ltr tl" dir="ltr" lang="tl"><span class="language tl" title="Tagalog"><b>Tagalog&#58; </b></span> Mga Unyon, Organisasyon, Kaharian, Imperyo</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> Союзи, Організації, Королівства, Імперії</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Almoravid_map.svg" class="mw-file-description" title="Almoravid Empire"><img alt="Almoravid Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Almoravid_map.svg/80px-Almoravid_map.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Almoravid_map.svg/120px-Almoravid_map.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Almoravid_map.svg/160px-Almoravid_map.svg.png 2x" data-file-width="537" data-file-height="536" /></a></span></div>
			<div class="gallerytext">
<p>Almoravid Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Austro-Hungary_Empire_(orthographic_projection).svg" class="mw-file-description" title="Austro-Hungary"><img alt="Austro-Hungary" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Austro-Hungary_Empire_%28orthographic_projection%29.svg/80px-Austro-Hungary_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Austro-Hungary_Empire_%28orthographic_projection%29.svg/120px-Austro-Hungary_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Austro-Hungary_Empire_%28orthographic_projection%29.svg/160px-Austro-Hungary_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Austro-Hungary
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Aztec_Empire_(orthographic_projection).svg" class="mw-file-description" title="Aztec Empire"><img alt="Aztec Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Aztec_Empire_%28orthographic_projection%29.svg/80px-Aztec_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Aztec_Empire_%28orthographic_projection%29.svg/120px-Aztec_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Aztec_Empire_%28orthographic_projection%29.svg/160px-Aztec_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Aztec Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Aztec_Empire_ME_(orthographic_projection).svg" class="mw-file-description" title="Aztec Empire (with dominance between Teozapotlan and Xoconochco)"><img alt="Aztec Empire (with dominance between Teozapotlan and Xoconochco)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Aztec_Empire_ME_%28orthographic_projection%29.svg/80px-Aztec_Empire_ME_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Aztec_Empire_ME_%28orthographic_projection%29.svg/120px-Aztec_Empire_ME_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Aztec_Empire_ME_%28orthographic_projection%29.svg/160px-Aztec_Empire_ME_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Aztec Empire (with dominance between Teozapotlan and Xoconochco)
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Biafra_map.png" class="mw-file-description" title="Biafra"><img alt="Biafra" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Biafra_map.png/80px-Biafra_map.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Biafra_map.png/120px-Biafra_map.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Biafra_map.png/160px-Biafra_map.png 2x" data-file-width="2000" data-file-height="2000" /></a></span></div>
			<div class="gallerytext">
<p>Biafra
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Benin_(1970).png" class="mw-file-description" title="Benin (Separatist state in Nigeria)"><img alt="Benin (Separatist state in Nigeria)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Benin_%281970%29.png/80px-Benin_%281970%29.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Benin_%281970%29.png/120px-Benin_%281970%29.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Benin_%281970%29.png/160px-Benin_%281970%29.png 2x" data-file-width="2000" data-file-height="2000" /></a></span></div>
			<div class="gallerytext">
<p>Benin (Separatist state in Nigeria)
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Captaincy_General_of_Chile_(orthographic_projection).svg" class="mw-file-description" title="Captaincy General of Chile"><img alt="Captaincy General of Chile" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Captaincy_General_of_Chile_%28orthographic_projection%29.svg/80px-Captaincy_General_of_Chile_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Captaincy_General_of_Chile_%28orthographic_projection%29.svg/120px-Captaincy_General_of_Chile_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Captaincy_General_of_Chile_%28orthographic_projection%29.svg/160px-Captaincy_General_of_Chile_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Captaincy General of Chile
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Chinchaysuyu_(orthographic_projection).svg" class="mw-file-description" title="Chincha Country"><img alt="Chincha Country" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Chinchaysuyu_%28orthographic_projection%29.svg/80px-Chinchaysuyu_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Chinchaysuyu_%28orthographic_projection%29.svg/120px-Chinchaysuyu_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Chinchaysuyu_%28orthographic_projection%29.svg/160px-Chinchaysuyu_%28orthographic_projection%29.svg.png 2x" data-file-width="549" data-file-height="549" /></a></span></div>
			<div class="gallerytext">
<p>Chincha Country
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Confederate_States_of_America_(orthographic_projection).svg" class="mw-file-description" title="Confederate States of America"><img alt="Confederate States of America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Confederate_States_of_America_%28orthographic_projection%29.svg/80px-Confederate_States_of_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Confederate_States_of_America_%28orthographic_projection%29.svg/120px-Confederate_States_of_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Confederate_States_of_America_%28orthographic_projection%29.svg/160px-Confederate_States_of_America_%28orthographic_projection%29.svg.png 2x" data-file-width="551" data-file-height="551" /></a></span></div>
			<div class="gallerytext">
<p>Confederate States of America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Dominion_of_Pakistan_%26_Indian_Controlled_Kashmir_(orthographic_projection).svg" class="mw-file-description" title="Dominion of Pakistan (with Indian Controlled Kashmir)"><img alt="Dominion of Pakistan (with Indian Controlled Kashmir)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Dominion_of_Pakistan_%26_Indian_Controlled_Kashmir_%28orthographic_projection%29.svg/80px-Dominion_of_Pakistan_%26_Indian_Controlled_Kashmir_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Dominion_of_Pakistan_%26_Indian_Controlled_Kashmir_%28orthographic_projection%29.svg/120px-Dominion_of_Pakistan_%26_Indian_Controlled_Kashmir_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Dominion_of_Pakistan_%26_Indian_Controlled_Kashmir_%28orthographic_projection%29.svg/160px-Dominion_of_Pakistan_%26_Indian_Controlled_Kashmir_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Dominion of Pakistan (with Indian Controlled Kashmir)
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Eurasian_Economic_Community_(orthographic_projection).svg" class="mw-file-description" title="Eurasian Economic Community"><img alt="Eurasian Economic Community" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Eurasian_Economic_Community_%28orthographic_projection%29.svg/80px-Eurasian_Economic_Community_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Eurasian_Economic_Community_%28orthographic_projection%29.svg/120px-Eurasian_Economic_Community_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Eurasian_Economic_Community_%28orthographic_projection%29.svg/160px-Eurasian_Economic_Community_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Eurasian Economic Community
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:European_Economic_Community_(orthographic_projection).svg" class="mw-file-description" title="European Economic Community"><img alt="European Economic Community" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/European_Economic_Community_%28orthographic_projection%29.svg/80px-European_Economic_Community_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/European_Economic_Community_%28orthographic_projection%29.svg/120px-European_Economic_Community_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/European_Economic_Community_%28orthographic_projection%29.svg/160px-European_Economic_Community_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>European Economic Community
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:First_Brazilian_Empire_(orthographic_projection).svg" class="mw-file-description" title="Empire of Brazil"><img alt="Empire of Brazil" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/First_Brazilian_Empire_%28orthographic_projection%29.svg/80px-First_Brazilian_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/First_Brazilian_Empire_%28orthographic_projection%29.svg/120px-First_Brazilian_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/First_Brazilian_Empire_%28orthographic_projection%29.svg/160px-First_Brazilian_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="1024" data-file-height="1024" /></a></span></div>
			<div class="gallerytext">
<p>Empire of Brazil
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Federal_Republic_of_Central_America_(orthographic_projection).svg" class="mw-file-description" title="Federal Republic of Central America"><img alt="Federal Republic of Central America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Federal_Republic_of_Central_America_%28orthographic_projection%29.svg/80px-Federal_Republic_of_Central_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Federal_Republic_of_Central_America_%28orthographic_projection%29.svg/120px-Federal_Republic_of_Central_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Federal_Republic_of_Central_America_%28orthographic_projection%29.svg/160px-Federal_Republic_of_Central_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Federal Republic of Central America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:First_Mexican_Empire_(orthographic_projection).svg" class="mw-file-description" title="First Mexican Empire"><img alt="First Mexican Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/First_Mexican_Empire_%28orthographic_projection%29.svg/80px-First_Mexican_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/First_Mexican_Empire_%28orthographic_projection%29.svg/120px-First_Mexican_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/First_Mexican_Empire_%28orthographic_projection%29.svg/160px-First_Mexican_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>First Mexican Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Frankish_Empire_(orthographic_projection).svg" class="mw-file-description" title="Frankish Empire"><img alt="Frankish Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Frankish_Empire_%28orthographic_projection%29.svg/80px-Frankish_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Frankish_Empire_%28orthographic_projection%29.svg/120px-Frankish_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Frankish_Empire_%28orthographic_projection%29.svg/160px-Frankish_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="551" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Frankish Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Third_Reich_(orthographic_projection).svg" class="mw-file-description" title="German Reich"><img alt="German Reich" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Third_Reich_%28orthographic_projection%29.svg/80px-Third_Reich_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Third_Reich_%28orthographic_projection%29.svg/120px-Third_Reich_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Third_Reich_%28orthographic_projection%29.svg/160px-Third_Reich_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>German Reich
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:German_Reich_1942_(Orthographic_Projection).svg" class="mw-file-description" title="German Reich (With Occupations)"><img alt="German Reich (With Occupations)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/German_Reich_1942_%28Orthographic_Projection%29.svg/80px-German_Reich_1942_%28Orthographic_Projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/German_Reich_1942_%28Orthographic_Projection%29.svg/120px-German_Reich_1942_%28Orthographic_Projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/German_Reich_1942_%28Orthographic_Projection%29.svg/160px-German_Reich_1942_%28Orthographic_Projection%29.svg.png 2x" data-file-width="512" data-file-height="512" /></a></span></div>
			<div class="gallerytext">
<p>German Reich (With Occupations)
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Great_Colombia_(orthographic_projection).svg" class="mw-file-description" title="Great Colombia"><img alt="Great Colombia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Great_Colombia_%28orthographic_projection%29.svg/80px-Great_Colombia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Great_Colombia_%28orthographic_projection%29.svg/120px-Great_Colombia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Great_Colombia_%28orthographic_projection%29.svg/160px-Great_Colombia_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Great Colombia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Granadine_Confederation_(orthographic_projection).svg" class="mw-file-description" title="Granadine Confederation"><img alt="Granadine Confederation" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Granadine_Confederation_%28orthographic_projection%29.svg/80px-Granadine_Confederation_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Granadine_Confederation_%28orthographic_projection%29.svg/120px-Granadine_Confederation_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Granadine_Confederation_%28orthographic_projection%29.svg/160px-Granadine_Confederation_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Granadine Confederation
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Italian_Colonial_Empire_(orthographic_projection).svg" class="mw-file-description" title="Italian Empire"><img alt="Italian Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Italian_Colonial_Empire_%28orthographic_projection%29.svg/80px-Italian_Colonial_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Italian_Colonial_Empire_%28orthographic_projection%29.svg/120px-Italian_Colonial_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Italian_Colonial_Empire_%28orthographic_projection%29.svg/160px-Italian_Colonial_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="551" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Italian Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Japanese_Empire_(orthographic_projection).svg" class="mw-file-description" title="Japanese Empire"><img alt="Japanese Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Japanese_Empire_%28orthographic_projection%29.svg/80px-Japanese_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Japanese_Empire_%28orthographic_projection%29.svg/120px-Japanese_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Japanese_Empire_%28orthographic_projection%29.svg/160px-Japanese_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="600" data-file-height="600" /></a></span></div>
			<div class="gallerytext">
<p>Japanese Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Tawantinsuyu_(orthographic_projection).svg" class="mw-file-description" title="Inca Empire"><img alt="Inca Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Tawantinsuyu_%28orthographic_projection%29.svg/80px-Tawantinsuyu_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Tawantinsuyu_%28orthographic_projection%29.svg/120px-Tawantinsuyu_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Tawantinsuyu_%28orthographic_projection%29.svg/160px-Tawantinsuyu_%28orthographic_projection%29.svg.png 2x" data-file-width="549" data-file-height="549" /></a></span></div>
			<div class="gallerytext">
<p>Inca Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Mughal_Empire_(orthographic_projection).svg" class="mw-file-description" title="Mughal Empire"><img alt="Mughal Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Mughal_Empire_%28orthographic_projection%29.svg/80px-Mughal_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Mughal_Empire_%28orthographic_projection%29.svg/120px-Mughal_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Mughal_Empire_%28orthographic_projection%29.svg/160px-Mughal_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Mughal Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:New_France_(orthographic_projection).svg" class="mw-file-description" title="New France"><img alt="New France" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/New_France_%28orthographic_projection%29.svg/80px-New_France_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/New_France_%28orthographic_projection%29.svg/120px-New_France_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/New_France_%28orthographic_projection%29.svg/160px-New_France_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>New France
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:New_Granada_(orthographic_projection).svg" class="mw-file-description" title="New Granada"><img alt="New Granada" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/New_Granada_%28orthographic_projection%29.svg/80px-New_Granada_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/New_Granada_%28orthographic_projection%29.svg/120px-New_Granada_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/New_Granada_%28orthographic_projection%29.svg/160px-New_Granada_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>New Granada
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Peru%E2%80%93Bolivia_Confederation_(orthographic_projection).svg" class="mw-file-description" title="Peru–Bolivia Confederation"><img alt="Peru–Bolivia Confederation" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Peru%E2%80%93Bolivia_Confederation_%28orthographic_projection%29.svg/80px-Peru%E2%80%93Bolivia_Confederation_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Peru%E2%80%93Bolivia_Confederation_%28orthographic_projection%29.svg/120px-Peru%E2%80%93Bolivia_Confederation_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Peru%E2%80%93Bolivia_Confederation_%28orthographic_projection%29.svg/160px-Peru%E2%80%93Bolivia_Confederation_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Peru–Bolivia Confederation
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Roman_Empire_(orthographic_projection).svg" class="mw-file-description" title="Roman Empire"><img alt="Roman Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Roman_Empire_%28orthographic_projection%29.svg/80px-Roman_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Roman_Empire_%28orthographic_projection%29.svg/120px-Roman_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Roman_Empire_%28orthographic_projection%29.svg/160px-Roman_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Roman Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Russian_Empire_(orthographic_projection).svg" class="mw-file-description" title="Russian Empire"><img alt="Russian Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Russian_Empire_%28orthographic_projection%29.svg/80px-Russian_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Russian_Empire_%28orthographic_projection%29.svg/120px-Russian_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Russian_Empire_%28orthographic_projection%29.svg/160px-Russian_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Russian Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Second_Mexican_Empire_(orthographic_projection).svg" class="mw-file-description" title="Second Mexican Empire"><img alt="Second Mexican Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Second_Mexican_Empire_%28orthographic_projection%29.svg/80px-Second_Mexican_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Second_Mexican_Empire_%28orthographic_projection%29.svg/120px-Second_Mexican_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Second_Mexican_Empire_%28orthographic_projection%29.svg/160px-Second_Mexican_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Second Mexican Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Songhai_Empire_(orthographic_projection).svg" class="mw-file-description" title="Songhai Empire"><img alt="Songhai Empire" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Songhai_Empire_%28orthographic_projection%29.svg/80px-Songhai_Empire_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Songhai_Empire_%28orthographic_projection%29.svg/120px-Songhai_Empire_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Songhai_Empire_%28orthographic_projection%29.svg/160px-Songhai_Empire_%28orthographic_projection%29.svg.png 2x" data-file-width="536" data-file-height="536" /></a></span></div>
			<div class="gallerytext">
<p>Songhai Empire
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Union_of_Soviet_Socialist_Republics_(orthographic_projection).svg" class="mw-file-description" title="Union of Soviet Socialist Republics"><img alt="Union of Soviet Socialist Republics" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Union_of_Soviet_Socialist_Republics_%28orthographic_projection%29.svg/80px-Union_of_Soviet_Socialist_Republics_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Union_of_Soviet_Socialist_Republics_%28orthographic_projection%29.svg/120px-Union_of_Soviet_Socialist_Republics_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Union_of_Soviet_Socialist_Republics_%28orthographic_projection%29.svg/160px-Union_of_Soviet_Socialist_Republics_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Union of Soviet Socialist Republics
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:United_Arab_Republic_(orthographic_projection).svg" class="mw-file-description" title="United Arab Republic"><img alt="United Arab Republic" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/United_Arab_Republic_%28orthographic_projection%29.svg/80px-United_Arab_Republic_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/United_Arab_Republic_%28orthographic_projection%29.svg/120px-United_Arab_Republic_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/United_Arab_Republic_%28orthographic_projection%29.svg/160px-United_Arab_Republic_%28orthographic_projection%29.svg.png 2x" data-file-width="680" data-file-height="680" /></a></span></div>
			<div class="gallerytext">
<p>United Arab Republic
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:United_Provinces_of_Central_America_(orthographic_projection).svg" class="mw-file-description" title="United Provinces of Central America"><img alt="United Provinces of Central America" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/United_Provinces_of_Central_America_%28orthographic_projection%29.svg/80px-United_Provinces_of_Central_America_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/United_Provinces_of_Central_America_%28orthographic_projection%29.svg/120px-United_Provinces_of_Central_America_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/United_Provinces_of_Central_America_%28orthographic_projection%29.svg/160px-United_Provinces_of_Central_America_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>United Provinces of Central America
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:United_States_of_Colombia_(orthographic_projection).svg" class="mw-file-description" title="United States of Colombia"><img alt="United States of Colombia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/United_States_of_Colombia_%28orthographic_projection%29.svg/80px-United_States_of_Colombia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/United_States_of_Colombia_%28orthographic_projection%29.svg/120px-United_States_of_Colombia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/United_States_of_Colombia_%28orthographic_projection%29.svg/160px-United_States_of_Colombia_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>United States of Colombia
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Viceroyalty_of_New_Granada_(orthographic_projection).svg" class="mw-file-description" title="Viceroyalty of New Granada"><img alt="Viceroyalty of New Granada" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Viceroyalty_of_New_Granada_%28orthographic_projection%29.svg/80px-Viceroyalty_of_New_Granada_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Viceroyalty_of_New_Granada_%28orthographic_projection%29.svg/120px-Viceroyalty_of_New_Granada_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Viceroyalty_of_New_Granada_%28orthographic_projection%29.svg/160px-Viceroyalty_of_New_Granada_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Viceroyalty of New Granada
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:New_Spain_(orthographic_projection).svg" class="mw-file-description" title="Viceroyalty of New Spain"><img alt="Viceroyalty of New Spain" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/New_Spain_%28orthographic_projection%29.svg/80px-New_Spain_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/New_Spain_%28orthographic_projection%29.svg/120px-New_Spain_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/New_Spain_%28orthographic_projection%29.svg/160px-New_Spain_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Viceroyalty of New Spain
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Viceroyalty_of_Peru_(orthographic_projection).svg" class="mw-file-description" title="Viceroyalty of Peru"><img alt="Viceroyalty of Peru" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Viceroyalty_of_Peru_%28orthographic_projection%29.svg/80px-Viceroyalty_of_Peru_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Viceroyalty_of_Peru_%28orthographic_projection%29.svg/120px-Viceroyalty_of_Peru_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Viceroyalty_of_Peru_%28orthographic_projection%29.svg/160px-Viceroyalty_of_Peru_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Viceroyalty of Peru
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Viceroyalty_of_the_R%C3%ADo_de_la_Plata_(orthographic_projection).svg" class="mw-file-description" title="Viceroyalty of the Río de la Plata"><img alt="Viceroyalty of the Río de la Plata" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Viceroyalty_of_the_R%C3%ADo_de_la_Plata_%28orthographic_projection%29.svg/80px-Viceroyalty_of_the_R%C3%ADo_de_la_Plata_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Viceroyalty_of_the_R%C3%ADo_de_la_Plata_%28orthographic_projection%29.svg/120px-Viceroyalty_of_the_R%C3%ADo_de_la_Plata_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Viceroyalty_of_the_R%C3%ADo_de_la_Plata_%28orthographic_projection%29.svg/160px-Viceroyalty_of_the_R%C3%ADo_de_la_Plata_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Viceroyalty of the Río de la Plata
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Wilsonian_Armenia_(orthographic_projection).svg" class="mw-file-description" title="Wilsonian Armenia"><img alt="Wilsonian Armenia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Wilsonian_Armenia_%28orthographic_projection%29.svg/80px-Wilsonian_Armenia_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Wilsonian_Armenia_%28orthographic_projection%29.svg/120px-Wilsonian_Armenia_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Wilsonian_Armenia_%28orthographic_projection%29.svg/160px-Wilsonian_Armenia_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Wilsonian Armenia
</p>
			</div>
		</li>
</ul>
<h2><span class="mw-headline" id="Subnationals">Subnationals</span></h2>
<div class="description mw-content-ltr hi" dir="ltr" lang="hi"><span class="language hi" title="Hindi"><b>हिन्दी&#58; </b></span> उपराष्ट्रीय इकाईयाँ</div>
<div class="description mw-content-ltr ka" dir="ltr" lang="ka"><span class="language ka" title="Georgian"><b>ქართული&#58; </b></span> <a href="https://ka.wikipedia.org/wiki/%E1%83%A1%E1%83%A3%E1%83%91%E1%83%94%E1%83%A0%E1%83%9D%E1%83%95%E1%83%9C%E1%83%A3%E1%83%9A%E1%83%98_%E1%83%94%E1%83%A0%E1%83%97%E1%83%94%E1%83%A3%E1%83%9A%E1%83%94%E1%83%91%E1%83%98" class="extiw" title="ka:სუბეროვნული ერთეულები">სუბეროვნული ერთეულები</a>.</div>
<div class="description mw-content-ltr pt" dir="ltr" lang="pt"><span class="language pt" title="Portuguese"><b>Português&#58; </b></span> <a href="https://pt.wikipedia.org/wiki/Entidades_subnacionais" class="extiw" title="pt:Entidades subnacionais">Entidades subnacionais</a>.</div>
<div class="description mw-content-ltr uk" dir="ltr" lang="uk"><span class="language uk" title="Ukrainian"><b>Українська&#58; </b></span> <a href="https://uk.wikipedia.org/wiki/%D0%90%D0%B4%D0%BC%D1%96%D0%BD%D1%96%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE-%D1%82%D0%B5%D1%80%D0%B8%D1%82%D0%BE%D1%80%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9_%D1%83%D1%81%D1%82%D1%80%D1%96%D0%B9" class="extiw" title="uk:Адміністративно-територіальний устрій">Субнаціональні утворення</a>.</div>
<ul class="gallery mw-gallery-traditional">
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Canary_Islands,_Spain_(orthographic_projection).png" class="mw-file-description" title="Canary Islands, Spain"><img alt="Canary Islands, Spain" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Canary_Islands%2C_Spain_%28orthographic_projection%29.png/80px-Canary_Islands%2C_Spain_%28orthographic_projection%29.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Canary_Islands%2C_Spain_%28orthographic_projection%29.png/120px-Canary_Islands%2C_Spain_%28orthographic_projection%29.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Canary_Islands%2C_Spain_%28orthographic_projection%29.png/160px-Canary_Islands%2C_Spain_%28orthographic_projection%29.png 2x" data-file-width="549" data-file-height="548" /></a></span></div>
			<div class="gallerytext">
<p>Canary Islands, Spain
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Catalan_Countries_(orthographic_projection).svg" class="mw-file-description" title="Catalan Countries"><img alt="Catalan Countries" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Catalan_Countries_%28orthographic_projection%29.svg/80px-Catalan_Countries_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Catalan_Countries_%28orthographic_projection%29.svg/120px-Catalan_Countries_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Catalan_Countries_%28orthographic_projection%29.svg/160px-Catalan_Countries_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Catalan Countries
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:French_Guiana_(orthographic_projection).svg" class="mw-file-description" title="French Guiana"><img alt="French Guiana" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/French_Guiana_%28orthographic_projection%29.svg/80px-French_Guiana_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/French_Guiana_%28orthographic_projection%29.svg/120px-French_Guiana_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/French_Guiana_%28orthographic_projection%29.svg/160px-French_Guiana_%28orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>French Guiana
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Greenland_(orthographic_projection).svg" class="mw-file-description" title="Greenland"><img alt="Greenland" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Greenland_%28orthographic_projection%29.svg/80px-Greenland_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Greenland_%28orthographic_projection%29.svg/120px-Greenland_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Greenland_%28orthographic_projection%29.svg/160px-Greenland_%28orthographic_projection%29.svg.png 2x" data-file-width="553" data-file-height="553" /></a></span></div>
			<div class="gallerytext">
<p>Greenland
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Quebec_(North_America_orthographic_projection).svg" class="mw-file-description" title="Québec, Canada"><img alt="Québec, Canada" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Quebec_%28North_America_orthographic_projection%29.svg/80px-Quebec_%28North_America_orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Quebec_%28North_America_orthographic_projection%29.svg/120px-Quebec_%28North_America_orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Quebec_%28North_America_orthographic_projection%29.svg/160px-Quebec_%28North_America_orthographic_projection%29.svg.png 2x" data-file-width="541" data-file-height="541" /></a></span></div>
			<div class="gallerytext">
<p>Québec, Canada
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Puerto_Rico_(orthographic_projection).svg" class="mw-file-description" title="Puerto Rico, U.S."><img alt="Puerto Rico, U.S." src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Puerto_Rico_%28orthographic_projection%29.svg/80px-Puerto_Rico_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Puerto_Rico_%28orthographic_projection%29.svg/120px-Puerto_Rico_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Puerto_Rico_%28orthographic_projection%29.svg/160px-Puerto_Rico_%28orthographic_projection%29.svg.png 2x" data-file-width="550" data-file-height="550" /></a></span></div>
			<div class="gallerytext">
<p>Puerto Rico, U.S.
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Great_Britain_(orthographic_projection).svg" class="mw-file-description" title="Great Britain"><img alt="Great Britain" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Great_Britain_%28orthographic_projection%29.svg/80px-Great_Britain_%28orthographic_projection%29.svg.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Great_Britain_%28orthographic_projection%29.svg/120px-Great_Britain_%28orthographic_projection%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Great_Britain_%28orthographic_projection%29.svg/160px-Great_Britain_%28orthographic_projection%29.svg.png 2x" data-file-width="792" data-file-height="792" /></a></span></div>
			<div class="gallerytext">
<p>Great Britain
</p>
			</div>
		</li>
		<li class="gallerybox" style="width: 135px">
			<div class="thumb" style="width: 130px; height: 110px;"><span typeof="mw:File"><a href="/wiki/File:Dagestan_(Federal_subject_of_Russia)_(orthographic_projection).png" class="mw-file-description" title="Dagestan (Federal subject of Russia)"><img alt="Dagestan (Federal subject of Russia)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Dagestan_%28Federal_subject_of_Russia%29_%28orthographic_projection%29.png/80px-Dagestan_%28Federal_subject_of_Russia%29_%28orthographic_projection%29.png" decoding="async" width="80" height="80" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Dagestan_%28Federal_subject_of_Russia%29_%28orthographic_projection%29.png/120px-Dagestan_%28Federal_subject_of_Russia%29_%28orthographic_projection%29.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Dagestan_%28Federal_subject_of_Russia%29_%28orthographic_projection%29.png/160px-Dagestan_%28Federal_subject_of_Russia%29_%28orthographic_projection%29.png 2x" data-file-width="553" data-file-height="552" /></a></span></div>
			<div class="gallerytext">
<p>Dagestan (Federal subject of Russia)
</p>
			</div>
		</li>
</ul>
</td></tr></tbody></table></div>
<p><br />
</p>
<h3><span class="mw-headline" id="SVG_software_tags">SVG software tags</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Grey%E2%80%93green_orthographic_projections_maps&amp;action=edit&amp;section=2" title="Edit section: SVG software tags">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<p>For the software used (<a href="/wiki/Category:SVG_graphics_by_software_used" title="Category:SVG graphics by software used">Category:SVG graphics by software used</a>):
</p>
<table class="messagebox plainlinks layouttemplate" style="margin:2px 10%;width:auto;border:2px solid #f28500;background:#ffe;color:#222;border-left-width:8px;border-collapse:collapse;"><tbody><tr>
<td class="mbox-image" style="padding-left:.9em"><span class="noviewer" typeof="mw:File"><span><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Commons-emblem-issue.svg/45px-Commons-emblem-issue.svg.png" decoding="async" width="45" height="45" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Commons-emblem-issue.svg/68px-Commons-emblem-issue.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Commons-emblem-issue.svg/90px-Commons-emblem-issue.svg.png 2x" data-file-width="48" data-file-height="48" /></span></span></td><td class="mbox-text">For <u>most of these graphics</u> the tag should be like <code>|Other fields={{Igen|+|<i>err#</i>|s=ggg}}</code><br />
<p>where <i><code>err#</code></i> is the W3C-errror count (seldom <code>0</code> for <a href="/wiki/Category:Valid_SVG_created_with_Inkscape:World_maps_(gggs)" title="Category:Valid SVG created with Inkscape:World maps (gggs)">valid SVG</a>).<br />
</p>
With  s=ggg the file is  subcatorized into <a href="/wiki/Category:Invalid_SVG_created_with_Inkscape:World_maps_(gggs)" title="Category:Invalid SVG created with Inkscape:World maps (gggs)">Invalid SVG created with Inkscape:World maps (gggs)</a>.</td></tr></tbody></table>
<dl><dd><dl><dd>or</dd></dl></dd></dl>
<ul><li><a href="/wiki/Template:Created_with_Adobe_Illustrator" title="Template:Created with Adobe Illustrator"><span style="font-family:monospace,monospace;">&#123;&#123;Created with Adobe Illustrator&#125;&#125;</span></a>, sorts into <a href="/wiki/Category:Created_with_Adobe_Illustrator" title="Category:Created with Adobe Illustrator">Category:Created with Adobe Illustrator</a>,</li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:Adobe-yes.svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Adobe-yes.svg/23px-Adobe-yes.svg.png" decoding="async" width="23" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Adobe-yes.svg/35px-Adobe-yes.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Adobe-yes.svg/47px-Adobe-yes.svg.png 2x" data-file-width="342" data-file-height="322" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;image&#32;was created with <a href="https://en.wikipedia.org/wiki/Adobe_Illustrator" class="extiw" title="w:Adobe Illustrator">Adobe Illustrator</a>.</div></div>
<ul><li><a href="/wiki/Template:Created_with_CorelDraw" class="mw-redirect" title="Template:Created with CorelDraw"><span style="font-family:monospace,monospace;">&#123;&#123;Created with CorelDraw&#125;&#125;</span></a>, sorts into <a href="/wiki/Category:Created_with_CorelDraw" title="Category:Created with CorelDraw">Category:Created with CorelDraw</a>,</li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:Corel_logo_initial.svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Corel_logo_initial.svg/27px-Corel_logo_initial.svg.png" decoding="async" width="27" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Corel_logo_initial.svg/41px-Corel_logo_initial.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Corel_logo_initial.svg/54px-Corel_logo_initial.svg.png 2x" data-file-width="422" data-file-height="343" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;image&#32;was created with <a href="https://en.wikipedia.org/wiki/CorelDRAW" class="extiw" title="w:CorelDRAW">CorelDRAW</a>.</div></div>
<ul><li><a href="/wiki/Template:Created_with_Dia" title="Template:Created with Dia"><span style="font-family:monospace,monospace;">&#123;&#123;Created with Dia&#125;&#125;</span></a>, sorts into <a href="/wiki/Category:Created_with_Dia" title="Category:Created with Dia">Category:Created with Dia</a>,</li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:Dia.svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Dia.svg/22px-Dia.svg.png" decoding="async" width="22" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Dia.svg/33px-Dia.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Dia.svg/44px-Dia.svg.png 2x" data-file-width="48" data-file-height="48" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;diagram&#32;was created with <a href="https://en.wikipedia.org/wiki/Dia" class="extiw" title="w:Dia">Dia</a>.</div></div>
<ul><li><a href="/wiki/Template:ElCompLib" class="mw-redirect" title="Template:ElCompLib"><span style="font-family:monospace,monospace;">&#123;&#123;ElCompLib&#125;&#125;</span></a>, sorts to <a href="/wiki/Category:Created_with_electrical_symbols_library" title="Category:Created with electrical symbols library">Category:Created with electrical symbols library</a></li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:BJT_NPN_symbol_(case,_unlabelled).svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/BJT_NPN_symbol_%28case%2C_unlabelled%29.svg/22px-BJT_NPN_symbol_%28case%2C_unlabelled%29.svg.png" decoding="async" width="22" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/BJT_NPN_symbol_%28case%2C_unlabelled%29.svg/33px-BJT_NPN_symbol_%28case%2C_unlabelled%29.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/BJT_NPN_symbol_%28case%2C_unlabelled%29.svg/44px-BJT_NPN_symbol_%28case%2C_unlabelled%29.svg.png 2x" data-file-width="77" data-file-height="77" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;<a href="https://en.wikipedia.org/wiki/circuit_diagram" class="extiw" title="w:circuit diagram">circuit diagram</a>&#32;was created with the <a href="/wiki/File:Electrical_symbols_library.svg" title="File:Electrical symbols library.svg">Electrical Symbols Library</a>.</div></div>
<ul><li><a href="/wiki/Template:Fig2SVG" class="mw-redirect" title="Template:Fig2SVG"><span style="font-family:monospace,monospace;">&#123;&#123;Fig2SVG&#125;&#125;</span></a>, does not sort by now (May 2008)</li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:Xfig_splash_logo.png" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Xfig_splash_logo.png/34px-Xfig_splash_logo.png" decoding="async" width="34" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Xfig_splash_logo.png/50px-Xfig_splash_logo.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Xfig_splash_logo.png/67px-Xfig_splash_logo.png 2x" data-file-width="137" data-file-height="90" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;image&#32;was created with <a href="https://en.wikipedia.org/wiki/Xfig" class="extiw" title="w:Xfig">Xfig</a> and a <i><a href="https://en.wikipedia.org/wiki/Figure" class="extiw" title="w:Figure">Fig</a>-to-<a href="https://en.wikipedia.org/wiki/SVG" class="extiw" title="w:SVG">SVG</a></i> conversion tool.</div></div>
<ul><li><a href="/wiki/Template:Gnuplot" class="mw-redirect" title="Template:Gnuplot"><span style="font-family:monospace,monospace;">&#123;&#123;Gnuplot&#125;&#125;</span></a>, does not sort by now (May 2008)</li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:Lissajous_small.svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Lissajous_small.svg/21px-Lissajous_small.svg.png" decoding="async" width="21" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Lissajous_small.svg/32px-Lissajous_small.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Lissajous_small.svg/43px-Lissajous_small.svg.png 2x" data-file-width="70" data-file-height="72" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;plot&#32;was created with <a href="https://en.wikipedia.org/wiki/Gnuplot" class="extiw" title="w:Gnuplot">Gnu</a><span class="plainlinks"><a rel="nofollow" class="external text" href="https://validator.w3.org/check?uri=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FSpecial%3AFilepath%2FGrey%25E2%2580%2593green_orthographic_projections_maps&amp;doctype=SVG+1.1&amp;ss=1#source"><i>plot</i></a></span>.</div></div>
<ul><li><a href="/wiki/Template:Created_with_Inkscape" title="Template:Created with Inkscape"><span style="font-family:monospace,monospace;">&#123;&#123;Created with Inkscape&#125;&#125;</span></a>, sorts into <a href="/wiki/Category:Created_with_Inkscape" title="Category:Created with Inkscape">Category:Created with Inkscape</a>, see also <a href="/wiki/Template:Inkscape-hand" title="Template:Inkscape-hand"><span style="font-family:monospace,monospace;">&#123;&#123;Inkscape-hand&#125;&#125;</span></a> (which sorts into <a href="/wiki/Category:Created_with_Inkscape-hand" title="Category:Created with Inkscape-hand">Created with Inkscape-hand</a>)</li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:Inkscape_Logo.svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Inkscape_Logo.svg/22px-Inkscape_Logo.svg.png" decoding="async" width="22" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Inkscape_Logo.svg/33px-Inkscape_Logo.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Inkscape_Logo.svg/44px-Inkscape_Logo.svg.png 2x" data-file-width="128" data-file-height="128" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;image&#32;was created with <a href="https://en.wikipedia.org/wiki/Inkscape" class="extiw" title="w:Inkscape">Inkscape</a>&#32;.</div></div>
<ul><li><a href="/wiki/Template:Created_with_OpenOffice.org" title="Template:Created with OpenOffice.org"><span style="font-family:monospace,monospace;">&#123;&#123;Created with OpenOffice.org&#125;&#125;</span></a>, sorts into <a href="/wiki/Category:Created_with_OpenOffice.org" title="Category:Created with OpenOffice.org">Category:Created with OpenOffice.org</a>, pays no attention on SVG or other file formats (May 2008)</li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:OpenOffice.org_2_icon_small.svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/OpenOffice.org_2_icon_small.svg/22px-OpenOffice.org_2_icon_small.svg.png" decoding="async" width="22" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/OpenOffice.org_2_icon_small.svg/33px-OpenOffice.org_2_icon_small.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/OpenOffice.org_2_icon_small.svg/44px-OpenOffice.org_2_icon_small.svg.png 2x" data-file-width="512" data-file-height="512" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;<a href="https://en.wikipedia.org/wiki/map" class="extiw" title="w:map">map</a>&#32;was created with <a href="https://en.wikipedia.org/wiki/OpenOffice.org" class="extiw" title="w:OpenOffice.org">OpenOffice.org</a>.</div></div>
<ul><li><a href="/wiki/Template:Created_with_Sodipodi" title="Template:Created with Sodipodi"><span style="font-family:monospace,monospace;">&#123;&#123;Created with Sodipodi&#125;&#125;</span></a>, sorts into <a href="/wiki/Category:Created_with_Sodipodi" title="Category:Created with Sodipodi">Category:Created with Sodipodi</a></li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:Sodipodi_Logo.svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Sodipodi_Logo.svg/29px-Sodipodi_Logo.svg.png" decoding="async" width="29" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Sodipodi_Logo.svg/43px-Sodipodi_Logo.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Sodipodi_Logo.svg/58px-Sodipodi_Logo.svg.png 2x" data-file-width="608" data-file-height="466" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;image&#32;was created with <a href="https://en.wikipedia.org/wiki/Sodipodi" class="extiw" title="w:Sodipodi">Sodipodi</a>.</div></div>
<ul><li><a href="/wiki/Template:Created_with_Scribus" title="Template:Created with Scribus"><span style="font-family:monospace,monospace;">&#123;&#123;Created with Scribus&#125;&#125;</span></a>, does not sort by now (May 2008), also for typesetting</li></ul>
<div style="display:inline-block;width:auto;white-space:nowrap;vertical-align:middle;direction:ltr;float:ltr;line-height:22px;height:24px;font-size:.96em;margin:0px;padding:2px 4px 2px 6px;color:#000;background:#F8F9FA;border:1px solid #BAB;"><span typeof="mw:File"><a href="/wiki/File:Scribus_logo.svg" class="mw-file-description"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Scribus_logo.svg/22px-Scribus_logo.svg.png" decoding="async" width="22" height="22" class="mw-file-element" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Scribus_logo.svg/33px-Scribus_logo.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Scribus_logo.svg/44px-Scribus_logo.svg.png 2x" data-file-width="744" data-file-height="744" /></a></span>&#160;<div lang="en" dir="ltr" class="description en" style="display:inline;">This &#32;<a href="https://en.wikipedia.org/wiki/Typesetting" class="extiw" title="w:Typesetting"><i>typeset</i></a>&#32;was created with <a href="https://en.wikipedia.org/wiki/Scribus" class="extiw" title="w:Scribus">Scribus</a><a href="https://en.wikipedia.org/wiki/Typesetting" class="extiw" title="w:Typesetting"><i>typeset</i></a>.</div></div>
<ul><li>For other software, by now categorize as usual, see <a href="/wiki/Commons:Created_with_..._templates" title="Commons:Created with ... templates">Commons:Created with ... templates</a> for a summary of software-related templates</li></ul>
<!-- 
NewPP limit report
Parsed by mw1369
Cached time: 20230717014942
Cache expiry: 1814400
Reduced expiry: false
Complications: [no‐toc]
CPU time usage: 0.822 seconds
Real time usage: 1.035 seconds
Preprocessor visited node count: 14143/1000000
Post‐expand include size: 151033/2097152 bytes
Template argument size: 57274/2097152 bytes
Highest expansion depth: 26/100
Expensive parser function count: 4/500
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 267741/5000000 bytes
Lua time usage: 0.273/10.000 seconds
Lua memory usage: 3068869/52428800 bytes
Number of Wikibase entities loaded: 0/400
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  820.603      1 -total
 60.72%  498.245      1 Template:Grey-green_orthographic_projections_maps
 52.82%  433.450      1 Template:Collapsed
 25.22%  206.996     90 Template:Description
 20.97%  172.084     10 Template:Autotranslate
 12.64%  103.739     10 Template:Created_with/en
 12.17%   99.880     10 Template:Created_with
 11.56%   94.867     10 Template:Created_with/layout
  6.58%   54.016      1 Template:Created_with_Adobe_Illustrator
  4.83%   39.671     18 Template:Hi
-->

<!-- Saved in parser cache with key commonswiki:pcache:idhash:8473283-0!canonical and timestamp 20230717014941 and revision id 771083033. Rendering was triggered because: page-view
 -->
</div><!--esi <esi:include src="/esitest-fa8a495983347898/content" /> --><noscript><img src="//commons.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" title="" width="1" height="1" style="border: none; position: absolute;" /></noscript>
<div class="printfooter" data-nosnippet="">Retrieved from "<a dir="ltr" href="https://commons.wikimedia.org/w/index.php?title=Grey–green_orthographic_projections_maps&amp;oldid=771083033">https://commons.wikimedia.org/w/index.php?title=Grey–green_orthographic_projections_maps&amp;oldid=771083033</a>"</div></div>
		<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Special:Categories" title="Special:Categories">Category</a>: <ul><li><a href="/wiki/Category:Locator_maps_(gray_and_green_scheme)" title="Category:Locator maps (gray and green scheme)">Locator maps (gray and green scheme)</a></li></ul></div></div>
	</div>
</div>

<div id="mw-navigation">
	<h2>Navigation menu</h2>
	<div id="mw-head">
		
<nav id="p-personal" class="vector-menu mw-portlet mw-portlet-personal vector-user-menu-legacy" aria-labelledby="p-personal-label" role="navigation"  >
	<h3
		id="p-personal-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Personal tools</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="pt-uls" class="mw-list-item active"><a class="uls-trigger" href="#"><span>English</span></a></li><li id="pt-anonuserpage" class="mw-list-item"><span title="The user page for the IP address you are editing as">Not logged in</span></li><li id="pt-anontalk" class="mw-list-item"><a href="/wiki/Special:MyTalk" title="Discussion about edits from this IP address [n]" accesskey="n"><span>Talk</span></a></li><li id="pt-anoncontribs" class="mw-list-item"><a href="/wiki/Special:MyContributions" title="A list of edits made from this IP address [y]" accesskey="y"><span>Contributions</span></a></li><li id="pt-createaccount" class="mw-list-item"><a href="/w/index.php?title=Special:CreateAccount&amp;returnto=Grey%E2%80%93green+orthographic+projections+maps" title="You are encouraged to create an account and log in; however, it is not mandatory"><span>Create account</span></a></li><li id="pt-login" class="mw-list-item"><a href="/w/index.php?title=Special:UserLogin&amp;returnto=Grey%E2%80%93green+orthographic+projections+maps" title="You are encouraged to log in; however, it is not mandatory [o]" accesskey="o"><span>Log in</span></a></li></ul>
		
	</div>
</nav>

		<div id="left-navigation">
			
<nav id="p-namespaces" class="vector-menu mw-portlet mw-portlet-namespaces vector-menu-tabs vector-menu-tabs-legacy" aria-labelledby="p-namespaces-label" role="navigation"  >
	<h3
		id="p-namespaces-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Namespaces</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="ca-nstab-main" class="selected mw-list-item"><a href="/wiki/Grey%E2%80%93green_orthographic_projections_maps" title="View the content page [c]" accesskey="c"><span>Gallery</span></a></li><li id="ca-talk" class="mw-list-item"><a href="/wiki/Talk:Grey%E2%80%93green_orthographic_projections_maps" rel="discussion" title="Discussion about the content page [t]" accesskey="t"><span>Discussion</span></a></li></ul>
		
	</div>
</nav>

			
<nav id="p-variants" class="vector-menu mw-portlet mw-portlet-variants emptyPortlet vector-menu-dropdown" aria-labelledby="p-variants-label" role="navigation"  >
	<input type="checkbox"
		id="p-variants-checkbox"
		role="button"
		aria-haspopup="true"
		data-event-name="ui.dropdown-p-variants"
		class="vector-menu-checkbox"
		aria-labelledby="p-variants-label"
	/>
	<label
		id="p-variants-label"
		 aria-label="Change language variant"
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">English</span>
	</label>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"></ul>
		
	</div>
</nav>

		</div>
		<div id="right-navigation">
			
<nav id="p-views" class="vector-menu mw-portlet mw-portlet-views vector-menu-tabs vector-menu-tabs-legacy" aria-labelledby="p-views-label" role="navigation"  >
	<h3
		id="p-views-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Views</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="ca-view" class="selected mw-list-item"><a href="/wiki/Grey%E2%80%93green_orthographic_projections_maps"><span>View</span></a></li><li id="ca-edit" class="mw-list-item"><a href="/w/index.php?title=Grey%E2%80%93green_orthographic_projections_maps&amp;action=edit" title="Edit this page [e]" accesskey="e"><span>Edit</span></a></li><li id="ca-history" class="mw-list-item"><a href="/w/index.php?title=Grey%E2%80%93green_orthographic_projections_maps&amp;action=history" title="Past revisions of this page [h]" accesskey="h"><span>History</span></a></li></ul>
		
	</div>
</nav>

			
<nav id="p-cactions" class="vector-menu mw-portlet mw-portlet-cactions emptyPortlet vector-menu-dropdown" aria-labelledby="p-cactions-label" role="navigation"  title="More options" >
	<input type="checkbox"
		id="p-cactions-checkbox"
		role="button"
		aria-haspopup="true"
		data-event-name="ui.dropdown-p-cactions"
		class="vector-menu-checkbox"
		aria-labelledby="p-cactions-label"
	/>
	<label
		id="p-cactions-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">More</span>
	</label>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"></ul>
		
	</div>
</nav>

			
<div id="p-search" role="search" class="vector-search-box-vue vector-search-box">
	<h3 >Search</h3>
	<form action="/w/index.php" id="searchform" class="vector-search-box-form">
		<div id="simpleSearch"
			class="vector-search-box-inner"
			 data-search-loc="header-navigation">
			<input class="vector-search-box-input"
				 type="search" name="search" placeholder="Search Wikimedia Commons" aria-label="Search Wikimedia Commons" autocapitalize="sentences" title="Search Wikimedia Commons [f]" accesskey="f" id="searchInput"
			>
			<input type="hidden" name="title" value="Special:MediaSearch">
			<input id="mw-searchButton"
				 class="searchButton mw-fallbackSearchButton" type="submit" name="fulltext" title="Search the pages for this text" value="Search">
			<input id="searchButton"
				 class="searchButton" type="submit" name="go" title="Go to a page with this exact name if it exists" value="Go">
		</div>
	</form>
</div>

		</div>
	</div>
	
<div id="mw-panel" class="vector-legacy-sidebar">
	<div id="p-logo" role="banner">
		<a class="mw-wiki-logo" href="/wiki/Main_Page"
			title="Visit the main page"></a>
	</div>
	
<nav id="p-navigation" class="vector-menu mw-portlet mw-portlet-navigation vector-menu-portal portal" aria-labelledby="p-navigation-label" role="navigation"  >
	<h3
		id="p-navigation-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Navigate</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="n-mainpage-description" class="mw-list-item"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z"><span>Main page</span></a></li><li id="n-welcome" class="mw-list-item"><a href="/wiki/Commons:Welcome"><span>Welcome</span></a></li><li id="n-portal" class="mw-list-item"><a href="/wiki/Commons:Community_portal" title="About the project, what you can do, where to find things"><span>Community portal</span></a></li><li id="n-village-pump" class="mw-list-item"><a href="/wiki/Commons:Village_pump"><span>Village pump</span></a></li><li id="n-help" class="mw-list-item"><a href="/wiki/Special:MyLanguage/Help:Contents" title="The place to find out"><span>Help center</span></a></li></ul>
		
	</div>
</nav>

	
<nav id="p-participate" class="vector-menu mw-portlet mw-portlet-participate vector-menu-portal portal" aria-labelledby="p-participate-label" role="navigation"  >
	<h3
		id="p-participate-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Participate</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="n-uploadbtn" class="mw-list-item"><a href="/wiki/Special:UploadWizard"><span>Upload file</span></a></li><li id="n-recentchanges" class="mw-list-item"><a href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]" accesskey="r"><span>Recent changes</span></a></li><li id="n-latestfiles" class="mw-list-item"><a href="/wiki/Special:NewFiles"><span>Latest files</span></a></li><li id="n-randomimage" class="mw-list-item"><a href="/wiki/Special:Random/File" title="Load a random file [x]" accesskey="x"><span>Random file</span></a></li><li id="n-contact" class="mw-list-item"><a href="/wiki/Commons:Contact_us"><span>Contact us</span></a></li></ul>
		
	</div>
</nav>

<nav id="p-tb" class="vector-menu mw-portlet mw-portlet-tb vector-menu-portal portal" aria-labelledby="p-tb-label" role="navigation"  >
	<h3
		id="p-tb-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Tools</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="t-whatlinkshere" class="mw-list-item"><a href="/wiki/Special:WhatLinksHere/Grey%E2%80%93green_orthographic_projections_maps" title="A list of all wiki pages that link here [j]" accesskey="j"><span>What links here</span></a></li><li id="t-recentchangeslinked" class="mw-list-item"><a href="/wiki/Special:RecentChangesLinked/Grey%E2%80%93green_orthographic_projections_maps" rel="nofollow" title="Recent changes in pages linked from this page [k]" accesskey="k"><span>Related changes</span></a></li><li id="t-specialpages" class="mw-list-item"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q"><span>Special pages</span></a></li><li id="t-permalink" class="mw-list-item"><a href="/w/index.php?title=Grey%E2%80%93green_orthographic_projections_maps&amp;oldid=771083033" title="Permanent link to this revision of this page"><span>Permanent link</span></a></li><li id="t-info" class="mw-list-item"><a href="/w/index.php?title=Grey%E2%80%93green_orthographic_projections_maps&amp;action=info" title="More information about this page"><span>Page information</span></a></li><li id="t-cite" class="mw-list-item"><a href="/w/index.php?title=Special:CiteThisPage&amp;page=Grey%E2%80%93green_orthographic_projections_maps&amp;id=771083033&amp;wpFormIdentifier=titleform" title="Information on how to cite this page"><span>Cite this page</span></a></li><li id="t-wikibase" class="mw-list-item"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q21167586" title="Link to connected data repository item [g]" accesskey="g"><span>Wikidata item</span></a></li></ul>
		
	</div>
</nav>

<nav id="p-coll-print_export" class="vector-menu mw-portlet mw-portlet-coll-print_export vector-menu-portal portal" aria-labelledby="p-coll-print_export-label" role="navigation"  >
	<h3
		id="p-coll-print_export-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">Print/export</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li id="coll-create_a_book" class="mw-list-item"><a href="/w/index.php?title=Special:Book&amp;bookcmd=book_creator&amp;referer=Grey%E2%80%93green+orthographic+projections+maps"><span>Create a book</span></a></li><li id="coll-download-as-rl" class="mw-list-item"><a href="/w/index.php?title=Special:DownloadAsPdf&amp;page=Grey%E2%80%93green_orthographic_projections_maps&amp;action=show-download-screen"><span>Download as PDF</span></a></li><li id="t-print" class="mw-list-item"><a href="/w/index.php?title=Grey%E2%80%93green_orthographic_projections_maps&amp;printable=yes" title="Printable version of this page [p]" accesskey="p"><span>Printable version</span></a></li></ul>
		
	</div>
</nav>

<nav id="p-wikibase-otherprojects" class="vector-menu mw-portlet mw-portlet-wikibase-otherprojects vector-menu-portal portal" aria-labelledby="p-wikibase-otherprojects-label" role="navigation"  >
	<h3
		id="p-wikibase-otherprojects-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">In other projects</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li class="wb-otherproject-link wb-otherproject-wikipedia mw-list-item"><a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" hreflang="en"><span>Wikipedia</span></a></li></ul>
		
	</div>
</nav>

	
<nav id="p-lang" class="vector-menu mw-portlet mw-portlet-lang vector-menu-portal portal" aria-labelledby="p-lang-label" role="navigation"  >
	<h3
		id="p-lang-label"
		
		class="vector-menu-heading "
	>
		<span class="vector-menu-heading-label">In Wikipedia</span>
	</h3>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list"><li class="interlanguage-link interwiki-en mw-list-item"><a href="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Maps/Conventions/Orthographic_maps" title="Wikipedia:WikiProject Maps/Conventions/Orthographic maps – English" lang="en" hreflang="en" class="interlanguage-link-target"><span>English</span></a></li></ul>
		<div class="after-portlet after-portlet-lang"><span class="wb-langlinks-edit wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q21167586#sitelinks-wikipedia" title="Edit interlanguage links" class="wbc-editpage">Edit links</a></span></div>
	</div>
</nav>

</div>

</div>

<footer id="footer" class="mw-footer" role="contentinfo" >
	<ul id="footer-info">
	<li id="footer-info-lastmod"> This page was last edited on 5 June 2023, at 04:03.</li>
	<li id="footer-info-copyright">Files are available under licenses specified on their description page. All structured data from the file namespace is available under the <a href="https://creativecommons.org/publicdomain/zero/1.0/" title="Definition of the Creative Commons CC0 License">Creative Commons CC0 License</a>; all unstructured text is available under the <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en" title="Definition of the Creative Commons Attribution/Share-Alike License">Creative Commons Attribution-ShareAlike License</a>;
additional terms may apply.
By using this site, you agree to the <a href="//foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Terms_of_Use" title="Wikimedia Foundation Terms of Use">Terms of Use</a> and the <a href="//foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy" title="Wikimedia Foundation Privacy Policy">Privacy Policy</a>.</li>
</ul>

	<ul id="footer-places">
	<li id="footer-places-privacy"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy">Privacy policy</a></li>
	<li id="footer-places-about"><a href="/wiki/Commons:Welcome">About Wikimedia Commons</a></li>
	<li id="footer-places-disclaimers"><a href="/wiki/Commons:General_disclaimer">Disclaimers</a></li>
	<li id="footer-places-wm-codeofconduct"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Universal_Code_of_Conduct">Code of Conduct</a></li>
	<li id="footer-places-mobileview"><a href="//commons.m.wikimedia.org/w/index.php?title=Grey%E2%80%93green_orthographic_projections_maps&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Mobile view</a></li>
	<li id="footer-places-developers"><a href="https://developer.wikimedia.org">Developers</a></li>
	<li id="footer-places-statslink"><a href="https://stats.wikimedia.org/#/commons.wikimedia.org">Statistics</a></li>
	<li id="footer-places-cookiestatement"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement">Cookie statement</a></li>
</ul>

	<ul id="footer-icons" class="noprint">
	<li id="footer-copyrightico"><a href="https://wikimediafoundation.org/"><img src="/static/images/footer/wikimedia-button.png" srcset="/static/images/footer/wikimedia-button-1.5x.png 1.5x, /static/images/footer/wikimedia-button-2x.png 2x" width="88" height="31" alt="Wikimedia Foundation" loading="lazy" /></a></li>
	<li id="footer-poweredbyico"><a href="https://www.mediawiki.org/"><img src="/static/images/footer/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" srcset="/static/images/footer/poweredby_mediawiki_132x47.png 1.5x, /static/images/footer/poweredby_mediawiki_176x62.png 2x" width="88" height="31" loading="lazy"></a></li>
</ul>

</footer>

<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgHostname":"mw1399","wgBackendResponseTime":100,"wgPageParseReport":{"limitreport":{"cputime":"0.822","walltime":"1.035","ppvisitednodes":{"value":14143,"limit":1000000},"postexpandincludesize":{"value":151033,"limit":2097152},"templateargumentsize":{"value":57274,"limit":2097152},"expansiondepth":{"value":26,"limit":100},"expensivefunctioncount":{"value":4,"limit":500},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":267741,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  820.603      1 -total"," 60.72%  498.245      1 Template:Grey-green_orthographic_projections_maps"," 52.82%  433.450      1 Template:Collapsed"," 25.22%  206.996     90 Template:Description"," 20.97%  172.084     10 Template:Autotranslate"," 12.64%  103.739     10 Template:Created_with/en"," 12.17%   99.880     10 Template:Created_with"," 11.56%   94.867     10 Template:Created_with/layout","  6.58%   54.016      1 Template:Created_with_Adobe_Illustrator","  4.83%   39.671     18 Template:Hi"]},"scribunto":{"limitreport-timeusage":{"value":"0.273","limit":"10.000"},"limitreport-memusage":{"value":3068869,"limit":52428800}},"cachereport":{"origin":"mw1369","timestamp":"20230717014942","ttl":1814400,"transientcontent":false}}});});</script>
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Article","name":"Grey\u2013green orthographic projections maps","url":"https:\/\/commons.wikimedia.org\/wiki\/Grey%E2%80%93green_orthographic_projections_maps","sameAs":"http:\/\/www.wikidata.org\/entity\/Q21167586","mainEntity":"http:\/\/www.wikidata.org\/entity\/Q21167586","author":{"@type":"Organization","name":"Contributors to Wikimedia projects"},"publisher":{"@type":"Organization","name":"Wikimedia Foundation, Inc.","logo":{"@type":"ImageObject","url":"https:\/\/www.wikimedia.org\/static\/images\/wmf-hor-googpub.png"}},"datePublished":"2009-11-17T13:19:30Z","dateModified":"2023-06-05T04:03:23Z","image":"https:\/\/upload.wikimedia.org\/wikipedia\/commons\/a\/a9\/None_%28orthographic_projection%29.svg","headline":"collection of locator maps"}</script><script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Article","name":"Grey\u2013green orthographic projections maps","url":"https:\/\/commons.wikimedia.org\/wiki\/Grey%E2%80%93green_orthographic_projections_maps","sameAs":"http:\/\/www.wikidata.org\/entity\/Q21167586","mainEntity":"http:\/\/www.wikidata.org\/entity\/Q21167586","author":{"@type":"Organization","name":"Contributors to Wikimedia projects"},"publisher":{"@type":"Organization","name":"Wikimedia Foundation, Inc.","logo":{"@type":"ImageObject","url":"https:\/\/www.wikimedia.org\/static\/images\/wmf-hor-googpub.png"}},"datePublished":"2009-11-17T13:19:30Z","dateModified":"2023-06-05T04:03:23Z","image":"https:\/\/upload.wikimedia.org\/wikipedia\/commons\/a\/a9\/None_%28orthographic_projection%29.svg","headline":"collection of locator maps"}</script>
</body>
</html>
'''

# Extrair os URLs e salvar em um arquivo JSON
urls = extrair_urls(html)
salvar_urls_em_arquivo(urls, 'urls.json')
