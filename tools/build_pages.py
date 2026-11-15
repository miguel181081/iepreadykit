import sys
out = sys.argv[1]
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | IEP Ready Kit</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://iepreadykit.com/{slug}">
{robots}<meta name="theme-color" content="#1F3A5F">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="IEP Ready Kit">
<meta property="og:title" content="{title} | IEP Ready Kit">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://iepreadykit.com/{slug}">
<meta property="og:image" content="https://iepreadykit.com/images/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="styles.css?v=5">
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','3355007808034064');
fbq('track','PageView');
</script>
<noscript><img height="1" width="1" style="display:none" alt="" src="https://www.facebook.com/tr?id=3355007808034064&ev=PageView&noscript=1"/></noscript>
<!-- End Meta Pixel Code -->
<script>
document.addEventListener('click',function(e){{var a=e.target.closest('a[href*="buy.stripe.com"]');if(a&&window.fbq){{fbq('track','InitiateCheckout',{{value:14.00,currency:'USD',content_name:'IEP Ready Kit'}});}}}});
</script>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="site-header"><div class="wrap">
<a class="logo" href="./" aria-label="IEP Ready Kit, home"><span class="logo-mark" aria-hidden="true">IEP</span><span class="logo-name">IEP Ready Kit</span></a>
<a class="btn btn-small" href="./">Back to home</a>
</div></header>
<main id="main" class="page"><div class="wrap narrow">
<h1>{title}</h1>
{body}
</div></main>
<footer class="site-footer"><div class="wrap">
<nav aria-label="Footer"><ul class="footer-links">
<li><a href="./">Home</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li><li><a href="refunds.html">Refunds</a></li><li><a href="contact.html">Contact</a></li>
</ul></nav>
<p class="disclaimer">Educational resource only. Not legal advice. Results are not guaranteed. © 2026 IEP Ready Kit.</p>
</div></footer>
</body>
</html>
"""
REVIEW = '<p class="notice" role="note"><strong>[LEGAL REVIEW NEEDED]</strong> This is a plain-language draft. Have it reviewed before launch.</p>'
pages = {
"privacy.html": ("Privacy Policy", "How IEP Ready Kit handles your information.", "", """
<p><em>Last updated: November 14, 2026</em></p>
<h2>What we collect</h2>
<p>When you buy the kit, our payment provider, Stripe, collects your payment details and email address. We do not see or store your full card number. We use your email address to send your receipt and the kit, and to answer your questions.</p>
<h2>Website analytics and advertising</h2>
<p>This site uses the Meta (Facebook) Pixel to measure visits and purchases and to help us understand our ads. The Pixel may set cookies and share information such as the pages you visit and whether you complete a purchase. You can limit this with your browser settings or your Meta ad preferences.</p>
<h2>Children's information</h2>
<p>This site is for parents and caregivers. We do not ask for, or knowingly collect, information about children.</p>
<h2>Your choices</h2>
<p>To ask about the information we hold about you, or to ask us to delete it, write to us at <a href="contact.html">our contact page</a>.</p>
<h2>Changes</h2>
<p>If we change this policy, we will update the date above.</p>
"""),
"terms.html": ("Terms of Use", "Terms for using the IEP Ready Kit site and product.", "", """
<p><em>Last updated: November 14, 2026</em></p>
<h2>What the kit is</h2>
<p>The IEP Ready Kit is a digital, printable resource that gives general information about the IEP process under the Individuals with Disabilities Education Act (IDEA).</p>
<h2>Not legal advice</h2>
<p>The kit and this website are not legal advice and do not create an attorney-client relationship. They do not replace advice from a licensed attorney, an advocate or your school's special education team. IEP rules vary by state and school district.</p>
<h2>No guaranteed outcomes</h2>
<p>We do not promise any result from your child's school, evaluation or IEP meeting.</p>
<h2>Your use</h2>
<p>The kit is for your own personal, non-commercial use. Please do not resell or republish it.</p>
<h2>Affiliation</h2>
<p>IEP Ready Kit is not affiliated with the U.S. Department of Education or any school district.</p>
<h2>Contact</h2>
<p>Questions about these terms? See our <a href="contact.html">contact page</a>.</p>
"""),
"refunds.html": ("Refund Policy", "Refund information for the IEP Ready Kit.", "", """
<h2>Our promise</h2>
<p>You can ask for a full refund at any time before the kit launches. After you receive the kit, you have 30 days to ask for a full refund if it is not useful for you. No forms and no questions you have to answer.</p>
<h2>Pre-sale</h2>
<p>The IEP Ready Kit is sold as a pre-sale. It will be sent to the email you used at checkout when it launches.</p>
<h2>How to ask</h2>
<p>Email us using the details on our <a href="contact.html">contact page</a> and include the email you used to order.</p>
"""),
"contact.html": ("Contact", "How to contact IEP Ready Kit.", "", """
<p>Questions about your order, the kit or refunds? Email us and we will reply as soon as we can.</p>
<p><strong>Email:</strong> <a href="mailto:iepreadykit@gmail.com">iepreadykit@gmail.com</a></p>
<p>We cannot give legal advice. For help with your child's rights, please contact a licensed attorney, an advocate or your state's parent training and information center through <a href="https://www.parentcenterhub.org/" target="_blank" rel="noopener noreferrer">parentcenterhub.org</a>.</p>
"""),
"404.html": ("Page not found", "The page you were looking for could not be found.", "noindex", """
<p>Sorry, we could not find that page. It may have moved or the link may be mistyped.</p>
<p><a class="btn" href="./">Go to the home page</a></p>
"""),
}
for slug,(title,desc,rb,body) in pages.items():
    robots = '<meta name="robots" content="noindex,nofollow">\n' if rb else ''
    open(f"{out}/{slug}","w").write(HEAD.format(title=title,desc=desc,slug=slug,robots=robots,body=body))
