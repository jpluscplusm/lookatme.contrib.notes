"""
Simplistic speaker notes
"""


#import urwid

from lookatme.tui import MarkdownTui
from lookatme.exceptions import IgnoredByContrib

def monkeypatch_method(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator

@monkeypatch_method(MarkdownTui)
def update_body(self):
    """Render the provided slide body
    """
    rendered = self.slide_renderer.render_slide(self.curr_slide, True)
    self.slide_body.body = rendered

def render_code(token, body, stack, loop):
    lang = token["lang"] or ""
    if lang != "notes":
        raise IgnoredByContrib()

    notes = token['text'] or ""
    with open('/tmp/notes-file', "w") as f:
            f.write(notes)
            f.close()
    
    return None; #urwid.Text("Yay! The notes extension works+1!")
