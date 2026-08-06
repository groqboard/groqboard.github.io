"""Rebuilds the FAQPage JSON-LD block from the FAQ actually rendered on the page.

Google requires FAQ structured data to match content the visitor can see; questions that
exist only in the schema are grounds for dropping the rich result for the whole page. The
two had drifted apart (four schema-only questions, five page-only ones), which is the kind
of thing nobody notices by reading, so it is generated instead of maintained by hand.

Run after editing the FAQ section:  python sync_faq_schema.py
"""
import html
import json
import re
import sys

PATH = "index.html"

src = open(PATH, encoding="utf-8").read()

# Questions and answers as the English reader sees them.
items = re.findall(
    r'<div class="faq-q" data-en="([^"]*)"[^>]*>.*?'
    r'<p class="faq-a" data-en="([^"]*)"',
    src,
    re.S,
)
if not items:
    sys.exit("no FAQ items found - did the markup change?")

faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": html.unescape(q),
            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)},
        }
        for q, a in items
    ],
}
block = json.dumps(faq, indent=8, ensure_ascii=False)
# Match the file's existing indentation for the closing brace of the block.
block = block[:-1] + "    }"

pattern = re.compile(
    r'(<!-- Structured Data: FAQ[^>]*-->\s*<script type="application/ld\+json">\n)'
    r'(.*?)'
    r'(\n\s*</script>)',
    re.S,
)
if not pattern.search(src):
    sys.exit("could not locate the FAQ JSON-LD block")

out = pattern.sub(lambda m: m.group(1) + "    " + block + m.group(3), src, count=1)
open(PATH, "w", encoding="utf-8", newline="").write(out)
print(f"synced {len(items)} FAQ entries into the JSON-LD block")
