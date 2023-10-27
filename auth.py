Autenticação:

Para garantir a segurança, suas credenciais da API (chave e segredo) não devem ser codificadas diretamente no código. Em vez disso, use variáveis de ambiente.

import os
import ccxt

API_KEY = os.environ.get('BINANCE_API_KEY')
API_SECRET = os.environ.get('BINANCE_API_SECRET')

if not API_KEY or not API_SECRET:
    raise ValueError("API credentials not set!")

exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})
