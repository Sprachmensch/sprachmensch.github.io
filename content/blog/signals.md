+++
title = "Signals"
date = "2026-01-13T16:18:07+01:00"
tags = []
+++

Handle interrupts/signals:

{{< codeimport "assets/code/signals.py" "python" >}}

You can register multiple handlers at once:

```python
signal=signal.signal(signal_SIGINT, FUNCTION)
signal=signal.signal(signal_SIGTER, FUNCTION)
```
