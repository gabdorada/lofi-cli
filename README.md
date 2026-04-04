# 🎵 lofi-station CLI

Uma estação de música lofi no terminal.
Escolha seu mood, foque e relaxe.

## Funcionalidades
- Seleção de mood (Focus / Chill)
- Interface bonita com Rich
- Timer Pomodoro integrado

## Decisões técnicas

### Player de áudio: pygame
Consideramos usar `yt-dlp + mpv` para streaming do YouTube direto
no terminal, porém o `mpv` requer Xcode 15 para compilação, 
incompatível com macOS 12. Optamos pelo `pygame` para manter 
a solução simples e funcional.