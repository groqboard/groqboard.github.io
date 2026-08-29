# Publicar la landing de la v11

La rama `v11-draft` tiene la landing de la version 11 lista y esperando.
`main` tiene a proposito la de la version 10, porque eso es lo que Google
Play sirve hoy.

## Cuando aprieten Publicar en Play Console y la v11 este VIVA en la tienda

```
cd "C:/Users/Alex/GroqBoard/Landing"
git checkout main
git merge v11-draft -m "Publica la landing de la v11: la tienda ya sirve el build 251"
git push origin main
```

GitHub Pages publica solo al hacer push a `main`. Tarda uno o dos minutos.

## Verificar despues

Abrir https://groqboard.com/ y comprobar tres cosas:

- La pastilla del hero dice "Free with your own API key", no "7-day free trial".
- El badge de arriba dice **v11.0**, no v10.0.
- En las capturas, el selector de planes dice **$2.99/mo**, no "$4.99 USD".

Si el navegador sigue mostrando lo viejo es cache: `Ctrl+Shift+R`.

## Que NO hay que hacer

- **No** usar `git add -A` en este repo. Barre archivos internos al sitio publico;
  ya paso una vez y hubo que sacar diez archivos a mano.
- **No** tocar `privacy.html` ni `terms.html`. Nunca se revirtieron a la v10 a
  proposito: describen el proxy de mas, lo cual no le miente a nadie, y Google
  estuvo leyendo esa URL mientras revisaba la v11.
- **No** editar a mano el bloque JSON-LD de la FAQ. Se genera:
  `python sync_faq_schema.py` despues de tocar la seccion visible.
- Si se cambia una imagen sin cambiarle el nombre, hay que subirle el `?v=N`
  o el navegador sigue sirviendo la vieja.

## Que se borra el dia que la v11 este publicada

Estas dos cosas existen solo mientras la tienda sirva la v10, y el merge de
`v11-draft` ya se las lleva:

- La regla CSS `.screenshot-item.phone.framed`.
- Las dos capturas v5 (`pic_v5_3_paywall_clean.png`, `pic_v5_2_settings_clean.png`)
  con su chip de `$4.99 USD`.

Y este archivo tambien se puede borrar.
