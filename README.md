zsh-syntax-highlighting / highlighters / root
---------------------------------------------

This is the `root` highlighter, that highlights the whole line if the current
user is root.


### How to tweak it

This highlighter defines the following styles:

* `root` - the style for the whole line if the current user is root.

To override one of those styles, change its entry in `ZSH_HIGHLIGHT_STYLES`,
for example in `~/.zshrc`:

```zsh
ZSH_HIGHLIGHT_STYLES[root]='bg=red'
```
