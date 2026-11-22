"""TF-IDF cosine similarity between skills (descriptions or bodies). Standard library only."""
import math
import re
from collections import Counter

STOP = set("""a an and are as at be by can do for from has have how i in is it its my of on or our the their
them this that to use user wants what when where which who why will with you your asks ask help
skill skills seller sellers store stores shop shops ecommerce commerce get make more not also into
all any each than then they these those""".split())
_INSTALL = re.compile(r"^## Install(?:ation)?[ \t]*\n.*?(?=^## |\Z)", re.S | re.M)
_SCOPE = re.compile(r"<!-- role-and-scope:start.*?<!-- role-and-scope:end -->", re.S)
_TAIL = re.compile(r"^## Limitations.*", re.S | re.M)


def tokens(text):
    return [w for w in re.findall(r"[a-z][a-z0-9]{2,}", text.lower()) if w not in STOP]


def description(text):
    """Description text without cited skill names (`other-skill`), which are deliberate pointers."""
    m = re.search(r"^description: (.*)$", text, re.M)
    return re.sub(r"`[a-z0-9-]+`", " ", m.group(1)) if m else ""


def body(text):
    b = text[text.find("\n---", 4) + 4:] if text.startswith("---") else text
    return _TAIL.sub("", _SCOPE.sub("", _INSTALL.sub("", b)))


def vectors(docs):
    """{name: text} -> {name: normalized tf-idf vector}"""
    toks = {k: tokens(v) for k, v in docs.items()}
    df = Counter(w for t in toks.values() for w in set(t))
    n = len(toks)
    out = {}
    for k, t in toks.items():
        vec = {w: c * math.log(n / df[w]) for w, c in Counter(t).items()}
        norm = math.sqrt(sum(x * x for x in vec.values())) or 1.0
        out[k] = {w: x / norm for w, x in vec.items()}
    return out


def cosine(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum(x * b.get(w, 0.0) for w, x in a.items())


def content_lines(text):
    """Normalized non-empty lines of the body (no headings, no generated sections), for clone detection."""
    out = set()
    for line in body(text).splitlines():
        line = re.sub(r"[*_`>#|]", " ", line)
        line = re.sub(r"\s+", " ", line).strip().lower()
        if len(line) >= 20:
            out.add(line)
    return out


def shared_line_ratio(a, b):
    """Share of the smaller file's lines that also appear verbatim in the other file."""
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))
