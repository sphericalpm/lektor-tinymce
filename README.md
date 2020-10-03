# lektor-tinymce
Lektor plugin for editing with the [TinyMCE text editor](https://www.tiny.cloud/features).

## Installation
Install the plugin from pypi with one of the [standard ways](https://www.getlektor.com/docs/plugins/).

## API key
To add an API key, create the file `configs/tinymce.ini` in your lektor project folder with the following contents:

    [licence]
    api-key = 'YOUR_API_KEY_HERE'

## Tiny MCE setting
To pass additional arguments (such as a list of plugins) into [tinymce.init()](https://www.tiny.cloud/docs/configure/integration-and-setup/), just add the following contents to the file `configs/tinymce.ini` in your lektor project folder:
    [config]
    settings = 'YOUR_SETTINGS'

Here is the example of the settings string:
    [config]
    settings = "plugins: 'image link lists autoresize table', image_advtab: true,"

Note that this string is passed directly into tinymce.init(), so it must follow the given format.
Some plugins, such as image upload, may not be fully integrated with lektor by default.
## License
The plugin is distributed under the MIT license
