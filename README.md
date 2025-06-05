# lektor-tinymce
Lektor plugin for editing with the [TinyMCE text editor](https://www.tiny.cloud/features).

## Installation
Install the plugin from pypi with one of the [standard ways](https://www.getlektor.com/docs/plugins/).

## Compatibility
This plugin uses non-API mechanisms in Lektor/Flask to inject its own code into the admin Jinja template. As a result, future changes to the Lektor admin backend or frontend code may break compatibility.
Version 0.6 should be compatible with Lektor versions starting from [3.3.6](https://github.com/lektor/lektor/releases/tag/v3.3.6).

## API key
The TinyMCE API key must be placed in a configs/tinymce.ini file (relative to your Lektor project directory), under the following section:
```ini
[licence]
api-key = "YOUR_API_KEY_HERE"
```

## TinyMCE configuration
To pass additional arguments (e.g. a list of plugins) into [tinymce.init()](https://www.tiny.cloud/docs/configure/integration-and-setup/), use the config section of the configs/tinymce.ini file:
```
[config]
settings = "branding: false, plugins: 'image link lists autoresize table'"
```

Note: This string is passed directly to tinymce.init(), so it must follow the proper JavaScript format.
Some plugins, such as image upload, may not be fully integrated with Lektor by default.

### ⚠️ IMPORTANT CHANGES IN v0.6

A new option named `targets` has been added to the `[config]` section. It specifies which fields should use the TinyMCE editor. The value must be a JavaScript array of **field labels** (i.e., the text in the grey rectangle at the top left of each field in the admin editor):
```
[config]
targets = "['Body', 'Page text']"
```

Additionally, a `force-refresh` option has been introduced. If set to "true", the admin page will reload on URL change:
```
[config]
force-refresh = "true"
```

## License
The plugin is distributed under the MIT license
