from docutils import nodes
import unicodedata

def char(name, rawtext, text, lineno, inliner, options={}, content=[]):
    if len(text) != 1:
        msg = inliner.reporter.error(
                "only one char allowed for unicode info"
                , line=lineno
                )
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]

    na = unicodedata.name(text)
    nu = ord(text)

    utext = "{0} (U+{1:0>4X}) ".format(na, nu)
    node = nodes.inline(rawtext, utext, **options)
    return [node, nodes.literal(rawtext,text, **options)], []

def setup(app):
    app.add_role('unicode_info', char)
    return
