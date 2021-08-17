# StickyDocs for Sublime Text

This is a plugin for Sublime Text that allows keeping the docs popup open when navigating the LSP completions list, emulating the behaviour of VSCode. See https://github.com/sublimelsp/LSP/issues/1421 for more details.

It works by hijacking the Up/Down arrow keybindings and showing the doc popup every time the keys are pressed.

## Installation
Clone/extract this repo under the `Packages` directory (Tools->Browse Packages)

## Usage
Press F12 when autocomplete is visible to toggle the sticky docs.
