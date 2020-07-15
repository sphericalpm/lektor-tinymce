# -*- coding: utf-8 -*-
from flask import render_template_string
from lektor.admin.modules import dash
from lektor.pluginsystem import Plugin


KEY = ''
TEMPLATE = '''
{% extends "dash.html" %}
{% block scripts %}
  {{ super() }}
  <script src="https://cdn.tiny.cloud/1/{{tinymce_api_key}}/tinymce/4/tinymce.min.js" referrerpolicy="origin"></script>
  <script>
    (new MutationObserver(function() {
        [...document.getElementsByTagName('textarea')].forEach(txt_elem => {
            if (txt_elem.className === 'form-control') {
                txt_elem.classList.add('tinymce-attached');
                tinymce.init({
                    target: txt_elem,
                    branding: false,
                    plugins: 'image link',
                    setup: function(editor) {
                        editor.on('Change', function(e) {
                            txt_elem.value = editor.getContent();

                            let ev = new Event('input', { bubbles: true });
                            ev.simulated = true;
                            txt_elem.dispatchEvent(ev);
                        });
                    }
                });
            };
        });
    })).observe(
        document.getElementsByTagName('body')[0],
        {
            subtree: true,
            childList: true
        },
    );
  </script>
{% endblock %}
'''


def patched_endpoint(*args, **kwargs):
    return render_template_string(
        TEMPLATE,
        tinymce_api_key=KEY
    )


class TinyMCEPlugin(Plugin):
    name = 'lektor-tinymce'
    description = u'Lektor Plugin for TinyMCE Text Editor use.'

    def on_setup_env(self, *args, **kwargs):
        global KEY
        config = self.get_config()
        KEY = config.get('licence.api-key', 'no-api-key')

    def on_server_spawn(self, *args, **kwargs):
        # remove all rules except the first one which is edit redirect
        while len(dash.bp.deferred_functions) > 1:
            dash.bp.deferred_functions.pop()
        # ... and fill all the rules back with our wrapper template
        for path, endpoint in dash.endpoints:
            dash.bp.add_url_rule(path, endpoint, patched_endpoint)

