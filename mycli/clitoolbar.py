from pygments.token import Token

def create_toolbar_tokens_func(get_key_bindings, get_is_refreshing):
    """
    Return a function that generates the toolbar tokens.
    """
    assert callable(get_key_bindings)

    token = Token.Toolbar

    def get_toolbar_tokens(cli):
        result = []
        result.append((token, ' '))

        if cli.buffers['default'].completer.smart_completion:
            result.append((token.On, '[F2] Smart Completion: ON  '))
        else:
            result.append((token.Off, '[F2] Smart Completion: OFF  '))

        if cli.buffers['default'].always_multiline:
            result.append((token.On, '[F3] Multiline: ON  '))
        else:
            result.append((token.Off, '[F3] Multiline: OFF  '))

        if cli.buffers['default'].always_multiline:
            result.append((token,
                ' (Semi-colon [;] will end the line)'))

        if get_key_bindings() == 'vi':
            result.append((token.On, '[F4] Vi-mode'))
        else:
            result.append((token.On, '[F4] Emacs-mode'))

        if get_is_refreshing():
            result.append((token, '     Refreshing completions...'))

        return result
    return get_toolbar_tokens
