# lektor-tinymce
Lektor plugin for editing with the [TinyMCE text editor](https://www.tiny.cloud/features).

## Installation
Install the plugin from pypi with one of the [standard ways](https://www.getlektor.com/docs/plugins/).

## API key
To add an API key, create the file `configs/tinymce.ini` in your lektor project folder with the following contents:

    [licence]
    api-key = 'YOUR_API_KEY_HERE'

## Tiny MCE setting
To past some settings params to the tinymce.init() (plugins for example), just add the following contents to the file `configs/tinymce.ini` in your lektor project folder:
    [config]
    settings = 'YOUR_SETTINGS'

Here is the example of the settings string:
    [config]
    settings = "plugins: 'image link lists autoresize table', image_advtab: true,"

## License
The plugin is distributed under the MIT license
